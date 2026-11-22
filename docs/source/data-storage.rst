.. _data-storage:

Data storage and management
=====

Datastores
------------

Prospero has the following datastores:

+------------------------+---------------------+------------+-----------------------------------+
| Type                   | Mount point         | Capacity   | For use by                        | 
|                        |                     |            |                                   |             
+========================+=====================+============+===================================+
| Homespace              | /users/             | 3.1 TB     | All                               |
+------------------------+---------------------+------------+-----------------------------------+
| Data storage           | /mnt/scratch        | 3.6 PB     | All                               |
+                        +---------------------+------------+-----------------------------------+
|                        | /mnt/data1          | 220 TB     | All                               |
+                        +---------------------+------------+-----------------------------------+
|                        | /mnt/aridata1       | 233 TB     | ARI members                       |
+------------------------+---------------------+------------+-----------------------------------+


Where to keep your data on Prospero
-----------------------------------

* Your **home directory** has a small quota. Use it for scripts, source code,
  configuration files and small results, not for datasets.
* **Scratch** (``/mnt/scratch``) is the main area for working data. Keep personal
  project data in ``/mnt/scratch/users/[USERNAME]`` and data shared between
  several users in ``/mnt/scratch/projects/[PROJECTNAME]``.
* ``/mnt/data1`` is a legacy volume, and ``/mnt/aridata1`` is reserved for
  members of the Astrophysics Research Institute.

Treat everything on Prospero as *working copies*. Keep the authoritative
version of irreplaceable data (raw observations, original input files, final
published results) in a location that is backed up and under your control, for
one of the storage options described in the Library's *Research data storage*
guidance, or a suitable repository.

Protecting your data
--------------------

Because Prospero volumes are not backed up, you are responsible for protecting
anything you cannot afford to lose. A commonly recommended approach is the
"3-2-1 rule": keep **three** copies of important data, on **two** different
types of storage, with **one** copy held off-site or in a different system.

* Keep **source code, job scripts and analysis scripts** under version control
  (for example ``git``) and push them to a remote repository.
* Keep **raw and input data** in at least one other location, and record where.
* Copy **final results** off Prospero as soon as they are produced.
* Do not rely on scratch space as the only home for anything important.


Organising and documenting your data
------------------------------------

Data that cannot be understood is of little use to anyone, including you in
six months' time.

* **Use a consistent directory structure** that separates raw inputs, processed
  data, code and results, for example ``raw/``, ``processed/``, ``scripts/`` and
  ``results/``.
* **Never modify raw data in place.** Treat input files as read-only and
  write derived data to a different location.
* **Use clear, consistent file names** without spaces, and include dates in
  ``YYYY-MM-DD`` form or version numbers where relevant.
* **Add a README** to each project directory describing what the data are, how
  they were produced, the meaning of columns or variables and units, who to
  contact, and any licence or access restrictions.
* **Prefer open, well-documented file formats** (for example CSV, HDF5, NetCDF,
  FITS, plain text) over proprietary ones where possible, so the data remain
  usable in the long term.

.. IMPORTANT::

   VSCode and Python environments such as ``conda`` can quickly fill your homespace with temporary hidden files (often caches) that may not show up with the ``du`` command. For example, check for directories such as ``.cache`` and ``.vscode-server``. It is recommended that you move these directories to your personal user space on the scratch space ``/mnt/scratch/users/[USERNAME]`` and create softlinks from your homespace to these from their original location. For example: 

.. code-block:: bash

   $ cd ~
   $ mv .vscode-server /mnt/scratch/users/[USERNAME]/
   $ ln -s /mnt/scratch/users/[USERNAME]/.vscode-server .vscode-server

Backups
------------
The homespace is backed up daily by an automated system. If you need access to a backup, please log an ITS helpdesk ticket. Nevertheless, users are advised to keep their source code on a version control system and maintain their own backups of mission-critical source code and data. 


