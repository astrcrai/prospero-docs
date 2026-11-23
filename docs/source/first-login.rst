.. _first-login:

Logging on for the first time
===============

Access to the terminal on the gateway node(s) is via SSH. Prospero has a single login node, login3. You reach it through the gateway address ``prospero2.ljmu.ac.uk``, which serves the whole Prospero facility.

.. NOTE::

   The original gateway address, ``prospero.ljmu.ac.uk`` is now disabled.  Note that ``login1`` and ``login2`` were both part of the original Prospero cluster that is now retired.

As a security measure, Prospero uses a non-standard SSH port (10022), therefore this port must be specified via the ``-p`` argument, e.g.

.. code-block:: ssh

    ssh ITSusername@prospero2.ljmu.ac.uk -p 10022

A more elegant solution is to add a code snippet to your ``.ssh/config`` in which you can specify that this port should always be used when connecting to Prospero:

.. code-block:: ssh-config

    Host prospero
        User ITSusername
        HostName prospero2.ljmu.ac.uk
        Port 10022

SSH config files can be used to specify many useful settings, as explained in the manual ``man 5 ssh_config``.

Once comfortable using ssh, you may wish to simplify logging onto Prospero by using an :ref:`ssh key pair <ssh-key-pair>`. 
