.. _modules-arepo:

Recommended modules for AREPO
=======================

AREPO is a hydrodynamics and gravity code for astrophysics and cosmology, used widely within the ARI. Code and documentation available `here <https://arepo-code.org/wp-content/userguide/index.html>`_.

AREPO users generally restrict their jobs to the ``epyc9k`` nodes, so can compile the code directly on ``login3``. The recommended modules are:

.. code-block:: arepo

   module load gsl/2.8/intel-oneapi-compilers-2025.3.2/a-khk6nt4
   module load openmpi/5.0.9/intel-oneapi-compilers-2025.3.2/a-wme4dry
   module load hdf5/1.14.6/intel-oneapi-compilers-2025.3.2/openmpi-5.0.9/a-ul73fui
   module load fftw/3.3.10/intel-oneapi-compilers-2025.3.2/openmpi-5.0.9/a-3mlterz
   module load gmp/6.3.0/gcc-15.2.0/a-vdkvo3x
   module load openblas/0.3.30/gcc-15.2.0/a-puzk4cn
   module load python/3.14.2/gcc-15.2.0/a-7uigfia
