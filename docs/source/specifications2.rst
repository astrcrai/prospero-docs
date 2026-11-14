.. _specifications:

Prospero specifications
=======================

This page describes the hardware that makes up the Prospero HPC facility,
so you can choose the right resources for your jobs. To request resources
for a job, see the :doc:`Slurm quickstart <scheduler>`; for where to keep
your data, see :doc:`storage`. If you do not yet have an account, see
:doc:`access`.

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

* **Original nodes** (commissioned 2020-2025) are based on HPE Apollo 2000
  shared-infrastructure chassis, each hosting up to four HPE XL225 compute
  nodes with ``epyc7k`` generation processors.
* **Newer nodes** (commissioned since 2025) are based on HPE Cray XD2000
  shared-infrastructure chassis, each hosting four HPE Cray XD225 compute
  nodes with ``epyc9k`` generation processors.

There are also two GPU-accelerated servers: an older Apollo 6500 server with
four NVIDIA A100 GPUs and ``epyc7k`` processors, and a newer server
commissioned since 2025.

.. TODO: the original sentence describing the newer GPU server was cut off
   ("The newer is ..."). Complete it, and fill in the Cray GPU row in the
   tables below.

.. list-table:: Compute nodes at a glance
   :header-rows: 1
   :widths: 24 14 10 12 20 10

   * - Node type
     - Generation
     - Nodes
     - Cores per node
     - Memory per node
     - GPUs per node
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
     - ``epyc9k``
     - 1
     - TBC
     - TBC
     - TBC

.. TODO: add a "Slurm partition" column linking each node type to the
   partition(s) that give access to it, and confirm the Cray GPU node count.


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
     - 2x AMD EPYC 32-core: 7502 at 2.5 GHz (36 nodes) or 7513 at 2.6 GHz
       (16 nodes)
     - 2x AMD EPYC 9534 64-core at 2.45 GHz
   * - Cores per node
     - 64
     - 128
   * - Memory
     - 512 GB DDR4-3200
     - 768 GB
   * - Local storage
     - 480 GB SATA SSD
     - 15 TB NVMe SSD
   * - Interconnect
     - HDR100 InfiniBand
     - HDR200 or NDR200 InfiniBand

.. TODO: the old page listed the Cray memory as DDR4-3200. EPYC 9004-series
   processors normally use DDR5, so please confirm the memory type before
   adding it to the Cray column above.


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
     - TBC
   * - Processors
     - 2x AMD EPYC 7262 8-core at 3.2 GHz
     - TBC
   * - Cores per node
     - 16
     - TBC
   * - Memory
     - 1.0 TB DDR4-3200
     - TBC
   * - Accelerators
     - 4x NVIDIA A100 80 GB
     - TBC
   * - Local storage
     - 1.9 TB SATA SSD
     - TBC
   * - Interconnect
     - HDR100 InfiniBand
     - TBC

.. TODO: complete the Cray GPU column (this was "To be filled in" on the
   old page) or remove it until the specification is confirmed.


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
     - 250 TB
     - HPE Apollo 4200 Gen10+ storage
   * - ``/mnt/aridata1``
     - ARI use
     - 250 TB
     - HPE Apollo 4200 Gen10+ storage server, RAID6

For quotas, backup arrangements and guidance on which area to use for what,
see :doc:`storage`.

.. TODO: spell out "ARI" in full on first use, and say whether backups
   apply to each area (or confirm that they are covered on the storage page).
