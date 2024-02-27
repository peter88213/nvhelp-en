Getting started
===============

Setting up novelibre
--------------------

If *novelibre* were a commercial application, all the
steps described below would be performed automatically
by a setup program. On Windows, for instance, this would
then be an *.exe* or *.msi* file that must be executed
with special authorizations and may even require a costly
certificate in order to be approved for download and
installation.

There is also the problem that a separate setup program would
have to be created and maintained for each operating system.
For Linux, it would be necessary to provide installation
packages or images, whereby there are a multitude of different
standards.

Because I don't run a software business, but am just a
hobbyist and rather want to write novels, I've decided to
go a different route: I provide a Python setup script
that works the same
way on all operating systems. The very last setup steps,
which vary depending on the operating system and may also
require special authorizations, must be carried out by the
intrepid users themselves. I do what I can to make these
steps easier, and provide detailed instructions for Windows
below. Enjoy!

Installing the application
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Unzip the downloaded zipfile.
2. Move into the unzipped folder and launch **setup.pyw**.
   This installs the application for the local user.

.. figure:: _images/gettingStarted04.png
   :alt: novelibre screenshot

Making novelibre accessible on the Desktop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   In the following chapters, the Windows procedure is described. 
   
   As a **Linux user**, you are expected to know how to set up 
   a program launcher on your specific desktop. 
   Roughly speaking, it is a matter of calling *python3* 
   with *novelibre.py* and the specified *.novx* file as 
   parameters. You may have to copy the program icon to the 
   image directory
   where the program launcher gets the icons from. 
   In doubt, refer to your desktop documentation. 
   It's a good idea to register the *novx* extension
   in the mimetypes as **text/xml**, so it can be opened
   by your web browser for display, using the 
   `novx.css style sheet <file_menu.html#copy-style-sheet>`__. 

3. Open the installation folder.

   .. figure:: _images/gettingStarted05.png
      :alt: novelibre screenshot

4. Drag and drop **run.pyw** to the desktop while holding
   down the ``Alt`` key. This creates a shortcut to launch
   *novelibre* from the Windows desktop. Now you can also
   drag and drop *.novx* project files to this shortcut.

   .. figure:: _images/gettingStarted06.png
      :alt: novelibre screenshot

5. Optionally, you can replace the "Python" icon with the
   *novelibre* logo you may find in the installation's
   *icons* subdirectory.

   To do this, right-click on the desktop shortcut and
   open the **Properties** dialog. Select the **Shortcut**
   Tab and click on the **Change icon** button (1). In the
   icon selection dialog, click on the **Browse...** button
   (2). This opens a file selection dialog. Move to
   ``<home>\.novx\icons`` and double-click on the "N" logo
   (3).

   .. figure:: _images/gettingStarted07.png
      :alt: novelibre screenshot

6. To rename the shortcut to *novelibre*, right-click on
   the desktop shortcut and open the **Properties**
   dialog. In the first tab, replace "Shortcut to run.pyw"
   with "novelibre".

   .. figure:: _images/gettingStarted08.png
      :alt: novelibre screenshot


Associating .novx files with novelibre
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

7. Optionally, you can associate the **.novx** file extension
   with the *novelibre* application. Then the project files
   are displayed with the *novelibre* icon in the Explorer,
   and you can open them with *novelibre* by double-click.
   Further, you can display *.novx* files with a web browser,
   using the `novx.css style sheet <file_menu.html#copy-style-sheet>`__.

   Double-click on the **add_novelibre.reg** script. Windows will
   display a warning and ask you for confirmation. If in doubt,
   you can inspect the *add_novelibre.reg* file with a text editor
   or ask an expert you trust.

   .. figure:: _images/gettingStarted09.png
      :alt: novelibre screenshot

   .. hint::
      You can undo this by executing the **remove_novelibre.reg**
      script. This removes all the *novelibre*-specific entries 
      from the Windows registry while keeping the application. 
      
      To uninstall the application and all its tools, plugins, 
      and configuration data, just delete the ``<home>\.novx``
      folder after executing the **remove_novelibre.reg** script.

