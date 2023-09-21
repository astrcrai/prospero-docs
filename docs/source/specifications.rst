Prospero specifications
=====

Prospero's is based primarily on `HPE Apollo (Gen 10) <https://www.hpe.com/us/en/compute/hpc/apollo-systems.html>`_ systems. The main computing partition is built from Apollo 2000 shared infrastructure chassis, each of which hosts four compute nodes. The GPU accelerated partition comprises a single Apollo 6500 chassis, hosting a single server with four GPU engines. Storage is provided by *yada yada yada* 

**Standard compute node specification:**

* HPE ProLiant XL225n Gen10+ server
* 2x AMD EPYC 32-core processors (7502 2.5GHz in 36 nodes, 7513 2.6GHz in 8 nodes) 
* 512GB DDR4-3200 memory
* 480GB SATA SSD local storage
* HDR100 Infiniband network interface

**Memory-rich compute nodes specification:**

High mem node1

* HPE ProLiant XL385 Gen10+ server
* 2x AMD EPYC 7502 2.6GHz 32-core processors
* 1.5TB DDR4-3200 memory
* 480GB SATA SSD local storage
* HDR100 Infiniband network interface

High mem node2 (coming soon)

* HPE ProLiant XL385 Gen10+ server
* 2x AMD EPYC 7763 2.45GHz 64-core processors
* 2.0TB DDR4-3200 memory
* 480GB SATA SSD local storage
* HDR100 Infiniband network interface

**GPU accelerated node specification:**

* HPE ProLiant XL675 Gen10+ server
* 2x AMD EPYC 7262 8-core 3.2GHz processors
* 1.0TB DDR4-3200 memory
* 1.9TB SATA SSD local storage
* HDR100 Infiniband network interface

As of August 2023, Prospero comprises 52 standard compute nodes, 1 memory-rich node and 1 GPU-accelerated node, yielding 3408 compute cores and 28.5 TB of distributed memory. 

**Networked storage:**

* General purpose:

  * HPE Apollo 4200 Gen10+ storage server with 250TB in RAID6 configuration (/mnt/data1)
  * HPE Apollo 4200 Gen9+ storage server with 80TB? in RAID6 configuration (/mnt/backup1)

* ARI use:

  * HPE Apollo 4200 Gen10+ storage server with 250TB in RAID6 configuration (/mnt/backup1)
  * Lenovo parallel datastore (3PB)
