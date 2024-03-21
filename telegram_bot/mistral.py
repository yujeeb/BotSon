import replicate

prompt_template = """
<s>[INST] 
Respond as a telegram bot named BotSon to a telegram user's message given below.
User message: {prompt} 
Bot Response: 
[/INST]
"""

def mistral_chat(input_text: str) -> str:
    output = replicate.run(
        "mistralai/mistral-7b-instruct-v0.2:79052a3adbba8116ebc6697dcba67ad0d58feff23e7aeb2f103fc9aa545f9269",
        input={
            "debug": False,
            "top_k": 50,
            "top_p": 0.9,
            "prompt": input_text,
            "temperature": 0.6,
            "max_new_tokens": 512,
            "min_new_tokens": -1,
            "prompt_template": "<s>[INST] {prompt} [/INST] ",
            "repetition_penalty": 1.15
        }
    )


    answer = ""
    for item in output:
        # https://replicate.com/mistralai/mistral-7b-instruct-v0.2/api#output-schema
        # print(item, end="")
        answer += item
    print()
    return answer

def mistral_large(input_text: str) -> str:
    # The mistralai/mixtral-8x7b-instruct-v0.1 model can stream output as it's running.
    output = replicate.run(
        "mistralai/mixtral-8x7b-instruct-v0.1",
        input={
            "top_k": 50,
            "top_p": 0.9,
            "prompt": input_text,
            "temperature": 0.6,
            "max_new_tokens": 1024,
            "prompt_template": prompt_template,
            "presence_penalty": 0,
            "frequency_penalty": 0
        }
    )
    
    answer = ""
    for item in output:
        # print(item, end="")
        answer += item
    print()
    return answer
