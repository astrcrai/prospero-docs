.. _slurm-job-examples:
 
Example job scripts
===================
 
This page gives ready-to-adapt job scripts for the most common types of job.
In every example, replace the ``<...>`` placeholders with values for your own
work, and change the module names to those shown by ``module avail``.
 
To use an example, copy it into a file (say ``myjob.sh``), edit it, and submit
it with::
 
   sbatch myjob.sh
 
.. contents:: On this page
   :local:
   :depth: 1
 
.. _slurm-example-serial:
 
Serial job
----------
 
A serial program uses a single CPU core. This is the simplest kind of job and
is the right choice for most small scripts and analyses.
 
.. code-block:: bash
 
   #!/bin/bash -l
   #SBATCH --job-name=serial
   #SBATCH --partition=nodes # or your preferred partition
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=1
   #SBATCH --mem=2G
   #SBATCH --time=00:30:00
   #SBATCH --output=%x_%j.out
 
   ./my_program input.dat
 
.. _slurm-example-python:
 
Python script
-------------
 
Load a Python module, then run your script. 
 
.. code-block:: bash
 
   #!/bin/bash -l
   #SBATCH --job-name=python-analysis
   #SBATCH --partition=nodes # or your preferred partition
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=1
   #SBATCH --mem=4G
   #SBATCH --time=01:00:00
   #SBATCH --output=%x_%j.out

   # It is assumed that the commands below are included in your .bash_profile
   # in order to allow the use of modules
   # flight start
   # flight env activate gridware

   module purge
   module load python3
 
   python3 analysis.py
 
.. note::
 
   Install packages on the login node, not in the job script. Compute nodes
   may not have internet access, and installing in every job wastes time.
 
.. _slurm-example-r:
 
R script
--------
 
.. code-block:: bash
 
   #!/bin/bash -l
   #SBATCH --job-name=r-analysis
   #SBATCH --partition=nodes # or your preferred partition
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=1
   #SBATCH --mem=4G
   #SBATCH --time=01:00:00
   #SBATCH --output=%x_%j.out

   # It is assumed that the commands below are included in your .bash_profile
   # in order to allow the use of modules
   # flight start
   # flight env activate gridware

   module purge
   module load <r-module>
 
   Rscript analysis.R
 
.. _slurm-example-multithreaded:
 
Multithreaded (shared-memory) job
---------------------------------
 
Programs that use threads, such as OpenMP codes, run as **one task with
several CPU cores**. All the cores must be on the same node.
 
.. code-block:: bash
 
   #!/bin/bash -l
   #SBATCH --job-name=openmp
   #SBATCH --partition=nodes # or your preferred partition
   #SBATCH --nodes=1
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=8
   #SBATCH --mem=16G
   #SBATCH --time=02:00:00
   #SBATCH --output=%x_%j.out
 
   # Tell the program how many threads to use
   export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
 
   ./my_openmp_program
 
Setting ``OMP_NUM_THREADS`` from ``$SLURM_CPUS_PER_TASK`` keeps the thread
count in step with what you requested. Other libraries have their own
variables, such as ``MKL_NUM_THREADS`` and ``OPENBLAS_NUM_THREADS``. Python's
``multiprocessing`` and R's ``parallel`` packages also need to be told how
many workers to start, so read the value from ``SLURM_CPUS_PER_TASK`` in your
code.
 
.. _slurm-example-mpi:
 
MPI job
-------
 
MPI programs run many cooperating processes, possibly across several nodes.
Use ``srun`` to launch them so that SLURM places the processes correctly.
 
.. code-block:: bash
 
   #!/bin/bash -l
   #SBATCH --job-name=mpi
   #SBATCH --partition=nodes # or your preferred partition
   #SBATCH --constraint=epyc9k
   #SBATCH --nodes=2
   #SBATCH --ntasks-per-node=128
   #SBATCH --mem=0
   #SBATCH --time=04:00:00
   #SBATCH --output=%x_%j.out

   # It is assumed that the commands below are included in your .bash_profile
   # in order to allow the use of modules
   # flight start
   # flight env activate gridware

   module purge
   module load <compiler-module> <mpi-module>
 
   srun ./my_mpi_program
 
This requests 2 nodes with 128 MPI processes on each, 256 in total. ``--mem=0``
means "all the memory on each node", which is a common choice when using whole
nodes. Without ``srun``, the program may start only one process.
 
.. important::
 
   Ensure that jobs are started using ``srun`` rather than ``mpirun``, as the latter may not guarantee that resources are allocated correctly.
 
.. _slurm-example-hybrid:
 
Hybrid MPI + OpenMP job
-----------------------
 
Some codes combine MPI between nodes with threads within each process:
 
