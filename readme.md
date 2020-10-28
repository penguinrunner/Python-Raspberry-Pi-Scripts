# Python Scripts

## Setup

###Downloading the Demo Scripts
* Open a terminal
    * Your terminal will always opens to your home folder
    * if you type `ls` you will "list" the conents of that folder
* Paste this command into the terminal
    * `git clone https://github.com/penguinrunner/Python-Raspberry-Pi-Scripts.git`
* Open the your home folder with the file browser and you will see a folder named `Python-Raspberry-Pi-Scripts`
* Now you have the project files!


###Installing Dependencies
* In a terminal copy and run this command 
    * `pip3 install RPi.GPIO`
    * This just uses Python3's package manager to install some things we need.


###Running the scripts
* All of the scripts are written for Python3 (not Python2 or Python2.7)
* In the terminal type `cd Python-Raspberry-Pi-Scripts` and you will enter that folder via the terminal
    * Remember you can type `ls` to see all the files in the terminal
* From here type `python3 hello_world.py` to run our first script
* If you see the output `Hello world from the world of python!` then it worked
* you can now run the rest of the scripts by typing `python3` and then the name of the script!



###Outputs
* Blink Led 1
    * General Setup of the script
    * Import needed libraries
    * Setup pin as an output
    * Turn the output on and off
    
    
* Blink Led 2
    * General Setup of the script
    * Import needed libraries
    * Setup pins as an outputs
    * Turn the output on and off
    * Uses two outputs


### Inputs
* Button Press 1
    * Basics of detecting an input on a GPIO pin


* Button Press 2
    * Basics of detecting an input on a GPIO pin
    * Control an output based on the input
    
    
* Button Press 3
    * Basics of detecting an input on a GPIO pin
    * Control an output based on the input
    * Non Blocking code while controlling each input/output
    
    
* Button Press 3
    * Basics of detecting an input on a GPIO pin
    * Control an output based on the input
    * Non Blocking code while controlling each input/output
    
    
* Button Press 4 (Can be skipped)
    * Basics of detecting an input on a GPIO pin
    * Control an output based on the input
    * Non Blocking code while controlling each input/output
    * Display which button is pressed on 1602A LCD Display
    
    
* Button Press 5
    * Basics of detecting an input on a GPIO pin
    * Control an output based on the input
    * Non Blocking code while controlling each input/output
    * Detect both the Rising and Falling of the input and control an out accordingly
    
    
### LCD Display
