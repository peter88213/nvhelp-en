nv_templates
===================

**Online help**

This page refers to the latest `nv_templates
<https://peter88213.github.io/nv_templates/>`__ release.
You can open it with **Help > Templates plugin Online help**.


Command reference
-----------------

File > New
~~~~~~~~~~

Create from template
^^^^^^^^^^^^^^^^^^^^

This creates a new project with the narrative structure from a Markdown
template file.

-  First, a file select dialog asks for the new project’s file name
   (noveltree v1.4+). If you cancel the dialog, you can select the file
   name later when saving the project.
-  Then a second file select dialog asks for the template file to apply.

Tools > Story Templates
~~~~~~~~~~~~~~~~~~~~~~~

Load
^^^^

This loads the narrative structure from a Markdown template file.

-  A file select dialog asks for the template file to apply.

Save
^^^^

This saves the narrative structure to a Markdown template file.

-  A file select dialog asks for the new template’s file name.

Open folder
^^^^^^^^^^^

This opens the templates folder with the OS file manager, so you can
manage and edit the templates.

Conventions
-----------

In *noveltree*, you can define a narrative structure with “Todo” Parts,
Chapters, and scenes. See
`Arcs <https://peter88213.github.io/noveltree/help/arcs>`__.
*nv_templates* faciliates the reuse of narrative structures.

Markdown file structure
~~~~~~~~~~~~~~~~~~~~~~~

The *Story Template* Markdown file defines such a structure with
headings and ordinary text.

First level heading for top level stages, e.g. acts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first level heading begins with ``#``, followed by a space and a
stage title.

Second level heading for minor stages or turning points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The second level heading begins with ``##``, followed by a space and a
stage title.

Ordinary text
^^^^^^^^^^^^^

Any text under a heading is used as a description for the element
generated from the heading.

Example
^^^^^^^
.. highlight:: markdown

:: 

   # ACT 1

   Setup

   ## Inciting Incident

   Also called "catalyst" or "call to adventure".
   This sets the protagonist in motion.

   ## Plot Point 1

   "Point of no return": The protagonist engages with the action 
   the inciting incident has created.

   # ACT 2

   Confrontation

   ## Midpoint

   The main turning point. A significant event, changing the 
   development of things from good to bad, or vice versa.

   ## Plot Point 2

   The aftermath of the Midpoint crisis.
   What changes the protagonist from "passenger" to "driver".  

   # ACT 3

   Resolution

   ## Climax

   The final moment of the story's conflict.

This file generates the following structure in an empty project:

.. figure:: _images/structure01.png
   :alt: Screenshot


