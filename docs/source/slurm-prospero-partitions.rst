.. _slurm-prospero-partitions:

Partitions on Prospero
----------------------
  
==========   ==========   ========   ==========
Name         Time limit   Priority   Resources
==========   ==========   ========   ==========
nodes        24 hours     Standard   All standard compute nodes (epyc7k and epyc9k)
long         72 hours     Low        All standard compute nodes (epyc7k and epyc9k)
test         1 hour       High       16 epyc7k nodes
himem        24 hours     Standard   Both memory-rich nodes
gpu-a100     24 hours     Standard   GPU-accelerated node (epyc7k, A100 GPU)
gpu-h200     24 hours     Standard   GPU-accelerated node (epyc9k, H200 GPU)
==========   ==========   ========   ==========

The ``nodes`` and ``long`` partitions share the same resources. Users should consider ``nodes`` as the standard partition. Jobs requiring a longer execution time may use ``long`` but this partition has a **lower priority factor** to encourage more frequent job cycling. Unless otherwise arranged with ITS, users of the ``gpu-a100`` and ``gpu-h200`` partitions can use a maximum of 2 GPUs at once.
