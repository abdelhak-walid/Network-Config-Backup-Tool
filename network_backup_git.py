import netmiko 
import datetime
import os
from netmiko import ConnectHandler

class SaveConfig:
	def __init__(self,device):
		self.device=device 
		self.device_add=device["ip"]
		self.current_time=datetime.datetime.now().strftime("%A %B %d -%Y _ %H h-%M mn-%S sec")
		self.current_day=datetime.datetime.now().strftime("%A-%B %d")

		self.Gather={}
		self.show_run=''
		self.show_startup=''

		print(f"{self.current_time:~^100}\n")
		self.connectToDevice()
		self.Gathering_info()

	def connectToDevice(self):
		print(f"Connecting to {self.device_add} ... \n")
		self.connect=ConnectHandler(**self.device)

	def Gathering_info(self):
		print("Gathering Data >.>.>.>.>.>.")
		self.Gather["show_running_config"]=self.connect.send_command("show run")
		self.Gather["show_startup-config"]=self.connect.send_command("show startup-config")

	def DATA_to_file(self):
		folder_path="C:\\Users\\hp\\Desktop\\Config_from_Topo1"
		folder_device_path=f"{folder_path}\\device{self.device['ip']}"
		folder_device_path_day=f"{folder_device_path}\\{self.current_day}"
		folder_device_path_day_running=f"{folder_device_path_day}\\Running_config"
		folder_device_path_day_startup=f"{folder_device_path_day}\\Startup_config"
		os.makedirs(folder_path,exist_ok=True)
		os.makedirs(folder_device_path,exist_ok=True)
		os.makedirs(folder_device_path_day,exist_ok=True)
		os.makedirs(folder_device_path_day_running,exist_ok=True)
		os.makedirs(folder_device_path_day_startup,exist_ok=True)
		file_path1=f"{folder_device_path_day_running}\\Running_config{self.current_time}.txt"
		file_path2=f"{folder_device_path_day_startup}\\Startup_config{self.current_time}.txt"

		with open(file_path1,"a",encoding="utf-8") as file :
			file.write(self.current_time+"\n\n")
			file.write(self.Gather["show_running_config"]+"\n\n")
			
			print(f"Connection succeeded !! : config saved to {file_path1}")
		with open(file_path2,"a",encoding="utf-8") as file :
			file.write(self.current_time+"\n\n")
			file.write(self.Gather["show_startup-config"]+"\n\n")
			print(f"Connection succeeded !! : config saved to {file_path2}")
		if self.connect:
			self.connect.disconnect()
			print("Disconnected from device.\n" + "-"*100)


R1={
	'device_type':'cisco_ios',
	'ip':'device-add',
	'username':'username',
	'password':'pass'
}


R2={
	'device_type':'cisco_ios',
	'ip':'device-add',
	'username':'username',
	'password':'pass'
}
R5={
	'device_type':'cisco_ios',
	'ip':'device-add',
	'username':'username',
	'password':'pass'
}
devices=[R1,R2,R5]
 

for device in devices : 
	try:
		Backup=SaveConfig(device)
		Backup.DATA_to_file()
		Backup.disconnect()
	except Exception as e : 
		print(e)
		continue



