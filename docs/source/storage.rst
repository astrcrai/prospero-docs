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
| Data storage           | /mnt/scratch        | 3.6 PB     | All                               |
+                        +---------------------+------------+-----------------------------------+
|                        | /mnt/data1          | 220 TB     | All                               |
+                        +---------------------+------------+-----------------------------------+
|                        | /mnt/aridata1       | 233 TB     | ARI members                       |
+------------------------+---------------------+------------+-----------------------------------+

Quotas
------------
Each user's homespace is limited to a quota of 30GB. Large datasets should be stored on the data volumes. 

VSCode and Python environments such as ``conda`` can quickly fill your homespace with temporary hidden files (often caches) that may not show up with the ``du`` command. For example, check for directories such as ``.cache`` and ``.vscode-server``. It is recommended that you move these directories to your personal user space on the scratch space ``/mnt/scratch/users/[USERNAME]`` and create softlinks from your homespace to these from their original location. For example: 

$ cd ~
$ mv .vscode-server /mnt/scratch/users/[USERNAME]/
$ ln -s /mnt/scratch/users/[USERNAME]/.vscode-server .vscode-server

Backups
------------
At present no volumes are backed up, so users are advised to keep their source code on a version control system and maintain their own backups. We hope to install a system to provide daily backups of the homespace during 2026. 

Best practice
------------
Please keep important code on the homespace and keep this backed up yourself. For most users, it is advised to keep data specific to personal projects in /mnt/scratch/users/[USERNAME]. Data for projects involving multiple users should be kept in /mnt/scratch/projects/[PROJECTNAME]. The volume /mnt/data1 is in principle available to all users but is a legacy system that predates the high-performance ClusterStor facility that hosts /mnt/archive. 
