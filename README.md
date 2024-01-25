# Zynq™ UltraScale+™ MPSoC (Kria KV260) Arch Linux

1. [FPGA Project Kria KV260](#fpga-project-kria-kv260)
    * [Requirements](#requirements)
    * [FPGA Design](#fpga-design)
2. [Petalinux Project](#petalinux-project)


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
![Example FPGA Design to create Petalinux project](Images\fpga_design.jpg "FPGA Design Example")

This is an simple example of a FPGA design to create a Petalinux project based on the [Kria KV260](https://www.xilinx.com/products/som/kria/kv260-vision-starter-kit.html). 

After creating the block design, the design is validated, synthesized, implemented and generated bitstream. Then it is required to export hardware, including bitstream *<project_name>.xsa*. The XSA file is used to create a Petalinux project. The XSA file *kria_kv260_bd_wrapper.xsa* is located in the folder **Kria KV260**.

When the XSA file has been exported successfully, the Petalinux project is ready to be created.

## Petalinux Project

