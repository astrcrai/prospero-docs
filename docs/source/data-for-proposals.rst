.. _data-for-proposals:

Data management planning
=====

Good research data management (RDM) makes your work reproducible, protects it
against loss, and helps you meet the requirements of your funder, your
publisher and the university. This page explains how to apply good RDM
practice when working on Prospero. It complements, and does not replace,
LJMU's own research data policies and the guidance of your funder.

.. note::

   Prospero is a *working* environment for computation. It is not an archive,
   and **at present none of its storage volumes are backed up** (see
   :doc:`storage`). Plan for your important data to live somewhere else as well.

Before you start: plan your data
--------------------------------

Most funders expect a data management plan (DMP), and it is much easier to
write one before a project begins than after. A DMP describes what data you will
create, how it will be stored, documented and shared, and who is responsible
for it. When planning a project that will use Prospero, consider:

* How much data will you generate, and in what file formats?
* How much of it needs to be kept after the project, and for how long?
* Does any of it have restrictions (see `Data that must not be stored on Prospero`_)?
* Who else needs access, inside and outside LJMU?
* Where will the master copy of any input data and any final results be kept?

LJMU's Research and Knowledge Exchange Data Management Policy expects the
arrangements for access to, and retention or destruction of, research data to
be set out in a data management plan. The Library's Research Engagement (Open
Research) team can help you draft a plan and give feedback on it, and LJMU
recommends the free `DMPonline <https://dmponline.dcc.ac.uk/>`_ tool, which has
templates for UKRI funders and others. Plans are typically short, often one to
three pages. See the Library's
`research data management pages <https://www.ljmu.ac.uk/library/researchers/research-data-management>`_
for the policy, guidance and contacts.

Data that must not be stored on Prospero
----------------------------------------

Under the Prospero :doc:`policies <policies>`:

* personal data should not be stored on the system, and
* survey data should not be stored on the system, even if anonymised.

If your project involves human participants, or any data that is sensitive,
confidential or subject to a data-sharing agreement, speak to your supervisor
or the University's data protection and research ethics contacts *before*
transferring anything to Prospero. Do not assume that a dataset is acceptable
because it has been pseudonymised or because it is "only for testing". See
also LJMU's Data Protection Policy and Information Security Policy, and the
Research Ethics and Governance guidance, which apply to research data in the
same way as to any other university information.

Where to keep your data on Prospero
-----------------------------------

Prospero has several storage areas with different purposes; the full list,
capacities and quotas are given on the :doc:`storage` page. In outline:

* Your **home directory** has a small quota. Use it for scripts, source code,
  configuration files and small results, not for datasets.
* **Scratch** (``/mnt/scratch``) is the main area for working data. Keep personal
  project data in ``/mnt/scratch/users/[USERNAME]`` and data shared between
  several users in ``/mnt/scratch/projects/[PROJECTNAME]``.
* ``/mnt/data1`` is a legacy volume, and ``/mnt/aridata1`` is reserved for
  members of the Astrophysics Research Institute.

Treat everything on Prospero as *working copies*. Keep the authoritative
version of irreplaceable data (raw observations, original input files, final
published results) in a location that is backed up and under your control, for
one of the storage options described in the Library's *Research data storage*
guidance, or a suitable repository.

Protecting your data
--------------------

Because Prospero volumes are not backed up, you are responsible for protecting
anything you cannot afford to lose. A commonly recommended approach is the
"3-2-1 rule": keep **three** copies of important data, on **two** different
types of storage, with **one** copy held off-site or in a different system.

* Keep **source code, job scripts and analysis scripts** under version control
  (for example ``git``) and push them to a remote repository.
* Keep **raw and input data** in at least one other location, and record where.
* Copy **final results** off Prospero as soon as they are produced.
* Do not rely on scratch space as the only home for anything important.

Moving data to and from Prospero
--------------------------------

See :ref:data_transfers.

Organising and documenting your data
------------------------------------

Data that cannot be understood is of little use to anyone, including you in
six months' time.

