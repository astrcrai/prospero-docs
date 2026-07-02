.. _my-reference-label: Access

Getting access
===============

Eligible LJMU staff and students (see :ref:`Policies`) wishing to obtain an account on Prospero should submit a ticket to the HPC section of the `LJMU IT Helpdesk <https://helpme.ljmu.ac.uk/>`_, to request the creation of an account. 

Per the usage policy, research collaborators at external institutions with a genuine need to use Prospero may also obtain an account. They must first register with LJMU as an honorary visiting academic or honorary visiting student, after which their LJMU sponsor may request the creation of a Prospero account for them via the helpdesk.

Logging on
--------------

Access to the terminal on the gateway node(s) is via SSH. New users should use the address

.. code-block:: gateway-address

    prospero2.ljmu.ac.uk

The old gateway, ``prospero.ljmu.ac.uk`` is only for legacy users. As a security measure, Prospero uses a non-standard SSH port (10022), therefore this port must be specified via the ``-p`` argument, e.g.

.. code-block:: ssh

    ssh ITSusername@prospero2.ljmu.ac.uk -p 10022

A more elegant solution is to add a code snippet to your ``.ssh/config`` in which you can specify that this port should always be used when connecting to Prospero:

.. code-block:: ssh-config

    Host prospero2.ljmu.ac.uk
        User ITSusername
        HostName prospero2.ljmu.ac.uk
        Port 10022

SSH config files can be used to specify many useful settings, as explained in the manual ``man 5 ssh_config``.

Migrating to the new operating system
--------------

Over the summer of 2026, Prospero's hardware will migrate to a newer operating system, and the use of more capable back-end infrastructure servers that will deliver superior performance. This is a major upgrade that will be performed in stages. In effect, a second cluster will be created based on the new operating system, using a separate gateway ``prospero2.ljmu.ac.uk`` and an entirely new home space. Compute nodes will be migrated from the old operating system to the new one in batches. They will cease to be accessible to SLURM partitions on the original gateway, and will become accessible to those on the new one. 

Users will need to create a new working environment on the home space at ``prospero2.ljmu.ac.uk``. Necessary libraries can be requested for central installation by Alces, by submitting an ITS helpdesk ticket. Any compiled codes will need to be recompiled against the new versions of libraries, using an updated compiler suite on the new partition. We recommend using the Intel OneAPI suite (and if necessary the openmpi library) by loading the appropriate module:

.. code-block:: compilers

    module load intel-oneapi-compilers/2025.3.2
    module load openmpi/5.0.9/intel-oneapi-compilers-2025.3.2

An important change that users should be aware of when using ``prospero2`` is that batch queue jobs submitted via ``SLURM`` should use invoke their executables with the ``srun`` command rather than ``mpirun``. We have found that using the latter can result in ``#SBATCH`` configuation values not being passed to the job. 
