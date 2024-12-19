Storage and data management
=====

Datastores
------------

Prospero has the following datastores:

+------------------------+---------------------+------------+-------------+
| Type                   | Mount point         | Capacity   | For use by  |
|                        |                     |            |             |
+========================+=====================+============+=============+
| Homespace              | /users/             | 3.1 TB     | All         |
+------------------------+---------------------+------------+-------------+
| Data storage           | /mnt/scratch        | 2 PB       | All         |
+                        +---------------------+------------+-------------+
|                        | /mnt/data1          | 220 TB     | All         |
+                        +---------------------+------------+-------------+
|                        | /mnt/backup1        | 66 TB      | Admins      |
+                        +---------------------+------------+-------------+
|                        | /mnt/aridata1       | 233 TB     | ARI members |
+                        +---------------------+------------+-------------+
|                        | /mnt/archive        | 3.0 PB     | ARI members |
+------------------------+---------------------+------------+-------------+

Quotas
------------

Currently each user's homespace is limited to a quota of 150GB with a hard limit of 175GB. Large datasets should be stored on /mnt/data1. 

Backups
------------
At this time users are recommended to keep their own backups.
