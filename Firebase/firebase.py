import pyrebase # firebase module named pyrebase !
class firebase:
    def __init__(self):
        self.status = "loading" # this is an optional variable to give an output info to your main script.Dont use it if you just learning the basics firebase.
        self.admin_info = "" # this is optional too ! If you want to send a message to users of this script you should have this kind a variable 

        self.config = {
                      """ PASTE THE COPPIED CONFIG VARIABLE INDEX TO THIS AREA """
                    }
        self.firebase = pyrebase.initialize_app(self.config) #Initiate firebase by this code
        self.storage = self.firebase.storage() # And create a storage 
        
    def upload(self,file_path,receiver):
        self.storage.child(file_path).put(receiver)
    def download(self,file_path,download_path):
        self.storage.child(file_path).download(download_path)
    def version_control(self):
        try:
            with open(version.txt,"r") as old_vers: #open current version.txt file
                old_vers = int(old_vers.readlines()[0].split("=")[-1]) # get version no from first line as integer
        except Exception as e:
            print(e)
        self.download("Info/version.txt").download(version.txt) #you can rewrite the path names for your own

        with open(version.txt, "r") as vers:  # now open new file
            version = int(vers.readlines()[0].split("=")[-1]) #get new version no
            vers.seek(0) # You have to use this to avoid errors that readlines function gives.(idk why :D )
            recipe = vers.readlines()[3].split(",") #this is our recipe for update files.
            vers.seek(0)
            self.admin_info = str(vers.readlines()[4]) # get admin_info
            vers.seek(0)
            if str(vers.readlines()[2]) == "terminate\n" or "terminate": # If you dont want users to reach your main app you can put a keyword like this to version file and use it on your main script.
                self.status = "terminate"
        if version - old_vers >= 1: # This section is up to you. Compare version numbers and do whether you want. But the we will use update function to download our new files.
            print("Auto update activated !")
            self.update(recipe)
            print("update completed.")
            self.status = "update"
        else :
            self.status = "okay"

    def update (self,recipe):
        for elm in recipe:
            if elm[-1] == "\n" : elm = elm[:-1] #Our output from readlines() function -file names- has \n on the end and we need to remove it.
            fname = elm.split("/")[-1] # split with "/" char and get last item that contains filename.
            print(elm)
            self.download("Update" + "/" + fname,pf.main+"/"+elm) #We need to create folder named "Update" on firebase storage and upload our new version file to this folder. and dont forget to upload version.txt to Info folder on storage.
        return "Completed"
