# deeprobot
Ressources for the DeepRobot training session

## Modifications des robots 

Pour les séances de TP, des robots Turtlebot3 seront utilisés. Pour lancer des algos de Deep Learning, nous remplacerons les cartes Raspberry Pi3 d'origine par des cartes Nvidia Jetson Nano. 

Des premières consignes sont disponibles sur ce dépôt hébergé à l'UTC : [gitlab-utc](https://gitlab.utc.fr/hds/turtlebot/installation-nvidia-jetson-nano)

### Liste des équipements nécessaires

Liste du matériel nécessaire pour installer les cartes Nvidia Jetson Nano sur les Turtlebot 3 : 
- Carte Nvidia Jetson Nano : [Jetson Nano](https://www.generationrobots.com/fr/403351-kit-de-developpement-nvidia-jetson-nano.html)
- Carte MicroSD de 16 Go minimum 
- Alimentation 5V 2A, non fourni dans le kit Jetson. Pour les tests sur table, il est possible de réutiliser l'alimentation de la Raspberry Pi3 qui fournit 2.5A sur 5V. Nous verrons par la suite comment fournir l'énergie nécessaire en embarqué. 
- Module Wifi : la Jetson Nano ne dispose pas de Wifi nativement. Il est possible d'ajouter des [dongles USB Wifi](https://www.generationrobots.com/fr/401554-dongle-wifi-pour-brickpi.html) ou une [carte PCIe Wifi](https://www.amazon.fr/Coolwell-Waveshare-Wireless-Bluetooth-Connector/dp/B07VRKKLCM/ref=sr_1_7?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=wifi+jetson+nano&qid=1568723686&sr=8-7). 
- une [caméra Raspberry Pi v2](https://www.generationrobots.com/fr/402231-module-camera-pi-noir-pour-raspberry-pi.html)
- un support de caméra. A compléter. 

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

## Installation logiciel

### Installation du système d'exploitation
Suivre la procédure d'installation du système sur une carte microSD prédite [ici](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write).
Attention, à la place de télécharger l'image proposée, on utilisera à la place [celle-ci](https://developer.download.nvidia.com/training/nano/dlinano_v1-0-0_image_20GB.zip).

### Installation de ROS
Suivre l'installation de ROS Melodic comme expliqué [ici](http://wiki.ros.org/melodic/Installation/Ubuntu)