.. important::
   Executing the program under Windows by double-clicking on the 
   *.novx* file  works under the hood by calling the currently 
   installed version of the Python interpreter. 
   
   If you update Python at a later date, you must then re-run 
   the **setup.pyw** script afterwards, and execute 
   **add_novelibre.reg** again. 
   Otherwise, Windows will not be able to find the new Python 
   version and will fail when trying to open *.novx* files on
   double-clicking. 
   
   Please keep that in mind, even if it's pretty unlikely that 
   *novelibre* will need a Python update in the near future.
   

Updating the application or a plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just execute the Steps 1 and 2 as described above. If there
is any further action required, the setup script will give you
a message.


Setting up LibreOffice
----------------------

I assume that *novelibre* users are already familiar with LibreOffice or
OpenOffice. Therefore, I will only give a few brief tips that relate
specifically to the interaction with *novelibre*.

Make the sections visible in the manuscript
   An essential part of the workflow is writing with LibreOffice
   *Writer* (everything also applies to OpenOffice). *novelibre*
   creates editable manuscript files that are meant to be temporary.
   These documents contain structural information that enables
   *novelibre* to recognize and correctly sort the sections when
   reading them back.

   For the whole thing to work, it is extremely important that you
   only write within the section boundaries. To do this, you might
   want to make the text boundaries visible in the LibreOffice settings.

   .. figure:: _images/gettingStarted01.png
      :alt: LibreOffice Writer screenshot

      LibreOffice Writer screenshot: Make sure the **View > Text Boundaries**
      menu entry is ticked. Writing outsides the visible text boundaries
      has no effect on your *novelibre* project.

Dock the Navigator
   To quickly find the chapters and sections of your novel, it is best to
   keep the LibreOffice Navigator in sight. I prefer to dock it to the left
   of the work area. To do this, first press ``F5`` to open the Navigator.
   By default, it appears as a pop-up window that can be placed anywhere
   on the screen. To dock it, double-click in a free gray space while holding
   down the ``Ctrl`` key, as shown in the following image.

   .. figure:: _images/gettingStarted02.png
      :alt: LibreOffice Writer screenshot

      LibreOffice Writer screenshot: The red X indicates the position for
      double-clicking.

   .. tip::
      The Navigator displays a confusing wealth of information. 
      It is best to reduce this to the headings first. To do this, select 
      "Headings" at the top of the tree and then click on the "Content Navigation View" 
      icon. This works if a document containing headings is loaded. 
   
      .. figure:: _images/gettingStarted03.png
         :alt: LibreOffice Writer screenshot
      
         LibreOffice Writer screenshot: The red O indicates the icon to click on.


Customize the look of your manuscript
   The manuscript created by *novelibre* has a layout that is similar to the
   "standard manuscript format" which is widely used to provide an overview
   of the total number of pages of a work to be printed.

   However, the set font is only available for Windows, and it is not particularly
   attractive. (I, for my part, have installed  the free `Courier Prime font
   <https://quoteunquoteapps.com/courierprime/>`__ on Windows and Linux, which
   gives me a pleasant typewriter feel) In addition, hyphenation is turned off,
   and the page size is set to A4, which is not the worldwide standard.

   That's not for you? No problem. This is what the **document templates** in
   LibreOffice are for. So if you don't like the look of the generated manuscript,
   simply apply a template that suits your needs and tastes. Perhaps you have
   to design your favorite template first, but your knowledge of this technique
   will pay off when it comes to designing print pages for self-publishing.

   In order to minimize circumstances, I recommend my `Style switcher extension
   <https://peter88213.github.io/StyleSwitcher/>`__, that allows you to customize
   your manuscript with a single mouse click.

   .. note::
      Loading a template or changing the default font and page size has no 
      impact on re-importing the document with *novelibre*.