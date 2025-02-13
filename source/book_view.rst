Book properties
===============

The Book properties view opens in the right pane
when you select "Book" in the tree,
or when you click on the |Show Book| toolbar icon.
It is the initial view after opening a *novelibre* project.

.. |Show Book| image:: _images/viewBook.png

.. image:: _images/book_view01.png
   :alt: novelibre screenshot


Title, description, and author
------------------------------

Title and description are displayed in an editable "index card".

The editing of book title and author can be completed by pressing the ``Enter`` key.
Changes to the description are applied when the mouse is clicked
anywhere outside the text input field.

After exporting the book to an *ODT* document, title and description
appear in the document properties.

.. image:: _images/book_view08.png
   :alt: Screenshot

These properties are visible, for example, when the mouse pointer is over
the document in the Windows Explorer.

.. image:: _images/book_view09.png
   :alt: Screenshot
      


Document language
-----------------

Expand or collapse this frame by clicking on the label.

.. image:: _images/book_view02.png
   :alt: novelibre screenshot

- Language code acc. to ISO 639-1
- Country code acc. to ISO 3166-2

This information controls the spelling checker for export documents.

.. image:: _images/book_view10.png
   :alt: LibreOffice Writer screenshot

If not set, the System locale setting will be used as default.


.. hint::
   You can also set or change the document language with *Writer*, then it will be applied on import. 

	.. image:: _images/book_view11.png
	   :alt: LibreOffice Writer screenshot
	   

Auto numbering
--------------

Expand or collapse this frame by clicking on the label.

.. image:: _images/book_view03.png
   :alt: novelibre screenshot

Auto number chapters/parts when refreshing the tree
   If this checkbox is ticked, all chapters/parts are automatically numbered
   each time `the tree is refreshed <file_menu.html#refresh-tree>`__.
   The chapter titles are replaced with a ``prefix-number-suffix``
   pattern (without the dashes).

   .. hint::   
      You can optionally exclude individual chapters/parts from auto-numbering 
      in the `Chapter/part properties 
      <chapter_view.html#do-not-auto-number-this-chapter-part>`__.

Prefix and suffix entries can be completed by pressing the ``Enter`` key.

.. note::
   Make sure to add a space character to separate the prefix or
   suffix from the chapter or part number.

Use Roman chapter numbers
   By default, arabic numbers, like "1", "2", "3" ... are used for auto-numbering.
   If this checkbox is ticked, Roman numbers, like "I", "II", "III", "IV" ...
   are used instead.

Restart chapter numbering at part beginning
   By default, the chapters are numbered consistently across the parts.
   If this checkbox is ticked, the chapter numbering starts again with "1"
   in each part.


Renamings
---------

Expand or collapse this frame by clicking on the label.

.. image:: _images/book_view04.png
   :alt: novelibre screenshot

*novelibre* provides some ready-made fields for sections and characters
to store information that should be at hand when writing.
If the default categories do not fit into your individual story planning
concept, you can rename these fields.
Editing the categories can be completed by pressing the ``Enter`` key.

"Not a scene" fields
   The heading replacements for *Plot progress*, *Characterization*, and
   *World building* are used when you set the `Scene frame
   <section_view.html#scene>`__ to **Not a scene**.
   These categories then apply to all sections that don't represent scenes.

"Other Scene" fields
   The heading replacements for *Opening*, *Peak emotional monent*, and
   *Ending* are used when you set the `Scene frame
   <section_view.html#scene>`__ to **Other**.
   These categories then apply to all sections that represent scenes
   other than "Action" and "Reaction".

"Character" fields
   If you want other categories than `Bio <character_view.html#bio>`__
   and `Goals <character_view.html#goals>`__ for your characters, you
   can enter them here. They will then apply to all characters.

   .. note::
      If you rename the *Bio* frame, it will keep the Birth/death date
      entries anyway.      


Narrative time
--------------

Expand or collapse this frame by clicking on the label.

.. image:: _images/book_view05.png
   :alt: novelibre screenshot

To get an overview of the course of the narrative time, you can enter
date/time information `for each section <section_view.html#date-time>`__.
The date can be specific *(YYYY-MM-DD)* or unspecific (number of days,
e.g. from the beginning of the story).

Reference date
   The reference date is optional. It can be used to convert relative dates
   into absolute dates, or vice versa. The timeline software plugins may
   use the reference date for creating events from sections that have no
   date or an unspecific one.

   Format: *YYYY-MM-DD*, according to ISO 8601.

   .. hint::
      Even if you don't need specific dates for your story, specifying
      a reference date might be helpful. Thus, a day of the week
      can be displayed along with the `unspecific date 
      <section_view.html#start>`__, and ages can be calculated for 
      `related characters <section_view.html#relationships>`__.  

