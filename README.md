# Zynq™ UltraScale+™ MPSoC (Kria KV260) Arch Linux

1. [FPGA Project Kria KV260](#fpga-project-kria-kv260)
    * [Requirements](#requirements)
    * [FPGA Design](#fpga-design)
2. [Petalinux Project](#petalinux-project)
    * [Requirements](#requirements-1)
    * [Creating a Petalinux Project](#creating-a-petalinux-project)
    * [Configuring a Petalinux Project](#configuring-a-petalinux-project)  
    * [Building a Petalinux Project](#building-a-petalinux-project)  
    * [Packaging a Petalinux Project](#packaging-a-petalinux-project)
    * [Preparing the Arch Linux ARM rootfs](#preparing-the-arch-linux-arm-rootfs)
    * [Preparing an SD card](#preparing-an-sd-card)
3. [Booting the Kria KV260 board](#booting-the-kria-kv260-board)
    * [Setting up the Arch Linux ARM](#setting-up-the-arch-linux-arm)
    * [Installing packages](#installing-packages)
    * [System information](#system-information)
    * [Installing fgpautil](#installing-fpgautil)


## FPGA Project (Kria KV260)

The FPGA project was created with Vivado ML Edition 2023.2.
### Requirements
* [Vivado ML Edition - 2023.2](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools.html)

### FPGA Design
A new project is created with the Vivado New Project Wizard. After the project is created, the block design is created with the Vivado IP Integrator. The block design is created with the following IP blocks:
* Zynq UltraScale+ MPSoC (set up in accordance with the requirements. The file Zynq UltraScale+ MPSoC LPD.tcl with presets for the Zynq UltraScale+ MPSoC can be found in the folder **Kria KV260**)
* Processor System Reset
* AXI Interconnect
* AXI BRAM Controllers
* Block Memory Generator
* System ILA (connected to the M_AXI_HPM0_LPD interface)

See the following image for the block design:
![Example FPGA Design to create Petalinux project](Images/fpga_design.jpg "FPGA Design Example")

This is an simple example of an FPGA design to create a Petalinux project based on the [Kria KV260](https://www.xilinx.com/products/som/kria/kv260-vision-starter-kit.html). 

After creating the block design, the design is validated, synthesized, implemented and generated bitstream. Then it is required to export hardware, including bitstream *<project_name>.xsa*. The XSA file is used to create a Petalinux project. The XSA file *kria_kv260_bd_wrapper.xsa* is located in the folder **Kria KV260**.

When the XSA file has been exported successfully, a Petalinux project is ready to be created.

## Petalinux Project

### Requirements

* [PetaLinux Tools Documentation: Reference Guide (UG1144)
](https://docs.xilinx.com/r/en-US/ug1144-petalinux-tools-reference-guide)
* [Ubuntu 22.04.2 LTS (virtual machine is preferred)](https://old-releases.ubuntu.com/releases/20.04.2/)
* [PetaLinux Tools 2023.2 (installed according to the documentation)](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/embedded-design-tools.html)

### Creating a Petalinux Project
An empty project is created with the following command:
```
petalinux-create --type project --template zynqMP --name <project name>
cd <project name>
```
### Configuring a Petalinux Project
After the project is created, the XSA file is imported with the following command:
```
petalinux-config --get-hw-description ~/<file_name>.xsa
```
After the XSA file has been imported successfully, the PetaLinux system configuration is opened. The following settings are changed:
```
→ Subsystem AUTO Hardware Settings  --->
	Ethernet Settings  --->
		[*] Randomise MAC address

→ FPGA Manager --->
	[*] Fpga Manager
	
→ Image Packaging Configuration --->
	Root filesystem type (INITRAMFS) --->
		(X) INITRAMFS
	(petalinux-initramfs-image) INITRAMFS/INITRD Image name
		petalinux-initramfs-image
```
Also, if needed, it is possible to implement changes to the kernel using the following command:
```
petalinux-config -c kernel
```
If any changes are needed to the rootfs, it is possible to implement the changes using the following command (no changes to the rootfs are needed for this build):
```
petalinux-config -c rootfs
```
### Building a Petalinux Project
After the settings have been changed, the PetaLinux system configuration is closed and the project is built with the following command (Internet connection is required for the build):
```
petalinux-build
```
### Packaging a Petalinux Project
After the project is built, the project is packaged with the following command:
```
petalinux-package --boot --format BIN --fsbl images/linux/zynqmp_fsbl.elf --u-boot images/linux/u-boot.elf --pmufw images/linux/pmufw.elf --fpga images/linux/system.bit --force
```
After the project is packaged, the BOOT.BIN file is located in the folder **images/linux**. The BOOT.BIN file is used to boot the Kria KV260 board.

### Preparing the Arch Linux ARM rootfs
The Arch Linux ARM rootfs is prepared with the following commands:
* Download the latest Arch Linux ARM rootfs to the home directory:
```bash
wget http://os.archlinuxarm.org/os/ArchLinuxARM-aarch64-latest.tar.gz
```
* Create a folder for the rootfs:
```bash
mkdir rootfs
```
* Extract the rootfs to the folder:
```bash
sudo tar xfvp ~/ArchLinuxARM-aarch64-latest.tar.gz -C ~/rootfs
```

### Preparing an SD card
Here are the steps to prepare an SD card for the PetaLinux SD card ext file system boot.

The SD card is formatted with two partitions using a partition editor such as GParted. The first partition should be at least 500 MB in size and formatted as a FAT32 file system. Ensure that there is 4 MB of free space preceding the partition. The first partition contains the boot loader, device tree, and kernel images. The second partition should be formatted as an ext4 files system and can take up the remaining space on the SD card. This partition stores the system root file system.

1. Label the first partition as BOOT.
2. Label the second partition as RootFS.

    See the following image for an example of the SD card partition:
    ![Example SD Card partition](Images/sd_card_partitions.jpg "Example SD Card partition with GParted")

3. Copy the files as follows:
    * FAT32 partition: BOOT.BIN, boot.scr, Image, image.ub, and ramdisk.cpio.gz.u-boot
    * EXT4 partition: the rootfs that has been prepared earlier needs to be copied to the partition

After the SD card is prepared, it is possible to boot the Kria KV260 board with the SD card.

## Booting the Kria KV260 board
The Kria KV260 board is booted with the SD card. The SD card is inserted into the SD card slot on the Kria KV260 board. The board is powered on and the boot process is started. The boot process is shown on the serial console such as PuTTY.
After the first boot of the Arch Linux ARM, the following will be displayed on the serial console:
```bash
Arch Linux 6.1.30-xilinx-v2023.2 (ttyPS0)

alarm login:
```
The default username is **alarm** and the default password is **alarm**.
After the login, similar information will be displayed on the serial console:
```bash
Last login: Thu Jan 25 02:27:46 from 192.168.1.2
[alarm@alarm ~]$
```
### Setting up the Arch Linux ARM
After the first boot, it is necessary to go to the root (the password is **root**). The following commands are executed:
```bash
[alarm@alarm ~]$ su
Password:
[root@alarm alarm]# pacman-key --init
[root@alarm alarm]# pacman-key --populate
[root@alarm alarm]# pacman -Syu
[root@alarm alarm]# pacman -S sudo
[root@alarm alarm]# reboot
```
After the updates, the installing of the sudo package and the reboot, it is necessary to log in as root and add a new user. The following commands are executed:
```bash
[root@alarm alarm]# nano /etc/sudoers
```
and add the following line:
```bash
ALL ALL=(ALL:ALL) ALL 
```
Save and exit the file. Then add a new user with the following command:
```bash
[root@alarm alarm]# useradd -m <username>
```
and set a password for the new user:
```bash
[root@alarm alarm]# passwd <username>
```
Also, it is possible to change the host name with the following command:
```bash
[root@alarm alarm]# nano /etc/hostname
```
Change the host name to the desired one. Save and exit the file and reboot.

Login with your new user name and password. In my case, the following is displayed:
```bash
[vtuser@kria-kv260 ~]$ 
```
### Installing packages
After the login, it is necessary to install the following packages. For example:
```bash
[vtuser@kria-kv260 ~]$ sudo pacman -S python3
[vtuser@kria-kv260 ~]$ sudo pacman -S gcc
[vtuser@kria-kv260 ~]$ sudo pacman -S neofetch
```
### System information
Now the Arch Linux ARM is ready to use. Write the following command to see the system information:
```bash
[vtuser@kria-kv260 ~]$ neofetch
```
You will see the following information:
![System information](Images/arch_linux_kria.jpg "System information")