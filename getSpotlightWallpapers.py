"""This little script is an attempt to automate the following simple task:
1.Goes to the assets folder
2.Looks for files modified within last 30 days and of size more than 100 KiloBytes
3.copies these files to your pictures folder
4.renames all files with their time of modification and adds a '.jpg' extension to them."""

import os,shutil,datetime

#now change directory to the location of spotlight image assets.
os.chdir("C:/Users/akashsharma/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets")

#sorting the files with respect to their modification date from latest to oldest though it is not necessary to sort
#you can just write filelist=os.listdir() instead of sorting
filelist=sorted(os.listdir(),key=os.path.getmtime,reverse=True)

#now get the date of day 30 days ago from today
threshold_time=datetime.date.today()-datetime.timedelta(days=30)

for name in filelist:
    file_time=datetime.date.fromtimestamp(os.path.getmtime(name))
    if file_time>threshold_time and os.path.getsize(name)>100000:
        origin="C:/Users/akashsharma/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/{}".format(name)
        target="C:/Users/akashsharma/Pictures/{}.jpg".format(str(os.path.getmtime(name)).replace('.','a'))
        shutil.copy(origin,target)
