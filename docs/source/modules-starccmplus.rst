.. _modules-starccmplus:

Recommended modules for StarCCM+
=======================

There are currently 2 versions of StarCCM installed. version 16 and version 18

.. code-block:: slurm

    flight env activate gridware
    module load apps/starccm/16.02.008-R8

    # Simulation Case File:
    INPUT="input.sim"

    # Machinefile:
    MACHINEFILE=hosts.star

    # Write Node List to Machinefile:
    scontrol show hostname ${SLURM_JOB_NODELIST} > ${MACHINEFILE}

    # Simcenter Licence Server Address:
    export CDLMD_LICENSE_FILE=1999@flex.cd-adapco.com

    # POD Licence Key:
    export LM_PROJECT=XXXXXXXXXXXXXXXXXXXXX

    # Start Parallel STAR-CCM+ Job:
    starccm+ -power -np ${SLURM_NTASKS} -machinefile ${MACHINEFILE} -batch ${INPUT} -collab -rr -rrthreads 63 -rgraphics mesa -graphics mesa

.. note::

    Take note that ``-rr -rrthreads 63 -rgraphics mesa -graphics mesa`` is required to be included. This is due to there is a known issue with StarCCM and AMD EPYC CPU's
