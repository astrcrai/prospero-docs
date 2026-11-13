Prospero specifications
=====

The Prospero facility is currently comprised of two generations of nodes with differing specifications. The original nodes, commissioned between 2020 and 2025, are based primarily on HPE Apollo 2000 shared-infrastructure chassis, each of which hosts up to four HPE XL225 compute nodes equipped with ``epyc7k`` generation processors. The newer nodes, commissioned since 2025, are based on HPE Cray XD2000 shared infrastructure chassis, each of which hosts four HPE Cray XD225 compute nodes with ``epyc9k`` generation processors.

Prospero also includes includes two GPU-accelerated servers. The older server is an Apollo 6500 chassis, hosting a single server with four nvidia A100 GPU engines and epyc7k processors. The newer is  


As of Q3/2025, Prospero comprises over 5000 compute cores and provides approximately 45 million core hours per year to the LJMU research community.


=====
Cray nodes
=====

* HPE Cray XD225v server
* 2x AMD EPYC 64-core processors (9534 2.45GHz) 
* 768GB DDR4-3200 memory
* 15TB NVMe SSD local storage
* HDR200 or NDR200 Infiniband network interface

Prospero currently has 13 standard Cray compute nodes.

**GPU accelerated node specification:**

* To be filled in....

=====
Apollo nodes based on ``epyc7k`` processors.
=====

**Standard compute node specification:**

* HPE ProLiant XL225n Gen10+ server
* 2x AMD EPYC 32-core processors (7502 2.5GHz in 36 nodes, 7513 2.6GHz in 16 nodes) 
* 512GB DDR4-3200 memory
* 480GB SATA SSD local storage
* HDR100 Infiniband network interface

Prospero currently has 52 standard Apollo compute nodes.

**Memory-rich compute nodes specification:**

High mem node1

* HPE ProLiant XL385 Gen10+ server
* 2x AMD EPYC 7502 2.6GHz 32-core processors
* 1.5TB DDR4-3200 memory
* 480GB SATA SSD local storage
* HDR100 Infiniband network interface

High mem node2

* HPE ProLiant XL385 Gen10+ server
* 2x AMD EPYC 7763 2.45GHz 64-core processors
* 2.0TB DDR4-3200 memory
* 480GB SATA SSD local storage
* HDR100 Infiniband network interface

**GPU accelerated node specification:**

* HPE ProLiant XL675 Gen10+ server
* 2x AMD EPYC 7262 8-core 3.2GHz processors
* 1.0TB DDR4-3200 memory
* 4x NVIDIA A100 80GB accelerator 
* 1.9TB SATA SSD local storage
* HDR100 Infiniband network interface

=====
Networked storage
=====

* General purpose:

  * HPE ClusterStor parallel storage with 3.6PB (/mnt/scratch)
  * HPE Apollo 4200 Gen10+ storage with 250TB (/mnt/data1)

* ARI use:

  * HPE Apollo 4200 Gen10+ storage server with 250TB in RAID6 (/mnt/aridata1)
