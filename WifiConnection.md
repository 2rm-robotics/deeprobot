# Connexion à un réseau Wifi WPA2 Enterprise en ligne de commande

Procédure :
- SSID  = eduroam
- CONNECTION_NAME = EDUROAM
- USERNAME = votre login, souvent adresse email complète, prenom.nom@mon-univ.fr  

```
# nmcli con add type wifi ifname wlan0 con-name CONNECTION_NAME ssid SSID
# nmcli con edit id CONNECTION_NAME
nmcli> set ipv4.method auto
nmcli> set 802-1x.eap peap
nmcli> set 802-1x.phase2-auth mschapv2
nmcli> set 802-1x.identity USERNAME
nmcli> set wifi-sec.key-mgmt wpa-eap
nmcli> save
nmcli> activate
```

Au prompt, on demande votre mot de passe. Une fois la connexion active, pour quitter :
```
nmcli> quit
```

Si connecté à la cible par Ethernet via routeur, il existe peut-être une route par défaut qui oriente tout le trafic (notamment les connexions vers Internet) vers la connexion RJ45. Il est nécessaire de supprimer cette route.

La première commande affiche la route et la seconde efface la route par défaut qui passe par la passerelle 192.168.0.1 (gateway de la connexion Ethernet RJ45) :
```
netstat -rn
sudo route del default gw 192.168.0.1
```

**Attention, NetworkManager permet d'afficher le mot de passe, il est conseillé de supprimer la connexion créée si la carte est utilisée par d'autres**
```
nmcli connection delete id CONNECTION_NAME
```
