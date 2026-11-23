Software
=====

Users may install software themselves in their home space or data space, so long as it does not require ``root`` (also known as ``superuser``) access. Users can also request that software is installed centrally by our HPC partners, Alces Flight.

Centralised software on Prospero is installed by Alces Flight within their ``gridware`` environment. We recommend starting the gridware within your startup script (e.g. ``.bash_profile``) with

.. code-block:: flight-start

    flight start
    flight env activate gridware

.. note::

   It is possible to create customised environments within ``flight``, e.g. for research groups needing a common set of packages. If you require this, please submit a :ref:`support ticket<Getting help & support>`. 

Modules
-------

Starting ``gridware`` makes the ``module`` command available, which provides access to common packages and libraries. To see a list of available modules, issue the command:

.. code-block:: modules

    module avail

To then load, for example, the latest available version of ``python3``, one can issue the command:

.. code-block:: python3
    
    module load apps/python3

For more information on modules, see `this link <https://modules.readthedocs.io/en/latest/>`_. Below we provide recommended module lists for use with popular software packages on Prospero. 

Modules for different Prospero processor types
-------

Some modules will activate software/libraries that are **compiled**, as opposed to interpreted. 

.. NOTE::

   In a compiled language, the target machine directly translates the program. In an interpreted language, the source code is not directly translated by the target machine. Instead, a different program, aka the interpreter, reads and executes the code.

Unless otherwise specified, the compilers (the program that converts source code into an executable file) generate native code, i.e. code that uses the instruction set of the processor the source code was compiled by. Hence, if one compiles code on the ``login3`` gateway node, the executable file will assume it can use all the instructions available to the ``epyc9k`` processors used by Prospero's HPE Cray XD225 nodes (``login3`` shares the same specification as an HPE Cray XD225 node). It is then possible that the executable file will **not** run on the ``epyc7k`` processors used by Prospero's HPE Apollo XL225 nodes. As such, when loading modules that activate compiled code, one needs to be aware of which node types the code will be executed on. Because of this, the ``gridware`` module environment has two separate module sets.

The first is:

.. code-block:: agnostic
    
    /opt/gridware/subscribed/etc/modulefiles/linux-rocky9-x86_64_v3

Modules in this set were compiled on ``epyc7k`` processors, making the software/libraries agnostic to which nodes the code is run on, as the newer ``epyc9k`` processors can run code compiled on older epyc processors.

The second is:

.. code-block:: zen4
    
    /opt/gridware/subscribed/etc/modulefiles/linux-rocky9-zen4

Modules in this set were compiled on ``epyc9k`` processors, optimising them for execution on the newer HPE Cray XD225 nodes. It is likely that this software, or software linking these libraries, will **not** run on the older HPE Apollo XL225 nodes, but it may run faster on the newer nodes.


