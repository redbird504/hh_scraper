from app.clients.client import Client
from app.clients.hh_client import HhClient

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "user-agent": 'Mozilla/5.0'
}

client = Client(headers)
hh_client = HhClient(client)


def get_hh_client() -> HhClient:
    return hh_client
