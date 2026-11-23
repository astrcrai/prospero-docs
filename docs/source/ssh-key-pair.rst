.. _ssh-key-pair:

Generating an SSH key pair
===========================================================

An SSH key pair replaces your password with two files: a private key that stays on your personal computer, and a public key that you copy to Prospero. When you connect from your personal computer to Prospero, SSH proves you hold the private key without ever sending it. This can be particularly convenient when using ``VS Code`` or transferring data using ``rsync``.

.. IMPORTANT::

   Never share, email or copy your private key. Only the public key should leave your personal computer.

The command to create an SSH key pair is:

.. code-block:: bash

    ssh-keygen -t ed25519

When asked where to save the key, press Enter to accept the default ``~/.ssh/id_ed25519`` or choose your own filename. If a key already exists there, answer ``n`` rather than overwriting it, and just reuse it.

When asked for a passphrase, type one you will remember. This protects the key if your laptop is lost or stolen. Nothing appears as you type. You can also just not have a passphrase, which is less secure. By default, two files are created: ``id_ed25519`` (private key) and ``id_ed25519.pub`` (public key).

Next, you can use the ``ssh-copy-id`` command to copy the public key to Prospero:

.. code-block:: bash

    ssh-copy-id -i ~/.ssh/id_ed25519.pub prospero 

Note that this last step assumes that you have configured your ``.ssh/config`` file as instructed `here <https://prospero-docs.readthedocs.io/en/latest/first_login.html>`_. 

You should now be able to log onto Prospero without needing to enter your LJMU password. If you used a passphrase for your SSH key pair, you will need to enter this.
