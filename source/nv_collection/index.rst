|external-link| `Deutsch <https://peter88213.github.io/nvhelp-de/nv_collection/>`_

.. |external-link| image:: ../_images/external-link.png

-----------------

=============
nv_collection
=============

**User guide**

This page refers to the latest `nv_collection
<https://github.com/peter88213/nv_collection/>`__ release.
You can open it with **Help > Collection plugin Online help**.

If you have several *novelibre* projects,
you can manage them as books in a collection, also organized by series.
A collection gives you quick access to your projects.

Start the collection manager
----------------------------

Open the collection manager from the main menu:
**File > Collection**.


Open a collection
-----------------

By default, the latest collection selected is preset.
You can change it with **File > Open**.


Create a new collection
-----------------------

With **File > New**, you can create a new collection.
This will close the current collection and open a file dialog
asking for the location and file name of the collection to create.
Once you specified a valid file path, a blank collection appears.


Create a new series
-------------------

With **Series > Add**, you can add a new series.
Edit the series’ title and description in the right window.


Add books to the collection
---------------------------

To add the current novelibre project as a book to the collection,
use **Book > Add current project to the collection**.
If a series is selected, the book is added as a part of this series.


Update book description
-----------------------

To update the book description from the current project,
use **Book > Update book data from the current project**.

.. caution::
   Be sure not to change the book title, because it is used as identifier.

To update the current project description from the book,
use **Book > Update project data from the selected project**.


Remove books from the collection
--------------------------------

To remove the selected book from the collection,
use **Book > Remove selected book from the collection**.


Move series and books
---------------------

Drag and drop while pressing the ``Alt`` key.

.. caution::
   Be aware, there is no "Undo" feature.


Remove books
------------

To remove a book from the collection,
either select the book and hit the ``Del`` key,
or use **Book > Remove selected book from the collection**.

.. note::
   When removing a book from the collection, 
   the project file associated is kept on disc.


Delete a series
---------------

To delete a series,
either select the series and hit the ``Del`` key,
or use **Series > Remove selected series but keep the books**.

.. note::
   When deleting a series, the books are kept by default.

To delete the selected series and remove all its books from the
collection,
use **Series > Remove selected series**.


Quit/Exit
---------

-  Under Windows you can exit with **File > Exit** or ``Alt``-``F4``.
-  Otherwise you can exit with **File > Quit** or ``Ctrl``-``Q``.
