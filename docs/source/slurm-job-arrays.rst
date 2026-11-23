.. _slurm-job-arrays:
 
Job arrays
==========
 
A **job array** submits many similar jobs with a single ``sbatch`` command.
Each element of the array runs the same script but gets a different index
number, which you use to select an input file, parameter value, random seed
and so on.
 
Arrays are the right tool whenever you would otherwise write a loop that calls
``sbatch`` many times. They are easier to manage, kinder to the scheduler, and
can be cancelled or monitored as a single unit.
 
A first array job
-----------------
 
.. code-block:: bash
 
   #!/bin/bash
   #SBATCH --job-name=array-test
   #SBATCH --partition=nodes # or your preferred partition
   #SBATCH --ntasks=1
   #SBATCH --mem=1G
   #SBATCH --time=00:10:00
   #SBATCH --array=1-10
   #SBATCH --output=%x_%A_%a.out
 
   echo "This is array task $SLURM_ARRAY_TASK_ID of job $SLURM_ARRAY_JOB_ID"
 
``--array=1-10`` creates ten tasks, numbered 1 to 10. Inside each, the
variable ``$SLURM_ARRAY_TASK_ID`` holds its number. In the output filename
``%A`` is the overall array job ID and ``%a`` is the task index, so each task
writes to its own file, for example ``array-test_123456_7.out``.
 
Array index syntax
------------------
 
.. list-table::
   :header-rows: 1
   :widths: 30 70
 
   * - ``--array=``
     - Tasks created
   * - ``1-10``
     - 1, 2, 3, ... 10
   * - ``0-99``
     - 100 tasks, numbered from 0
   * - ``1,3,5,7``
     - Just the listed numbers
   * - ``1-20:2``
     - 1, 3, 5, ... 19 (step of 2)
   * - ``1-100%10``
     - 1 to 100, but at most 10 running at once
 
.. tip::
 
   Use the ``%`` throttle (for example ``--array=1-1000%20``) to stop a large
   array from filling the whole cluster, or from overwhelming shared storage
   or a licence server.
 
Example: one input file per task
--------------------------------
 
Suppose you have a text file, ``files.txt``, listing one input filename per
line. Each array task can pick out its own line:
 
.. code-block:: bash
 
   #!/bin/bash
   #SBATCH --job-name=process-files
   #SBATCH --partition=nodes # or your preferred partition
   #SBATCH --ntasks=1
   #SBATCH --mem=4G
   #SBATCH --time=01:00:00
   #SBATCH --array=1-50
   #SBATCH --output=logs/%x_%A_%a.out
 
   # Pick line number N from files.txt, where N is this task's index
   INPUT=$(sed -n "${SLURM_ARRAY_TASK_ID}p" files.txt)
 
   echo "Task $SLURM_ARRAY_TASK_ID processing $INPUT"
   ./my_program "$INPUT" > "results/${INPUT}.result"
 
Make sure the ``logs`` and ``results`` directories exist before you submit,
since SLURM will not create the ``--output`` directory for you::
 
   mkdir -p logs results
   sbatch process_files.sh
 
Example: a parameter sweep
--------------------------
 
Pass the index straight to your program as a parameter or random seed:
 
.. code-block:: bash
 
   #!/bin/bash
   #SBATCH --job-name=sweep
   #SBATCH --partition=nodes # or your preferred partition
   #SBATCH --ntasks=1
   #SBATCH --time=00:20:00
   #SBATCH --array=0-99
   #SBATCH --output=logs/%x_%A_%a.out

   # It is assumed that the commands below are included in your .bash_profile
   # in order to allow the use of modules
   # flight start
   # flight env activate gridware

   module load <python-module>
 
   python3 simulate.py --seed $SLURM_ARRAY_TASK_ID
 
For combinations of several parameters, compute them from the index in your
script, or write one combination per line in a file and use the ``sed``
approach shown above.
 
Managing array jobs
-------------------
 
.. code-block:: bash
 
   squeue -u $USER                # arrays appear as 123456_[1-100] while pending
   scancel 123456                 # cancel the whole array
   scancel 123456_7               # cancel just task 7
   sacct -j 123456                # accounting for every task
 
Re-running only failed tasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
If a few tasks failed, list them with ``sacct`` and resubmit only those
indices:
 
.. code-block:: bash
 
   sacct -j 123456 --state=FAILED,TIMEOUT,OUT_OF_MEMORY -X --format=JobID,State
   sbatch --array=7,23,41 process_files.sh
 
Good practice
-------------
 
* Each array task should do a meaningful amount of work, ideally at least a
  few minutes. Thousands of tasks lasting a few seconds each put heavy load
  on the scheduler. Instead, loop over several inputs within each task.
* Use a throttle (``%N``) for large arrays.
* Remember that every array task is a separate job, so the resources you
  request (``--mem``, ``--time``, etc.) apply **per task**.
 
