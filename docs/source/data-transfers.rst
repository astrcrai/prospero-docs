.. _data-transfers:

Trasferring data to and from Prospero
=====

We recommend ``rsync``, which can resume interrupted transfers and only copies
what has changed. Prospero uses a non-standard SSH port (see :doc:`access`), so
the port must be specified. To copy a directory *to* Prospero:

.. code-block:: bash

   rsync -avP -e "ssh -p 10022" mydata/ ITSusername@prospero2.ljmu.ac.uk:/mnt/scratch/users/ITSusername/mydata/

and to copy results *back* to your own machine:

.. code-block:: bash

   rsync -avP -e "ssh -p 10022" ITSusername@prospero2.ljmu.ac.uk:/mnt/scratch/users/ITSusername/results/ ./results/

If you have added Prospero to your ``~/.ssh/config`` as described there, the
``-e "ssh -p 10022"`` option is not needed. The trailing slashes matter to
``rsync``: ``mydata/`` copies the *contents* of the directory, whereas ``mydata``
copies the directory itself.

**Check that transfers are intact.** For important data, compare checksums at
both ends:

.. code-block:: bash

   sha256sum myfile.dat            # run on both systems and compare the output
   sha256sum -c checksums.sha256   # verify a list of files against stored checksums

**Many small files.** Transferring and storing hundreds of thousands of tiny
files is slow and puts strain on shared file systems. Where practical, bundle
them into an archive first:

.. code-block:: bash

   tar -czf mydata.tar.gz mydata/
