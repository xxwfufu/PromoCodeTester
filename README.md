Étapes pour lancer Chrome en mode debug
Ferme toutes les fenêtres Chrome ouvertes.

Ouvre une invite de commandes (Terminal) :

Sur Windows :

Appuie sur Win + R, tape cmd puis Entrée.

Sur macOS :

Ouvre Spotlight (Cmd + Espace), tape Terminal puis Entrée.

Sur Linux :

Ouvre ton terminal habituel.

Lance Chrome avec l’option remote debugging :

Windows :
Copie-colle la commande suivante (modifie le chemin si besoin) :

kotlin
Copier
Modifier
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:/ChromeDebug"
--remote-debugging-port=9222 active le mode debug sur le port 9222.

--user-data-dir="C:/ChromeDebug" crée un nouveau profil utilisateur Chrome pour éviter de fermer ton Chrome principal.

macOS :

swift
Copier
Modifier
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/ChromeDebug"
Linux :

kotlin
Copier
Modifier
google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/ChromeDebug"
Une fois lancé, Chrome s’ouvre normalement.

Ouvre la page où tu veux tester les codes (ex: site de promo).

Lance ton script Python.
https://www.roblox.com/fr/redeem
