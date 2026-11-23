.. _interactive-jobs:
 
Interactive jobs
================
 
Sometimes you want to work directly on a compute node: to test a program, debug
a problem, or run something that needs your input. An **interactive job** gives
you a command-line session on a compute node, using the same resource
allocation system as batch jobs.
 
Use interactive sessions for testing and development, and batch jobs for
production runs. An idle interactive session still occupies the resources you
requested, so please end it when you have finished.
 
Starting a session with ``srun``
--------------------------------
 
The simplest way is ``srun --pty``:
 
.. code-block:: bash
 
   srun --partition=<partition-name> --ntasks=1 --cpus-per-task=2 \
        --mem=4G --time=01:00:00 --pty bash
 
If resources are available your prompt will change to show a compute node name.
If not, ``srun`` waits until a node is free. To leave the session, type
``exit`` or press ``Ctrl+D``.
 
Starting a session with ``salloc``
----------------------------------
 
``salloc`` reserves resources and starts a shell, from which you can launch
programs with ``srun``. This is useful for MPI testing:
 
.. code-block:: bash
 
   salloc --partition=nodes --nodes=1 --ntasks=4 --time=00:30:00
   srun ./my_mpi_program
   exit
 
Interactive GPU session
-----------------------
 
.. code-block:: bash
 
   srun --partition=gpu-a100 --gres=gpu:1 --cpus-per-task=4 \
        --mem=16G --time=01:00:00 --pty bash
 
Once on the node, you can check the GPU with ``nvidia-smi``.
 
Tips
----
 
* Keep the time limit short. A session is ended when the limit is reached,
  and you will lose any unsaved work.
* Load the modules you need after the session starts, with ``module load``.
* Short interactive requests usually start quickly, but if the cluster is
  busy you may have to wait.
* If your connection drops, the session ends. For longer-running work use a
  batch job instead, or start the session inside ``tmux`` or ``screen`` on the
  login node.
* <Add any Prospero-specific instructions for graphical applications, Jupyter
  or similar here.>
 
