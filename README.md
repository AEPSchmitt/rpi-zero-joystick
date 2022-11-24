# rpi-zero-joystick
USB Joystick using a RPi zero as the controller

# Setup Pi Zero as a USB device using
```
sudo echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
sudo echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules
```
