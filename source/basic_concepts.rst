Basic concepts
==============


Summary
   - With *novelibre* you can organize your novel on three hierarchical levels.
   - If you shorten your novel, you can exclude individual chapters and sections
     without deleting them immediately.
     You can also write sections with alternative text so that you can decide
     later what you want to include in the final version.
     To do this, change the *type*.
   - Part of organizing your writing project is keeping track of the
     qualitative progress of your work.
     With *novelibre* you can break this down to the section level
     using the *section completion status* and section notes.
   - *novelibre* offers a limited number of options for highlighting text.
   - Comments, footnotes and endnotes that you insert with *Writer* are not lost.
   - Language assignments for the spell checker in *Writer* are not lost.
   - So that you don't get confused, *novelibre* can lock the project against
     changes as long as you are working with OpenOffice or LibreOffice.


The Book hierarchy
------------------

Parts
~~~~~

A novel is expected to be divided into chapters and sections. Parts
are optional; technically they are first level chapters.
However, in the *novelibre* project tree they are on the same
level as the chapters, but they produce a heading one level above.
Thus, parts are mainly for inserting first level headings between the
chapters, if needed.

.. hint::
   You can convert chapters into parts and vice versa by simply 
   `changing the level <tree_context_menu.html#change-level>`__.

.. note::
   A predecessor of *novelibre* was `novelyst 
   <https://peter88213.github.io/novelyst/>`__. 
   There, the parts were on a higher hierarchy level in the project tree 
   than the chapters, as it corresponds to logical perception. 
   It was therefore possible to move parts together with their subordinate 
   chapters, or to mark entire parts as "Unused". In practice, however, 
   this proved to be cumbersome. I find it easier to move only the part 
   boundaries and leave the chapter order unchanged when defining parts. 


Chapters
~~~~~~~~

A *novelibre* project must at least have one chapter. In the exported
documents, regular chapters have a second level heading.

For *novelibre*, the chapters only serve as containers for sections
to which the actual dramaturgical function is assigned.
This is why there are only a few `chapter properties <chapter_view.html>`__
to be set.


Sections
~~~~~~~~

All body text of a novel in *novelibre* belongs to sections.
Sections can be scenes, pieces of exposition, descriptions, narrative
summaries---it is entirely up to you how you divide your text into
sections. There is a variety of `metadata for sections
<section_view.html>`__ for your free use.

In the text body of the exported documents, sections are separated by
section dividers by default, like so:

``* * *``

However, if you need more fragmented sections when plotting and organizing
than the reader should see later, you can also `append sections
<section_view.html#append-to-previous-section>`__ to each
other as new paragraphs with no section divider inbetween.


Part/chapter/section types
--------------------------

Each part, chapter, and section is of a type that can be changed via
context menu or Part/Chapter/Section menu. The type can be *Normal* or
*Unused*.

Normal
   -  "Normal" type parts, chapters, and sections are counted. The totals
      are displayed in the status bar.
   -  "Normal" type sections are exported to the manuscript and included in
      the word count.
   -  "Normal" type parts and chapters can have subelements of each type.
   -  "Normal" type tree elements are color coded according to the
      `coloring mode settings <view_menu.html#coloring-mode>`__.

Unused
   You can mark parts, chapters, and sections as unused to exclude them
   from word count totals and export.

   -  The subelements of unused parts and chapters are unused as well.
   -  If you mark a section "Unused", its properties are preserved.
   -  Unused tree elements are displayed in gray.


Section completion status
-------------------------

You can assign a status to each "Normal" type section via context menu
or Section menu.
You can choose between *Outline*, *Draft*, *1st Edit*, *2nd Edit*,
and *Done*.

-  You can choose a `coloring mode <view_menu.html#coloring-mode>`__
   to display sections in different colors depending on their
   completion status.
-  Optionally, you can declare one of the status to be the current
   `work phase <book_view.html#writing-progress>`__,
   and choose a `coloring mode <view_menu.html#coloring-mode>`__
   that highlights sections that are behind schedule.
-  Newly created sections are set to "Outline" by default.
-  Word counts by status appear in the `Book properties
   <book_view.html#writing-pogress>`__.

.. hint::
   The `"sticky" section notes <section_view.html#sticky-note>`__
   are intended for more detailed information 
   on what still needs to be done for a section.

   
-----------------


Characters and story world
--------------------------

You can define characters, locations, and items, and you can relate
them to sections to keep track of their place in the story.
There is also some metadata stored with *novelibre*, mainly as a
quick reference that might come in handy when writing or editing.

.. note::
   *novelibre* is not meant as a tool for extensive world building. 
   For this, there is a plethora of dedicated applications, online
   and offline wikis, and notetaking software. However, *novelibre* 
   offers the option of linking images and files with the characters, 
   locations, and items to facilitate access if your external 
   application allows this.
   
   The `nv_zim plugin 
   <https://github.com/peter88213/nv_zim/>`__ 
   connects the writing project with a **Zim Desktop Wiki**.
   This allows the elements of the narrative world 
   to be linked to corresponding wiki pages.
   
.. important::
   If you want to assign **viewpoint characters** to your sections, 
   you first have to `create <characters_menu.html#add>`__ 
   the characters that come into question. 


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

.. tip::
   *novelibre* has no support for images in the text body. 
   You can instead use comments as placeholders. Replace them with your 
   images (or any other special formatting beyond the capabilities of 
   *novelibre*) at the end, when you prepare your `finished novel 
   <export_menu.html#final-manuscript-document-export-only>`__ 
   for publishing. 


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
the project can be automatically locked in order to prevent confusion.
This behavior depends on the `Export settings <export_menu.html#options>`__.

.. important::
   The project can only be locked if all changes are saved. 

In locked state, the project cannot be modified via the user interface.
The footer bar is then displayed in reversed colors, the menu entries
for changing data or exporting other documents are greyed out, and
the widgets in the *Properties* view are disabled.

The project lock state is persistent. This is achieved by automatically
creating a lock file named ``.LOCK.<project name>.novx#``. If you delete
this file while *novelibre* is not running, the project will be unlocked
upon next start.

Usually, the project is automatically unlocked after reimporting the
externally edited document.

.. hint::
   The project lock is nothing more than a strong reminder. You can 
   `unlock the project <file_menu.html#unlock>`__ at any time at your 
   own risk. You also can manually `lock the project <file_menu.html#lock>`__,
   if necessary. The |Lock/Unlock| toolbar button toggles the locking state.


.. |Lock/Unlock| image:: _images/lock.png


