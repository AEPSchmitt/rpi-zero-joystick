# rpi-zero-joystick
USB Joystick using a RPi zero as the controller

![front](https://user-images.githubusercontent.com/9079958/203825713-0c92cdd8-e0c5-41dc-a1be-481c72eb6f3f.jpg)
![back](https://user-images.githubusercontent.com/9079958/203825724-0f0f1d84-456d-44ae-966c-154d751dac32.jpg)

Default configuration sends direction via USB as keyboard arrow key inputs

# Setup Pi Zero as a USB device using
```
sudo echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
sudo echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules
```

# Connect Pi and Joystick
![pin_guide](https://user-images.githubusercontent.com/9079958/203833725-930b8ebe-c719-4736-a3ca-f6de4dd2146d.png)
Use these pins or change the connections in the joystick.py file
