# Compress a single file
def zip(zip_name,file_name):
    import zipfile         
    zf = zipfile.ZipFile(zip_name, 'w')
    zf.write(file_name, compress_type=zipfile.ZIP_DEFLATED)
    zf.close()
    

# Compress multiple files from a folder
def zip_all(zip_name,folder):
	import os
	import zipfile
 
	zf = zipfile.ZipFile(zip_name, 'w')
 
	for folder, subfolders, files in os.walk(folder):
 	   for file in files:
 	       if file.endswith('.pdf'):
	            zf.write(os.path.join(folder, file),os.path.relpath(os.path.join(folder,file), folder),compress_type = zipfile.ZIP_DEFLATED)
	zf.close()


# Extract a single file from a zip file
def unzip(zip_file,file_name,folder):
	import zipfile         
	zf = zipfile.ZipFile(zip_file)
	zf.extract(file_name, folder)
	zf.close()


# Extract all files:
def unzip_all(zip_file,path):
    from zipfile import ZipFile
    zf = ZipFile(file, 'r')
    zf.extractall(path)
    zf.close() 
    #print('Unzipped all files from %s to %s' %(str(zip_file),str(path)))
    
# Read files from a zip file
def read_zip(zip_file,folder):
'''extract only those files that have a size below 1MB'''
	import zipfile
	stories_zip = zipfile.ZipFile(zip_file)
	for file in stories_zip.namelist():
	    if stories_zip.getinfo(file).file_size < 1024*1024:
	        stories_zip.extract(file, folder)         
	stories_zip.close()



