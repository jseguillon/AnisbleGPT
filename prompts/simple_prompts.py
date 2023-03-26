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

class ParallelPrompt(AnsiblePrompt):
    def __init__(self, sub_prompts):
        super().__init__()
        self.sub_prompts = sub_prompts

    async def new_message(self, text, file_list, **user_params):
        self.add_conversation_message("user", text)

        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as executor:
            tasks = [loop.run_in_executor(executor, sub_prompt.new_message, text, file_list, **user_params) for sub_prompt in self.sub_prompts]
            results = await asyncio.gather(*tasks)

        combined_answer = " ".join([result.gpt_answer for result in results])
        self.add_conversation_message("assistant", combined_answer)
        return AnsibleChatAnswer(combined_answer, file_list)

class ParallelSubPrompt1(OneShotPrompt):
    description = "Parallel Sub-prompt 1"
    command = "/parallel_sub_prompt1"

class ParallelSubPrompt2(OneShotPrompt):
    description = "Parallel Sub-prompt 2"
    command = "/parallel_sub_prompt2"
