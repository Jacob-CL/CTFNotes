# Proxmark 3
## Install
- https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/md/Installation_Instructions/Linux-Installation-Instructions.md
- The mismatch error is safe to ignore, as part of the process you have to uncomment a line for the device (Proxmark3 easy) and so when you modify Makefile.platform.sample (or any tracked file), git considers the working directory "dirty" which triggers the "-suspect" suffix in version strings.
