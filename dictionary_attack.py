import re, itertools, hashlib, sys

with open('shadow', 'r') as s:
   lines = s.readlines()

users = {}
for line in lines:
   try:
      username, user_hash = re.findall('^([^:]+):\$1\$([^:]+):.+', line)[0]
   except IndexError:
      continue  # si la ligne ne contient pas de hash on passe a la ligne suivante
   else:
      users[username]=user_hash

with open('dico_mini_fr', 'r') as d:
   lines = d.readlines()

for line in lines:
    word = line.strip()
    userHash = hashlib.md5(word.encode('utf')).hexdigest() #Pour chaque ligne on hash le mot.
    for username, password in users.items():
        if userHash == password: # On verifie si le hash du mot courant correspond a un hash du fichier shadow.
            print("Le mot de passe trouver pour l'utilisateur "+username+" est: "+word)
