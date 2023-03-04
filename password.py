from banner import *
import os
import subprocess
import argparse

banner('NETSH')
# Create the argument parser
# parser = argparse.ArgumentParser(description='netsh utility')

# Add the host argument (optional)
# parser.add_argument('-H', '--host', type=str, help='Host name or IP address to ping')

# Parse the arguments
# args = parser.parse_args()  

# Set the host variable to the value passed in the argument, or to google.com if none is provided
# host = args.host if args.host else "google.com"


command = f"netsh wlan show profiles"
ping_result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output = ping_result.stdout.decode('utf-8')

profiles = []
for line in output.splitlines():
    if "All User Profile" in line:
        profile = line.split(":")[-1].strip()
        profiles.append(profile)

print("Available Networks Are:\n")
print('Id\tName')
print('\t')
for index,items in enumerate(profiles):
    print(index+1,'\t'+items)
print('\n')

value = int(input("Enter an ID to get password: \n"))
if len(profiles) == 0:
    print("No wireless network profiles found.")
elif value > 0 and value <= len(profiles):
    original_value = profiles[value - 1]
    command = f'netsh wlan show profiles name="{original_value}" key=clear'
    ping_result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = ping_result.stdout.decode('utf-8')
    password_found = False
    for line in output.splitlines():
        if "Key Content" in line:
            password = line.split(":")[-1].strip()
            print(f"\nPassword for {original_value}: {password}\n\n")
            print(f"Thank you for using my tool.\n\n")
            password_found = True
            break
    if not password_found:
        print("\nThis network is encrypted using a different method. Please try a different network.\n\n")
else:
    print("\n\nPlease enter a valid number for the ID.\n\n")



# command = f"netsh wlan show profiles"
# ping_result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
# output = ping_result.stdout.decode('utf-8')
