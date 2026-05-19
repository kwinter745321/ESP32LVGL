# README - Video 90

20 May 2026

# Scope

# Files

 - Firmware 
   - copy of firmware information from video 88

 - Flash

   - etc 
     - system.conf
     - default.board

   - home
     - lib - with our typical drivers
     - various MicroPython programs

# Caution

During an OTA upgrade the upyOS files overwrite what ever resides in their directories.
Meaning the default.board may be reverted to their original file.  Make a backup of the file
and replace.  Then run "loadboard etc/default.board"