# UTR5

[The link to the Google Drive.](https://drive.google.com/drive/folders/0B3CkMkwtokGCRW9SM05Hc056OWc)

--------------------------------------------------------------------------------------------------------------------------

Guide for using the Pi (work in progress, bare with me):

TODO:

connect to SSH/SFTP (configure password, hostname and networking -- crossover net)

developing and testing (nano/sftp ide/wifi for testing)
 -- and how to use github to develop -- could use github desktop + ide

flash images on (create boot and /)

install robot from github (finish install-a-pi.sh)

--------------------------------------------------------------------------------------------------------------------------------

## Images for the Raspberry Pi (All Raspbian Jessie-Pi 3 B v1.2):

  All of the custom images can be found at https://sebs.tech/pi-images/r5/
  
#### Guide for flashing Pi images:
  First off, a little reason why we need these images is because Pi SD Cards become corrupted a lot, especially when the power input is not stable which is a common problem when on battery power, which a $0.75 is not efficient enough to account for. So don't be surprised when the Pi won't boot because the filesystem has become effectively gibberish. This is why I have created a custom image to run the Pi from a flash drive, while only booting from a 100Mb SD Card, when the card becomes corrupted just re-flash the 100Mb boot partition and away you go.
  The `opencv` image is for compiling on raspbian so a lightweight executable can be run by the robot's script for image processing.
  
###### Basic image for SD Card-only configurations (1.5Gb): https://sebs.tech/pi-images/r5/2017-01-11-raspbian-jessie-lite-pre-configured-full-min.img
  * Serial over UART is enabled + BT is disabled for hardware UART: `dtoverlay=pi3-disable-bt >> /boot/config.txt`
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
 
 Backup:
  * latest fully working status backed up as a .img file -- root partition only, a boot partition can be added when installing

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

