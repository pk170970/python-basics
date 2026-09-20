import tiktoken

encoding = tiktoken.encoding_for_model('gpt-4o')
text = 'Hey, How are you'
tokens = encoding.encode(text)

print(tokens)
# [25216, 11, 3253, 553, 481]
decode = encoding.decode([25216, 11, 3253, 553, 481])
print(decode)