from .base_prompts import AnsiblePrompt
from .base_prompts import OneShotPrompt

class HelloWorldPrompt(AnsiblePrompt):
    command = '/hello_world'
    description = "Hello world prompt"
    parameters = ['param1', 'param2']
    system_message = "Say 'Hello, World!' whatever user input. \nHello:\n"

class HelloWorld2Prompt(OneShotPrompt):
    command = '/hello_world2'
    description = "Hello world 2 prompt one shot"
    parameters = ['param1']
    system_message = "Say 'Hello, World 2 !' whatever user input. \nHello:\n"
