#!/bin/bash
cp -R /home/pi/.octoprint /home/pi/.octoprint2
cp -R /home/pi/.octoprint /home/pi/.octoprint3
cp -R /home/pi/.octoprint /home/pi/.octoprint4
sudo chown -R pi:pi /home/pi/.octoprint2
sudo chown -R pi:pi /home/pi/.octoprint3
sudo chown -R pi:pi /home/pi/.octoprint4
cd /etc/systemd/system/
sudo sed s/127.0.0.1/0.0.0.0/ < octoprint.service | sed s/5000/5001/ | sed s/--port=\${PORT}/--port=\${PORT}\ --basedir=\\/home\\/pi\\/\.octoprint2/ > octoprint2.service
sudo sed s/127.0.0.1/0.0.0.0/ < octoprint.service | sed s/5000/5002/ | sed s/--port=\${PORT}/--port=\${PORT}\ --basedir=\\/home\\/pi\\/\.octoprint3/ > octoprint3.service
sudo sed s/127.0.0.1/0.0.0.0/ < octoprint.service | sed s/5000/5003/ | sed s/--port=\${PORT}/--port=\${PORT}\ --basedir=\\/home\\/pi\\/\.octoprint4/ > octoprint4.service
sudo systemctl enable octoprint2
sudo systemctl enable octoprint3
sudo systemctl enable octoprint4
sudo systemctl start octoprint2
sudo systemctl start octoprint3
sudo systemctl start octoprint4
echo "SUBSYSTEM==\"tty\", ATTRS{idVendor}==\"0403\", ATTRS{idProduct}==\"6001\", ATTRS{devpath}==\"\", ATTRS{serial}==\"AM00N6SL\", SYMLINK+=\"M100\"" > /etc/udev/rules.d/99-usb.rules
echo "SUBSYSTEM==\"tty\", ATTRS{idVendor}==\"0403\", ATTRS{idProduct}==\"6001\", ATTRS{devpath}==\"\", ATTRS{serial}==\"AB0KDT74\", SYMLINK+=\"M200\"" >> /etc/udev/rules.d/99-usb.rules
echo "SUBSYSTEM==\"tty\", ATTRS{idVendor}==\"0403\", ATTRS{idProduct}==\"6001\", ATTRS{devpath}==\"\", ATTRS{serial}==\"AB0KDFPC\", SYMLINK+=\"M300\"" >> /etc/udev/rules.d/99-usb.rules
echo "SUBSYSTEM==\"tty\", ATTRS{idVendor}==\"0403\", ATTRS{idProduct}==\"6001\", ATTRS{devpath}==\"\", ATTRS{serial}==\"AR0K4OMU\", SYMLINK+=\"M400\"" >> /etc/udev/rules.d/99-usb.rules