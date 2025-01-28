Saving data
===========

*novelibre* saves the entire novel text as well as all metadata
in a single text file with the file extension ``.novx``.
The text and spreadsheet documents created in the work process are considered
temporary files, as their contents can be restored from the corresponding *novx*
project file as long as it is kept up to date by timely reimport.
So if a specific editing status is to be archived, this one project file is sufficient.
However, there may also be additional files such as timelines or a project wiki.


Change notification
-------------------

If you change the project during a *novelibre* session, the color of the footer bar
changes to goldenrod to show that there are unsaved changes.
This change notification is retained until you save the project or restore an earlier
editing status.

.. hint::
   For technical reasons, the change notification is retained even if you undo all changes. 
   It therefore does not actually show a changed editing status, but that 
   changes were made since last save. 
 
To discard all changes since the last save, you can restore the last saved status via the
`Reload <file_menu.html#reload>`__ menu command.

Backup files
------------

*novelibre* is designed to secure its data as well as possible.
The current files are neither overwritten nor completely deleted,
but backup copies with the extension ``.bak`` are created.
In this way, the penultimate editing status is still available
and can even be restored via the
`Restore backup <file_menu.html#restore-backup>`__ menu command.

.. hint:: 
   *novelibre* creates such *bak* backup copies not only for *novx* files, 
   but also for the temporary text and spreadsheet documents and for 
   files that are e.g. synchronized via plugins, such as timelines.

Optionally, you can also make *novelibre* create a copy of the project file
in a
`custom backup directory <tools_menu.html#backup-options>`__
each time it is saved.
You should not work in this backup directory, which is why the backup copies
are given a file name suffix that you must remove manually when restoring.


-----------------


Remarks on the file format
--------------------------

*novx* files are text files that are human-readable and can in principle
be displayed and edited with any text editor.
The text and data are structured using XML tags
making the file understandable for computers.

The definition of the *novx* XML format can be found here:

https://peter88213.github.io/novxlib-docs/

The information is intended for computer experts who are interested in using the
various standard techniques for reading and processing XML files.
As a novelist and regular user, you don't have to worry about any of this.
However, you can relax in the knowledge that there are no secrets about
the storage of your work results.

Anyway, there is one aspect for you to consider, namely the file version.
It can happen that *novelibre* is extended by features that make it necessary to
extend the *novx* file format as well.
This is then noted in the changelog.
In such cases, the version number of the *novx* file format is incremented.
This version number is stored in the *novx* file and is checked by *novelibre*
each time a project is opened.
If *novelibre* encounters a file version that was created with a newer program version,
this means that this project could contain information that the currently running program
does not know and that could therefore be lost when it is saved again.
For this reason, *novelibre* will not open such a file and will display a corresponding
error message in the status bar.

.. important::
   To avoid such problems, simply make sure that, if you are working on several computers, 
   you have the same program version of *novelibre* installed everywhere. 
   Preferably the latest release. 
   


