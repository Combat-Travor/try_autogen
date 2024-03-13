import autogen

# 設定の読み込み
config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": "gpt-4-0125-preview",
    }
)
llm_config = {
    "config_list": config_list,
    "timeout": 100,
}

# UserProxy（ユーザの代理役）
user_proxy = autogen.UserProxyAgent(
    name="UserProxy",
    llm_config=llm_config,
    system_message="""あなたは、ユーザとの連絡窓口です。ユーザの調査依頼に応じて、WebResearcher、Writer、Reviewerなどに指示を出します。
    WebResearcher、Writer、Reviewerからの報告を受け取り、ユーザに回答を行うか、WebResearcher、Writer、Reviewerに別の指示を出します。
    ユーザが[end]と入力したら、タスクを終了してください。
    """,
    # エージェントの会話に人間が介入するかどうかのモード
    human_input_mode="TERMINATE",
    # 必要に応じてプログラムを実行するために、code_execution_configを設定する。
    code_execution_config={
        "use_docker": False,
    }
)

# WebResearcher
web_researcher = autogen.AssistantAgent(
    name="WebResearcher",
    llm_config=llm_config,
    system_message="""あなたは、WebResearcherです。ユーザからの依頼に基づいて、Web上の情報を収集します。
    収集した情報を元に、Writerに報告書の作成を依頼します。
    またWebからデータを収集するために、必要に応じてプログラムコードを書いて、UserProxyにコードの実行を依頼してください。
    """
)

# Writer
writer = autogen.AssistantAgent(
    name="Writer",
    llm_config=llm_config,
    system_message="""あなたは、Writerです。WebResearcherからの情報を元に、ユーザへの報告書を作成します。
    作成した報告書は、Reviewerにレビューを依頼して、レビュー結果に応じて修正してください。
    """,
)

# Reviewer
reviewer = autogen.AssistantAgent(
    name="Reviewer",
    llm_config=llm_config,
    system_message="あなたは、Reviewerです。Writerが作成した報告書を確認し、ユーザに提出します。",
)

# グループの定義
groupchat = autogen.GroupChat(
    agents=[
        user_proxy, 
        web_researcher, 
        writer, 
        reviewer
    ], 
    messages=[], 
    max_round=12
    )
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# マルチAIエージェントにタスクを依頼する。
user_proxy.initiate_chat(
    manager,
    message="""人工知能に関するニュースを調査し、以下の条件を満たすように、調査報告書を作成してください。
    # 条件
    - 調査報告書はmarkdown形式で記載してください。
    - なぜそのニュースが注目されているかの解説を報告に含めてください。
    - 高校生や老人など様々な人が理解できるように具体例等を挙げて、わかりやすく説明するように記載してください。
    """
)