nv_editor
================

**Online help**

This page refers to the latest `nv_editor
<https://peter88213.github.io/nv_editor/>`__ release.
You can open it with **Help > Editor plugin Online help**.


Launch the section editor
-------------------------

-  Open a section editor window by double-clicking on a section or via
   the **Section > Edit** menu entry when a section is selected, or by
   hitting the *Enter* key.
-  If the project is locked, editor windows cannot be opened.
-  If you choose a section already open, the window will be brought to
   the foreground.

Select text
-----------

-  Select a word via double-clicking.
-  Select a paragraph via triple-clicking.
-  Extend the selection via **Shift-Arrow**.
-  Extend the selection to the next word via **Ctrl-Shift-Arrow**.
-  **Ctrl-A** selects the whole text.

Copy/Paste text
---------------

-  **Ctrl-C** copies the selected text to the clipboard.
-  **Ctrl-X** cuts the selected text and moves it to the clipboard.
-  **Ctrl-V** pastes the clipboard text content to the cursor position.

Format text
-----------

.. role:: html(code)
   :language: html

It is assumed that very few types of text markup are needed for a novel
text:

-  *Emphasized* (usually shown as italics).
-  *Strongly emphasized* (usually shown as capitalized).
-  *Citation* (paragraph visually distinguished from body text).

-  **Ctrl-I** places "emphasized" markup around the selected text or at the
   cursor, like so:

   :html:`<em>Example</em>`

   If the selection is already emphasized, the command removes the markup.
-  **Ctrl-B** places "strong" markup around the selected text or at the
   cursor, like so:

   :html:`<strong>Example</strong>`

   If the selection is already strong, the command removes the markup.

-  **Ctrl-M** removes “emphasized” and “strong” markup from the selection.


Undo/Redo
---------

-  **Ctrl-Z** undoes the last editing. Multiple undo is possible.
-  **Ctrl-Y** redoes the last undo. Multiple redo is possible.

Split a section
---------------

Via **File > Split at cursor position** or **Ctrl-Alt-S** you can split
the section at the cursor position.

-  All the text from the cursor position is cut and pasted into a newly
   created section.
-  The new section is placed after the currently edited section.
-  The new section is appended to the currently edited section.
-  The new section has the same status as the currently edited section.
-  The new section is of the same type as the currently edited section.
-  The new section has the same viewpoint character as the currently
   edited section.
-  The editor loads the newly created section.

Create a section
----------------

Via **File > Create section** or **Ctrl-Alt-N** you can create a
section.

-  The new section is placed after the currently edited section.
-  The new section is of the same type as the currently edited section.
-  The editor loads the newly created section.

Word count
----------

-  The section word count is displayed at the status bar at the bottom
   of the window.
-  By default, word count is updated manually, either by pressing the
   **F5** key, or via the **Word count > Update** menu entry.
-  The word count can be updated “live”, i.e. just while entering text.
   This is enabled via the **Word count > Enable live update** menu
   entry.
-  Live update is disabled by the **Word count > Disable live update**
   menu entry.

.. note::
   *Live updating the word count is resource intensive and may slow down
   the program when editing big sections. This is why it’s disabled by
   default.*

Apply changes
-------------

-  You can apply changes to the section with **Ctrl-S**. Then “Modified”
   status is displayed in *noveltree*.
-  If the project is locked in *noveltree*, you will be asked to unlock
   it before changes can be applied.

Exit
----

-  You can exit by clicking on **Exit**, by closing the window, or with **Ctrl-Q**.
-  When exiting the program, you will be asked for applying changes.
