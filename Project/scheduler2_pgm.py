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

#Folder to paste the data
os.chdir(r"E:\Tesorait")
os.mkdir(day_month_year)
