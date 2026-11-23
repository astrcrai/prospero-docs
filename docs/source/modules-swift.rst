.. _modules-swift:

Recommended modules for SWIFT
=======================

SWIFT is a hydrodynamics and gravity code for astrophysics and cosmology, used widely within the ARI. Its code and documentation are available `here <http://swift.dur.ac.uk/>`_.

To run SWIFT on either the ``epyc7k`` or ``epyc9k`` nodes (i.e. processor agnostic), it is recommended to load the following modules:

.. code-block:: node-agnostic

   module load intel-oneapi-compilers/2025.3.2
   module load openmpi/5.0.9/intel-oneapi-compilers-2025.3.2/a-mc4ghdh
   module load metis/5.1.0/intel-oneapi-compilers-2025.3.2/a-p3mdotl
   module load gsl/2.8/intel-oneapi-compilers-2025.3.2/a-3u6nn6b
   module load fftw/3.3.10/intel-oneapi-compilers-2025.3.2/openmpi-5.0.9/a-ruypg6o
   module load hdf5/1.14.6/intel-oneapi-compilers-2025.3.2/openmpi-5.0.9/a-yagvvhx
   module load sundials/5.8.0/intel-oneapi-compilers-2025.3.2/openmpi-5.0.9/a-evskisp

and to compile the code on an ``epyc7k`` node, for example by starting an :doc:`interactive session <slurm-interaction-jobs>`: 

.. code-block:: bash
 
   srun --partition=nodes --constraint=epyc7k --ntasks=1 --cpus-per-task=16 \
        --mem=8G --time=01:00:00 --pty bash

If you intend to restrict your job to the ``epyc9k`` nodes, you can compile directly on ``login3``. In this case the recommended modules are:

.. code-block:: epyc9k

	module load intel-oneapi-compilers/2025.3.2
	module load openmpi/5.0.9/intel-oneapi-compilers-2025.3.2
	module load metis/5.1.0/intel-oneapi-compilers-2025.3.2
	module load sundials/5.8.0/intel-oneapi-compilers-2025.3.2
	module load gsl/2.8/intel-oneapi-compilers-2025.3.2
	module load fftw/3.3.10/intel-oneapi-compilers-2025.3.2
	module load hdf5/1.14.6/intel-oneapi-compilers-2025.3.2/openmpi-5.0.9/a-he5rnib
