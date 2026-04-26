import requests as req

def get_data(endpoint):
    return req.get(endpoint)
    