import pytest
from src.api_client import IntelXClient

def test_intesx_simulation_result():
    #test simulation system is return correct result
    client = IntelXClient(api_key=" ")
    test_email = "test@example.com"

    result = client.check_breach(test_email)

    #test infrastructure (assertion)
    assert result['email_address'] == test_email
    assert isinstance(result['breached'], bool)
    assert 'site_where_breached' in result

def test_api_client_simulation_mode_toggle():
    #test if input api key the system will turn the simulation mode off or not or willing to connect to wrong api key
    client_sim = IntelXClient(api_key=" ")
    client_real = IntelXClient(api_key= "actual-key-123")