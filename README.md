# UTR5

[The link to the Google Drive.](https://drive.google.com/drive/folders/0B3CkMkwtokGCRW9SM05Hc056OWc)

--------------------------------------------------------------------------------------------------------------------------

## Guide for using the Pi (work in progress, bare with me):

#### Step 0. Installing the Pi
* If you have an SD Card and a Flash drive, please see the boot and root SD Card images, flash the boot image to the SD Card and the root image to the flash drive then boot the Pi with both plugged in. (The SD Card only needs to be 100Mb or larger, the SD Card must be 4Gb or larger)  
* If you have only an SD Card--it must be 4Gb or larger--you can simply flash the 'basic pre-configured' image to the SD Card.  
* To flash images, use [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/) on Windows, and `dd if=example.img of=/dev/sdcard bs=4k` on Linux

#### Step 1. Connecting to the Pi
Now, there are many ways of connecting to the Pi with different features, I am going to list each of the *sensible* ones and their scenarios.
##### 1. The easiest: Using a UART to USB Cable
By using a UART to USB cable, it is a simple process of plugging in the RX, TX and GND pins, then connecting via a terminal emulator i.e. [PuTTY](http://www.putty.org/).  
Connect GND to pin 6
Connect RX to pin 8
Connect TX to pin 10
Please see [this diagram](http://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2a.jpg) if you are unsure on pin numbers
Once the pins are connected properly, you can launch PuTTY and click on Serial ([pic](https://i.stack.imgur.com/XgR6I.png)), then you must figured out which COM port the UART cable has been assigned to on your system. The best way to do this is to go to the device manager and go to the `Ports (COM & LPT)` section and find your adaptor ([pic](http://www.usconverters.com/images/xs1000-article/device-manager.jpg))
##### 2. Using ethernet (this can provide internet too)
##### 3. Using WiFi
connect to SSH/SFTP (configure password, hostname and networking -- crossover net)

developing and testing (nano/sftp ide/wifi for testing)
 -- and how to use github to develop -- could use github desktop + ide

flash images on (create boot and /)

install robot from github (finish install-a-pi.sh)

--------------------------------------------------------------------------------------------------------------------------------

## Images for the Raspberry Pi (All Raspbian Jessie-Pi 3 B v1.2):

  All of the custom images can be found at https://sebs.tech/pi-images/r5/
  
#### Guide for flashing Pi images:
  First off, a little reason why we need these images is because Pi SD Cards become corrupted a lot, especially when the power input is not stable which is a common problem when on battery power, which a $0.75 voltage regulator is not efficient enough to account for. So don't be surprised when the Pi won't boot because the filesystem has become effectively gibberish. This is why I have created a custom image to run the Pi from a flash drive, while only booting from a 100Mb SD Card, when the card becomes corrupted just re-flash the 100Mb boot partition and away you go.
  The `opencv` image is for compiling on raspbian so a lightweight executable can be run by the robot's script for image processing.
  
###### Basic image for SD Card-only configurations (1.5Gb): https://sebs.tech/pi-images/r5/2017-01-11-raspbian-jessie-lite-pre-configured-full-min.img
  * Serial over UART is enabled + BT is disabled for hardware UART: `raspi-config`, `dtoverlay=pi3-disable-bt >> /boot/config.txt`
  * SSH/SFTP is enabled: `raspi-config`
  * I2C is enabled: `raspi-config`
  * Pi Camera port is enabled: `raspi-config`
  * Hostname/local IP is configured: `raspi-config`, the local IP is dynamically assigned via ethernet, the hostname is `region5pi.local`
  * Username and password is configured: Username: `pi`, password: `region5`, pi is an admin user and has sudo access, but please no root login
  * Wifi ready: use SSID `2WIRE123` and PSK `QGKWMVVJ`, after enabling use `ifdown wlan0 && sleep 10 && ifup wlan0` and the Pi should pick up and IP address
  * Ethernet ready for ICS: yes
  * Disabled DHCP on boot: `raspi-config` (too slow to have it enabled)
  * Srunken filesystem: yes
  * `raspi-config` updated: yes
  * update, upgrade, dist-upgrade: yes, 25/2/17
  
###### Boot image for SD Card (100Mb): coming soon
  * Same as above but only the 100Mb boot partition
  
###### Root image for Flash Drive (1.4Gb): coming soon
  * Same as above but only the root parition, it also unmounts the SD Card to help avoid corruption
  
###### SD Card-only image for `opencv` (5.8Gb): https://sebs.tech/pi-images/r5/2017-01-11-raspbian-jessie-lite-pre-configured-full-opencv-min.img
  * Pre-configured same as the SD Card-only image but with `opencv`, `python3` and related dependencies installed
  * use `export PYTHONPATH=/usr/local/lib/python3/dist-packages/` to find `cv2.so`
  * [Install script](https://gist.githubusercontent.com/willprice/c216fcbeba8d14ad1138/raw/6e9024162b2645989d5eca6db19f81df49a6accd/install-opencv.sh)
  * +`apt-get install pip3`
  * +`pip3 install numpy`
 
###### Backup: coming soon
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

