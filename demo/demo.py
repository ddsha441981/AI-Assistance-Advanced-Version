# import speech_recognition as s_r
# print(s_r.Microphone.list_microphone_names()) #print all the microphones connected to your machine
# mic = s_r.Microphone(device_index=1)
# print(mic)

# import speech_recognition as s_r
# print(s_r.__version__) # just to print the version not required
# r = s_r.Recognizer()
# my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
# with my_mic as source:
#     print("Say now!!!!")
#     r.adjust_for_ambient_noise(source) #reduce noise
#     audio = r.listen(source) #take voice input from the microphone
# print(r.recognize_google(audio)) #to print voice into text

# text = "python is an easy language to learn."
# v = text.split("python is")[1]
# v = text.split("an easy")[1]
# print(v)

# import os
#
#
# class Finder:
#     def __init__(self, *args, **kwargs):
#         self.server_name = kwargs['server_name']
#         self.password = kwargs['password']
#         self.interface_name = kwargs['interface']
#         self.main_dict = {}
#
#     def run(self):
#         command = """sudo iwlist wlp2s0 scan | grep -ioE 'ssid:"(.*{}.*)'"""
#         result = os.popen(command.format(self.server_name))
#         result = list(result)
#
#         if "Device or resource busy" in result:
#                 return None
#         else:
#             ssid_list = [item.lstrip('SSID:').strip('"\n') for item in result]
#             print("Successfully get ssids {}".format(str(ssid_list)))
#
#         for name in ssid_list:
#             try:
#                 result = self.connection(name)
#             except Exception as exp:
#                 print("Couldn't connect to name : {}. {}".format(name, exp))
#             else:
#                 if result:
#                     print("Successfully connected to {}".format(name))
#
#     def connection(self, name):
#         try:
#             os.system("nmcli d wifi connect {} password {} iface {}".format(name,
#        self.password,
#        self.interface_name))
#         except:
#             raise
#         else:
#             return True
#
# if __name__ == "__main__":
#     # Server_name is a case insensitive string, and/or regex pattern which demonstrates
#     # the name of targeted WIFI device or a unique part of it.
#     server_name = "example_name"
#     password = "your_password"
#     interface_name = "your_interface_name" # i. e wlp2s0
#     F = Finder(server_name=server_name,
#                password=password,
#                interface=interface_name)
#     F.run()

# import os
#
# os.system("netsh interface show interface")
# os.system("wlan")
#
# def enable():
#     os.system("netsh interface set interface 'Wifi' enabled")
#
#
# def disable():
#     os.system("netsh interface set interface 'Wifi' disabled")
#
# if __name__ == '__main__':
#     disable()

# import subprocess
#
# results = subprocess.check_output(["netsh", "wlan", "show", "network"])
# results = results.decode("ascii")
# results = results.replace("\r","")
# ls = results.split("\n")
# ls = ls[4:]
# ssids = []
# x = 0
# while x < len(ls):
#     if x % 5 == 0:
#         ssids.append(ls[x])
#     x += 1
#
# print(ssids)

# import subprocess
# results = subprocess.check_output(["netsh", "wlan", "show", "network"])
# print(results)

# importing subprocess
# import subprocess
#
# # getting meta data of the wifi network
# meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
#
# # decoding meta data from byte to string
# data = meta_data.decode('utf-8', errors="backslashreplace")
#
# # spliting data by line by line
# # string to list
# data = data.split('\n')
#
# # creating a list of wifi names
# names = []
#
# # traverse the list
# for i in data:
#
#     # find "All User Profile" in each item
#     # as this item will have the wifi name
#     if "All User Profile" in i:
#         # if found split the item
#         # in order to get only the name
#         i = i.split(":")
#
#         # item at index 1 will be the wifi name
#         i = i[1]
#
#         # formatting the name
#         # first and last chracter is use less
#         i = i[1:-1]
#
#         # appending the wifi name in the list
#         names.append(i)
#
# # printing the wifi names
# print("All wifi that system has connected to are ")
# print("-----------------------------------------")
# for name in names:
#     print(name)

# importing the subprocess module
import subprocess

# using the check_output() for having the network term retrival
devices = subprocess.check_output(['netsh','wlan','show','network'])

# decode it to strings
devices = devices.decode('ascii')
devices= devices.replace("\r","")

# displaying the information
print(devices)
