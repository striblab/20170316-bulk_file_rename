# Bulk file rename

by [Frey Hargarten](https://github.com/jeffhargarten)

Renames all files fitting a specified parameter to the desired pattern using regex. Requires [Python3](https://www.python.org/download/releases/3.0/).

### Usage:


1. Edit this line in the script to fit your needs. 


rename(r'c:\yourdirectoryhere\anotherfolder', r'*.doc', r'newfilenaming(%s)')


The example renames all .doc files in a given folder to new(x).doc. Use https://regex101.com/ for further reference


2. run script


```bash
$ python3 bulk_file_rename.py <filename>
```
