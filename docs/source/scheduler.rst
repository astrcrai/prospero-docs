=====
Slurm quickstart
=====

The Prospero HPC cluster is made up of a number of compute nodes, which consist of one or more processors, memory and in the case of the GPU nodes, GPUs. 
These computing resources are allocated to the user by the resource manager. This is achieved through the submission of jobs by the user. A job describes the computing resources required to run application(s) and how to run it. 
Prospero uses Slurm as a job scheduler and resource manager.

Slurm commands overview
=======================

In the following, you will learn how to submit your job using the Slurm Workload Manager. If you aren't acquainted with Slurm, the following will introduce you to the basics. 
The main commands for using Slurm are summarized in the table below.

=======     ===========
Command	    Description
=======     ===========
sbatch	    Submit a batch script
srun	    Run a parallel job(step)
squeue	    View information about jobs in the scheduling queue
scancel	    Signal or cancel jobs, job arrays or job steps
sinfo	    View information about nodes and partitions
=======     ===========

Creating a batch script
=======================
The most common type of jobs are batch jobs which are submitted to the scheduler using a batch job script and the sbatch command.
A batch job script is a text file containing information about the job to be run: the amount of computing resource and the tasks that must be executed.
A batch script is summarized by the following steps:

*	the interpreter to use for the execution of the script: bash, python, ...
*	directives that define the job options: resources, run time, ...
*	setting up the environment: prepare input, environment variables, ...
*	run the application(s)

As an example, let's look at this simple batch job script:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --job-name=exampleJob
    #SBATCH --time=02:00:00
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem=2G
    #SBATCH --partition=compute

    flight env activate gridware
    module load MyApp/1.2.3

    srun myapp -i input -o output

In the previous example, the first line ``#!/bin/bash`` specifies that the script should be interpreted as a bash script.
The lines starting with ``#SBATCH`` are directives for the workload manager. These have the general syntax

.. code-block:: bash

    #SBATCH option_name=argument

Now that we have introduced this syntax, we can go through the directives one by one. The first directive is

.. code-block:: bash

    #SBATCH --job-name=exampleJob

which sets the name of the job. It can be used to identify a job in the queue and other listings.  

The remaining lines specify the resources needed for the job. The first one is the maximum time your job can run. If your job exceeds the time limit, it is terminated regardless of whether it has finished or not.

.. code-block:: bash

    #SBATCH --time=02:00:00

The time format is hh:mm:ss (or d-hh:mm:ss where d is the number of days). Therefore, in our example, the time limit is 2 hours.
The next four lines of the script describe the computing resources that the job will need to run

.. code-block:: bash

    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --mem=2G

In this instance we request one task (process) to be run on one compute core. A task corresponds to a process (or an MPI rank). One CPU thread (used, for example, with OpenMP) is requested for the one task as well as 2 GiB of memory, allocated to the whole job.
The next line defines the Slurm partition to which the job will be submitted. Slurm partitions are (possibly overlapping) groups of nodes with similar resources or associated limits. In our example, the job doesn't use a lot of resources and will fit perfectly onto the standard ``compute`` partition. A complete list of Slurm partitions available on Prospero is given :ref:`below<Slurm partitions>`.

.. code-block:: bash

    #SBATCH --partition=compute

Now that the needed resources for the job have been defined, the next step is to set up the environment. For example, copy input data from your home directory to the scratch file system or export environment variables.

.. code-block:: bash

    module load MyApp/1.2.3

In our example, we load a module so that the MyApp application is available to the batch job. Finally, with everything set up, we can launch our program using the srun command.

.. code-block:: bash

    srun myapp -i input -o output


Submit a batch job
=======================

To submit the job script we just created we use the sbatch command. The general syntax can be condensed as

.. code-block:: bash

    $ sbatch [options] job_script [job_script_arguments ...]

The available options are the same as the one you use in the batch script: sbatch --ntasks=1 in the command line and #SBATCH --ntasks=1 in a batch script are equivalent. The command line value takes precedence if the same option is present both on the command line and as a directive in a script.
For the moment let's limit ourselves to the most common way to use the sbatch: passing the name of the batch script which contains the submission options.

.. code-block:: bash
    
    $ sbatch myjob.sh
    Submitted batch job 123456

The sbatch command returns immediately and if the job is successfully submitted, the command prints out the ID number of the job.


Examine the queue
=======================

Once you have submitted your batch script it won't necessarily run immediately. It may wait in the queue of pending jobs for some time before its required resources become available. In order to view your jobs in the queue, use the squeue command.

.. code-block:: bash

    $ squeue
    JOBID PARTITION     NAME     USER  ST       TIME  NODES NODELIST(REASON)
    123456     small exampleJ prospero_usr  PD       0:00      1 (Priority)

The output shows the state of your job in the ST column. In our case, the job is pending (PD). The last column indicates the reason why the job isn't running: Priority. This indicates that your job is queued behind a higher priority job. One other possible reason can be that your job is waiting for resources to become available. In such a case, the value in the REASON column will be Resources.
Let's look at the information that will be shown if your job is running:

