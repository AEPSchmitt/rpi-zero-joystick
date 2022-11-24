# rpi-zero-joystick
USB Joystick using a RPi zero as the controller

![20221124_162355](https://user-images.githubusercontent.com/9079958/203823412-d64952d0-b818-4908-8cc7-6daa2401da2f.jpg)
![20221124_162401](https://user-images.githubusercontent.com/9079958/203823588-61804350-8956-43ec-8aa7-945b60696ae7.jpg)

# Setup Pi Zero as a USB device using
```
sudo echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
sudo echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules
```
