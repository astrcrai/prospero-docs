Software
=====

Centralised software on Prospero is installed by Alces Flight within their ``gridware`` environment. We recommend starting the gridware within your startup script (e.g. ``.bash_profile``) with

.. code-block:: flight-start

    flight start
    flight env activate gridware

.. note::

   It is possible to create customised environments within ``flight``, e.g. for research groups needing a common set of packages. If you require this, please submit a :ref:`support ticket<Getting help & support>`. 

Starting ``gridware`` makes the ``module`` command available, which provides access to common packages and libraries. To see a list of available modules, issue the command:

.. code-block:: modules

    module avail

To then load, for example, the latest available version of ``python3``, one can issue the command:

.. code-block:: python3
    
    module load apps/python3

For more information on modules, see `this link <https://modules.readthedocs.io/en/latest/>`_. Below we provide recommended module lists for use with popular software packages on Prospero. 

Recommended modules
-------

**Intel OneAPI compiler suite with OpenMpi** 

.. code-block:: intel_oneapi_mpi

	module load intel-oneapi-compilers/2025.3.2 # not 100% sure this is needed, but I had it loaded anyway
	module load openmpi/5.0.9/intel-oneapi-compilers-2025.3.2

**StarCCM+** 

There is currently 2 versions of StarCCM installed. version 16 and version 18

.. code-block:: slurm

    flight env activate gridware
    module load apps/starccm/16.02.008-R8

    # Simulation Case File:
    INPUT="input.sim"

    # Machinefile:
    MACHINEFILE=hosts.star

    # Write Node List to Machinefile:
    scontrol show hostname ${SLURM_JOB_NODELIST} > ${MACHINEFILE}

    # Simcenter Licence Server Address:
    export CDLMD_LICENSE_FILE=1999@flex.cd-adapco.com

    # POD Licence Key:
    export LM_PROJECT=XXXXXXXXXXXXXXXXXXXXX

    # Start Parallel STAR-CCM+ Job:
    starccm+ -power -np ${SLURM_NTASKS} -machinefile ${MACHINEFILE} -batch ${INPUT} -collab -rr -rrthreads 63 -rgraphics mesa -graphics mesa

.. note::

    Take note that ``-rr -rrthreads 63 -rgraphics mesa -graphics mesa`` is required to be included. This is due to there is a known issue with StarCCM and AMD EPYC CPU's


**SWIFT / COLIBRE** 

Code and documentation available `here <http://swift.dur.ac.uk/>`_.

.. code-block:: swift

	module load intel-oneapi-compilers/2025.3.2
	module load openmpi/5.0.9/intel-oneapi-compilers-2025.3.2
	module load metis/5.1.0/intel-oneapi-compilers-2025.3.2
	module load sundials/5.8.0/intel-oneapi-compilers-2025.3.2
	module load gsl/2.8/intel-oneapi-compilers-2025.3.2
	module load fftw/3.3.10/intel-oneapi-compilers-2025.3.2
	module load hdf5/1.14.6/intel-oneapi-compilers-2025.3.2/openmpi-5.0.9/a-he5rnib


**Anaconda**

The ``gridware`` environment includes an installation of Anaconda that can be enabled via

.. code-block:: anaconda-activate

    flight env activate gridware
    module load apps/anaconda3/2023.03/bin

Once activated, Anaconda should be initialised using the following command.

.. code-block:: anaconda-init

    conda init <SHELL>

Essentially, this step modifies the configuration file(s) for the requested shell(s) by adding the commands that launch Anaconda. This way, Anaconda is automatically loaded upon subsequent logins and you can skip enabling step described above. The default shell available on Prospero is ``Bash``. 

A comprehensive introduction to Anaconda is beyond the scope of this document, and we refer the reader to the official documentation available `here <https://docs.anaconda.com/free/anacondaorg/user-guide/>`_. However, you can create a new environment, arbitrarily called ``testenv`` in our case, via

.. code-block:: anaconda-create

    conda create -n testenv

and afterwards activate it via

.. code-block:: anaconda-activate

    conda activate testenv

Once activated, Python modules can be added to the new environment via, e.g.,

.. code-block:: anaconda-install

    conda install numpy
	
*Using a Python environment in your Slurm scripts*

In order to use your Python environment in a job submitted to the queue, you will need to load it first. To that aim, add the following lines to your batch script before running any Python code

.. code-block:: anaconda-slurm

    flight env activate gridware
    module load apps/anaconda3/2023.03/bin
    eval "$( conda shell.bash hook )"
    conda activate testenv

Following those lines, you can run any Python program using your environment by including lines like the following in the script.

.. code-block:: anaconda-srun

   srun python testprog.py

