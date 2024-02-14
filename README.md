# Try AutoGen

このリポジトリでは、AIマルチエージェントフレームワークである、AutoGenを試してみます。

## AutoGenとは

マイクロソフトが提供する、AIマルチエージェントフレームワークです。
以下に公式のGitHubリポジトリを示します。

[microsoft/autogen](https://github.com/microsoft/autogen)

## サンプルプログラム

### try_assistantagent.py（改良中）

システムを開発するために必要な複数のエージェントを作成し、それらを協調させ、システム開発を行うプログラムです。

## 実行方法

### 事前準備

1. OpenAIのAPIキーを取得します。OpenAIの公式サイトから取得してください。取得方法については、[【非エンジニア向け】ChatGPT(OpenAI)のAPIキー取得方法をわかりやすく解説！](https://www.goatman.co.jp/media/chatgpt/openai-api-key/#%253A~%253Atext%253DChatGPT%25EF%25BC%2588OpenAI%25EF%25BC%2589%2520API%25E3%2582%25AD%25E3%2583%25BC%25E3%2582%2592%25E5%258F%2596%25E5%25BE%2597%25E3%2581%2599%25E3%2582%258B%25E6%2589%258B%25E9%25A0%2586%25201%2520Step1%2520OpenAI%25E3%2581%25AE%25E3%2582%25A2%25E3%2582%25AB%25E3%2582%25A6%25E3%2583%25B3%25E3%2583%2588%25E4%25BD%259C%25E6%2588%2590%2520API%25E3%2582%25AD%25E3%2583%25BC%25E3%2582%2592%25E5%258F%2596%25E5%25BE%2597%25E3%2581%2599%25E3%2582%258B%25E3%2581%259F%25E3%2582%2581%25E3%2581%25AB%25E3%2581%25AF%25E3%2580%2581%25E3%2581%25BE%25E3%2581%259A%25E3%2581%25AFOpenAI%25E3%2581%25AE%25E3%2582%25A2%25E3%2582%25AB%25E3%2582%25A6%25E3%2583%25B3%25E3%2583%2588%25E4%25BD%259C%25E6%2588%2590%25E3%2581%258C%25E5%25BF%2585%25E8%25A6%2581%25E3%2581%25A7%25E3%2581%2599%25E3%2580%2582%2520...%25202%252C6%2520Step6%2520API%2520keys%25E3%2583%259A%25E3%2583%25BC%25E3%2582%25B8%25E3%2581%25A7%25E3%2580%258CCreate%2520new%2520secret%2520key%25E3%2580%258D%25E3%2582%2592%25E6%258A%25BC%25E3%2581%2599%2520)を参照してください。
2. GitHub CodeSpacesを利用するために、GitHubのアカウントを作成してください。GitHubのアカウントの作成方法については、[GitHub Codespacesの始め方](https://zenn.dev/protoout/articles/68-github-codespaces-setup)を参照してください。

### プログラムの実行

1. このリポジトリから、GitHub CodeSpacesを起動します。
2. OAI_CONFIG_LIST.exampleをOAI_CONFIG_LISTにファイル名を変更します。
3. `api_key`にOpenAIのAPIキーを設定します。
4. try_assistantagent.pyを実行します。

```bash
python try_assistantagent.py
```
