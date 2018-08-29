# RoboPi Reference

## SSH Remote Access
On your laptop, connect to the Robo wireless network (password provided by your teachers), open the Terminal app, and type:

```
ssh student@192.168.21.XXX
```

...where XXX is the number of your RoboPi (robo-XXX)

SSH Password: Engineering!1

## Manual Control
You will be using SSH to remotely control the robot. Use the code from the BSMRKRS robo-control repository.

## Web Interface
http://192.168.21.XXX

...where XXX is the number of your RoboPi (robo-XXX)

The web page is stored in /home/student/robo-html and updated from the BSMRKRS robo-html repository

## Autonomy / Sensors
https://github.com/BSMRKRS/robotonomy

This code has examples for using sensors and sending feedback to the web interface.

## Camera
Start the camera:
```
/home/student/start_camera.sh &
```

Stop the camera:
```
/home/student/stop_camera.sh
```

View the camera: </br>
http://192.168.21.XXX:8080

## Using the terminal
Read through this tutorial on using the shell: http://ryanstutorials.net/linuxtutorial/navigation.php

## Pin Documentation

**Important Pin Info:**

Pins Servo 0 - 7 and ADC pins share bandwidth; This means that a device can not be plugged into a Servo 0 - 7 pin and an ADC pin label with the same number. Example: Servo 5 and ADC 5 can not be used at the same time. </br>

**Correct Pin Numbers (Mikronauts's Pin Labeling is incorrect):**

![alt text](https://github.com/BSMRKRS/bsmLib/blob/master/docs/pics/pins.jpg)


## New RoboPi Setup
- Enable and swap bluetooth/console serial aliases
  - Edit `/boot/config.txt`
  ```
  sudo nano /boot/config.txt
  ```
    - Change (or add) `enable_uart=0` to `enable_uart=1`
    - Add:
    ```
    #swap BT and serial ports
    dtoverlay=pi3-miniuart-bt
    ```
  - Reboot
  ```
  sudo reboot now
  ```
