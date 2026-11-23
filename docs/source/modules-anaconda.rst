.. _modules-anaconda:

Recommended modules for Anaconda
=======================

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
