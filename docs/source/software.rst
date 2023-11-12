Software
=====

Centralised software on Prospero is installed by Alces Flight within their ``gridware`` environment. We recommend starting the gridware within your startup script (e.g. ``.bash_profile``) with

.. code-block:: flight-start

    flight start
    flight activate env gridware

.. note::

   It is possible to create customised environments within ``flight``, e.g. for research groups needing a common set of packages. If you require this, please submit a :ref:`support ticket<Getting help & support>`. 

Starting ``gridware`` makes the ``module`` command available, which provides access to common packages and libraries. To see a list of available modules, issue the command:

.. code-block:: modules

    module avail

To then load, for example, the latest available version of ``python3``, one can issue the command:

.. code-block:: python3
    
    module load apps/python3

For more information on modules, see `this link <https://modules.readthedocs.io/en/latest/>`_. Below we provide recommended module list for use with popular software packages on Prospero. 

Recommended modules
-------

**Intel OneAPI compiler suite** 

Lorem ipsum 

**Gadget4** 

Lorem ipsum 

**StarCCM+** 

Lorem ipsum 

**SWIFT** 

Code and documentation available `here <http://swift.dur.ac.uk/>`_.
Note that the recommended module for SWIFT are slightly more complicated, as we have found that it helps to use ``openmpi`` compiled against a specific version of the low-level ``ucx`` communication library.

.. code-block:: swift

    module load apps/oneapi/2021.2.0
    module load compiler-rt
    module load tbb
    module load mpi/openmpi/4.0.5/intel-2021.2.0+ucx-1.8.0
    export LD_LIBRARY_PATH=/opt/apps/alces/ucx/1.11.2+intel-2021.2.0+el8/lib:$LD_LIBRARY_PATH
    export PATH=/opt/apps/alces/oneapi/2021.2.0/compiler/2021.2.0/linux/bin/intel64/:$PATH
    module load libs/metis/5.1.0/intel-2021.2.0
    module load libs/gsl/2.6/intel-2021.2.0
    module load libs/fftw3_double/3.3.8/intel-2021.2.0+openmpi-4.0.5
    module load apps/hdf5_mpi/1.12.0/intel-2021.2.0+openmpi-4.0.5
    module load libs/sundials_sp/5.8.0/intel-2021.2.0

Note that the ``sundials`` differential equation solver is only needed if you are using versions of ``SWIFT`` that use the ``CHIMES`` chemistry network (e.g. the ``COLIBRE`` branch). 

Relatedly with SWIFT, it is recommended to export the following environment variables in ``slurm`` job submission scripts:

.. code-block:: swift-slurm

    export UCX_IB_RCACHE_MAX_REGIONS=32768
    export UCX_IB_GID_INDEX=0
    export OMPI_MCA_btl_openib_allow_ib=1
    export OMPI_MCA_btl_openib_if_include="mlx5_0:1"
    export OMPI_MCA_btl=^vader,tcp,openib,uct

In the event of code lock-ups, we advise reducing the value of ``UCX_IB_RCACHE_MAX_REGIONS`` by factors of 2 until the issue resolves. We have seen some cases where values as low as 4096 are needed for stability, at the expense of performance.
