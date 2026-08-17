# OpenRouter LLM

OpenRouter LLMノードは、OpenRouterサービスを通じて利用可能な厳選された言語モデル群にテキストプロンプト（必要に応じて画像や動画も）を送信し、生成されたテキスト応答を返します。Anthropic（Claude）、OpenAI（GPT）、Google（Gemini）、xAI（Grok）、DeepSeek、Qwen、Mistral、Z.AI（GLM）、Moonshot（Kimi）、Perplexity Sonar のモデルに対応しており、選択したモデルが対応している場合、推論努力（reasoning effort）やWeb検索コンテキストなどのモデル固有のオプションを表示します。

## 入力

`model` セレクタは動的です。モデルを選択すると、以下の共通入力に加えて、モデル固有のウィジェット（推論努力、Web検索コンテキスト、画像・動画スロット）が表示されます。

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | 応答の生成に使用するOpenRouterモデル。モデルを選択すると、そのモデル固有の入力が表示されます（下記のモデルセクションを参照）。 | DYNAMIC_COMBO | 必須 | 厳選された34のOpenRouterモデルオプション |
| `prompt` | モデルに入力するテキスト。空白以外の文字が1文字以上必要です。 | STRING | 必須 | 複数行テキスト |
| `seed` | サンプリング用のシード。0に設定すると省略されます。ほとんどのモデルはこれをヒントとしてのみ扱います。（デフォルト: 0） | INT | 必須 | 0 ～ 2147483647 |
| `system_prompt` | モデルの動作を決定づける基本指示。（デフォルト: ""） | STRING | 任意 | 複数行テキスト |

**`seed` に関する注意:** このパラメータには「control_after_generate」動作があります。つまり、ユーザーのウィジェット設定に応じて、ノード実行ごとに自動的に変更（例: ランダム化、増分、固定）するよう設定できます。

**`system_prompt` に関する注意:** このパラメータはオプションであり、ユーザーインターフェース上では詳細パラメータとしてマークされています。

### Anthropic Claude 入力

以下のモデルで共通です: `anthropic/claude-opus-5`、`anthropic/claude-opus-4.8`、`anthropic/claude-opus-4.7`、`anthropic/claude-fable-5`、`anthropic/claude-sonnet-5`、`anthropic/claude-haiku-4.5`。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推論努力。"off" を指定すると推論が完全に無効になります。（デフォルト: "off"） | COMBO | 任意 | "off"<br>"low"<br>"medium"<br>"high" |

### OpenAI GPT 入力

以下のモデルで共通です: `openai/gpt-5.6-sol-pro`、`openai/gpt-5.6-sol`、`openai/gpt-5.6-terra-pro`、`openai/gpt-5.6-terra`、`openai/gpt-5.6-luna-pro`、`openai/gpt-5.6-luna`、`openai/gpt-5.5-pro`、`openai/gpt-5.5`。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推論努力。"off" を指定すると推論が完全に無効になります。（デフォルト: "off"） | COMBO | 任意 | "off"<br>"low"<br>"medium"<br>"high" |

### Google Gemini 3.5 Flash 入力

対象モデル: `google/gemini-3.5-flash`。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推論努力。"off" を指定すると推論が完全に無効になります。（デフォルト: "off"） | COMBO | 任意 | "off"<br>"low"<br>"medium"<br>"high" |

### xAI Grok 入力

以下のモデルで共通です: `x-ai/grok-4.5`、`x-ai/grok-4.20`、`x-ai/grok-4.3`。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推論努力。"off" を指定すると推論が完全に無効になります。（デフォルト: "off"） | COMBO | 任意 | "off"<br>"low"<br>"medium"<br>"high" |

### DeepSeek 入力

以下のモデルで共通です: `deepseek/deepseek-v4-pro`、`deepseek/deepseek-v4-flash`、`deepseek/deepseek-v3.2`。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推論努力。"off" を指定すると推論が完全に無効になります。（デフォルト: "off"） | COMBO | 任意 | "off"<br>"low"<br>"medium"<br>"high" |

### Qwen 3.6 Plus / Flash 入力

以下のモデルで共通です: `qwen/qwen3.6-plus`、`qwen/qwen3.6-flash`。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推論努力。"off" を指定すると推論が完全に無効になります。（デフォルト: "off"） | COMBO | 任意 | "off"<br>"low"<br>"medium"<br>"high" |

