# data-sniffing-automation-on-BusPirate-using-python

# Using the BusPirate
I connected the BusPirate to my laptop. Then I wired up two arduinos that are communicating using the I²C protocol, just sending numbers from the slave device to the master device. Then I used a Software named Teraterm to communicate with the device. Then I opened Teraterm and selected the Serial option, and selected the port to which the BusPirate is connected to. Then I sent `?` to the device, which shows a list of available commmands that can be used.

I then entered `m` to Select which protocol I want to sniff from. I wanted to sniff I²C traffic, so I entered the option which corresponded to the I²C option, which is 4. then it will show the select speed option, we can skip that and just enter `W` to turn the power supplies on, followed by `P` to connect the pull-up resistors to the pins

We can then enter `(0)` to show the list of available commands that can be used. We can enter `(1)` to see if the BusPirate has detected any I²C addresses connected to it. The BusPirate returns that it detected an I²C device on its terminals, so we can send `(2)` to sniff traffic on the I²C bus. The BusPirate should print to the Serial what its reading on the I²C bus, in Hex values.

# Automating the process using Python

I used a code editor (VSCode in my case) to write the python script. I've used the Serial library and the time library for the code. 

The code sends the commands that we sent ourselves, and returns what the BusPirate reads from the I²C bus. 
