'''
This project is dedicated to generate some good deck builders
useful link: https://scryfall.com/docs/api

'''

import requests
import csv
import urllib.parse
api_main_link = 'https://api.scryfall.com/'
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

query_test = "one ring"
query_test= urllib.parse.quote(query_test)

def fulltextsearch(query_test): # Function to optimize fulltextsearch
    card_search = '/cards/search?'
    link_for_query = api_main_link + card_search + 'q=' + query_test
    return link_for_query
test_search = requests.get(fulltextsearch(query_test))

total_cards_search = test_search.json()['total_cards']

print(f"We've detected {total_cards_search} cards in your query")
print('They are:')
query_result = test_search.json()['data']
# print(query_result[0]['name']) #  this line was used as testing

def save_query_results(query_result):
    with open('list_query_result_only_names.csv', 'w', newline='') as query_name_file:
        list_query_result_only_names = csv.writer(query_name_file, delimiter=';')
        list_query_result_only_names.writerow(['Name', 'Type'])        
        for i in range(total_cards_search):            
            list_query_result_only_names.writerow ([query_result[i]['name'], \
                                                   query_result[i]['type_line']])

save_query_results(query_result)