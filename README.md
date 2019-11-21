# deeprobot
Ressources for the DeepRobot training session

## Modifications des robots 

Pour les séances de TP, des robots Turtlebot3 seront utilisés. Pour lancer des algos de Deep Learning, nous remplacerons les cartes Raspberry Pi3 d'origine par des cartes Nvidia Jetson Nano. 

Des premières consignes sont disponibles sur ce dépôt hébergé à l'UTC : [gitlab-utc](https://gitlab.utc.fr/hds/turtlebot/installation-nvidia-jetson-nano)

### Liste des équipements nécessaires

Liste du matériel nécessaire pour installer les cartes Nvidia Jetson Nano sur les Turtlebot 3 : 
- Carte Nvidia Jetson Nano : [Jetson Nano](https://www.generationrobots.com/fr/403351-kit-de-developpement-nvidia-jetson-nano.html)
- Carte MicroSD de 32 Go minimum 
- Alimentation 5V 2A, non fourni dans le kit Jetson. Pour les tests sur table, il est possible de réutiliser l'alimentation de la Raspberry Pi3 qui fournit 2.5A sur 5V. Nous verrons par la suite comment fournir l'énergie nécessaire en embarqué. 
- Module Wifi : la Jetson Nano ne dispose pas de Wifi nativement. Il est possible d'ajouter des [dongles USB Wifi](https://www.generationrobots.com/fr/401554-dongle-wifi-pour-brickpi.html) ou une [carte PCIe Wifi](https://www.amazon.fr/Coolwell-Waveshare-Wireless-Bluetooth-Connector/dp/B07VRKKLCM/ref=sr_1_7?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=wifi+jetson+nano&qid=1568723686&sr=8-7). 
- une [caméra Raspberry Pi v2](https://www.generationrobots.com/fr/402231-module-camera-pi-noir-pour-raspberry-pi.html)
- un support de caméra. On pourra réutiliser les équerres de maintien de batteries disponibles sur les turtlebot3 pour fixer la caméra. 

### Installation sur le robot

Etape 1 : démonter la Raspberry, pour cela vous pouvez vous aider des étapes de montage [Turtlebot3 Harware Setup](http://emanual.robotis.com/docs/en/platform/turtlebot3/hardware_setup/)

Etape 2 : ajout des composants 

- installer la carte Wifi sur la Jetson
- installer la caméra RpiV2 sur le port 


TODO: mettre une photo


Etape 3 : installation de la carte Jetson sur le robot
- comme indiqué [ici](https://gitlab.utc.fr/hds/turtlebot/installation-nvidia-jetson-nano), placez de préférence la carte pour que les ports soient à l'arrière

TODO: mettre une photo

- alimentation électrique : TODO 

Etape 4 : installation mécanique 

TODO: Mettre une photo

## Installation logicielle

### Installation et mise à jour du système d'exploitation
Suivre la procédure d'installation du système sur une carte microSD prédite [ici](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write).
Attention, à la place de télécharger l'image proposée, on utilisera à la place [celle-ci](https://developer.download.nvidia.com/training/nano/dlinano_v1-0-0_image_20GB.zip).
 
Mettez à l'heure votre carte Jetson Nano : 
```
sudo date -s '31 OCT 2019 14:23:35'
```

Si vous obtenez ce message : 
```
dlinano@jetson-nano:~$ sudo apt dist-upgrade 
E: Could not get lock /var/lib/dpkg/lock-frontend - open (11: Resource temporarily unavailable)
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), is another process using it?
```
désactiver les services systemd de mises à jour automatiques des paquets qui peuvent vous bloquer lors des appels **apt** : 
```
sudo systemctl disable apt-daily.timer
sudo systemctl disable apt-daily-upgrade.timer
sudo systemctl stop apt-daily.timer
sudo systemctl stop apt-daily-upgrade.timer
```
Vous aurez peut-être besoin de tuer certains process à la main : 
```
ps aux 

root      7106  0.0  0.0   1912   480 ?        Ss   05:42   0:00 /bin/sh /usr/lib/apt/apt.systemd.daily update
root      7115  0.0  0.0   1912  1232 ?        S    05:42   0:00 /bin/sh /usr/lib/apt/apt.systemd.daily lock_is_held 
root      7841 21.1  2.1 242116 85676 ?        Sl   05:43   5:09 /usr/bin/python3 /usr/bin/unattended-upgrade --downl
```

Lancer les mises à jour de l'OS
```
sudo apt update
sudo apt -y dist-upgrade 
```

### Installation de ROS
Suivre l'installation de ROS Melodic comme expliqué [ici](http://wiki.ros.org/melodic/Installation/Ubuntu)

### Installation des dépots Turtlebot3 

Suivre les instructions ici : http://emanual.robotis.com/docs/en/platform/turtlebot3/raspberry_pi_3_setup/#install-linux-ubuntu-mate

```
mkdir -p ~/catkin_ws/src 
cd ~/catkin_ws/src
git clone https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
cd ~/catkin_ws/src/turtlebot3
sudo rm -r turtlebot3_description/ turtlebot3_teleop/ turtlebot3_navigation/ turtlebot3_slam/ turtlebot3_example/
sudo apt-get install ros-melodic-rosserial-python ros-melodic-tf
source /opt/ros/melodic/setup.bash
cd ~/catkin_ws/
catkin_make
source ~/catkin_ws/devel/setup.bash
rosrun turtlebot3_bringup create_udev_rules
```

Configuration du ~/.bashrc, ajoutez ces lignes : 

```
export ROS_MASTER_URI=http://127.0.0.1:11311
export HOSTNAME=127.0.0.1
export TURTLEBOT3_MODEL=burger
```

Puis recharger le fichier :
```
source ~/.bashrc
```
