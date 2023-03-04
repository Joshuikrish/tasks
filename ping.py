from banner import *
import os
import subprocess
import argparse

banner('PING')
# Create the argument parser
parser = argparse.ArgumentParser(description='PING utility')

# Add the host argument (optional)
parser.add_argument('-H', '--host', type=str, help='Host name or IP address to ping')

# Parse the arguments
args = parser.parse_args()

# Set the host variable to the value passed in the argument, or to google.com if none is provided
host = args.host if args.host else "google.com"
command = f"ping {host} -n 4"
ping_result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
print(ping_result.stdout.decode('utf-8'))