.. code-block:: bash

    $ squeue
    JOBID   PARTITION   NAME     USER  ST       TIME  NODES NODELIST(REASON)
    123456  small       exampleJ prospero_usr   R      35:00      1 node-0123

The ST column will now display a R value (for RUNNING). The TIME column will represent the time your job has been running. The list of nodes on which your job is executing is given in the last column of the output.
In practice the list of jobs printed by this command will be much longer since all jobs, including those belonging to other users, will be visible. In order to see only the jobs that belong to you use the squeue command with the --me flag.

.. code-block:: bash

    $ squeue --me

The squeue command can also be used to determine when your pending job will start.

.. code-block:: bash

    $ squeue --me --start
    JOBID PARTITION     NAME     USER ST          START_TIME  NODES SCHEDNODES           NODELIST(REASON)
    123456     batch Computat   vananh PD 2021-06-01T16:10:28      1 node0012             (Priority)
    123457     batch Computat   vananh PD 2021-06-01T18:21:28      1 (null)               (Priority)

In our example, both jobs listed will start June 1 at different times. You will also notice that for the first job, the scheduler plan to run the job on node0012 while for the second job, no node has been chosen yet.

Cancelling a job
=======================

Sometimes things just don't go as planned. If your job doesn't run as expected, you may need to cancel your job. This can be achieved using the scancel command which takes the job ID of the job to cancel.

.. code-block:: bash

    $ scancel <jobid>

The job ID can be obtained from the output of the sbatch command when submitting your job or by using squeue. The scancel command applies to either a pending job waiting in the queue or to an already running job. In the first case, the job will simply be removed from the queue while in the latter, the execution will be stopped.

Slurm partitions
=======================

Prospero offers the following Slurm partitions:

=========   ===========     ========     ==========           
Name	    Time limit	    Priority     Resources             
=========   ===========     ========     ==========           
compute	    24 hours	    Standard     All standard compute nodes (Prospero-I and Prospero-II)                   
long	    72 hours	    Low          All standard compute nodes (Prospero-I and Prospero-II)
test	    1 hour          High         All standard compute nodes (Prospero-I)
himem	    24 hours        Standard     Both memory-rich nodes
gpu         24 hours        Standard     GPU-accelerated node
ari    	    12 hours        Standard     A single node ringfenced to ARI users
transients  12 hours        Standard     A single node (no Infiniband) ringfenced to daily analysis of Liverpool Telescope data 
=========   ===========     ========     ==========

The ``compute`` and ``long`` partitions share the same resources. Users should consider ``compute`` as the standard partition. Jobs requiring a longer execution time may use ``long`` but this partition has a **lower priority factor** to encourage more frequent job cycling. Unless otherwise arranged with ITS, users of the ``gpu`` partition can use a maximum of 2 GPUs at once. The ``ari`` and ``transients`` partitions are ringfenced to members of the Astrophysics Research Institute.

Slurm priorities
=======================

Prospero uses Slurm's `multifactor priority algorithm <https://slurm.schedmd.com/priority_multifactor.html>`_. The scheduler prioritises larger jobs and primarily balances the usage of accounts (``ARI``, ``FET``, ``LJMU``) rather than individual users. Therefore, for example, two users with the same individual consumption level will have differing FairShare scores if their accounting groups have seen markedly different resource consumption in recent days. At present, the scheduler aims to apportion 5% of the resources to the ``LJMU`` group (which currently contains only a small number of users) and divides the remainder equally between ``ARI`` and ``FET``. 

Slurm scripts in the Prospero-II era
=======================

As of July 2025, Prospero comprises two islands of nodes (Prospero-I and Prospero-II) that have significantly different `specifications <https://prospero-docs.readthedocs.io/en/latest/specifications.html>`_, most notably they have different numbers of cores and different memory footprints. To maximise the effective use of Prospero's resources, all nodes from both islands can be accessed from the ``compute`` and ``long`` partitions. This has implications for how Slurm scripts should be written. Specifically, the scripts should not assume a particular node specification (e.g. a particular number of cores, or memory footprint, per node), since (unless otherwise instructed) the scheduler can to allocate jobs to nodes from either (or both) island. Users are therefore discouraged from using the ``#SBATCH --nodes=`` option unless there is a specific reason to do so. 

To illustrate why: consider the following example:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --partition=compute
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=64
    #SBATCH --ncpus-per-task=1

If allocated to the Prospero-I partition, the job will make efficient use of resources, as all compute cores on the nodes will be used, but if allocated to the Prospero-II partition only half of the cores will be utilised on each node. The job could actually be executed on a single Prospero-II node. Therefore, for this simple example it is recommended to instead specify:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --partition=compute
    #SBATCH --ntasks=128
    #SBATCH --ncpus-per-task=1

which will enable Slurm to allocate the job the 128 cores it requests by allocating either two Prospero-I nodes, or a single Prospero-II node.

It is possible to submit jobs to the ``compute`` and ``long`` partitions, but restrict them to running on only one type of node, i.e. only Prospero-I nodes or only Prospero-II nodes. To do this, one includes the SLURM option ``--constraint=epyc7k`` to restrict to Prospero-I nodes and ``--constraint=epyc9k`` to restrict to Prospero-II nodes.  


