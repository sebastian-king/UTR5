# UTR5

[The link to the Google Drive.](https://drive.google.com/drive/folders/0B3CkMkwtokGCRW9SM05Hc056OWc)

--------------------------------------------------------------------------------------------------------------------------

## Guide for using the Pi:

*DM me (@seb) in the Slack for help*

#### Step 0. Installing the Pi
*SD Card images and instructions are found in the section below this*

* If you have an SD Card and a Flash drive, please see the boot and root SD Card images, flash the boot image to the SD Card and the root image to the flash drive then boot the Pi with both plugged in. (The SD Card only needs to be 100Mb or larger, the SD Card must be 4Gb or larger)  
* If you have only an SD Card--it must be 4Gb or larger--you can simply flash the 'basic pre-configured' image to the SD Card.  
* To flash images, use [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/) on Windows, and `dd if=example.img of=/dev/sdcard bs=4k` on Linux

#### Step 1. Connecting to the Pi
Now, there are many ways of connecting to the Pi with different features, I am going to list each of the *sensible* ones and their scenarios.
##### 1. The easiest: Using a UART to USB Cable
By using a UART to USB cable, it is a simple process of plugging in the RX, TX and GND pins, then connecting via a terminal emulator i.e. [PuTTY](http://www.putty.org/).  
* Connect GND to pin 6
* Connect RX to pin 8
* Connect TX to pin 10

Please see [this diagram](http://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2a.jpg) if you are unsure on pin numbers.

You can also power the Pi using the UART cable, using the `VCC` pin, however, ***MAKE ABSOLUTELY SURE YOU KNOW WHAT PIN YOU ARE PLUGGING THE VCC INTO***, if you plug the 5V `VCC` pin into the 3.3V pin that's next to it, it's probably goodbye to the Pi. The correct 5V pin should be on the outside row of pins, and is pin 2.  
Or, the Pi can also be powered via the conventional Micro USB, then just leave the `VCC` unplugged.
Once the pins are connected properly, you can launch PuTTY and click on Serial ([pic](https://i.stack.imgur.com/XgR6I.png)), then you must figure out which COM port the UART cable has been assigned to on your system. The best way to do this is to go to Device Manager and go to the `Ports (COM & LPT)` section and find your adaptor ([pic](http://www.usconverters.com/images/xs1000-article/device-manager.jpg)).  
Type that into PuTTY, e.g. COM3, then enter 115200 as the speed/baudrate, then click Open.  
You should now have a blank, black terminal. Although it is blank, type in `pi` and hit enter, you should then be prompted for the password.

A nice bonus to this method is also that the connection will survive reboots and allow you to debug failed boots.  
The downside will be providing internet, although we can connect the Pi to UT's WiFi for downloading packages quickly if using a Serial connection. We simply can't use UT's WiFi for connecting to the Pi. UT's WiFi requires MS CHAPv2 auth encryption. Also, the Serial connection will not give us the filesystem access that SFTP gives us.  
**NOTE: I'm not completely sure if the UART cable gives the Pi enough current to boot with an SD Card and flash drive together.**

##### 2. Using ethernet (this can provide internet too)
*Note:* These instructions are for configuring via Windows, Linux people should know how to Linux.

First, obviously, power up the Pi and plug in the ethernet between the Pi and your computer.

Now, do you want to provide internet for the Pi or just connect to it?

If we just want to connect to the Pi, we can connect to it by going to PuTTY and making an SSH connection to `region5pi.local`.  *However, this requires the computer knowing what `region5pi.local` resolves to. There are four ways to do this, the first is by using iTunes' Bonjour service--this is just a little mDNS resolver that will qualify the hostname. You can just install iTunes and never open it. The second method is by using something like WireShark and finding the hostname's IP address yourself, this isn't very intuitive for those who don't understand networking. Or, as a last resort, you can manually set your ethernet adaptor's details and try to connect using that IP to the Pi, or maybe even try to ping the whole ethernet adaptor's subnet.*

If we want to provide internet to the Pi as well as connecting via SSH/SFTP. We can use Window's ICS (Internet Connection Sharing), this is very simple and easy to set up and will give the Pi an IP address assigned from your computer so you don't need the iTunes/WireShark methods. Your computer can of course remain using it's own internet meanwhile providing internet to the Pi.  
The steps for ICS are as follows:
* Make your WiFi connection shared with your ethernet, described here: http://www.countrymilewifi.com/how-to-share-computers-wifi-with-ethernet-devices.aspx
* Open the command prompt, and type in `ipconfig`. Keep typing it in until the ethernet adaptor shows an IP address like `192.168.137.X`.
* Connect to that IP or `region5pi.local` using PuTTY.

##### 3. Using WiFi
Obviously to use the WiFi, it has to be first configured on the Pi. The images I have provided have the WiFi pre-configured to connect to a network called `2WIRE123` with the password `QGKWMVVJ`. If you have a phone capable of making a hotspot, you can create a hotspot with these details and the Pi will connect to your phone, then connect your laptop to your phone and try to connect to `region5pi.local` via PuTTY. *The same problems with resolving `region5pi.local` exist as for the ethernet connections, see the italicised part of that section for details.*  

If a phone is not a workable solution--due to not being able to change the name of the broadcast network or something--a little WiFi router or bridge can be set up using these details for the Pi. A WiFi router would let us develop from laptops while the robot runs around on the test field, it might be a good idea to look into setting that up.  

And last, you can of course change the WiFi details to match your hotspot, these can be modified in `/etc/wpa_supplicant/wpa_supplicant.conf` by quickly plugging into the Serial connection, or your preferred method.

#### Step 2. Configuring the Pi
I have created a script that will put the robot code onto the Pi so that it will be immediately ready to run and develop on it.
Simply download the [script from this repository](https://raw.githubusercontent.com/afloresescarcega/UTR5/master/install-a-pi.sh) and run it on the Pi.

#### Step 3. Developing on the Pi

Now that you have completed Steps 0-2, you are ready to test and code.

My preferred way of developing on the Pi is generally not liked by most people, but I think it is very convenien;t. I just pop up a WiFi hotspot, login to the Pi via SSH and develop using `nano` and it's very-very-limited syntax checking. But this method means that I can work from any device (even the terminal on my phone) without having to install anything, and I can do it wirelessly. I can also just save the file in `nano` and run the script on the Pi where it needs to be really quickly and easily.

However, this is not really a great option if you're writing something long or complicated, because you don't have a mouse and scrolling takes ages, plus there is no wrapping (overflow is cut off and takes a lot of scrolling to see). If you are writing something hefty, I would suggest an IDE on your laptop, of course. Something like Sublime or the good-old-fashioned Notepad++ will do fine since you can't test the code on your laptops (you're writing for Pi-arch-only libraries). Along with this IDE, you can use the SFTP that works along side SSH (so long as you have SSH working, you can use SFTP) this is a great way to push your code to the Pi, login with the same details as you would with SSH using a program such as FileZilla (or some IDEs come with FTP support and a key bind to push to the code) and you can just upload and test code that way.

Alternatively, instead of using SFTP you can push your code to a github experimental branch and pull that branch onto the Pi and try things that way. GitHub desktop would work nicely for that, and maintain version control for you and your coding comrades.

--------------------------------------------------------------------------------------------------------------------------------

## Images for the Raspberry Pi (All Raspbian Jessie-Pi 3 B v1.2):

  All of the custom images can be found at https://www.helpfulseb.com/pi-images/r5/
  
#### Guide for flashing Pi images:
  First off, a little reason why we need these images is because Pi SD Cards become corrupted a lot, especially when the power input is not stable which is a common problem when on battery power, which a $0.75 voltage regulator is not efficient enough to account for. So don't be surprised when the Pi won't boot because the filesystem has become effectively gibberish. This is why I have created a custom image to run the Pi from a flash drive, while only booting from a 100Mb SD Card, when the card becomes corrupted just re-flash the 67Mb boot partition and away you go.
  The `opencv` image is for compiling on raspbian so a lightweight executable can be run by the robot's script for image processing.
  
###### Basic image for SD Card-only configurations (1.5Gb): https://www.helpfulseb.com/pi-images/r5/2017-01-11-raspbian-jessie-lite-pre-configured-full-min.img
  * Serial over UART is enabled + BT is disabled for hardware UART: `raspi-config`, `dtoverlay=pi3-disable-bt >> /boot/config.txt`
  * SSH/SFTP is enabled: `raspi-config`
  * I2C is enabled: `raspi-config`
  * Pi Camera port is enabled: `raspi-config`
  * Hostname/local IP is configured: `raspi-config`, the local IP is dynamically assigned via ethernet, the hostname is `region5pi.local`
  * Username and password is configured: Username: `pi`, password: `region5`, pi is an admin user and has sudo access, but please no root login
  * Wifi ready: use SSID `2WIRE123` and PSK `QGKWMVVJ`, after enabling use `ifdown wlan0 && sleep 10 && ifup wlan0` and the Pi should pick up an IP address
  * Ethernet ready for ICS: yes
  * Disabled DHCP on boot: `raspi-config` (too slow to have it enabled)
  * Srunken filesystem: yes
  * `raspi-config` updated: yes
  * update, upgrade, dist-upgrade: yes, 25/2/17
  * TODO: must do something about hciuart service
  
###### Boot image for SD Card (67Mb): https://www.helpfulseb.com/pi-images/r5/2017-01-11-raspbian-jessie-lite-pre-configured-boot-min.img
  * Same as above but only the boot partition
  
###### Root image for Flash Drive (1.5Gb): https://www.helpfulseb.com/pi-images/r5/2017-01-11-raspbian-jessie-lite-pre-configured-root-min.img
  * Same as above but only the root parition, it also unmounts the SD Card to help avoid corruption using `noauto`
  
###### SD Card-only image for `opencv` (5.8Gb): https://www.helpfulseb.com/pi-images/r5/2017-01-11-raspbian-jessie-lite-pre-configured-full-opencv-min.img
  * Pre-configured same as the SD Card-only image but with `opencv`, `python3` and related dependencies installed
  * use `export PYTHONPATH=/usr/local/lib/python3/dist-packages/` to find `cv2.so`
  * [Install script](https://gist.githubusercontent.com/willprice/c216fcbeba8d14ad1138/raw/6e9024162b2645989d5eca6db19f81df49a6accd/install-opencv.sh)
  * +`apt-get install pip3`
  * +`pip3 install numpy`
 
###### Backup: coming soon, once we have a working set up to back up
  * Latest fully working status backed up as an .img file, root partition only, a boot partition can be added when installing

--------------------------------------------------------------------------------------------------------------------------

## Field Parts [WIP]

[comment]: <> (Visit http://www.tablesgenerator.com/markdown_tables# to easily generate tables like the one below)
[comment]: <> (Be sure to copy the table data and "File" -> "Paste table data")


| Thing                                                                                                         | Price per item | Quantity      | Where to buy | Link                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------|----------------|---------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------|
| 16 Feet of 2' x 4' (2 in. x 4 in. x 8 ft)                                                                     | 3.37           | 2             | Home Depot   | http://www.homedepot.com/p/2-in-x-4-in-x-8-ft-2-Ground-Contact-Pressure-Treated-Lumber-106147/206970948                              |
| 1⁄2” x 4’ x 8’ MDF panels.                                                                                    | $22.15         | 2             | Home Depot   | http://www.homedepot.com/p/MDF-Panel-Common-1-2-in-x-4-ft-x-8-ft-Actual-1-2-in-x-49-in-x-97-in-M31240849097000000A/202332602         |
| 3/16” x 7’ x 7’ pegboard comes in 3/16 in. x 4 ft. x 8 ft                                                     | 19.37          | 2             | Home Depot   | http://www.homedepot.com/p/Pegboard-White-Panel-Common-3-16-in-x-4-ft-x-8-ft-Actual-0-155-in-x-47-7-in-x-95-7-in-486140/202189722    |
| Forty nine 2”x1’x1’ “grid blocks” cut from sheets of Extruded Polystyrene (XPS) comes in 2 in. x 4 ft. x 8 ft | 36.73          | 2             | Home Depot   | http://www.homedepot.com/p/Owens-Corning-FOAMULAR-150-2-in-x-4-ft-x-8-ft-R-10-Scored-Squared-Edge-Insulation-Sheathing-45W/100320352 |
| One 1⁄4” x 3’ x 7’ clear acrylic sheet                                                                        | ?              | 1             |              |                                                                                                                                      |
| one 1⁄4” x 4’ x 7’ clear acrylic sheet                                                                        | ?              | 1             |              |                                                                                                                                      |
| 1⁄4 – 20 x 2-1/2 inch flat Phillips head machinescrews and T-nuts.                                            |                | Unclear if 20 |              |                                                                                                                                      |

[Image of an assembled field](http://imgur.com/a/lrKux.jpg)

