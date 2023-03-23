import pytest
from ansible_chat import AnsibleChat

@pytest.mark.parametrize("user_input,expected_command_name,expected_user_params,expected_text", [
    ("/hello_world2 param1:'test value' some text", "/hello_world2", {"param1": "test value"}, "some text"),
    ("/chained", "/chained", {}, ""),
    ("plain text", None, {}, "plain text"),
])
def test_parse_input_parametrized(user_input, expected_command_name, expected_user_params, expected_text):
    ansible_chat = AnsibleChat([])
    command_name, user_params, text = ansible_chat.parse_input(user_input)

    assert command_name == expected_command_name
    assert user_params == expected_user_params
    assert text == expected_text
