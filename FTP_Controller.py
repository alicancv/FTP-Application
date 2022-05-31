import ftplib
import os

class FTP_Controller:
    def __init__(self):
        self.ftp = ftplib.FTP()
        self.ftp.encoding = "UTF-8"
        
    def login(self, host, port, user, password):
        self.ftp.connect(host, port)
        self.ftp.login(user, password)

    def disconnect(self):
        self.ftp.quit()
        
    def upload_file(self, local_path, remote_path):
        self.ftp.cwd(remote_path)
        
        with open(local_path, "rb") as file:
            self.ftp.storbinary(f"STOR {os.path.split(local_path)[1]}", file)
            
    def download_file(self, local_path, remote_path):
        remote_local_path, target_file_name = os.path.split(remote_path)
        self.ftp.cwd(remote_local_path)

        with open(local_path+os.path.split(remote_path)[1], "wb") as file:
            self.ftp.retrbinary(f"RETR {target_file_name}", file.write)
    
    def make_dir(self, dir_name, remote_path):
        self.ftp.cwd(remote_path)
        self.ftp.mkd(dir_name)
        
    def remove_file_or_dir(self, remote_path):
        remote_local_path, target = os.path.split(remote_path)
        self.ftp.cwd(remote_local_path)
        
        try:
            self.ftp.rmd(target)
        except:
            self.ftp.delete(target)
        
    def rename_file_or_dir(self, new_name, remote_path):
        remote_local_path, old_name = os.path.split(remote_path)
        self.ftp.cwd(remote_local_path)
        self.ftp.rename(old_name, new_name)
        
    def show_dir(self, remote_path = ""):
        self.ftp.cwd(remote_path)
        file_names = self.ftp.nlst()
        file_names.insert(0, '..')
        
        return file_names 
    
    def change_dir(self, remote_path):
        self.ftp.cwd(remote_path)

    def current_wdir(self):
        return self.ftp.pwd()