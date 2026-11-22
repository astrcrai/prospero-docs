.. _slurm-index:
 
Introduction to SLURM
=======================
 
Prospero uses the `SLURM <https://slurm.schedmd.com/>`_ workload manager to
share its compute resources fairly between users. These pages explain how to
describe your work to SLURM, submit it, monitor it and fix problems.
 
If you have never used a job scheduler before, start with
:ref:`slurm-concepts` and then :ref:`first-slurm-job`. If you already know
what you want to run, go straight to the :ref:`slurm-job-examples`.
 
.. toctree::
   :maxdepth: 2
   :caption: Contents
 
   concepts
   first-job
   requesting-resources
   modules
   job-examples
   job-arrays
   interactive-jobs
   monitoring
   best-practice
 
Quick reference
---------------
 
.. list-table::
   :header-rows: 1
   :widths: 35 65
 
   * - Command
     - Purpose
   * - ``sbatch script.sh``
     - Submit a job script to the queue.
   * - ``squeue -u $USER``
     - Show your queued and running jobs.
   * - ``scancel <jobid>``
     - Cancel a job.
   * - ``sacct -j <jobid>``
     - Show accounting information for a job (including finished jobs).
   * - ``sinfo``
     - Show partitions and the state of their nodes.
   * - ``srun --pty bash``
     - Start an interactive session on a compute node.
 