Convert dates to days
   This transforms specific section dates into days, related to the
   reference date.

Convert days to dates
   This transforms unspecific section dates into specific ones, using
   the reference date.

.. note::
   For large novels, the conversion may take some time, depending on 
   your system. During the conversion time, the clicked button will 
   display *"Please wait ..."*.  

.. hint::
   The commands above convert all dated sections at once. If you want to 
   do the conversion for single sections, just go to the 
   `Section properties view <section_view.html#start>`__.
   

Writing progress
----------------

Expand or collapse this frame by clicking on the label.

.. image:: _images/book_view06.png
   :alt: novelibre screenshot

With *novelibre*, you can set a word count target and track your
writing progress.

.. note::
   Regardless of the entries made here, you can see the word count 
   in the status bar at any time. 

Log writing progress
   By default, *novelibre* stores a log entry with the word counts
   for each day on which you edit the project. You can prevent
   this by unticking the **Log writing progress** checkbox.

   .. hint::
      For viewing the daily progress log, you may want to 
      install the `nv_progress plugin 
      <https://github.com/peter88213/nv_progress/>`__.

Words to write
   Here you can enter a number (without decimal points or separators)
   indicating your writing goal in words.
   The entry can be completed by pressing the ``Enter`` key.

Starting count
   Here you can enter a number (without decimal points or separators)
   indicating the word count you want to start from.
   The entry can be completed by pressing the ``Enter`` key.

Set actual wordcount as start
   Click this button to enter your current word count in the **Starting
   count** field.

Words written
   Here the difference between your actual word count and the starting
   count is displayed. The percentage refers to the words to write.

Work phase
   This setting is for the tree viewer `"Work phase" coloring mode
   <view_menu.html#coloring-mode>`__.

   - Sections with the same completion status as the selected work
     phase are black.
   - Sections that are ahead of the selected work phase are green.
   - Sections that are behind the selected work phase are magenta.


Links
-----

Expand or collapse this frame by clicking on the label.

.. image:: _images/world_view02.png
   :alt: Screenshot
   
This is a list for image and research document links.

Although *novelibre* holds some character/location/item data, it is
not the right application for extensive world building. For this,
you may want to use more powerful software, like `Zim Desktop Wiki
<https://zim-wiki.org/>`__. In this case, *novelibre* allows you to
create links to the text files that will take you quickly to the right
places in the wiki.

Or you have collected some images that could inspire you when writing.
Then simply create links to these images to open them with your
system's standard image viewer.

.. tip::
   If you have collected several images for a character in a folder 
   that your standard image viewer can browse through, a single link 
   to any image file is sufficient.  
   
The links are displayed in a list in the order they are entered.

Add Link
   When clicking on |Add|, a file selection dialog opens. The selected
   file will be added to the link list.

   .. hint::
      By default, the dialog shows image files. For other file types, 
      change the selector in the lower right corner. 
      
      .. image:: _images/filePicker01.png
         :alt: Screenshot
         

Remove Link
   When clicking on |Remove| or pressing the ``Del`` key,
   the selected link is removed from the list.

Open Link
   When double-clicking on a link, or clicking on |Goto|,
   the link is opened with the standard application for the link's file type.

   .. hint::
      If you want to open certain linked files with another application than the 
      standard application, you can provide a *novelibre* "launcher" setting. 
      For this, just create a text file named **launchers.ini** in the 
      ``.novx/config``  directory (where all configuration files are stored).
      Here you can assign applications to the file extensions.
      
      Zim desktop wiki pages are a special case. 
      For this, the Zim program is assigned to the `.zim` extension. 
      
      This example shows a setting that makes *novelibre* open text files
      with the *Zim Desktop Wiki* application instead of the standard text 
      editor: 
      
      ::
     
         [SETTINGS]
         .zim = C:/Program Files (x86)/Zim Desktop Wiki/zim.exe 
         
      .. image:: _images/launchers.png
         :alt: Screenshot
         

.. |Add| image:: _images/add.png
.. |Goto| image:: _images/goto.png
.. |Remove| image:: _images/remove.png


Cover thumbnail
---------------

A cover thumbnail is displayed with the book properties if you
provide a PNG image file with the project name along with the *.novx*
file. The recommended image width is 100 to 200 pixels.

.. image:: _images/book_view12.png
   :alt: Windows Explorer Screenshot
   
   
.. image:: _images/book_view07.jpg
   :alt: novelibre screenshot


