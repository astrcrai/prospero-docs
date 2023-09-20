Getting access
===============

Eligible LJMU staff and students (see :ref:`Policies`) wishing to obtain an account on Prospero should submit a ticket to the HPC section of the `LJMU IT Helpdesk <https://helpme.ljmu.ac.uk/>`_, to request the creation of an account. 

Per the usage policy, research collaborators at external institutions with a genuine need to use Prospero may also obtain an account. They must first register with LJMU Human resources as an ``external consultant`` in order to obtain an ITS account, after which their LJMU sponsor may request the creation of a Prospero account for them via the helpdesk.

Logging on
--------------

Access to the terminal on the gateway node(s) is via SSH. The gateway's address is

.. code-block:: gateway-address

    prospero.ljmu.ac.uk

As a security measure, Prospero uses a non-standard SSH port (10022), therefore this port must be specified via ``-p`` argument, e.g.

.. code-block:: ssh

    ssh ITSusername@prospero.ljmu.ac.uk -p 10022

Alternatively, we suggest adding a code snippet to your ``.ssh/config`` file like the following:

.. code-block:: ssh-config

    Host prospero.ljmu.ac.uk
        User ITSusername
        HostName prospero.ljmu.ac.uk
        Port 10022