.. code-block:: bash
 
   #!/bin/bash -l
   #SBATCH --job-name=hybrid
   #SBATCH --partition=nodes # or your preferred partition
   #SBATCH --constraint=epyc9k
   #SBATCH --nodes=2
   #SBATCH --ntasks-per-node=8
   #SBATCH --cpus-per-task=16
   #SBATCH --mem=0
   #SBATCH --time=04:00:00
   #SBATCH --output=%x_%j.out

   # It is assumed that the commands below are included in your .bash_profile
   # in order to allow the use of modules
   # flight start
   # flight env activate gridware

   module purge
   module load <compiler-module> <mpi-module>
 
   export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
 
   srun ./my_hybrid_program
 
Each node runs 8 MPI processes with 16 threads each, using 128 cores per node.
 
.. _slurm-example-gpu:
 
GPU job
-------
 
Request GPUs from a GPU partition with ``--gres``:
 
.. code-block:: bash
 
   #!/bin/bash -l
   #SBATCH --job-name=gpu-test
   #SBATCH --partition=gpu-a100 # or your preferred gpu partition
   #SBATCH --gres=gpu:1
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=4
   #SBATCH --mem=32G
   #SBATCH --time=02:00:00
   #SBATCH --output=%x_%j.out

   # It is assumed that the commands below are included in your .bash_profile
   # in order to allow the use of modules
   # flight start
   # flight env activate gridware

   module purge
   module load <cuda-module>
 
   # Show which GPU(s) the job was given
   nvidia-smi
 
   python3 train.py
 
SLURM sets ``CUDA_VISIBLE_DEVICES`` so that your program sees only the GPUs
allocated to it. A typical machine-learning workflow is to create a virtual
environment as shown in :ref:`slurm-example-python` and install your framework
(for example PyTorch) into it.
 
.. _slurm-example-highmem:
 
Large-memory job
----------------
 
If your program needs more memory than is available on standard nodes, use the
large-memory partition and request the memory explicitly:
 
.. code-block:: bash
 
   #!/bin/bash -l
   #SBATCH --job-name=bigmem
   #SBATCH --partition=himem
   #SBATCH --ntasks=1
   #SBATCH --cpus-per-task=4
   #SBATCH --mem=900G
   #SBATCH --time=12:00:00
   #SBATCH --output=%x_%j.out
 
   ./my_memory_hungry_program
 
Use ``sacct`` (see :ref:`slurm-job-monitoring`) to check how much memory a trial
run actually used before requesting a large amount.
 
.. _slurm-example-multiple-serial:
 
Several small tasks in one job
------------------------------
 
If you have a few independent serial tasks that each run for a similar time,
you can run them side by side within one job. Start each with ``srun`` in the
background and then ``wait`` for them all to finish:
 
.. code-block:: bash
 
   #!/bin/bash -l
   #SBATCH --job-name=multi
   #SBATCH --partition=nodes # or your preferred partition
   #SBATCH --ntasks=4
   #SBATCH --cpus-per-task=1
   #SBATCH --mem-per-cpu=2G
   #SBATCH --time=01:00:00
   #SBATCH --output=%x_%j.out
 
   srun --ntasks=1 --exclusive ./my_program input1.dat &
   srun --ntasks=1 --exclusive ./my_program input2.dat &
   srun --ntasks=1 --exclusive ./my_program input3.dat &
   srun --ntasks=1 --exclusive ./my_program input4.dat &
 
   wait
 
For larger numbers of tasks, a job array is usually simpler: see
:ref:`slurm-job-arrays`.
 
.. _slurm-dependencies:
 
Chaining jobs with dependencies
-------------------------------
 
You can make one job wait for another, for example to run an analysis once a
simulation has finished. ``sbatch --parsable`` prints just the job ID, which
you can store in a variable:
 
.. code-block:: bash
 
   jobid1=$(sbatch --parsable step1.sh)
   jobid2=$(sbatch --parsable --dependency=afterok:$jobid1 step2.sh)
   sbatch --dependency=afterok:$jobid2 step3.sh
 
Common dependency types:
 
.. list-table::
   :header-rows: 1
   :widths: 30 70
 
   * - Type
     - The new job starts...
   * - ``afterok:<jobid>``
     - only if the earlier job finished successfully.
   * - ``afterany:<jobid>``
     - after the earlier job ends, whether or not it succeeded.
   * - ``afternotok:<jobid>``
     - only if the earlier job failed (useful for clean-up).
 
If an ``afterok`` job fails, jobs waiting on it will never run. Cancel them
with ``scancel``.
 
.. _slurm-email-notifications:
 
Email notifications
-------------------
 
To be emailed when a job starts, ends or fails, add:
 
.. code-block:: bash
 
   #SBATCH --mail-type=END,FAIL
   #SBATCH --mail-user=<your-email-address>
 
Avoid ``--mail-type=ALL`` on job arrays, as it can send a very large number of
messages.
 
Example scripts
-------------------

The Alces Flight environment includes a number of helpful example SLURM scripts for users to adapt. The types of script can be viewed using

.. code-block:: bash

    flight job list-templates

and then copied to your working directory using the copy-template command, i.e to copy the "simple serial" example, use:

.. code-block:: bash

    flight job copy-template 3

