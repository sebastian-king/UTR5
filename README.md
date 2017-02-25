# UTR5

[The link to the Google Drive.](https://drive.google.com/drive/folders/0B3CkMkwtokGCRW9SM05Hc056OWc)

--------------------------------------------------------------------------------------------------------------------------

Guide for using the Pi (work in progress, bare with me):

TODO:

connect to SSH/SFTP (configure password, hostname and networking -- crossover net)

developing and testing (nano/sftp ide/wifi for testing)
 -- and how to use github to develop -- could use github desktop + ide

flash images on (create boot and /)
d
install robot from github (finish install-a-pi.sh)

Images (All Raspbian Jessie, and Pi 3 B):
 basic configured SD:
  * serial enabled + diable BT for hard uart -- dtoverlay=pi3-disable-bt >> /boot/config.txt
  * ssh enabled -- raspi-config
  * i2c enabled -- raspi-config
  * hostname + local IP -- raspi-config && keep local IP assigned by the PI so that eth requests on variable subnets work
  * username + password -- username: pi, passwd: `passwd`, no root:root login please, only pi:root.
  * not expanded -- yes
  * wifi ready -- use 2WIRE123 QGKWMVVJ, after enabling use `ifdown wlan0 && sleep 10 && ifup wlan0`
  * eth net ready -- yes, ICS
  * pi camera enabled -- raspi-config
  * disable dhcp on boot -- raspi-config (too slow to have it enabled)
  
  ```
  network={
        ssid="2WIRE123"
        psk="QGKWMVVJ"
  }
  ```
 
 basic boot SD:
  * same as above but only 100Mb boot partition
  
 basic flash drive:
  * same as above but only the 4Gb root parition -- somehow unmounts boot post-post

 opencv:
  * partition pre-configured same as the SD card but with opencv installed for compiling on the architechture
 
 backup:
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

