# Nano Banana Pro（Google Gemini Image）

Nano Banana Pro（Google Gemini Image）は、Google の Vertex AI Gemini 画像モデルを使用して画像を生成または編集します。テキストプロンプトと、必要に応じて参照画像やファイルを Gemini API に送信し、生成された画像と、任意のテキストレスポンスを返します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 生成する画像、または適用する編集内容を説明するテキストプロンプト。モデルが従うべき制約、スタイル、詳細を含めます。デフォルトは空文字列です。 | STRING | はい | N/A |
| `model` | 使用する Gemini 画像モデル。「Nano Banana 2 (Gemini 3.1 Flash Image)」オプションは API に `gemini-3.1-flash-image` として送信され、「gemini-3-pro-image-preview」は `gemini-3-pro-image` として送信されます。 | COMBO | はい | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | シードを特定の値に固定すると、モデルは繰り返しリクエストに対して同じ応答を返すよう最善を尽くします。ただし、決定的な出力は保証されません。モデルやその他のパラメータ設定を変更すると、同じシード値でも応答が異なる場合があります。デフォルト: 42。 | INT | はい | 0 ～ 18446744073709551615 |
| `aspect_ratio` | 出力画像の希望するアスペクト比。"auto" に設定すると、入力画像のアスペクト比に合わせられます。画像が提供されない場合は、通常 16:9 のスクエア画像が生成されます。デフォルト: "auto"。 | COMBO | はい | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | 出力解像度の指定。2K/4K では Gemini ネイティブのアップスケーラーが使用されます。 | COMBO | はい | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | 画像のみの出力には "IMAGE" を選択し、生成画像とテキストレスポンスの両方を返すには "IMAGE+TEXT" を選択します。 | COMBO | はい | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | 視覚的なコンテキストとして使用するオプションの参照画像。複数の画像を含めるには、Batch Images ノードを使用します（最大 14 枚）。 | IMAGE | いいえ | N/A |
| `files` | モデルのコンテキストとして使用するオプションのファイル。Gemini Generate Content Input Files ノードからの入力を受け付けます。 | GEMINI_INPUT_FILES | いいえ | N/A |
| `system_prompt` | モデルの動作を決定づける基本指示。デフォルトでは、モデルに常に画像を生成するよう指示する定義済みのシステムプロンプトが設定されています。 | STRING | いいえ | N/A |

**制約事項：**

* `prompt` は、先頭と末尾の空白を削除した後も空であってはなりません。空の場合はエラーが発生します。
* `images` 入力は最大 14 枚の画像を受け付けます。14 枚を超えるとエラーが発生します。
* `files` 入力は、`GEMINI_INPUT_FILES` データ型を出力するノードに接続する必要があります。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `image` | Gemini モデルによって生成または編集された画像。 | IMAGE |
| `string` | モデルからのテキストレスポンス。`response_modalities` が "IMAGE" に設定されている場合、この出力は空になります。 | STRING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/ja.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
