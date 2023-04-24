#!./venv/bin/python
import subprocess
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

###
#
#
#           Purpose of this script is to test and analyse internet and network connectivity
#           by simply pinging Google's DNS server and other servers that may be remore or local.
#
#
#           In order to use this correctly, a .env file is required with the ip addresses of
#           servers that you need to ping.
#
#           Please configure the .env file.
#               ADDRESSES="<your list of ip addresses delimited by ",">"
#
#           Make sure python-dotenv is installed to the local virtual environment.
#               python3 -m venv venv
#               source venv/bin/activate
#               pip install python-dotenv 
#
#
###


def ping_server(server_ip):
    ping = subprocess.Popen(['ping', server_ip, "-c", "15"], stdout=subprocess.PIPE)
    return ping

# Doing the pings for all addresses in .env

pings_list = []
error_list = []
success_list = []
addresses = os.getenv("IP_ADDRESSES").split(",")

for address in addresses:
    ping_object = {}
    ping_command = ping_server(address)
    ping_object["ip_address"] = address
    ping_object["output"] = ping_command.communicate()[0]
    ping_object["success"] = True
    ping_object["return_code"] = ping_command.returncode
    if ping_object["return_code"] != 0:
        ping_object["success"] = False
        error_list.append(ping_object)
    else:
        success_list.append(ping_object)
    pings_list.append(ping_object)

# ### 
# # 
# # Local Logging Portion 
# # 
# # ###

log_dir_path = os.path.join(os.getcwd(), "logs")
error_log = os.path.join(log_dir_path, "error.txt")
success_log = os.path.join(log_dir_path, "success.txt")
all_log = os.path.join(log_dir_path, "all.txt")

# Make the logs directory if it's not there
if not os.path.exists(log_dir_path):
    os.makedirs(log_dir_path)

# Make error.txt if it's not there
if not os.path.exists(error_log):
    with open(error_log, "w") as f:
        f.write("Error Log for Failed Pings with date")

# Make success.txt if it's not there
if not os.path.exists(success_log):
    with open(success_log, "w") as f:
        f.write("Success Log for Successful Pings with date")

# Make all.txt if it's not there
if not os.path.exists(all_log):
    with open(all_log, "w") as f:
        f.write("Log for All Pings with date")

# Populate error.txt
if len(error_list) > 0:
    with open(error_log, "a") as f:
        for line in error_list:
            f.write(f"\n{datetime.datetime.now()} - Failed for ip address:{line['ip_address']} with return code: {line['return_code']}")

# Populate success.txt
if len(success_list) > 0:
    with open(success_log, "a") as f:
        for line in success_list:
            f.write(f"\n{datetime.datetime.now()} - Succeeded for ip address:{line['ip_address']} with return code: {line['return_code']}")

# Populate all.txt
with open(all_log, "a") as f:
        for line in pings_list:
            f.write(f"\n{datetime.datetime.now()} - Ping for ip address:{line['ip_address']} with return code: {line['return_code']}; Success: {line['success']}")

