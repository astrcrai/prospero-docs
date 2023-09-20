Storage and data management
=====

Datastores
------------

Prospero has the following datastores:

+------------------------+---------------+------------+-------------+
| Type                   | Mount point   | Capacity   | For use by  |
|                        |               |            |             |
+========================+===============+============+=============+
| Homespace              | /users/       | 3.1 TB     | All         |
+------------------------+---------------+------------+-------------+
| Data storage           | /mnt/data1    | 220 TB     | All         |
+                        +---------------+------------+-------------+
|                        | /mnt/backup1  | 66 TB      | Admins      |
+                        +---------------+------------+-------------+
|                        | /mnt/aridata1 | 233 TB     | ARI members |
+                        +---------------+------------+-------------+
|                        | /mnt/lustre1  | 1.5 PB     | ARI members |
+                        +---------------+------------+-------------+
|                        | /mnt/lustre2  | 1.3 PB     | ARI members |
+------------------------+---------------+------------+-------------+

Quotas
------------

Currently users homespace are limited with a quota with a soft limit and a hard limit. The softlimit is 150GB and the hardlimit is 175GB. Due to this recommend that if you have any large simulations then this should be should be stored within data1. A larger general purpose storage area is being looked at currently.

Backups
------------
At this time users are recommended to keep their own backups.
