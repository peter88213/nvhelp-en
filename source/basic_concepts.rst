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
   under **Document language**.

Text passages in sections
   Paragraph-wise or inline text markup for other languages is supported by
   *novelibre*.

