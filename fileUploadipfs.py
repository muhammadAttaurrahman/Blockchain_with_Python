import ipfshttpclient

api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
new_file = api.add('housing.names')