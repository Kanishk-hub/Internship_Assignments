1. Navigate the File System:

pwd       # Print working directory
ls        # List directory contents
cd ..     # Move up one directory
cd /path  # Change to a specific directory

File Manipulation:

New-Item -Path . -Name "file.txt" -ItemType "File"    # Create a file 


mkdir mydir                # Create a directory

cp file.txt mydir/         # Copy file to directory

mv file.txt newfile.txt    # Rename/move file

rm newfile.txt             # Delete file

rmdir mydir                # Delete directory
