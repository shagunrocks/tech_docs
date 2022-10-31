import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

folder = "1nz9YDxY3nh-Xw2TfqbOkoEbxP2brxj3-"

directory = "D:/hello/hi"
for f in os.listdir(directory):
    filepath = os.path.join(directory, f)
    gfile = drive.CreateFile({'parents': [{"id": folder}], 'title': f})
    gfile.SetContentFile(filepath)
    gfile.Upload()
