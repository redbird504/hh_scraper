from .client import Client
from .hh_client import HhClient

__all__ = ('hh_client',)

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "user-agent": 'Mozilla/5.0'
}

client = Client(headers)

hh_client = HhClient(client)
