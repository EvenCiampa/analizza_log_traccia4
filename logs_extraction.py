from collections import defaultdict


def logs_extraction(logs):
    """
    Analizza i log e calcola statistiche aggregate per data.

    Questa funzione processa una lista di log ed estrae informazioni statistiche
    raggruppate per user, incluso il numero di ip distinti e eventi distinti.

    Args:
        logs (list): Lista di log, dove ogni log è una lista/tupla con formato:
                     [data_ora, user_id, ..., ..., ..., evento]
                     - Indice 1: ID utente
                     - Indice 7: IP
                     - Indice 4: tipo di evento

    Returns:
        dict: Dizionario con le statistiche aggregate per data.
              Formato: {
                  "user_id": {
                      "inidrizzo:IP": int,
                      "num_eventi": int
                  },
                  ...
              }

    """
    # Dizionari per tracciare utenti ed eventi univoci per data
    # Uso set per garantire unicità automatica
    IP_per_user = defaultdict(set)
    events_per_IP = defaultdict(set)

    # Processa ogni log entry
    for i, log in enumerate(logs):
        # Valida la struttura del log
        if not isinstance(log, (list, tuple)) or len(log) < 5:
            raise ValueError(
                f"Log alla posizione {i} non ha il formato corretto. "
                f"Atteso almeno 5 elementi, ricevuti {len(log) if isinstance(log, (list, tuple)) else 'tipo non valido'}"
            )

        # Estrai i campi necessari
        indirizzo_IP = log[7]
        user_id = log[1]
        evento = log[4]
        # Valida che i campi non siano None o vuoti
        if not indirizzo_IP or not user_id or not evento:
            continue
            ## se c'è un null viene escluso questo elemento dal conteggio


        if user_id not in IP_per_user:
            IP_per_user[user_id] = set()
        IP_per_user[user_id].add(indirizzo_IP)

        if indirizzo_IP not in events_per_IP:
            events_per_IP[indirizzo_IP] = set()
        events_per_IP[indirizzo_IP].add(evento)

    conteggio = indirizzo_IP.count(evento)

    # Costruisci il dizionario di output unendo i due precedenti

    output = {}

    for user_id in sorted(IP_per_user.keys()):
        ip_list = list(IP_per_user[user_id])

        # conteggio totale eventi per tutti gli IP dell'utente
        total_events = 0
        for ip in ip_list:
            total_events += len(events_per_IP[ip])

        output[user_id] = {
            "indirizzi_IP": ip_list,
            "numero_eventi": total_events
        }

    return output