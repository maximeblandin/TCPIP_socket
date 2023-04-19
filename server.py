import socket

# CONSTANTE : Numéro de port. Le port de communication TCP de KUKA est :
C_numPort = 8000
# CONSTANTE : Nom de domaine.
C_domaineServeur = socket.gethostname()

# Création d une socket socketServeur, dont l address family est AF_INET (iPv4) et le type est SOCK_STREAM.
socketServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Lien entre la socket et le serveur.
socketServeur.bind((C_domaineServeur, C_numPort))
# Creation du serveur TCP-IP. On autorise 1 requête de connexion.
socketServeur.listen(1)
# Acceptation des connexions externes. La socket créée se nomme socketClient et possède l'adresse adresseClient
(socketClient, adresseClient) = socketServeur.accept()

# Affichage de l adresse du client connecté.
print("{} connecte.".format(adresseClient))
while True:
    # Lecture du message. Taille maximale : 1024 bits.
    data = socketClient.recv(1024).decode()
    if not data:
        # break si reception vide.
        break
    print("from connected user: " + str(data))

print("Connexion close.")
socketClient.close()
