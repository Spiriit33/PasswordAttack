import re, itertools, hashlib, sys, datetime



start=datetime.datetime.now()
maxLength = 5
minLength = 3
string=""
size=0
alphaBay  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@','_','#','-2','1','2','3','4','5','6','7','8','9']



def redo(string,size):
    if size <= maxLength:
        for i in alphaBay:
            calcString=string+i
            calcSize=size+1
            redo(calcString,calcSize)
            if minLength <= len(string):
                current_hash=hashlib.md5(calcString.encode('utf')).hexdigest()
                if current_hash in users.values():
                    time = datetime.datetime.now() - start;
                    print('mot de passe trouve \'{}\' pour l\'utilisateur {}'.format(calcString, ','.join(i for i in users if users[i] == current_hash)))


with open('shadow', 'r') as f:
    lines = f.readlines()

users = {}

for line in lines:
   try:
      user, user_hash = re.findall('^([^:]+):\$1\$([^:]+):.+', line)[0]
   except IndexError:
      continue  # si la ligne ne contient pas de hash on passe a la ligne suivante
   else:
      users[user] = user_hash

print('\n'+str(len(users))+' Mot de passe chiffré sous MD5 trouvé (entre '+str(minLength+1)+' et '+str(maxLength+1)+' caractères), dechiffrage en cours...\n')
sys.stdout = open('brut_force_decrypt.txt', 'w')
redo(string,size)

