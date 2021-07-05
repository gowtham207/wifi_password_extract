#!/usr/bin/python2
import subprocess
import re


command = subprocess.run(["netsh","wlan","show","profile"],capture_output=True).stdout.decode()
profile = (re.findall("All User Profile     : (.*)\r", command))

if len(profile) != 0:
    for name in profile:
        wifi_dict = dict()
        command2=subprocess.run(["netsh","wlan","show","profile",name],capture_output=True).stdout.decode()
        if re.search("Security key           : Absent",command2):
            continue
        else:
            wifi_dict["ssid"]=name
            command3=subprocess.run(["netsh","wlan","show","profile",name,"key=clear"],capture_output=True).stdout.decode()
            password=re.search("Key Content            :(.*)\r",command3)
            if password == None:
                wifi_dict["password1"]=none
            else:
                wifi_dict["password1"]=password[1]
                print(wifi_dict)

            print("username: ",wifi_dict["ssid"])
            print("password: ",wifi_dict["password1"])




