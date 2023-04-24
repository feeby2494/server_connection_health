# server_connection_health

Purpose of this script is to test and analyse internet and network connectivity 
by simply pinging Google's DNS server and other servers that may be remore or local.

In order to use this correctly, a .env file is required with the ip addresses of
servers that you need to ping.

# Please configure the .env file.
    ADDRESSES="<your list of ip addresses delimited by ",">"
    
# Make sure python-dotenv is installed to the local virtual environment.
    python3 -m venv venv
    source venv/bin/activate
    pip install python-dotenv 