* **Use a consistent directory structure** that separates raw inputs, processed
  data, code and results, for example ``raw/``, ``processed/``, ``scripts/`` and
  ``results/``.
* **Never modify raw data in place.** Treat input files as read-only and
  write derived data to a different location.
* **Use clear, consistent file names** without spaces, and include dates in
  ``YYYY-MM-DD`` form or version numbers where relevant.
* **Add a README** to each project directory describing what the data are, how
  they were produced, the meaning of columns or variables and units, who to
  contact, and any licence or access restrictions.
* **Prefer open, well-documented file formats** (for example CSV, HDF5, NetCDF,
  FITS, plain text) over proprietary ones where possible, so the data remain
  usable in the long term.

Making your results reproducible
--------------------------------

To reproduce a result you need to know exactly what produced it. For each
significant set of results, keep a record of:

* the **version of your code**, for example the ``git`` commit hash
  (``git rev-parse HEAD``);
* the **job script** used to run it, including the Slurm options;
* the **software environment**, for example the output of ``module list``, and for
  Python environments ``conda env export > environment.yml``;
* the **input data and parameters**, including random-number seeds;
* the **date** the job ran and the Slurm job ID.

A simple approach is to store the job script, an environment listing and a short
text log in the same directory as the output files, and to commit scripts and
documentation to version control.

Sharing data with collaborators
-------------------------------

For data shared between several Prospero users, use a project directory
(``/mnt/scratch/projects/[PROJECTNAME]``) rather than copying files between
personal areas. Agree within the group who is responsible for the contents,
how the directory is organised, and who tidies it up at the end of the
project. Keep file permissions no more open than needed; for example
``chmod -R g+rX directory`` gives group members read access without making
files writable.

Collaborators at other institutions can be granted access to Prospero if they
meet the criteria in the :doc:`policies`; for larger datasets, consider whether
sharing via a repository would be more appropriate.

Publishing and preserving data
------------------------------

Many funders and journals expect the data underlying a publication to be made
available, and many expect data to be retained for a number of years after a
project ends. Check your funder's and publisher's specific requirements, and
LJMU's Records Retention Schedule, which sets out how long records are kept. You
may also need to include a *data availability statement* in your papers.

To make data publicly available and citable:

* Consider the **LJMU Research Data Repository** (`opendata.ljmu.ac.uk
  <http://opendata.ljmu.ac.uk>`_), the University's institutional repository for
  open-access research data. Each deposit is issued with a DOI, and data are
  deposited through Symplectic, the University's research information system. If
  your funder or discipline favours a subject-specific repository, use that
  instead; general-purpose repositories such as `Zenodo <https://zenodo.org/>`_
  are also widely used. For repository queries, contact
  researchonline@ljmu.ac.uk.
* Choose a **licence** for the data (for example a Creative Commons licence) and
  state it clearly in your README and metadata.
* Include enough **documentation and metadata** for others to understand and
  reuse the data, and cite the dataset in related publications. LJMU asks for a
  README file to accompany every deposit, and the Library provides a template.
* Where possible, follow the FAIR principles, described in the next section.

Not all data can or should be shared openly. Restrictions arising from
confidentiality, third-party agreements or commercial interests should be
recorded in your data management plan. For questions about intellectual property
or commercially exploitable data, contact LJMU's Knowledge Exchange and
Commercialisation team.

The FAIR principles
-------------------

The FAIR Guiding Principles (Wilkinson *et al.*, `Scientific Data 3, 160018
<https://doi.org/10.1038/sdata.2016.18>`_, 2016) describe how data should be
managed so that both people and computers can find and reuse them. They are
widely referenced by funders and publishers, and LJMU encourages researchers to
follow them; the `GO FAIR <https://www.go-fair.org/fair-principles/>`_ and
`OpenAIRE <https://www.openaire.eu/how-to-make-your-data-fair>`_ websites
explain them in more detail. FAIR stands for Findable, Accessible,
Interoperable and Reusable.

