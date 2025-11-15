'''
Scrivere un programma Python che legge una lista di log anonimizzati. Ciascun elemento della lista di log è costituito dalle seguenti otto informazioni:

Data/Ora
Identificativo unico dell’utente
Contesto dell’evento
Componente
Evento
Descrizione
Origine
Indirizzo IP
La lista di log è memorizzata in un file JSON. Ogni log è una lista contenente le otto informazioni riportate sopra.

L'obiettivo è quello di estrarre alcune informazioni dalla lista di log e salvarle in un file in formato JSON.

Estrarre le seguenti informazioni:

per ogni utente:
la lista degli indirizzi IP diversi associati a lui;
per ogni indirizzo IP diverso quanti eventi sono associati a lui.
'''

import json
import argparse
from logs_extraction import logs_extraction


def parse_args():
    parser = argparse.ArgumentParser(description="Codice Esercitazione")
    parser.add_argument("-i", "--input", default="test_data/test_small.json" , help="Percorso file JSON input")
    parser.add_argument("-o", "--output", default="test_data/output", help="Percorso file JSON output")
    return parser.parse_args()


def main():
    args = parse_args()

    # 1. Carica file JSON
    with open(args.input, "r", encoding="utf-8") as f:
        logs = json.load(f)

    # 2. Estrai risultati
    results = logs_extraction(logs)

    # 3. Scrivi output su file
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print(f"Output salvato in: {args.output}")


if __name__ == "__main__":
    main()