### Mistral Large 2512 入力

対象モデル: `mistralai/mistral-large-2512`。このモデルにはモデル固有のパラメータウィジェットは追加されず、共通入力と `images` 参照スロットのみが適用されます。

### Mistral Medium 3.5 入力

対象モデル: `mistralai/mistral-medium-3-5`。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推論努力。"off" を指定すると推論が完全に無効になります。（デフォルト: "off"） | COMBO | 任意 | "off"<br>"low"<br>"medium"<br>"high" |

### Moonshot Kimi K3 / K2.6 入力

以下のモデルで共通です: `moonshotai/kimi-k3`、`moonshotai/kimi-k2.6`。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推論努力。"off" を指定すると推論が完全に無効になります。（デフォルト: "off"） | COMBO | 任意 | "off"<br>"low"<br>"medium"<br>"high" |

### Perplexity Sonar Pro 入力

対象モデル: `perplexity/sonar-pro`。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | 取得するWeb検索コンテキストの量。大きいほど根拠のある回答になりますが、遅く／高コストになります。（デフォルト: "medium"） | COMBO | 任意 | "low"<br>"medium"<br>"high" |

### Perplexity Sonar Reasoning Pro / Deep Research 入力

以下のモデルで共通です: `perplexity/sonar-reasoning-pro`、`perplexity/sonar-deep-research`。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | 取得するWeb検索コンテキストの量。大きいほど根拠のある回答になりますが、遅く／高コストになります。（デフォルト: "medium"） | COMBO | 任意 | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | 推論努力。"off" を指定すると推論が完全に無効になります。（デフォルト: "off"） | COMBO | 任意 | "off"<br>"low"<br>"medium"<br>"high" |

### 推論専用モデル

以下のモデルで共通です: `qwen/qwen3.6-max-preview`、`z-ai/glm-4.6`、`z-ai/glm-5`、`moonshotai/kimi-k2-thinking`。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推論努力。"off" を指定すると推論が完全に無効になります。（デフォルト: "off"） | COMBO | 任意 | "off"<br>"low"<br>"medium"<br>"high" |

### 参照入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `images` | オプションの参照画像。URLとして送信されます。拡張可能スロット: `image_1` から `image_N` まで接続できます。N は選択したモデルに依存します。 | IMAGE | 任意 | 0 ～ N枚（Nはモデルにより8、10、または20） |
| `videos` | オプションの参照動画。URLとして送信されます。拡張可能スロット: `video_1` から `video_N` まで接続できます。動画対応モデルでのみ利用可能です。 | VIDEO | 任意 | 0 ～ 4本 |

**モデルの対応状況と制限に関する注意:**

- 画像対応: Anthropic Claude、OpenAI GPT、Google Gemini 3.5 Flash、xAI Grok モデルは最大20枚、Qwen 3.6 Plus/Flash と Moonshot Kimi K3/K2.6 は最大10枚、Mistral Large 2512 と Mistral Medium 3.5 は最大8枚。DeepSeek、Qwen 3.6 Max Preview、Z.AI GLM、Moonshot Kimi K2 Thinking、Perplexity Sonar モデルは画像を受け付けません。
- 動画対応: 動画を受け付けるのは `google/gemini-3.5-flash`、`qwen/qwen3.6-plus`、`qwen/qwen3.6-flash` のみで、最大4本です。
- 選択したモデルが対応している数を超えて画像や動画を接続すると、ノードはエラーを発生させます。
- `reasoning_effort` を "low"、"medium"、"high" に設定すると、モデルは内部的に推論しますが、推論トレースは返しません。"off" を指定すると推論が完全に無効になります。
- `search_context_size` ウィジェットは Perplexity Sonar モデルにのみ表示されます。`reasoning_effort` と `search_context_size` ウィジェットは詳細パラメータとしてマークされています。
- ノードは、選択したモデルに基づいておおよその価格バッジ（1KトークンあたりのUSD）を表示します。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `output` | 選択したOpenRouterモデルから生成されたテキスト応答。 | STRING |

**エラーに関する注意:** OpenRouter が API エラー、空の応答（choices なし）、またはモデルによる拒否を返した場合、ノードはエラーを発生させます。

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/ja.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
