#imports
from os.path import abspath,join,dirname,normpath,basename
from os import makedirs,rename,rmdir
import requests,zipfile,io
import shutil
#Setup data
data_folder=join(dirname(abspath('')),'data')
makedirs(data_folder,exist_ok=True)
#Download zipped data
years = ['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
base_link = "https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-YEAR.zip"
for year in years:
    link = base_link.replace('YEAR',year)
    download = requests.get(link)
    z = zipfile.ZipFile(io.BytesIO(download.content))
    all_members = z.filelist
    for member in all_members:
        name = member.filename
        if '.csv' in name and 'MACOS' not in name:
            print(f"Extracting {name}")
            entire_path = z.extract(member,path=data_folder)
            print("done")
            path = basename(normpath(entire_path))
            if year not in path:
                rename(entire_path,entire_path.replace('.csv',f'{year}.csv'))
    b=2
#Fixing one which is a folder for no reason
folder_path = join(data_folder,'2016 Stack Overflow Survey Results')
fix_path = join(data_folder,'2016 Stack Overflow Survey Responses.csv')
broken_path = join(folder_path,'2016 Stack Overflow Survey Responses.csv')
shutil.move(broken_path,fix_path)
rmdir(folder_path)