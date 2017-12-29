import glob, os

def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, 
                  os.path.join(dir, titlePattern % title + ext))

# change file path and regex parameters here. use https://regex101.com/ for reference
rename(r'c:\yourdirectoryhere\anotherfolder', r'*.doc', r'newfilenaming(%s)')