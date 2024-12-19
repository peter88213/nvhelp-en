Abandoning novelibre
====================

You have put a lot of time and effort into a novel project with *novelibre*,
but have come to the conclusion that *novelibre* is not right for you after all?
Don't worry, the effort was not in vain.
You can export just about anything in the form of *Writer* text documents
and *Calc* spreadsheets.


How to continue using your projects without novelibre
-----------------------------------------------------

So if you prefer to continue working in the classic way with OpenOffice or LibreOffice,
simply create a
`final manuscript document <export_menu.html#final-manuscript-document-export-only>`__
and a `section list <section_menu.html#section-list-export-only>`__
or a `plot grid <plot_menu.html#export-plot-grid-for-editing>`__.
In addition, descriptions of your characters, locations etc.,
as text documents, tables, or `desktop wiki
<https://github.com/peter88213/nv_zim/>`__  as required.
You can then continue all of this manually.

- Useful when switching to `yWriter <https://spacejock.com/yWriter7.html>`__
  is the `nv_yw7 plugin <https://github.com/peter88213/nv_yw7/>`__.
- When switching to `novelWriter <https://novelwriter.io/>`__, you can first
  convert your project to a yWriter project (see above), and then turn it
  into a *novelWriter* project using the
  `yw2nw converter tool <https://peter88213.github.io/yw2nw/>`__.

In case *novelibre* is no longer available for any reason,
you can view *.novx* files in a web browser using the
`css style sheet <file_menu.html#copy-style-sheet>`__,
and copy everything you want via the clipboard.

For experts, there is also the option of creating completely different file formats
from the *.novx* files using *XSLT* transformation.
Examples for this can be found in the
`novelibre repository <https://github.com/peter88213/novelibre/tree/main/xslt>`__.


How to uninstall novelibre
--------------------------

1. Open the installation folder (the subdirectory ``.novx`` in your user directory).

   .. tipp::
      This is particularly easy to do from *novelibre* with
      **Tools > Open installation folder**.
 
2. If you have set *novelibre* under Windows as the default application for *.novx* files,
   undo this by executing  ``remove_novelibre.reg`` (double-click and confirm).

3. Go up one level to your user directory and delete the installation folder.
   This will remove *novelibre* along with the plugins and utilities from your computer.

4. Remove the *novelibre* shortcut from the desktop.


.. note:: 
   As developer, I am naturally interested in your experiences with *novelibre*.
   Feel free to leave a note in the 
   `discussions forum <https://github.com/peter88213/novelibre/discussions>`__





