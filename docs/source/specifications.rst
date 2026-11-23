.. _specifications:

Prospero specifications
=======================

This page describes the hardware comprising the Prospero HPC facility,
so you can choose the right resources for your jobs. 

.. .. TODO: update the "as of" date below whenever node counts change.

As of Q3/2025, Prospero comprises over 5000 compute cores and provides
approximately 45 million core hours per year to the LJMU research
community.

.. contents:: On this page
   :local:
   :depth: 2


Overview
--------

Prospero has two generations of compute nodes, which differ in processor
generation and interconnect speed:

* **First generation** nodes (commissioned 2020-2025) use AMD ``epyc7k`` processors and are mostly based on HPE Apollo 2000
  shared-infrastructure chassis, each hosting up to four HPE XL225 compute nodes.
* **Second generation** nodes (commissioned since 2025) use AMD ``epyc9k`` generation processors and are mostly are based on HPE Cray XD2000
  shared-infrastructure chassis, each hosting four HPE Cray XD225 compute nodes.

There are also two first generation nodes (with ``epyc7k`` processors) that have large memory footprints: one has 1.5TB and the other has 2.0TB.

Prospero has two GPU-accelerated servers: a first generation Apollo 6500 server with
four NVIDIA A100 GPUs and ``epyc7k`` processors, and a second generation DL380 server with four NVIDIA H200 GPUs and ``epyc9k`` processors.

.. list-table:: Compute nodes at a glance
   :header-rows: 1
   :widths: 24 14 10 12 20 10

   * - Node type
     - Generation
     - Nodes
     - Cores per node
     - Memory per node
     - GPUs
   * - Standard (Apollo)
     - ``epyc7k``
     - 52
     - 64
     - 512 GB
     - --
   * - Standard (Cray)
     - ``epyc9k``
     - 13
     - 128
     - 768 GB
     - --
   * - High-memory 1
     - ``epyc7k``
     - 1
     - 64
     - 1.5 TB
     - --
   * - High-memory 2
     - ``epyc7k``
     - 1
     - 128
     - 2.0 TB
     - --
   * - GPU (Apollo)
     - ``epyc7k``
     - 1
     - 16
     - 1.0 TB
     - 4x A100 80 GB
   * - GPU (Cray)
     - Intel Xeon 6710E
     - 1
     - 128
     - 1.0TB
     - 4x H200 140GB


Standard compute nodes
----------------------

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :widths: 22 39 39

   * -
     - Apollo (``epyc7k``)
     - Cray (``epyc9k``)
   * - Number of nodes
     - 52
     - 13
   * - Server
     - HPE ProLiant XL225n Gen10+
     - HPE Cray XD225v
   * - Processors
     - | 2x AMD EPYC 32-core:
       | 7502 at 2.5 GHz (36 nodes)
       | 7513 at 2.6 GHz (16 nodes)
     - 2x AMD EPYC 9534 64-core at 2.45 GHz
   * - Cores per node
     - 64
     - 128
   * - Memory
     - 512 GB DDR4
     - 768 GB DDR5
   * - Local storage
     - 480 GB SATA SSD
     - 15 TB NVMe SSD
   * - Interconnect
     - HDR100 InfiniBand
     - HDR200 or NDR200 InfiniBand


High-memory nodes
-----------------

Two nodes are available for jobs that need more memory than a standard node
provides.

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :widths: 22 39 39

   * -
     - High-memory 1
     - High-memory 2
   * - Server
     - HPE ProLiant XL385 Gen10+
     - HPE ProLiant XL385 Gen10+
   * - Processors
     - 2x AMD EPYC 7502 32-core at 2.6 GHz
     - 2x AMD EPYC 7763 64-core at 2.45 GHz
   * - Cores per node
     - 64
     - 128
   * - Memory
     - 1.5 TB DDR4-3200
     - 2.0 TB DDR4-3200
   * - Local storage
     - 480 GB SATA SSD
     - 480 GB SATA SSD
   * - Interconnect
     - HDR100 InfiniBand
     - HDR100 InfiniBand


GPU-accelerated nodes
---------------------

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :widths: 22 39 39

   * -
     - Apollo (``epyc7k``)
     - Cray (``epyc9k``)
   * - Server
     - HPE ProLiant XL675 Gen10+
     - HPE ProLiant DL380 Gen 12 
   * - Processors
     - 2x AMD EPYC 7262 8-core at 3.2 GHz
     - 2x Intel Xeon 6710E 64-core at 2.4GHz
   * - Cores per node
     - 16
     - 128
   * - Memory
     - 1.0 TB DDR4-3200
     - 1.0 TB DDR5-6400
   * - Accelerators
     - 4x NVIDIA A100 80 GB
     - 4x NVIDIA H200 140GB
   * - Local storage
     - 1.9 TB SATA SSD
     - 15 TB TB NVMe
   * - Interconnect
     - HDR100 InfiniBand
     - NDR200 Infiniband


Networked storage
-----------------

.. list-table::
   :header-rows: 1
   :widths: 18 22 14 46

   * - Path
     - Use
     - Capacity
     - Technology
   * - ``/mnt/scratch``
     - General purpose
     - 3.6 PB
     - HPE ClusterStor parallel storage
   * - ``/mnt/data1``
     - General purpose
     - 220 TB
     - HPE Apollo 4200 Gen10+ storage
   * - ``/mnt/aridata1``
     - ARI use
     - 230 TB
     - HPE Apollo 4200 Gen10+ storage server, RAID6

For quotas, backup arrangements and guidance on which area to use for what,
see :doc:`Data storage <data-storage>`.

