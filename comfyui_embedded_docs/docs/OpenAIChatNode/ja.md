# OpenAI ChatGPT

このノードは、OpenAI モデルからテキスト応答を生成します。テキストプロンプト（および必要に応じて画像やファイル）を OpenAI モデルに送信し、生成されたテキスト応答を返します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | モデルへのテキスト入力で、応答を生成するために使用されます（デフォルト: 空） | STRING | 必須 | - |
| `persist_context` | このパラメータは非推奨であり、効果はありません（デフォルト: False） | BOOLEAN | 必須 | - |
| `model` | 応答の生成に使用されるモデル（デフォルト: `gpt-5`） | COMBO | 必須 | `gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | モデルのコンテキストとして使用するオプションの画像。複数の画像を含めるには、Batch Images ノードを使用できます | IMAGE | 任意 | - |
| `files` | モデルのコンテキストとして使用するオプションのファイル。OpenAI Chat Input Files ノードからの入力を受け入れます | OPENAI_INPUT_FILES | 任意 | - |
| `advanced_options` | モデルのオプション設定。OpenAI Chat Advanced Options ノードからの入力を受け入れます | OPENAI_CHAT_CONFIG | 任意 | - |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `output_text` | OpenAI モデルによって生成されたテキスト応答 | STRING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/ja.md)

---
**Source fingerprint (SHA-256):** `25bb3648a4e1ea5668486375153ac4c96b542082c88958d4f62b93adf1db5b2a`
