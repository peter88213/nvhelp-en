Plot menu
=========

**Plot elements operation**

.. figure:: _images/plot_menu01.png
   :alt: novelibre screenshot

Add Arc
-------

**Add a new story arc**

You can add a project note to the tree with **Plot > Add arc**.

-  If an arc is selected, the new item is placed after the selected one.
-  Otherwise, the new arc is placed at the last position.
-  The new arc has an auto-generated title. You can change it in the
   right pane.

Add Plot point
--------------

**Add a new Plot point to the selected arc**

You can add a plot point to an arc with **Plot > Add Plot point**.

- If a plot point is selected, the new plot point is placed after the selected one.
- If an arc is selected, the new plot point is placed at the last position.
- Otherwise, no new plot point is generated.
- The new plot point has an auto-generated title. You can change it in
  the right pane.

Insert Stage
------------

**Insert a stage between the sections**

This inserts a stage after the selected chapter or section.
By default, the new stage is on the second level. You can
change the level to first (see below).

Change Level
------------

**Change the level of the selected stages**

You can change the level of the selected stages with **Plot > Change Level**.

.. figure:: _images/plot_menu02.png
   :alt: novelibre screenshot

-  **1st Level** is displayed in bold face.
-  **2nd Level** is displayed in regular font.

.. note::
   The stage level is only for visual distinction. It has no
   influence on the program functions. 

Export plot description
-----------------------

**Export an ODT document**

You can export a plot description with **Plot > Export plot description**.

This will generate a new OpenDocument text document (odt) containing
stages, arcs, and plot points, each with description.
File name suffix is ``_plot``.


Export plot list (spreadsheet)
------------------------------

**Export an ODS document**

You can export a plot list with **Plot > Export plot list (spreadsheet)**.

This will generate a new OpenDocument spreadsheet (ods) containing a
table with a row for each section and a column for each arc.
Associations between arcs and sections are color-highlighted.
Plot point titles are displayed.

The arc titles and the section titles are hyperlinked to the
respective descriptions in other exported documents, if any.

File name suffix is ``_plotlist``.

.. figure:: _images/plot_menu04.png
   :alt: LibreOffice screenshot

   LibreOffice screenshot. Note the hyperlink from the arc title in the
   plot list (left) to the arc in the plot description (right). 

.. note::
   Hyperlinks in ODS spreadsheets are absolute within the file system, 
   so they might not work after moving the location of your project file
   to another folder or computer. In this case, you will have to 
   export the spreadsheet anew.  

Show plot list
--------------

**Show an HTML report with plot elements**

You can show a plot list in your web browser with **Plot > Show plot list**.

This will generate a list-formatted HTML file, and launch your system’s
web browser for displaying it. The HTML plot list is similar to the
ODS plot list (see above), but without any hyperlinks.

.. figure:: _images/plot_menu03.jpg
   :alt: Edge browser screenshot

   Edge browser screenshot


-  The Report is a temporary file, auto-deleted on program exit.
-  If needed, you can have your web browser save or print it.

