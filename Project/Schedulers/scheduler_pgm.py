"""This code will copy the dicom files from main folder (which has the dicom image inside )
and check it with the source folder (which has only the jpeg images)
and paste it to given folder path (which is tesorait)
and also it will send mail if the similar dicom file was missed """
# Importing shutil for copy
# import os for giving access my system path
# Import time and schedule for making time and run automatically in given time
# import smtplib and others for sending mail

import shutil
import os
import re
import schedule
import time
from datetime import datetime,timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#paths for source and main folders
base_source_path = r"E:\Autobackup\classwise"
base_main_path = r"E:\Autobackup\classwise"

#previous day's date
previous_date = datetime.now() - timedelta(days=1)
day_month_year = f"{previous_date.day:02d}-{previous_date.month:02d}-{previous_date.year:04d}"
day_month = f"{previous_date.day:02d}{previous_date.month:02d}"

#Folder paths based on the previous day's date
source_folders = [os.path.join(base_source_path, f"chs0{i}meg", "cxr", day_month_year, "output", "abnormal") for i in range(1, 6)]
main_folders = [os.path.join(base_main_path, f"chs0{i}meg", "cxr", day_month_year, "input") for i in range(1, 6)]

tesorit_folder = r"E:\Tesorait"
paste_folder = os.path.join(tesorit_folder,day_month_year)
os.makedirs(paste_folder, exist_ok=True)


print("Program Started")

def Automatic():
    '''
    Automatically paste dicom images from two folders
    '''
    for source_folder, main_folder in zip(source_folders, main_folders):
        print("Program Started inside the Automatic")
        folder = os.listdir(source_folder)
        next_folder = os.listdir(main_folder)

        a = []
        for file in folder:
            base_name_1 = re.sub(r'\.(jpg|jpeg|dcm)$', '', file, flags=re.IGNORECASE)  #this will replace the extension with empty space


            a.append(base_name_1)
        print("a", a)

        b = []
        for nxt in next_folder:
            base_name_2 = re.sub(r'\.(jpg|jpeg|dcm)$', '', nxt, flags=re.IGNORECASE)  #this will replace the extension with empty space
            b.append(base_name_2)
        print("b", b)

        check_a = []
        for y in a:
            check_a.append(y[:15])  #print only the 15 letters from all the images like WJH_01_1002_001 this only.
            #print("A:",check_a)

        check_b = []
        for z in b:
            check_b.append(z[:15])  #print only the 15 letters from all the images like WJH_01_1002_001 this only.
            #print("B:",check_b)

        common_file_name = set(check_a) & set(check_b)             #this will get the common names of the images
        uncommon_file_name = set(check_a) - set(check_b)           #this will get the uncommon names of the images
        common_names = list(common_file_name)
        uncommon_name = list(uncommon_file_name)
        print('common:', common_names)
        print('uncommon:', uncommon_name)

        for file in next_folder:
            if file.endswith(".dcm") or file.endswith(".DCM"):     #this will check dicom file alone
                filename_without_extension = re.sub(r'\.(dcm|DCM|Dcm)$', "", file, flags=re.IGNORECASE) #this will remove the extension
                filename_without_extension = re.sub(r'\.(dcm|DCM|Dcm)$', "", filename_without_extension,flags=re.IGNORECASE)  #this will double check the extenion and remove
                filename_without_extension= filename_without_extension[:15] #this will get the 15 letters only like WJH_01_2005_001
                #print("filename_without_extension:",filename_without_extension)
                if filename_without_extension in common_names:
                    source_path = os.path.join(main_folder, file)
                    #print("source_path", source_path)
                    destination_path = os.path.join(paste_folder, file)
                    #print("destination_path", destination_path,)
                    try:
                        shutil.copy(source_path, destination_path)
                        print("File copied successfully.")
                    except Exception as e:
                        print("Error copying file:", e)

        print("Files copied successfully.")
'''
        # The below line will send mail for me if any dicom is not present
        sender_email = "mthejas664@gmail.com"
        app_password = "osdo jovg odtq umsq"
        receiver_email = "intern.chsind@gmail.com"
    
        if d:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, app_password)
    
            subject = "Regd: Images Not Found"
            body = f"Dear Team,\n\nI hope this mail finds you well.\nThe following images are not found:\n"
            body += "\n".join(d)
            body += "\n\nThank you."
            body += "\n\nRegards,"
            body += "\nRathnavel"
            body += "\nIntern"
            body += "\nCorporeal Health Solution"
    
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
    
            message.attach(MIMEText(body, "plain"))
    
            server.sendmail(sender_email, receiver_email, message.as_string())
    
            server.quit()
    
            print("Email sent successfully.")
        else:
            print("No uncommon names to send.")


j = schedule.every().day.at("17:37").do(Automatic)

counter = 0

while True:
    schedule.run_pending()
    time.sleep(1)
    counter += 1
    print("Awaiting for the response")
    if counter == 50:
        print("inside Scheduler")
        schedule.cancel_job(j)
        break

'''

Automatic()
print("Finished scheduler operations")
