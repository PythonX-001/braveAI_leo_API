from leo_API import Leo

leo = Leo()

# It initially contains Brave's specified System Prompt.
response = leo.ask('What is the weather like today?')
print(response.completion)
#max_tokens_to_sample is an int : 400 to 2048
# You can use it as Llama by explicitly leaving System Prompt empty.
response = leo.ask('What is the weather like today?', system_prompt='',max_tokens_to_sample=2048)
print(response.completion)