# Remote Laser Mover #

This project takes an Arduino Uno with two servo motors connected to it along with a laser pointer attached and opens up to different clients (still experimenting with different interfaces ATM) to allow the pointer to be controlled remotely.

<br/>

## Repository Sections ##

This repo contains different folders in the base directory.

### RemoteLaserMover_arduino ###

This folder contains the Arduino project created in PlatformIO which will host a local server and perform the motor changes.

### RemoteLaserMover_testclient ###

This folder currently contains some client tests I am working on. It is meant to have barebones functionality to help develop the Arduino portion of the project.