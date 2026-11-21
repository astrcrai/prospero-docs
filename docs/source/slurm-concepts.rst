.. _slurm-concepts:
 
SLURM concepts
===============
 
Prospero is made up of many separate computers, called **nodes** (for more details, see :ref:`specifications`). Rather than
logging in to a compute node and running programs by hand, you ask SLURM to
run your work for you. SLURM keeps track of which resources are free, decides
whose job runs next, starts your job on suitable nodes and records how much it
used.
 
The typical workflow is:
 
#. Log in to the **login** or **gateway** node (``login3.prospero.ljmu.ac.uk``).
#. Write a **job script** describing the resources you need and the commands
   to run.
#. Submit it with ``sbatch``. SLURM places it in a **queue**.
#. When resources are free, SLURM starts the job on one or more **compute
   nodes**.
#. When the job ends, its output is available in the files you asked for.
 
Key terms
---------
 
.. list-table::
   :header-rows: 1
   :widths: 25 75
 
   * - Term
     - Meaning
   * - Node
     - A single computer in the cluster, with its own CPUs, memory and
       (sometimes) GPUs.
   * - Partition
     - A named group of nodes with shared limits, such as a maximum run
       time. Partitions are SLURM's queues. Use ``sinfo`` to list them.
   * - Job
     - A request for resources, plus the commands to run on them.
   * - Task
     - A process that SLURM launches as part of a job. An MPI program with 64
       ranks is 64 tasks. A serial program is one task.
   * - CPUs per task
     - The number of CPU cores allocated to each task. Multithreaded programs
       (OpenMP, Python multiprocessing, etc.) need more than one.
   * - Job step
     - A command launched inside a job with ``srun``. Every job has at least
       one step.
   * - Job array
     - A set of near-identical jobs submitted in one go. See
       :ref:`slurm-job-arrays`.
   * - Wall time
     - The maximum real-world time your job may run for, set with
       ``--time``.
 
Login node and compute nodes
-----------------------------
 
The login node is shared by everyone and exists for editing files, compiling
small programs and submitting jobs. Anything that needs real computing power
must run on the compute nodes, via SLURM.
 
.. warning::
 
   Processes that use significant CPU or memory on the login nodes may be
   stopped without warning.
 
How jobs are scheduled
----------------------
 
Jobs do not necessarily start in the order they were submitted. SLURM
calculates a **priority** for each pending job, based mainly on:
 
* **Fair-share**: users and groups who have recently used a lot of the
  system get a lower priority than those who have used little.
* **Age**: the longer a job has been waiting, the higher its priority.
* **Job size**: this depends on local configuration. <describe any
  site-specific weighting here>
 
Specfically, Prospero adopts SLURM's `multifactor priority algorithm <https://slurm.schedmd.com/priority_multifactor.html>`_. The scheduler prioritises larger jobs and balances the usage across accounts.

SLURM also uses **backfill**: a small, short job can start early if it fits
into a gap without delaying a higher-priority job. This is a good reason to
request an accurate (not excessive) time limit and only the resources you
need, because smaller requests are easier to fit in.

A list of the partitions available on Prospero can be found on the :ref:`slurm-prospero-partitions` page, but users are advised to first learn how to request :ref:`resources<slurm-requesting-resources>`.
