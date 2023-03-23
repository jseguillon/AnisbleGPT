from .base_prompts import ChainedPrompt, AnsiblePrompt

class ChainedPrompt1(ChainedPrompt):
    command = '/chained'
    description = "Chained prompt"
    parameters = []

    def __init__(self):
        sub_prompts = [HelloChained1(), HelloChained2()]
        super().__init__(sub_prompts)

class HelloChained1(AnsiblePrompt):
    system_message = "Say 'Hello, Chained!'"
    
class HelloChained2(AnsiblePrompt):
    system_message = "Say 'Hello, Chained 2!'"
