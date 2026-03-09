import pytest
import httpx
from src.api_client import BreachDirectoryClient

@pytest.mark.asyncio

async def test_breach_directory_simulation():
    #test simulation system is return correct result
    client = BreachDirectoryClient(api_key="")
    test_email = "test@example.com"

    async with httpx.AsyncClient() as async_client:
        result = await client.check_breach(async_client, test_email)

    #test infrastructure (assertion)
    assert result['email_address'] == test_email
    assert 'breached' in result
    assert isinstance(result['breached'], bool)
    assert 'site_where_breached' in result

def test_client_init_config():
    key = "test-123"
    client = BreachDirectoryClient(api_key=key)
    assert client.api_key == key
    assert client.headers["X-RapidAPI-Key"] == key