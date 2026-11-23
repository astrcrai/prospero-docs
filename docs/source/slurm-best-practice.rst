.. _slurm-best-practice:
 
Best practice and troubleshooting
=================================
 
Best practice
-------------
 
Be a good neighbour
^^^^^^^^^^^^^^^^^^^
 
* **Never run heavy computation on the login nodes.** Use ``sbatch`` or an
  interactive job.
* **Request what you need, and no more.** Over-requesting wastes resources
  and makes your jobs wait longer. Check past jobs with ``sacct`` or ``seff``.
* **Set a realistic time limit.** Slightly generous is fine; ten times too
  long is not.
* **Use job arrays** instead of submitting thousands of individual jobs, and
  make sure each task does a worthwhile amount of work.
 
Make your work reliable
^^^^^^^^^^^^^^^^^^^^^^^
 
* **Test small first.** Run a short version of your job, or use an interactive
  session, before submitting a large one.
* **Load modules inside the script** and begin with ``module purge``.
* **Use full paths or ``cd`` explicitly**, rather than assuming the working
  directory.
* **Write checkpoints** if your program supports them, so a job that hits its
  time limit can be restarted rather than rerun from scratch.
* **Keep job scripts under version control** (for example, with Git) so you
  can reproduce past results.
* **Name output files with ``%x_%j``** (job name and ID) so they are never
  overwritten.
 
Be careful with files
^^^^^^^^^^^^^^^^^^^^^
 
* Write large or numerous temporary files to the scratch area, not your home
  directory. <Describe Prospero's storage areas and quotas here.>
* Avoid creating very large numbers of small files, which is slow on parallel
  file systems. Combine them into archives where possible.
 
.. _slurm-troubleshooting:
 
Troubleshooting
---------------
 
My job is stuck in the pending (PD) state
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
Run ``squeue -j <jobid>`` and read the ``REASON`` column (see
:doc:`slurm-job-monitoring`). ``Priority`` and ``Resources`` just mean it is
waiting. A smaller request, or a shorter ``--time``, may start sooner. To see
SLURM's estimate, use ``squeue -j <jobid> --start``.
 
``sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
The partition or account name is wrong, or you do not have access to it.
Check the spelling against ``sinfo`` and your project details.
 
``sbatch: error: Requested node configuration is not available``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
You have asked for more CPUs, memory or GPUs than any node in the partition
has. Use ``sinfo -N -l -p <partition>`` to see what the nodes offer.
 
My job failed with ``OUT_OF_MEMORY`` or "oom-kill"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
The job used more memory than ``--mem`` allowed and was stopped. Look at
``MaxRSS`` in ``sacct`` for a similar job, then request more memory with
``--mem`` or ``--mem-per-cpu``.
 
My job ended with state ``TIMEOUT``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
It reached its ``--time`` limit. Increase ``--time`` (within the partition's
maximum), make the program faster, or use checkpointing and resubmit.
 
There is no output file
^^^^^^^^^^^^^^^^^^^^^^^
 
* The job may not have started yet: check ``squeue``.
* The directory in ``--output`` may not exist. SLURM will not create it.
* The job may have failed immediately: check ``sacct -j <jobid>``.
 
``/bin/bash^M: bad interpreter`` or other strange errors on the first line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
The script was probably created on Windows and has Windows-style line endings.
Convert it::
 
   dos2unix myjob.sh
 
``module: command not found``, or a program is missing in the job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
Check that the script starts with ``#!/bin/bash`` (not ``#!/bin/sh``) and that
the right modules are loaded **inside** the script.
 
My ``#SBATCH`` options seem to be ignored
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
``#SBATCH`` lines must come before any command in the script, and must have no
space between ``#`` and ``SBATCH``. Comment out an option by adding a second
``#``, for example ``##SBATCH --mem=4G``.
 
My MPI job runs only one process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
Launch the program with ``srun`` (or ``mpirun``, as recommended for your MPI
library) and make sure ``--ntasks`` or ``--ntasks-per-node`` is set. See
:ref:`slurm-example-mpi`.
 
Getting help
------------
 
If you are still stuck, please file an HPC support ticket (see :doc: `getting help <help>` and include:
 
* the job ID,
* the job script (or its location),
* the output of ``sacct -j <jobid> --format=JobID,State,ExitCode,Elapsed,MaxRSS,ReqMem``,
* the output file, and any error messages.
 
