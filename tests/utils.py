from tokenio.config import TestConfig
from tokenio.proto.address_pb2 import Address
from tokenio.proto.alias_pb2 import Alias
from tokenio.token_client import TokenClient
from tokenio.utils import generate_nonce


def initialize_client():
    config = TestConfig()
    client = TokenClient(config)
    return client


def generate_alias():
    email = "python-sdk-test-{}-noverify@example.com".format(generate_nonce())
    alias = Alias(value=email, type=Alias.EMAIL)
    return alias


def generate_address():
    address = Address(house_number='425', street='Broadway', city='Redwood City',
                      post_code='94063', country='US')
    return address
