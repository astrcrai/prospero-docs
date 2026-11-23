.. _slurm-job-monitoring:
 
Monitoring and managing jobs
============================
 
Once you have submitted a job you can see where it is in the queue, follow its
progress, and cancel it if necessary.
 
Viewing the queue with ``squeue``
---------------------------------
 
.. code-block:: bash
 
   squeue -u $USER              # your jobs
   squeue -j 123456             # one particular job
   squeue -u $USER -t PENDING   # only your waiting jobs
   squeue -u $USER --start      # estimated start times for pending jobs
 
Typical output::
 
   JOBID   PARTITION  NAME   USER      ST  TIME   NODES  NODELIST(REASON)
   123456  <partition> hello <username> PD  0:00   1      (Priority)
   123457  <partition> sim   <username> R   12:41  2      <node[01-02]>
 
Job states
^^^^^^^^^^
 
.. list-table::
   :header-rows: 1
   :widths: 20 80
 
   * - State
     - Meaning
   * - ``PD``
     - Pending: waiting for resources or for higher-priority jobs.
   * - ``R``
     - Running.
   * - ``CG``
     - Completing: the job has ended and is being cleaned up.
   * - ``CD``
     - Completed successfully (seen in ``sacct``).
   * - ``F``
     - Failed (non-zero exit code).
   * - ``TO``
     - Timed out: it reached its ``--time`` limit.
   * - ``OOM``
     - Out of memory: it used more than it requested.
   * - ``CA``
     - Cancelled, by you or an administrator.
 
Pending reasons
^^^^^^^^^^^^^^^
 
The ``REASON`` shown for a pending job explains why it has not started:
 
.. list-table::
   :header-rows: 1
   :widths: 30 70
 
   * - Reason
     - Meaning
   * - ``Priority``
     - Other jobs have higher priority. Nothing is wrong: your job is waiting
       its turn.
   * - ``Resources``
     - Your job is next, but the requested resources are not yet free.
   * - ``Dependency``
     - It is waiting for another job (see :ref:`slurm-dependencies`).
   * - ``DependencyNeverSatisfied``
     - The job it depended on failed. Cancel and resubmit.
   * - ``QOSMaxJobsPerUserLimit`` / ``AssocGrpCpuLimit``
     - You or your group have reached a usage limit. The job starts when
       other jobs finish.
   * - ``ReqNodeNotAvail``
     - Some requested nodes are reserved or unavailable (for example,
       maintenance).
 
Looking at running jobs
-----------------------
 
The output file you named with ``--output`` is written while the job runs, so
you can follow it live::
 
   tail -f hello_123456.out
 
Press ``Ctrl+C`` to stop watching. Your job is not affected.
 
For full details of a job, including its node list, working directory and
requested resources::
 
   scontrol show job 123456
 
Cancelling jobs
---------------
 
.. code-block:: bash
 
   scancel 123456                     # one job
   scancel 123456_7                   # one task of an array
   scancel -u $USER                   # all of your jobs
   scancel -u $USER --state=PENDING   # only your waiting jobs
   scancel --name=hello               # all your jobs called "hello"
 
.. _slurm-accounting:
 
Checking finished jobs with ``sacct``
-------------------------------------
 
``squeue`` shows only current jobs. Use ``sacct`` to look at jobs that have
finished:
 
.. code-block:: bash
 
   sacct -j 123456
   sacct -u $USER --starttime=2026-11-01
 
Choose the columns to display with ``--format``:
 
.. code-block:: bash
 
   sacct -j 123456 --format=JobID,JobName,Partition,State,Elapsed,Timelimit,MaxRSS,ReqMem,ExitCode
 
Useful columns:
 
.. list-table::
   :header-rows: 1
   :widths: 25 75
 
   * - Column
     - Meaning
   * - ``Elapsed``
     - How long the job actually ran.
   * - ``Timelimit``
     - The time you requested.
   * - ``MaxRSS``
     - The largest amount of memory used by any task. Compare with
       ``ReqMem`` to see whether you requested too much or too little.
   * - ``ExitCode``
     - ``0:0`` means success. A non-zero first number is the program's exit
       status.
   * - ``State``
     - The final state, for example ``COMPLETED``, ``FAILED``, ``TIMEOUT``.
 
.. note::
 
   ``MaxRSS`` is reported on the job's *steps* (for example ``123456.batch``),
   not on the top-level line. Look at the ``.batch`` row.
 
.. Job efficiency with ``seff``
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
.. ``seff`` gives a quick summary of how efficiently a completed job used the CPUs and memory it was given::
 
.. seff 123456
 
.. Use it to right-size future requests. If CPU efficiency is low, you probably requested more cores than your program used.
 
Viewing the cluster with ``sinfo``
----------------------------------
 
.. code-block:: bash
 
   sinfo                       # summary of partitions and node states
   sinfo -p <partition-name>   # one partition
   sinfo -N -l                 # one line per node, with details
 
Node states you may see include ``idle`` (free), ``mix`` (partly used),
``alloc`` (fully used), ``drain`` (being taken out of service) and ``down``.
 
