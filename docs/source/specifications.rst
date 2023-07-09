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

**Networked storage:**

* General purpose:

  * HPE Apollo 4200 Gen10+ storage server with 250TB in RAID6 configuration
  * HPE Apollo 4200 Gen9+ storage server with 80TB? in RAID6 configuration 

* ARI use:

  * HPE Apollo 4200 Gen10+ storage server with 250TB in RAID6 configuration
  * Lenovo parallel datastore (3PB)