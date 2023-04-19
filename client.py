import socket

# Nom d'hote du serveur.
domaineServeur = '192.168.1.1'
# Numéro de port du serveur.
portServeur = 32002


# Instance de la socket client.
socketClient = socket.socket()
# Connexion au serveur.
socketClient.connect((domaineServeur, portServeur))
# Initialisation de la communication
message = ''

# Envoi de messages tant que message différent de "fin".
while message.lower().strip() != 'fin':
    # Actualisation du message.
    #message = input(" -> ")
    # Envoi du message.
    #socketClient.send(message.encode())
    WENGLOR = socketClient.recv(1024)
    print(WENGLOR)

# Fermeture de la connexion
socketClient.close()
