import boto3
import sys
import json

query = ' '.join(sys.argv[1:])

client = boto3.client('bedrock-runtime')
print(query)
prompt = """
<s>[INST] <<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible.
<</SYS>>
 """
response = client.invoke_model(
    body=json.dumps({
    "prompt": prompt + '\n' + query + "\n [/INST]",
		"max_gen_len": 512,
		"temperature": 0.2,
		"top_p": 0.9
    }),
    modelId='meta.llama2-70b-chat-v1'
)
print(json.loads(response['body'].read().decode('utf-8'))['generation'])