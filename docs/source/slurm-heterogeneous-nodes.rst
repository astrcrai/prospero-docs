.. _slurm-heterogeneous-nodes:
 
Efficient use of nodes in a heterogeneous system
===================

As of July 2025, Prospero's cpu-only nodes come in two different :ref:`specifications <specifications>`.

Most notably they are equipped with processors **that have differing numbers of cores**, and different memory footprints. The standard compute partitions (``nodes`` and ``long``, see the :ref: `partitions<slurm-prospero-partitions>` page) on SLURM include nodes of both specification. Unless otherwise instructed, SLURM will assume that jobs can be submitted to either type of node, including a mix of both types for parallel or array jobs. 

SLURM submission scripts therefore should **not** assume a particular node specification (e.g. a particular number of cores, or memory footprint, per node). Users are therefore discouraged from requesting resources with the ``#SBATCH --nodes=`` option unless there is a specific reason to do so. 

To illustrate why: consider the following example:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --partition=nodes
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=64
    #SBATCH --cpus-per-task=1

If allocated to the older Apollo-based nodes with ``epyc7k`` processors (64 cores per node) the job will make efficient use of resources, as all compute cores on the nodes will be used. But if allocated to the newer Cray-based nodes with ``epyc9k`` processors (128 cores per node), only half of the cores will be used on each node; the job could actually be executed on a single Cray node. Therefore, for this simple example it is recommended to instead specify:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --partition=nodes
    #SBATCH --ntasks=128
    #SBATCH --cpus-per-task=1

which will enable Slurm to allocate the job the 128 cores it requests by allocating either two Apollo nodes, or a single Cray node.

It is possible to submit jobs to the ``nodes`` and ``long`` partitions, but restrict them to running on only one type of node, i.e. only Apollo nodes or only Cray nodes. To do this, one includes the SLURM option ``--constraint=epyc7k`` to restrict to Apollo nodes and ``--constraint=epyc9k`` to restrict to Cray nodes.  

One should also be aware that the ``login3`` node has the same specification as the Cray nodes, and hence has ``epyc9k`` processors. Compiling code natively on the ``login3`` node therefore runs the risk of including instructions that are specific to the ``epyc9k`` processors and which will not run on ``epyc7k`` processors if a job is assigned to an Apollo node. If one is submitting jobs to the queue that are agnostic to the specification of the nodes, it is important to compile your code in such a way that instructions specific to ``epyc9k`` processors are not included; this includes linking to libraries compiled in the same way. If you need help to ensure this is done correctly, please log an HPC help ticket. 

Finally, note that it is not advised to run parallel jobs that span both types of node. This is because the Apollo and Cray nodes are networked via different Infiniband switches that are not interconnected: communication between Apollo and Cray nodes is therefore only possible via ethernet, which is high latency and relatively low bandwith. Execution of parallel jobs spanning both types of node is possible, but the performance is likely to be very poor.
