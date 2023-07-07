Prospero specifications
=====

Hardware 
------------

Prospero's is based primarily on `HPE Apollo (Gen 10) <https://www.hpe.com/us/en/compute/hpc/apollo-systems.html>`_ systems. The main computing partition is built from Apollo 2000 shared infrastructure chassis, each of which hosts four compute nodes. The accelerated partition comprises a single Apollo 6500 chassis, hosting a single server with four GPU engines. Storage is provided by *yada yada yada* 

**Standard compute node specification:**

* HPE ProLiant XL225n Gen10+ server
* 2x AMD EPYC 7502 2.5GHz (36 nodes) or 2x AMD EPYC 7513 2.6GHz (8 nodes) 32-core processors
* 512GB DDR4-3200 memory
* 480GB SATA SSD local storage
* HDR100 Infiniband network interface

**Memory-rich compute node specification:**

* HPE ProLiant XL385 Gen10+ server
* 2x AMD EPYC 7502 2.6GHz 32-core processors
* 1.5TB DDR4-3200 memory
* 480GB SATA SSD local storage
* HDR100 Infiniband network interface

**Accelerated node specification:**

* HPE ProLiant XL675 Gen10+ server
* 2x AMD EPYC 7262 8-core 3.2GHz processors
* 1.0TB DDR4-3200 memory
* 1.9TB SATA SSD local storage
* HDR100 Infiniband network interface

As of July 2023, Prospero comprises 44 standard compute nodes, 1 memory-rich node and 1 accelerated node. This yields a total of 2944 compute cores and 24.5 TB of distributed memory. 

A brief history
------------

Prospero is a unified response to the growth of a number of independent HPC facilities within LJMU, particularly with the Astrophysics Research Institute, the School of Engingeering, and the School of Biological Sciences, each of which outgrew local infrastructure capabilities. 

**Initial system:**

* Development of a new system was catalysed by the award of two major research grants to the ARI in 2018/19, from the European Research Council and the Royal Society, and enabling an ambitious facility to be planned.
* The grants were part-matched by LJMU, and DTP/HPE were approached to provide a design proposal meeting the broad requirements of the university's HPC users.
* An initial system comprising 20 standard compute nodes, a memory-rich compute node, and XX TB of NFS storage saw `first light' in August 2020. 



Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

