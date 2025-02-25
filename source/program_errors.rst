Program errors
==============

*novelibre* has proven to be very stable in daily use.
There are no mysterious crashes and no third-party program packages are used,
as they occasionally cause problems with other application programs.

Nevertheless, there is no guarantee that it is free of bugs.
*novelibre* has an open program architecture to enable extensive functional
extensions through plugins.
Unfortunately, this also means that a bug in one plugin can affect the entire program.


What to do in case of error?
----------------------------

1. Save your data

   If a program error occurs that does not lead to a hard termination,
   a warning window reporting an unexpected error should open.
   In this case, you can try to save changes.

2. Update the application and all plugins

   Please make sure you have the latest version of
   *novelibre* and all its plugins.
   If you have an outdated version of the program, the error you are experiencing
   might already have been fixed.

3. Report the bug

   If the error persists, you might experience a bug that is yet unknown.

   In the installation directory of *novelibre* there should be a text file named
   `error.log`, which lists the lines of code that led to the error.
   The content of this file can help the developer to fix the problem.

   So if you want to contribute to the improvement of *novelibre*, you can go to the
   home page of *novelibre* or a plugin which may look suspicious,
   and submit a bug report in the *Issues* section.
   However, you need a user account to do this, which is free of charge.

   .. hint::
      Take a look at the issues to see whether your error has already been reported. 
      If this is the case, you can add a comment to this issue. 
      
      If you know your way around a little, you can also take a look at the closed 
      issues and reopen one if necessary. 
      
      If you are reporting a new bug, please fill out the *Bug report* form.
      Please indicate which plugins you have installed. 
   
4. Uninstall plugins

   If *novelibre* can be started, open the
   `plugin manager <tools_menu.html#plugin-manager>`__,
   delete all plugins one after the other, and restart *novelibre*.
   If the error can no longer be reproduced, you can
   continue working without plugins for the time being.

5. Return to an old version

   If this doesn't help, but you have been working with *novelibre* for a long time
   without any problems, the problem may have been introduced with a faulty update.
   If you still have the previous program version in your *Download* folder,
   reinstall it (and the old plugins if any).




















