def unzip(file,path):
    from zipfile import ZipFile
    zf = ZipFile(file, 'r')
    zf.extractall(path)
    zf.close() 