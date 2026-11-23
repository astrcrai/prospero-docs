.. _slurm-using-modules:
 
Loading software with modules
=============================
 
Software on Prospero is managed with **environment modules**, which let you
choose which programs and versions are available in your shell. Modules must
be loaded **inside your job script**, as the job runs in a fresh environment.

Remember that (per the :doc:`software <software>` page) it is recommended to start ``gridware`` within your startup script (e.g. ``.bash_profile``), e.g.

.. code-block:: flight-start

    flight start
    flight env activate gridware

This enables you to use ``modules``.


Useful commands
---------------
 
.. code-block:: bash
 
   module avail              # list available software
   module avail python       # search for a particular package
   module load <name>        # load a module
   module list               # show what is currently loaded
   module unload <name>      # unload one module
   module purge              # unload everything
 
Using modules in a job script
-----------------------------
 
Place ``module load`` lines after the ``#SBATCH`` block and before running the
program:
 
.. code-block:: bash
 
   #!/bin/bash -l
   #SBATCH --job-name=py-test
   #SBATCH --partition=nodes # or your preferred partition
   #SBATCH --time=00:10:00

   # It is assumed that the commands below are included in your .bash_profile
   # in order to allow the use of modules
   # flight start
   # flight env activate gridware

   module purge
   module load <python-module>
 
   python3 myscript.py
 
Starting with ``module purge`` guarantees a clean, reproducible environment.
 
.. tip::
 
   Specify the full version (for example ``<name>/<version>``) rather than
   relying on the default, which may change when software is updated and
   alter your results.
 
