from pymongo import MongoClient
import subprocess
import time
from random import randint

def main():
    """
    Definisce un'interfaccia testuale per il testing del sistema
    """
    print("Connesso al database.")
    action = None

    while action != 0:
        print("\nScegi un'azione:")
        
        print("1 - Visualizzazione nomi collezioni")
        print("2 - Caricamento dati (grades)")
        print("3 - Lettura dati")
        print("4 - Eliminazione collezione (grades)")
        print("5 - Lettura dati con nodi disabilitati")
        print("6 - Caricamento dati (grades) con nodo disabilitato")
        print("0 - esci")

        action = int(input())

        print()

        if action == 1:
            print_collection_names()
        elif action == 2:
            insert_data()
        elif action == 3:
            get_data()
        elif action == 4:
            drop_collection()
        elif action == 5:
            get_data_with_node_offline()
        elif action == 6:
            insert_with_node_offline()

def get_collections_names():
    """
    Ritorna la lista di nomi delle collezioni presenti nel DB corrente
    """
    return db.list_collection_names()

def print_collection_names():
    """
    Stampa i nomi delle collezioni presenti nel DB corrente
    """
    collections = get_collections_names()
    print("Nomi delle collezioni presenti nel DB:")

    for elem in collections:
        print("- {e}".format(e = elem))

def insert_data():
    """
    Crea la collezione 'grades' abilitandone lo sharding con una chiave ad hash.
    Importa i dati da un file json tramite applicativo mongoimport.
    """
    if 'grades' not in get_collections_names():

        grades = db['grades']
        client.admin.command('shardCollection', 'myFirstDB.grades', key = {"_id" : "hashed"})
        print("Collezione 'grades' creata e sharding abilitato. Avvio del caricamento dati...")

        p = subprocess.run(['mongoimport', '--host', 'localhost', '--port', '15000', '--db', 'myFirstDB', '--collection',
        'grades', '--file', 'grades.json'])

        print("Dati della collezione 'grades' inseriti nel DB")
    else: 
        print("La collezione 'grades' è già disponibile nel DB")

def get_data(name = None):
    """
    Ritorna la numerosità dei documenti in una collezione
    """
    col_name = name

    if col_name is None:
        print("Inserisci il nome della collezione:")
        col_name = str(input())

    if name is not None or col_name in get_collections_names():
        try:
            coll = db.get_collection(col_name)
            print("La collezione contiene " + str(coll.count_documents({})) + " documenti.")
        except Exception as e:
            print("Eccezione in lettura")
            print(e)
    else:
        print("Collezione non esistente")    

def drop_collection():
    """
    Elimina la collezione 'grades' se presente nel DB.
    """
    if 'grades' in get_collections_names():
        db["grades"].drop()
        print("La collezione 'grades' è stata eliminata")
    else: 
        print("La collezione 'grades' non è presente nel DB")

def get_data_with_node_offline():
    """
    Blocca un paio di nodi del sistema e successivamente effettua la richiesta dei documenti.
    Terminata la lettura, riabilita i nodi bloccati.
    """
    print("Inserisci il nome della collezione:")
    col_name = str(input())

    if col_name in get_collections_names():
        print("Blocco un nodo dello shard3")
        node1 = 'shard3server' + str(randint(1,3))
        subprocess.run(['docker', 'stop', node1])

        print("Blocco un nodo dello shard2")
        node2 = 'shard2server' + str(randint(1,2))
        subprocess.run(['docker', 'stop', node2])

        print("Attendo qualche secondo in modo che vengano rieletti i PRIMARI")
        time.sleep(5)

        get_data(col_name)

        print("\nRipristino i nodi")
        subprocess.run(['docker', 'start', node1])
        subprocess.run(['docker', 'start', node2])
    else:
        print("Collezione non esistente")   

def insert_with_node_offline():
    """
    Inserimento della collezione 'grades' in seguito al blocco di un nodo del sistema.
    Effettua il drop della collezione se già esistente.
    Riabilita il nodo al termine dell'inserimento.
    """
    drop_collection()

    print("Blocco un nodo dello shard3")
    node = 'shard3server' + str(randint(1,3))
    subprocess.run(['docker', 'stop', node])

    print("Attendo qualche secondo in modo che vengano rieletti i PRIMARI")
    time.sleep(5)

    print("Avvio inserimento dati...")
    insert_data()

    print("Ripristino il nodo")
    subprocess.run(['docker', 'start', node])
    

if __name__ == "__main__":
    # connessione al router mongos
    client = MongoClient("mongodb://localhost:15000")

    # ottengo il riferimento al database
    db = client.get_database('myFirstDB')

    main()

    client.close()