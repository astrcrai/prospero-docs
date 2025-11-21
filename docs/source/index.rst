.. include:: ../README.rst

Documentation for the PROSPERO HPC facility
===========================================================

Prospero is the centralised high performance computing (HPC) facility for research at `Liverpool John Moores University <https://ljmu.ac.uk/>`_. The facility was commissioned in August 2020, is hosted and administered by LJMU's `IT services division <https://www.ljmu.ac.uk/itservices>`_.

.. image:: images/hpe_apollo2000.png
  :width: 800
  :alt: Prospero

Prospero is available for use by all research staff and postgraduate research students at LJMU, subject to usage `policies <https://prospero-docs.readthedocs.io/en/latest/policies.html>`_. To start using Prospero please see `Getting Access <https://prospero-docs.readthedocs.io/en/latest/access.html>`_.

.. IMPORTANT::

   21/11/2025 - The HPE ClusterStor parallel file system (/mnt/scratch) has now been expanded to 3.6PB capacity. 


.. IMPORTANT::

   28/07/2025 - Phase-2 of Prospero is underway. The first 13 nodes with the `Prospero-2 specification <https://prospero-docs.readthedocs.io/en/latest/specifications.html>`_ have been installed and are available in the compute and long SLURM partitions. The dissimilar specifications of Prospero-I and Prospero-II nodes has **important implications** for how job submission scripts should be written, please see `here <https://prospero-docs.readthedocs.io/en/latest/scheduler.html#slurm-scripts-in-the-prospero-ii-era>`_.


.. NOTE::

   Prospero uses the Linux operating system and does not run software designed for Windows


Contents
--------

.. toctree::
  :maxdepth: 1
  :caption: ABOUT HPC at LJMU

  Home <self>
  specifications
  storage

    
.. toctree::
  :maxdepth: 1
  :caption: GETTING STARTED

  access

.. toctree::
  :maxdepth: 2
  :caption: RUNNING JOBS

  scheduler

.. toctree::
  :maxdepth: 3
  :caption: SOFTWARE

  software


.. toctree::
  :maxdepth: 4
  :caption: GETTING HELP
  
  help
  policies

.. toctree::
  :maxdepth: 5
  :caption: ADDITIONAL RESOURCES

  highlights
  history
  vnc
  usage
  environmental
