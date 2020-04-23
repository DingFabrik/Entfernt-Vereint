#!/bin/bash
# script ohne sudo aufrufen
sudo apt-get update && sudo apt-get upgrade -y
sudo apt -y autoremove
# git install und 
sudo apt-get -y install git
sudo apt-get -y install python3-tk
git clone https://github.com/dingfabrik/Entfernt-Vereint.git
sudo apt-get -y install chromium-browser
# remove keyring data
rm .local/share/keyrings/*
# install anydesk
wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | sudo apt-key add -
echo "deb http://deb.anydesk.com/ all main" | sudo tee /etc/apt/sources.list.d/anydesk-stable.list
sudo apt update
sudo apt -y install anydesk
# autostart 
echo "[Desktop Entry]"|sudo tee /etc/xdg/autostart/jitsiStart.desktop 
echo "Type=Application"|sudo tee -a /etc/xdg/autostart/jitsiStart.desktop 
echo "Name=JitsiStart"|sudo tee -a /etc/xdg/autostart/jitsiStart.desktop 
echo "Comment=Start for Jitsi"|sudo tee -a /etc/xdg/autostart/jitsiStart.desktop 
echo "Exec=/home/"$USER"/start_jitsi.sh"|sudo tee -a /etc/xdg/autostart/jitsiStart.desktop 
echo "Terminal=FALSE"|sudo tee -a /etc/xdg/autostart/jitsiStart.desktop 
# app starter 
echo "[Desktop Entry]"|tee Schreibtisch/AppStarten.desktop
echo "Version=1.0"|tee -a Schreibtisch/AppStarten.desktop
echo "Type=Application"|tee -a Schreibtisch/AppStarten.desktop
echo "Name=App starten"|tee -a Schreibtisch/AppStarten.desktop
echo "Comment="|tee -a Schreibtisch/AppStarten.desktop
echo "Exec=/home/"$USER"/start_jitsi.sh"|tee -a Schreibtisch/AppStarten.desktop
echo "Icon="|tee -a Schreibtisch/AppStarten.desktop
echo "Path=/home/"$USER"/Entfernt-Vereint"|tee -a Schreibtisch/AppStarten.desktop
echo "Terminal=false"|tee -a Schreibtisch/AppStarten.desktop
echo "StartupNotify=false"|tee -a Schreibtisch/AppStarten.desktop
chmod +x Schreibtisch/AppStarten.desktop
# Edit Namen
echo "[Desktop Entry]"|tee Schreibtisch/EditNamen.desktop
echo "Version=1.0"|tee -a Schreibtisch/EditNamen.desktop
echo "Type=Application"|tee -a Schreibtisch/EditNamen.desktop
echo "Name=Edit Namen"|tee -a Schreibtisch/EditNamen.desktop
echo "Comment="|tee -a Schreibtisch/EditNamen.desktop
echo "Exec=mousepad 'Entfernt-Vereint/namen.txt'"|tee -a Schreibtisch/EditNamen.desktop
echo "Icon="|tee -a Schreibtisch/EditNamen.desktop
echo "Path="|tee -a Schreibtisch/EditNamen.desktop
echo "Terminal=false"|tee -a Schreibtisch/EditNamen.desktop
echo "StartupNotify=false"|tee -a Schreibtisch/EditNamen.desktop
chmod +x Schreibtisch/EditNamen.desktop
# show manual
echo "[Desktop Entry]"|tee Schreibtisch/Anleitung.desktop
echo "Version=1.0"|tee -a Schreibtisch/Anleitung.desktop
echo "Type=Application"|tee -a Schreibtisch/Anleitung.desktop
echo "Name=Anleitung"|tee -a Schreibtisch/Anleitung.desktop
echo "Comment="|tee -a Schreibtisch/Anleitung.desktop
echo "Exec=atril 'Entfernt-Vereint/VideoLaptop Anleitung.pdf'"|tee -a Schreibtisch/Anleitung.desktop
echo "Icon="|tee -a Schreibtisch/Anleitung.desktop
echo "Path="|tee -a Schreibtisch/Anleitung.desktop
echo "Terminal=false"|tee -a Schreibtisch/Anleitung.desktop
echo "StartupNotify=false"|tee -a Schreibtisch/Anleitung.desktop
chmod +x Schreibtisch/Anleitung.desktop
# set desktop wallpaper
xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitor0/workspace0/last-image --set /home/$USER/Entfernt-Vereint/videoDF-wallpaper.png 
# set energy options - shutdown on power button press
xfconf-query -c xfce4-power-manager -p /xfce4-power-manager/power-button-action -s 4
# set energy options - when lid close
xfconf-query -c xfce4-power-manager -p /xfce4-power-manager/lid-action-on-battery -n -t int -s 0
xfconf-query -c xfce4-power-manager -p /xfce4-power-manager/lid-action-on-ac -n -t int -s 0
# set energy options - no screen lock
xfconf-query -c xfce4-power-manager -p /xfce4-power-manager/lock-screen-suspend-hibernate -s false
# starte app konfigurieren
cp ./Entfernt-Vereint/start_jitsi.sh .
chmod +x start_jitsi.sh
./start_jitsi.sh
# nach Start wieder schliessen

