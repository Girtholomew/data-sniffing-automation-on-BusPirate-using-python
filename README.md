# Buspirate data snifiing automation using python

# Using the BusPirate
Connected the BusPirate to my laptop. Then wired up two arduinos that are communicating using the I²C protocol, just sending numbers from the slave device to the master device. Then I used a software named Teraterm to communicate with the device. Then I opened Teraterm and selected the Serial option, and selected the port to which the BusPirate is connected to. Then I sent `?` to the device, which shows a list of available commmands that can be used.

Entered `m` to Select which protocol I want to sniff from. In order to sniff I²C traffic, entered the option which corresponded to the I²C option, which is 4. It will show the select speed option, we can skip that and just enter `W` to turn the power supplies on, followed by `P` to connect the pull-up resistors to the pins

`(0)` can then be entered to show the list of available commands that can be used. `(1)` can be entered to see if the BusPirate has detected any I²C addresses connected to it. The BusPirate returns that it detected an I²C device on its terminals, so `(2)` can be sent to sniff traffic on the I²C bus. The BusPirate should print to the Serial what its reading on the I²C bus, in Hex values.

# Automating the process using Python

Used a code editor (VSCode in my case) to write the python script. The Serial library and the time library was used for the code. 

The code sends the commands that we sent ourselves, and returns what the BusPirate reads from the I²C bus. 
