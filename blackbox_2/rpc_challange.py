import pyjsonrpc

http_client = pyjsonrpc.HttpClient(
    url = "http://hack.israeltechallenge.com:8000",
    username = "ITC"
)

print http_client.call("help")
print http_client.call("ping")
username = 'ITC'
password = 'l33#'

print http_client.call("login", username, password)
print http_client.call("__doc__")
