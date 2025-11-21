Prospero specifications
=====

The Prospero facility is comprised of two "islands", Prospero-I and Prospero-II. Prospero-I, commissioned in 2020, is based primarily on HPE Apollo 2000 shared infrastructure chassis, each of which hosts up to four HPE XL225 compute nodes. Prospero-I includes a GPU-accelerated partition comprised of a single Apollo 6500 chassis, hosting a single server with four GPU engines. 

Prospero-II, commissioned in 2025, is based on HPE Cray XD2000 shared infrastructure chassis, each of which hosts four HPE Cray XD225 compute nodes. 

=====
Prospero-II
=====

**Standard compute node specification:**

* HPE Cray XD225v server
* 2x AMD EPYC 64-core processors (9534 2.45GHz) 
* 768GB DDR4-3200 memory
* 15TB NVMe SSD local storage
* HDR200 Infiniband network interface

Currently Prospero-II comprises 4 such chassis with 13 compute nodes.

=====
Prospero-I
=====

**Standard compute node specification:**

* HPE ProLiant XL225n Gen10+ server
* 2x AMD EPYC 32-core processors (7502 2.5GHz in 36 nodes, 7513 2.6GHz in 16 nodes) 
* 512GB DDR4-3200 memory
* 480GB SATA SSD local storage
* HDR100 Infiniband network interface


 Combined performance of all 52 Prospero-I nodes is 84.7 Tflops.

  * Single node performance of 1.9 Tflops for the EPYC2 nodes.
  * Single node performance of 1.75 Tflops for the EPYC3 nodes.

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

As of December 2023, Prospero comprises 52 standard compute nodes, 2 memory-rich node and 1 GPU-accelerated node, yielding 3536 compute cores and 32.2 TB of distributed memory. 

=====
Networked storage
=====

* General purpose:

  * HPE ClusterStor parallel storage with 3.6PB (/mnt/scratch)
  * HPE Apollo 4200 Gen10+ storage with 250TB (/mnt/data1)

* ARI use:

  * HPE Apollo 4200 Gen10+ storage server with 250TB in RAID6 (/mnt/aridata1)
