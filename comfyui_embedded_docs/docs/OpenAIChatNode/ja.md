> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/ja.md)

このノードはOpenAIモデルからテキスト応答を生成します。テキストプロンプトを送信して生成された応答を受け取ることで、AIモデルとの会話を行うことができます。このノードは、以前のコンテキストを記憶できるマルチターン会話をサポートしており、モデルの追加コンテキストとして画像やファイルを処理することもできます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | はい | - | モデルへのテキスト入力。応答を生成するために使用されます（デフォルト：空） |
| `persist_context` | BOOLEAN | はい | - | マルチターン会話のために、呼び出し間でチャットコンテキストを保持します（デフォルト：True） |
| `model` | COMBO | はい | 複数のOpenAIモデルが利用可能 | 応答生成に使用するOpenAIモデル |
| `images` | IMAGE | いいえ | - | モデルのコンテキストとして使用するオプションの画像。複数の画像を含めるには、Batch Imagesノードを使用できます（デフォルト：None） |
| `files` | OPENAI_INPUT_FILES | いいえ | - | モデルのコンテキストとして使用するオプションのファイル。OpenAI Chat Input Filesノードからの入力を受け付けます（デフォルト：None） |
| `advanced_options` | OPENAI_CHAT_CONFIG | いいえ | - | モデルのオプション設定。OpenAI Chat Advanced Optionsノードからの入力を受け付けます（デフォルト：None） |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output_text` | STRING | OpenAIモデルによって生成されたテキスト応答 |
