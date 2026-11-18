.. _first_job:

Running your first job with SLURM
=================================

Prospero uses the `SLURM <https://slurm.schedmd.com/>`_ job scheduler to share
its resources between users. Instead of running programs directly on the
login node, you write a short *job script* describing what you want to run and
what resources you need, and submit it to SLURM. SLURM then queues your job and
runs it on a compute node as soon as resources are available.

This page walks you through submitting a very simple job for the first time.

.. important::

   Do not run computationally intensive programs on the login nodes.
   These are shared by all users and are only intended for editing files,
   submitting jobs and performing light tasks.

Before you start
----------------

You will need:

* An account on Prospero (see :ref:`getting-access`).
* To be logged in to the login node (see :ref:`first_login`).


Step 1: Create a job script
---------------------------

A job script is a plain text file containing two parts: lines beginning with
``#SBATCH``, which tell SLURM what resources you need, followed by the commands
you want to run.

Create a file called ``hello.sh`` using a text editor such as ``nano``::

   nano hello.sh

and paste in the following:

.. code-block:: bash

   #!/bin/bash
   #SBATCH --job-name=hello
   #SBATCH --partition=test  # `test` is a short duration SLURM partition on Prospero  
   #SBATCH --nodes=1
   #SBATCH --ntasks=1
   #SBATCH --time=00:01:00
   #SBATCH --output=hello_%j.out

   echo "Hello from $(hostname)"
   echo "This job started at $(date)"
   sleep 10
   echo "This job finished at $(date)"

Save the file and exit (in ``nano``, press ``Ctrl+O``, ``Enter``, then
``Ctrl+X``).

What do the ``#SBATCH`` lines mean?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Option
     - Meaning
   * - ``--job-name=hello``
     - A name for your job, shown when you check the queue.
   * - ``--partition=<partition-name>``
     - Which group of nodes (partition) to run on. We chose to run on ``test`` which is Prospero's high priority partition for short jobs.
   * - ``--nodes=1``
     - The number of nodes required.
   * - ``--ntasks=1``
     - The number of tasks (processes) to run. One is enough for this example.
   * - ``--time=00:01:00``
     - The maximum run time (``HH:MM:SS``). Your job is stopped if it
       exceeds this, so always request slightly more than you expect to need.
   * - ``--output=hello_%j.out``
     - The file that the job's output is written to. ``%j`` is replaced by the
       job ID.

Step 2: Submit the job
----------------------

Submit your script to SLURM with ``sbatch``::

   sbatch hello.sh

If the submission is successful, SLURM prints the ID of your job::

   Submitted batch job 123456

Make a note of this number: you will use it to check on or cancel your job.

Step 3: Check the status of your job
------------------------------------

To see your jobs in the queue, use ``squeue``::

   squeue -u $USER

You will see output similar to::

   JOBID   PARTITION  NAME   USER      ST  TIME  NODES  NODELIST(REASON)
   123456  <partition> hello <username> R   0:03  1      <node-name>

The ``ST`` column shows the state of the job. The most common states are:

* ``PD``: pending (waiting for resources to become available)
* ``R``: running
* ``CG``: completing

Once your job has finished it will disappear from the list. This job should
only take around ten seconds once it starts running.

Step 4: View the output
-----------------------

When the job has finished, an output file will appear in the directory you
submitted it from. The filename contains your job ID::

   ls
   hello.sh  hello_123456.out

View it with ``cat``::

   cat hello_123456.out

You should see something like::

   Hello from <node-name>
   This job started at Wed 18 Nov 10:15:02 GMT 2026
   This job finished at Wed 18 Nov 10:15:12 GMT 2026

Note that the hostname is that of a *compute node*, not the login node. This
confirms that your job ran on the cluster.

Congratulations, you have run your first SLURM job!

Cancelling a job
----------------

If you need to cancel a job, either while it is queued or running, use
``scancel`` with the job ID::

   scancel 123456

Checking a completed job
------------------------

To see a summary of a job after it has finished, including how long it ran
and whether it completed successfully, use ``sacct``::

   sacct -j 123456

Troubleshooting
---------------

**My job stays in the** ``PD`` **state for a long time.**
   The ``REASON`` column in ``squeue`` explains why. ``Resources`` or
   ``Priority`` simply mean the job is waiting its turn.

**I get "Invalid account or account/partition combination".**
   Check that the partition name is correct and that you have access to it.

**There is no output file.**
   The job may not have started yet, or may have failed immediately. Check
   ``squeue`` and ``sacct -j <jobid>``.

Next steps
----------

* Learn how to request more cores, memory and GPUs: :ref:`requesting-resources`
* Load software using environment modules: :ref:`using-modules`
* Run many similar jobs at once with job arrays: :ref:`job-arrays`
* Run an interactive session: :ref:`interactive-jobs`

If you get stuck, please contact the support team at <support-email>.

A few things to adjust before publishing:

Cross-references: the :ref: labels (getting-access, requesting-resources, etc.) are placeholders and will cause Sphinx warnings until matching labels exist, so rename or remove them.
Account flag: if Prospero requires users to specify a project or account, add #SBATCH --account=<project> to the example script and the options table.
Partition and limits: use a partition that’s quick to schedule, so a new user’s first job starts promptly.

I can also write the follow-on pages, such as requesting resources, job arrays or interactive sessions, in the same style.

Claude Code is built into this app
