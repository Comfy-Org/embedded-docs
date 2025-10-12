> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/ja.md)

このノードは、GoogleのGemini AIモデルと対話してテキスト応答を生成することができます。テキスト、画像、音声、動画、ファイルなど複数の種類の入力をコンテキストとして提供でき、モデルがより関連性の高い意味のある応答を生成するのに役立ちます。ノードはAPI通信と応答の解析を自動的に処理します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | はい | - | モデルへのテキスト入力で、応答の生成に使用されます。モデルに対する詳細な指示、質問、コンテキストを含めることができます。デフォルト: 空文字列。 |
| `model` | COMBO | はい | `gemini-2.0-flash-exp`<br>`gemini-2.0-flash-thinking-exp`<br>`gemini-2.5-pro-exp`<br>`gemini-2.0-flash`<br>`gemini-2.0-flash-thinking`<br>`gemini-2.5-pro`<br>`gemini-2.0-flash-lite`<br>`gemini-1.5-flash`<br>`gemini-1.5-flash-8b`<br>`gemini-1.5-pro`<br>`gemini-1.0-pro` | 応答生成に使用するGeminiモデルです。デフォルト: gemini-2.5-pro。 |
| `seed` | INT | はい | 0 から 18446744073709551615 | seedを特定の値に固定すると、モデルは繰り返しリクエストに対して同じ応答を提供するよう最善を尽くします。ただし、決定的な出力は保証されません。また、モデルや温度などのパラメータ設定を変更すると、同じseed値を使用した場合でも応答にばらつきが生じることがあります。デフォルトではランダムなseed値が使用されます。デフォルト: 42。 |
| `images` | IMAGE | いいえ | - | モデルのコンテキストとして使用するオプションの画像です。複数の画像を含める場合は、Batch Imagesノードを使用できます。デフォルト: None。 |
| `audio` | AUDIO | いいえ | - | モデルのコンテキストとして使用するオプションの音声です。デフォルト: None。 |
| `video` | VIDEO | いいえ | - | モデルのコンテキストとして使用するオプションの動画です。デフォルト: None。 |
| `files` | GEMINI_INPUT_FILES | いいえ | - | モデルのコンテキストとして使用するオプションのファイルです。Gemini Generate Content Input Filesノードからの入力を受け付けます。デフォルト: None。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `STRING` | STRING | Geminiモデルによって生成されたテキスト応答です。 |
