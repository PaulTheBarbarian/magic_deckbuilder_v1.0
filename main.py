'''
This project is dedicated to generate some good deck builders
useful link: https://scryfall.com/docs/api

'''

import requests
import csv

# THE FIRST PART OF THIS CODE IS DESIGNED TO TEST THE CALL TO THE API
# THE CALL USED WAS ONLY TO ALL CARDS NAMES
# Structure - header is 'Data'. type of object is 'catalog'
# Given that this was a test, all variable names were in portuguese, my mother-tongue.
# future developments will be written in english
def register_all_cards_names():
    todas_cartas = None
    card_names_bulk_data = requests.get('https://api.scryfall.com/catalog/card-names') # only fetch specific cards
    print(card_names_bulk_data.status_code)
    print(card_names_bulk_data.json())
    nome_carta = card_names_bulk_data.json()['data'][0]
    todas_cartas = card_names_bulk_data.json()['data']
    # tamanho_conteudo = len(card_names_bulk_data.json()['data'])
    print(nome_carta)
    #print(tamanho_conteudo)
    arq = open('lista_de_todas_as_cartas.txt', "w", encoding="utf-8")
    # for i, nome_cada_item in enumerate(todas_cartas):
    #     arq.write(f'{i+1} - {nome_cada_item}\n')
    arq.close()

#SECOND PART: NAVIGATE THROUGH CARD OBJECTS (With name, type, description etc)
# II.a - Let's shorten the scope for this project: make deck builders with all cards from 
# magic the gathering online
# mtgo_id must be populated (type: int)

with open('list_cards_mtgo.csv', 'w', newline='') as file_mtgo:
    list_cards_mtgo = csv.writer(file_mtgo, delimiter= ';')
    list_cards_mtgo.writerow((1, 2, 3, 'test'))
