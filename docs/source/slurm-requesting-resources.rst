.. _requesting-resources:
 
Requesting resources
====================
 
Every job script begins with a block of ``#SBATCH`` lines that tell SLURM what
the job needs. This page describes the options you will use most often.
 
``#SBATCH`` lines must appear **before** the first executable command in the
script. Anything after that is ignored by SLURM.
 
You can also give any of these options on the command line, which overrides
the value in the script::
 
   sbatch --time=02:00:00 myjob.sh
 
Common options
--------------
 
.. list-table::
   :header-rows: 1
   :widths: 35 65
 
   * - Option
     - Meaning
   * - ``--job-name=<name>``
     - A short name for the job, shown in ``squeue``.
   * - ``--partition=<name>``
     - The partition to run in.
   * - ``--account=<project>``
     - The project to charge the job to (if required on Prospero).
   * - ``--time=<HH:MM:SS>``
     - Maximum run time. Also accepts ``D-HH:MM:SS``, for example
       ``2-00:00:00`` for two days.
   * - ``--nodes=<n>``
     - | Number of nodes.
       | **Please only request nodes (rather than CPUs) if absolutely necessary**.
       | For details of why this is important, see:ref:`slurm-heterogeneous-nodes`.
   * - ``--ntasks=<n>``
     - Total number of tasks (processes).
   * - ``--ntasks-per-node=<n>``
     - Number of tasks to place on each node.
   * - ``--cpus-per-task=<n>``
     - CPU cores per task (for multithreaded programs).
   * - ``--mem=<size>``
     - Memory per **node**, for example ``16G``.
   * - ``--mem-per-cpu=<size>``
     - Memory per CPU core, for example ``4G``. Do not combine with
       ``--mem``.
   * - ``--gres=gpu:<n>``
     - Number of GPUs per node.
   * - ``--output=<file>``
     - File for standard output. ``%j`` is replaced by the job ID.
   * - ``--error=<file>``
     - File for standard error. If omitted, errors go to the output file.
   * - ``--mail-type=<events>``
     - Send email on ``BEGIN``, ``END``, ``FAIL`` or ``ALL``.
   * - ``--mail-user=<address>``
     - Address for notification emails.
   * - ``--array=<range>``
     - Make this a job array. See :ref:`slurm-job-arrays`.
   * - ``--dependency=<type:jobid>``
     - Start only after another job has finished. See
       :ref:`slurm-dependencies`.
 
Filename patterns
^^^^^^^^^^^^^^^^^
 
In ``--output`` and ``--error``, these placeholders are replaced by SLURM:
 
* ``%j``: job ID
* ``%x``: job name
* ``%u``: your username
* ``%A`` and ``%a``: array job ID and array task index
 
For example, ``--output=%x_%j.out`` produces ``hello_123456.out``.
 
Choosing the right amount of resource
-------------------------------------
 
Time
^^^^
 
If your job exceeds ``--time`` it is killed. If you request far more than you
need, it may wait longer in the queue. As a rule of thumb, run a small test,
note how long it takes, and request 20-50% more than that.
 
Memory
^^^^^^
 
If your job uses more memory than you requested it is killed (see
:ref:`slurm-troubleshooting`). After a job finishes you can check how much it
really used with ``sacct`` or ``seff`` (see :ref:`slurm-monitoring`) and adjust
future requests.
 
CPUs, tasks and nodes
^^^^^^^^^^^^^^^^^^^^^
 
The right combination depends on how your program is parallelised:
 
.. list-table::
   :header-rows: 1
   :widths: 30 30 40
 
   * - Type of program
     - Request
     - Example
   * - Serial (one process, one thread)
     - ``--ntasks=1 --cpus-per-task=1``
     - Most simple scripts
   * - Multithreaded (OpenMP, threads)
     - ``--ntasks=1 --cpus-per-task=N``
     - Python multiprocessing, MATLAB
   * - MPI
     - ``--ntasks=N`` (and optionally ``--nodes``)
     - Many simulation codes
   * - MPI + threads (hybrid)
     - ``--ntasks=N --cpus-per-task=M``
     - Some CFD, molecular dynamics
 
.. important::
 
   Requesting more CPUs does not make a program faster unless the program is
   written to use them. A serial program given 32 cores will use one and waste
   31.
 
GPUs
^^^^
 
Request GPUs with ``--gres=gpu:<n>`` and use a GPU partition, for example::
 
   #SBATCH --partition=<gpu-partition>
   #SBATCH --gres=gpu:1
 
Only request as many GPUs as your software can use.
 
Environment variables available in jobs
---------------------------------------
 
SLURM sets a number of variables inside your job that you can use in scripts:
 
.. list-table::
   :header-rows: 1
   :widths: 40 60
 
   * - Variable
     - Value
   * - ``$SLURM_JOB_ID``
     - The job ID.
   * - ``$SLURM_JOB_NAME``
     - The job name.
   * - ``$SLURM_SUBMIT_DIR``
     - The directory you ran ``sbatch`` from.
   * - ``$SLURM_NTASKS``
     - Total number of tasks.
   * - ``$SLURM_CPUS_PER_TASK``
     - CPUs per task (only set if ``--cpus-per-task`` was given).
   * - ``$SLURM_ARRAY_TASK_ID``
     - The array index (array jobs only).
 
By default a job starts in the directory it was submitted from.
 
