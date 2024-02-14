import autogen

# 設定の読み込み
config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": "gpt-4",
    }
)

llm_config = {
    "config_list": config_list,
    "timeout": 100,
}

pm = autogen.UserProxyAgent(
    name="PROJECT-MANAGER",
    llm_config=llm_config,
    system_message="""あなたは、システム開発プロジェクトのプロジェクトマネージャーです。
    ユーザの要望に応じて、要件定義担当、システムアーキテクト、設計担当、プログラマ、テスターなどに指示を出します。
    """,
    human_input_mode="ALWAYS",
)

# 要件定義担当
requirement_definition = autogen.AssistantAgent(
    name="requirement-difinition",
    llm_config=llm_config,
    system_message="あなたは、要件定義担当です。要件定義を行います。",
)

# システムアーキテクト担当
system_architect = autogen.AssistantAgent(
    name="system-architect",
    llm_config=llm_config,
    system_message="あなたは、システムアーキテクト担当です。要件に応じてシステムのアーキテクチャを設計します。。",
)

# 設計担当
designer = autogen.AssistantAgent(
    name="system-designer",
    llm_config=llm_config,
    system_message="あなたは、設計担当です。基本設計や詳細設計、機能設計を行います。",
)

# プログラマ
programer = autogen.AssistantAgent(
    name="programer",
    llm_config=llm_config,
    system_message="""
    あなたは、プログラマです。要件や設計、システムアーキテクトの成果物に応じてプログラムを作成します。
    """,
)

# テスター
tester = autogen.AssistantAgent(
    name="tester",
    llm_config=llm_config,
    system_message="""あなたは、テスターです。プログラマが作成したプログラムコードのテストを行います。""",
)

groupchat = autogen.GroupChat(
    agents=[
        pm, 
        requirement_definition, 
        system_architect, 
        designer, 
        programer, 
        tester
    ], 
    messages=[], 
    max_round=12
    )

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

pm.initiate_chat(
    manager,
    message="YouTubeからコメントを取得して、音声で返答するVTuberの仕組みを作って下さい。"
)