Getting started
===============

Starting from zero
------------------

If you start *novelibre* by dragging a *.novx* file onto the icon,
that project will be opened. Otherwise, the project from the last
session will be automatically reopened, if there is one.

Let's assume that neither is the case, for example when the program
is called up for the very first time after installation.
Let's also assume that we have not yet made any preparations, i.e.
we have neither a work in progress nor an outline of any kind. First
of all, we create a new empty project with **File > New > Empty project**.

.. figure:: _images/getting_started01.png
   :alt: novelibre screenshot
   
A file selection dialog opens and asks for the file name and location
of the new project.

.. tip::
   It is advantageous to create a separate folder for the project, as 
   all exported documents are also stored here. This also includes 
   auxiliary files such as timelines or project-related configuration 
   files for tools and plugins. 

It is not mandatory, but we should then enter a title and the author's
name. Perhaps also a description of our idea. To get started right away,
we will postpone the remaining project settings until later.

.. figure:: _images/getting_started02.png
   :alt: novelibre screenshot
   
We need at least one section in order to get space to begin writing.
And this must belong to a chapter. So we now create the first
chapter with **Chapter > Add**.

.. figure:: _images/getting_started03.png
   :alt: novelibre screenshot
   
After the chapter is created, *novelibre* sets the focus on the chapter
title entry at the top of the right pane. Let's overwrite the default
title.

.. figure:: _images/getting_started04.png
   :alt: novelibre screenshot
   
.. hint::
   If you decide to let *novelibre* `auto-number the chapters 
   <book_view.html#auto-numbering>`__, you can skip this and keep the
   default chapter title. 

There are several ways to add a section now. In this example, we
right-click on the chapter, and select **Add section**.

.. figure:: _images/getting_started05.png
   :alt: novelibre screenshot


Starting the manuscript immediately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As soon as the new section appears in the tree view, we can export a
manuscript. Just click on the |Export manuscript| toolbar icon.

.. |Export manuscript| image:: _images/manuscript.png

.. figure:: _images/getting_started06.png
   :alt: novelibre screenshot
   
Done! LibreOffice should now appear with the manuscript open.
Just start writing your novel within the text boundary.

.. figure:: _images/getting_started07.png
   :alt: Libreoffice screenshot
   
We can now continue working with LibreOffice `as described on the next
page <writing.html>`__, creating new sections and chapters as we write.

.. tip::
   You can now work on the manuscript document "on the seat of your pants"
   until it makes sense for  you to transfer the whole thing back to 
   *novelibre* in order to create an overview and set up your project 
   organization there.
   
   However, I recommend doing this at least daily at the end of your writing 
   session and exporting a new manuscript document the next day. 
   Then you won't get behind with entering the section titles and content 
   descriptions, and you will get your chapters numbered, if desired. 
   In addition, *novelibre* then saves entries in the daily word count log.
   
   
Creating a chapter structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you prefer to make a plan first before you start writing, *novelibre* is
the right tool for you.
Then you don't start LibreOffice with an empty manuscript, but first create
a framework of empty chapters for which you enter content information.
Or you can leave it at one chapter for the time being and create empty sections
in it, which you can later distribute to chapters.
The results of this preliminary work can be exported as text documents in the
form of synopses, e.g on
`chapter <chapter_menu.html#export-chapter-descriptions-for-editing>`__ or
`section <section_menu.html#export-section-descriptions-for-editing>`__ level.


Creating a dramatic structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

However, you can also start on a more abstract level and first create and
describe stages like acts or steps in order to later insert the sections as
scenes.
For this, you first create at least one chapter. Then create your stages.

.. figure:: _images/getting_started08.png
   :alt: novelibre screenshot

The system is described on the `Plotting with novelibre <plotting.html>`__
page.
There you also can learn how to set up multiple strands or character arcs.

.. tip::
   With the `nv_templates plugin <nv_templates/index.html>`__ you can have 
   *novelibre* set up your new project with a pre-made structure like the
   "Three Act Model" or "Save The Cat". 


-----------------


Starting with a work in progress
--------------------------------

Let's assume that you have already written an extensive novel manuscript with
LibreOffice and now want to edit it with *novelibre*.
In this case you first make sure to set it up in a way, *novelibre* can
recognize its parts, chapters, and sections.

.. important::
   How to set up a work in progress for import
      A work in progress has no third level heading.
      
      -  *Heading 1* → New chapter title (beginning a new section).
      -  *Heading 2* → New chapter title.
      -  ``* * *`` → Section divider (not needed for the first section in a
         chapter).
      -  All other text is considered section content.
      



create your new project
with **File > New > Create from ODT...**.

.. figure:: _images/getting_started09.png
   :alt: novelibre screenshot

A file selection dialog opens and asks for the *.odt* document. The new project will
be created in the same directory and named after the manuscript file, but with the *.novx*
extension.

.. caution::
   Once your novel is imported into *novelibre*, your initial *.odt* document is no
   longer needed. So if you want to keep it, you best move it elsewhere, so that
   it is not overwritten by a later `exported document 
   <export_menu.html#manuscript-for-printing-export-only>`__. 





Starting with an outline
------------------------

.. important::
   How to set up an outline for import
      An outline has at least one third level heading.
      
      -  *Heading 1* → New chapter title (beginning a new section).
      -  *Heading 2* → New chapter title.
      -  *Heading 3* → New section title.
      -  All other text is considered to be chapter/section description.
