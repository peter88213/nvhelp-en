Basic concepts
==============


Part/chapter/section types
--------------------------

Each part, chapter, and section is of a type that can be changed via
context menu or Part/Chapter/Section menu. The type can be *Normal* or
*Unused*.

Normal
   -  “Normal” type parts, chapters, and sections are counted. The totals
      are displayed in the status bar.
   -  “Normal” type sections are exported to the manuscript and included in
      the word count.
   -  “Normal” type parts and chapters can have subelements of each type.
   -  “Normal” type tree elements are color coded according to the
      `coloring mode settings <view_menu.html#coloring-mode>`__.

Unused
   You can mark parts, chapters, and sections as unused to exclude them
   from word count totals and export.

   -  The subelements of unused parts and chapters are unused as well.
   -  If you mark a section “Unused”, its properties are preserved.
   -  Unused tree elements are displayed in gray.


Section completion status
-------------------------

You can assign a status to each “Normal” type section via context menu
or Section menu.

-  Newly created sections are set to “Outline” by default.
-  Word counts by status appear in the `Book properties
   <book_view.html#writing-pogress>`__.

-----------------

Formatting text
---------------

It is assumed that very few types of text markup are needed for a novel
text. When importing from ODT, *novelibre* supports the following
formats:

-  *Emphasized* style or italics.
-  *Strongly emphasized* style or bold.
-  *Quotations* (paragraph visually distinguished from body text).
-  *Unordered list item* (indented paragraph with a bullet).


Comments, footnotes, endnotes
-----------------------------

ODT comments, footnotes, and endnotes are supported by *novelibre*.


About document language handling
--------------------------------

ODF documents are generally assigned a language that determines spell
checking and country-specific character substitutions. In addition,
Office Writer lets you assign text passages to languages other than the
document language to mark foreign language usage or to suspend spell
checking.

Document overall
   The project language (Language code acc. to ISO 639-1 and country code
   acc. to ISO 3166-2) can be set in the **Book** settings (right pane)
   under `Document language <book_view.html#document-language>`__.

Text passages in sections
   Paragraph-wise or inline text markup for other languages is supported by
   *novelibre*.

-----------------

Project lock
------------

When exporting a document that can be edited outsides *novelibre*,
the project is automatically locked in order to prevent confusion.

.. important::
   The project cannot be locked unless changes are saved. 

In locked state, the project cannot be modified via the user interface.
The footer bar is then displayed in reversed colors, the menu entries
for changing data or exporting other documents are greyed out, and
the widgets in the *Properties* view are disabled.

The project lock state is persistent. This is achieved by automatically
creating a lock file named ``.LOCK.<project name>.novx#``. If you delete
this file while *novelibre* is not running, the project will be unlocked
upon next start.

Usually, the project is automatically unlocked after re-importing the
externally edited document.

.. hint::
   The project lock is nothing more than a strong reminder. You can 
   `unlock the project <file_menu.html#unlock>`__ at any time at your 
   own risk. You also can manually `lock the project <file_menu.html#lock>`__,
   if necessary. The |Lock/Unlock| toolbar button toggles the locking state.


.. |Lock/Unlock| image:: _images/lock.png


