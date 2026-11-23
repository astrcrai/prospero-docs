.. _index:

Documentation for the PROSPERO HPC facility
===========================================================

Prospero is the centralised high performance computing (HPC) facility for research at `Liverpool John Moores University <https://ljmu.ac.uk/>`_. The facility was commissioned in August 2020, is hosted and administered by LJMU's `IT services division <https://www.ljmu.ac.uk/itservices>`_.

.. image:: images/hpe_apollo2000.png
  :width: 800
  :alt: Prospero

Prospero is available for use by all research staff and postgraduate research students at LJMU, subject to usage :ref:`policies <policies>`. To start using Prospero please see :ref:`Getting access <getting_access>`.

.. IMPORTANT::

   13/11/2026 - The migration of Prospero to the RHEL v9.7 operating system is now complete. Access to the system is now only possible through login3. It is important to recognise that Prospero is now a heterogeneous facility, with the SLURM cpu partitions including nodes with two different specifications: this has **important implications** for how job submission scripts should be written, please see :ref:`here <slurm-heterogeneous-nodes>`.

.. NOTE::

   Prospero uses the Linux operating system and does not run software designed for Windows


Contents
--------

.. toctree::
  :maxdepth: 2
  :caption: ABOUT HPC at LJMU

  Home <self>
  specifications
    
.. toctree::
  :maxdepth: 2
  :caption: FOR NEW USERS

  getting_access
  first_login
  ssh_key_pair
  first_job

.. toctree::
  :maxdepth: 2
  :caption: SLURM

  slurm-index
  slurm-concepts
  slurm-requesting-resources
  slurm-prospero-partitions
  slurm-using-modules
  slurm-job-examples
  slurm-job-arrays
  slurm-interactive-jobs
  slurm-job-monitoring
  slurm-best-practice
  slurm-heterogeneous-nodes

.. toctree::
  :maxdepth: 2
  :caption: SOFTWARE

  software
  modules-arepo
  modules-starccmplus
  modules-swift

.. toctree::
  :maxdepth: 2
  :caption: YOUR DATA 

  data-storage
  data-for-proposals
  data-transfers
  data-lifecycle

.. toctree::
  :maxdepth: 2
  :caption: GETTING HELP

  common issues
  help

.. toctree::
  :maxdepth: 2
  :caption: ADDITIONAL RESOURCES

  policies
  highlights
  history
  vnc
  responsible_hpc
