<h3>TP Password Attack</h3>
<hr>
<h5>Le fichier shadow</h5>
Le fichier shadow présent sur linux (chemin : /etc/shadow) contient les
mot de passes chiffrés des utilisateurs ainsi que quelques informations sur l'age du mot passe. Voici la structure : <br>
<p style="border-top: 1px solid lightgray; border-bottom: 1px solid lightgray; padding: 10px 0px;">
<b>username:password:UID:GID:full_name:directory:shell</b>
</p>
<h4>Structure du fichier</h4>
<p><b>username</b><br>
Nom de l'utilisateur<br>
<b>password</b><br>
Le hash du mot de passe<br>
<b>UID: User id</b><br>
int : id de l'utlisateur<br>
<b>GID : Groupe ID</b><br>
int : id du Groupe auquel il appartient<br>
<b>full_name</b><br>
Nom complet de l'utilisateur (nom / prenom)
<br>
<b>directory</b><br>
Répertoire personnel de l'utilisateur<br>
<b>shell</b><br>
Shell par défaut de l'utilisateur
</p>
<hr>
<h3>Algorithme de hashage</h3>
<p>L'algorithme cryptographique utilisé pour generer les hash est le MD5.</p>
<hr>
<h3>Attaque par brute force</h3>
<p>L'attaque par brute force consiste à tester toute sortes de combinaisons
pour deviner le mot de passe ou identifiant d'un utilisateur et se connecter à son compte.
La première contre-mesure à prendre est de limiter le nombre d'essai de connection (rate-limiting) et d'adopter les bests pratices pour generer un mot de passe
fort qui mettrait trop longtemps à l'attaquant de découvrir.</p>
<h5>Exemple</h5>
Voici mon fichier python : <a href="">url</a>.
<ul>
<li>On commence par créer une chaine de caractéres aleatoire defini par sa longueur minimum (ici 4) et maximum (6).
On répéte cette tache de maniere continue pour tester n'importe quelle combinaison.</li>
<li>On chiffre ensuite cette chaine de caractere en MD5 et on a la compare aux différents hash présent dans le fichier shadow.</li>
<li>Beaucoup de patience.....</li>
</ul>
<hr>
<h3>Attaque par dictionnaire</h3>
<p>L'attaque par dictionnaire consiste à utiliser une liste de mots définit déjà par défaut par un fichier trouvé sur le net
ou en créant son propre dictionnaire par le biais de l'ingenierie sociale et de parcourir ce dictionnaire en comparant les hash.</p>
<h5>Exemple</h5>
Voici mon fichier python : <a href="">url</a>
<ul>
<li>On ouvre le fichier shadow et recupères les données.</li>
<li>On lit le dictionnaire et chiffre chaque donnée en MD5.</li>
<li>Comparaison des hash entre les deux fichier, si ça match un mot de passe est trouvée.</li>
<li>Le tour est joué!</li>
</ul>
<hr>
<h3>Avantage et inconvénients</h3>
<p>Chaque méthode posséde une certaine effacité mais amene aussi beaucoup de contraintes :</p>
<h5>Attaque par Brute force</h5>
<table class="table">
<tr>
    <th>Avantages</th>
    <th>Inconvenients</th>
</tr>
<tr>
    <td>100 % efficace! / Simple d'utilisation</td>
    <td>Le temps</td>
</tr>
</table>
<h5>Attaque par dictionnaire</h5>
<table class="table">
<tr>
    <th>Avantages</th>
    <th>Inconvenients</th>
</tr>
<tr>
    <td>Rapide </td>
    <td>N'est pas efficace a 100%</td>
</tr>
</table>
