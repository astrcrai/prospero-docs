Storage and data management
=====

Datastores
------------

Prospero has the following datastores:

+------------------------+---------------------+------------+-----------------------------------+
| Type                   | Mount point         | Capacity   | For use by                        | 
|                        |                     |            |                                   |             
+========================+=====================+============+===================================+
| Homespace              | /users/             | 3.1 TB     | All                               |
+------------------------+---------------------+------------+-----------------------------------+
| Data storage           | /mnt/scratch        | 2 PB       | All                               |
+                        +---------------------+------------+-----------------------------------+
|                        | /mnt/data1          | 220 TB     | All                               |
+                        +---------------------+------------+-----------------------------------+
|                        | /mnt/backup1        | 66 TB      | Admins                            |
+                        +---------------------+------------+-----------------------------------+
|                        | /mnt/aridata1       | 233 TB     | ARI members                       |
+                        +---------------------+------------+-----------------------------------+
|                        | /mnt/archive        | 3.0 PB     | ARI members                       |
|                        |                     |            | Will be decomissioned Q2/2025     |
+------------------------+---------------------+------------+-----------------------------------+

Quotas
------------
Each user's homespace is limited to a quota of 150GB with a hard limit of 175GB. Large datasets should be stored on the data volumes.

Backups
------------
At present no volumes are backed up, so users are advised to keep their source code on a version control system and maintain their own backups.

Future storage
------------
We are currently commissioning a new HPE ClusterStor parallel filesystem, which we hope will be available Q2/2025.
