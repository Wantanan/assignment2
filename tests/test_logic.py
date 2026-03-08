import pytest
from src.api_client import BreachDirectoryClient

def test_breach_directory_simulation_result():
    #test simulation system is return correct result
    client = BreachDirectoryClient(api_key=" ")
    test_email = "test@example.com"

    result = client.check_breach(test_email)

    #test infrastructure (assertion)
    assert result['email_address'] == test_email
    assert 'found' in result
    assert isinstance(result['found'], bool)
    assert 'sources' in result

def test_client_mode_logic():
    #test if not api key the simulation mode will be True
    client_no_key = BreachDirectoryClient(api_key="")
    assert client_no_key.simulation_mode is True

    #test if api key the simulation mode is turn off and will be False
    client_with_key = BreachDirectoryClient(api_key="12345-abcde")
    assert client_with_key.simulation_mode is False