.. note::

   **FAIR does not mean open.** FAIR data can have access restrictions, for
   example because of confidentiality or commercial agreements. What matters is
   that the data are well described, that it is clear how they can be accessed
   and under what conditions, and that the description itself is findable.

The table below summarises each principle and what it means in practice for
data produced on Prospero.

.. list-table::
   :header-rows: 1
   :widths: 18 38 44

   * - Principle
     - What it asks for
     - In practice
   * - **Findable**
     - Data and metadata have a globally unique, persistent identifier; data are
       described with rich metadata; metadata include the identifier of the
       data; and both are registered or indexed in a searchable resource.
     - Deposit the data in a repository that issues a DOI, such as the LJMU
       Research Data Repository, and complete the metadata fields fully
       (title, description, keywords, dates, funder). Cite the DOI in your
       papers. A directory on Prospero is not a findable dataset.
   * - **Accessible**
     - Data can be retrieved by their identifier using a standard, open and free
       protocol, with authentication and authorisation where necessary; metadata
       remain available even when the data are no longer available.
     - Use a repository so that the data can be retrieved through a persistent
       link. If the data are restricted, say so in the metadata and explain how
       to request access. Do not make Prospero the only place the data can be
       obtained: access to it is limited to approved users and it is not an
       archive.
   * - **Interoperable**
     - Data and metadata use a formal, shared and broadly applicable language
       and vocabularies, and include qualified references to other data.
     - Use open, standard file formats (for example CSV, HDF5, NetCDF, FITS),
       follow the conventions and metadata standards of your field, define
       variable names and units, and use community vocabularies where they
       exist. Link to related datasets, code and publications by DOI.
   * - **Reusable**
     - Data have plenty of accurate and relevant attributes, a clear data
       usage licence, detailed provenance, and meet domain-relevant community
       standards.
     - Include a README, state a licence (for example a Creative Commons
       licence), and record provenance: the code version, software environment,
       parameters and input data used to produce the results (see
       `Making your results reproducible`_).

FAIR also applies to **research software**. Code used to produce published results
should be kept under version control, given a licence and, where appropriate,
archived with a DOI (for example by linking a ``git`` repository to Zenodo) so
that it can be cited alongside the data.

You do not need to make every dataset perfectly FAIR. Aim to apply the
principles as far as is reasonable for the data you are depositing, and record
any limitations, and the reasons for them, in your README and data management
plan.

Finishing a project or leaving LJMU
-----------------------------------

When a project ends, or before you leave the university:

#. Copy anything you need to keep to a backed-up location or repository.
#. Make sure collaborators and your supervisor or principal investigator know
   where the data and code are, and that documentation is up to date.
#. Delete temporary and intermediate files from Prospero. Shared storage is a
   limited resource and other users are waiting for it.
#. Transfer responsibility for any shared project directories to a continuing
   member of staff.

Acknowledging Prospero
----------------------

If Prospero was used to produce results that you publish, please include the
standard acknowledgement given on the :doc:`policies` page. This allows the
facility's contribution to research to be tracked.

Checklist
---------

* I have a data management plan, or have recorded my data plans somewhere my
  team can see them.
* No personal or survey data is stored on Prospero.
* Irreplaceable data and final results have a copy outside Prospero.
* Code and job scripts are under version control.
* Large transfers have been checked with checksums.
* My project directory has a README and a clear structure.
* I have recorded the code version, environment and parameters for key results.
* I know where my data will be published or preserved, and for how long.
* Where data are being shared, they have a persistent identifier, a licence,
  open-format files and a README (the FAIR principles).

Getting help
------------

For questions about using Prospero storage, raise a query with the HPC section
of the `LJMU Helpdesk <https://helpme.ljmu.ac.uk/>`_ (see :doc:`help`). For
questions about data management plans, the LJMU data repository or research
data policy, contact the Library's Research Engagement (Open Research) team via
the `Library's research data management pages <https://www.ljmu.ac.uk/library/researchers/research-data-management>`_.
For data protection and ethics questions, contact the relevant University
teams.
