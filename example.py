from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# See https://github.com/microsoft/autogen/blob/main/OAI_CONFIG_LIST_sample
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# You can also set config_list directly as a list, for example, config_list = [{'model': 'gpt-4', 'api_key': '<your OpenAI API key here>'},]
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})

# UserProxyAgent: 人間の代理として、コードの実行やアシスタントへのフィードバックを行う役割を担うエージェント。
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False}) # IMPORTANT: set to True to run code in docker, recommended
# 
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")

# This initiates an automated chat between the two agents to solve the task

