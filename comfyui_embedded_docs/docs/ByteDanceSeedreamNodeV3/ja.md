# ByteDanceSeedreamNodeV3

ByteDance Seedream 4.5 & 5.0 は、テキストプロンプトからの画像生成（text-to-image）や、オプションの参照画像に基づく画像生成・編集を、ByteDance Seedream 4.0、4.5、5.0 モデルを使用して最大 4K 解像度で行います。このノードは、プロンプトと参照画像を ByteDance API に送信し、生成タスクの完了を待って、結果の画像テンソルを返します。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 画像を作成または編集するためのテキストプロンプト。前後の空白を除去した後も空であってはなりません。 | STRING | はい | Multiline text |
| `model` | 使用する Seedream モデルを選択します。各モデルには、以下の独自のサブパラメータと制限があります。 | DYNAMIC_COMBO | はい | "seedream 5.0 pro"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Seedream 5.0 Pro 入力 (seedream 5.0 pro)

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 推奨サイズを選択します。下の幅と高さを使用するには「Custom」を選択します。デフォルト: このモデルの最初の推奨プリセット。 | COMBO | いいえ | Model-specific recommended size presets<br>"Custom" |
| `width` | 画像のカスタム幅。この値は `size_preset` が `Custom` に設定されている場合にのみ有効です。デフォルト: 2048。 | INT | いいえ | 1024 to 3136 (step 2) |
| `height` | 画像のカスタム高さ。この値は `size_preset` が `Custom` に設定されている場合にのみ有効です。デフォルト: 2048。 | INT | いいえ | 1024 to 2496 (step 2) |
| `prompt_optimization` | 参照画像が提供された場合のプロンプト最適化モード。「standard」は高品質、「fast」は短い生成時間になります。デフォルト: "standard"。 | COMBO | いいえ | "standard"<br>"fast" |
| `seed` | 生成に使用するシード。デフォルト: 42。 | INT | いいえ | 0 to 2147483647 |
| `watermark` | 画像に「AI生成」の透かしを追加するかどうか。デフォルト: false。 | BOOLEAN | いいえ | true / false |
| `thinking` | モデルのプロンプト最適化推論（'thinking'）を有効にして、プロンプトへの適合性を高めます。生成時間が大幅に増加する可能性があります（特に Seedream 5.0 Pro）。テキストから画像を生成する場合にのみ無効にできます（参照画像が提供されている場合は無効にできません）。デフォルト: true。 | BOOLEAN | いいえ | true / false |

### Seedream 5.0 Lite 入力 (seedream 5.0 lite)

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 推奨サイズを選択します。下の幅と高さを使用するには「Custom」を選択します。デフォルト: このモデルの最初の推奨プリセット。 | COMBO | いいえ | Model-specific recommended size presets<br>"Custom" |
| `width` | 画像のカスタム幅。この値は `size_preset` が `Custom` に設定されている場合にのみ有効です。デフォルト: 2048。 | INT | いいえ | 1024 to 6240 (step 2) |
| `height` | 画像のカスタム高さ。この値は `size_preset` が `Custom` に設定されている場合にのみ有効です。デフォルト: 2048。 | INT | いいえ | 1024 to 4992 (step 2) |
| `max_images` | 生成する画像の最大数。1 の場合は正確に 1 枚の画像が生成されます。1 より大きい場合は、モデルは 1 枚から max_images 枚までの関連画像（例: ストーリーシーン、キャラクターのバリエーション）を生成します。画像の合計（入力 + 生成）は 15 を超えることはできません。デフォルト: 1。 | INT | いいえ | 1 to 14 |
| `fail_on_partial` | 有効にすると、要求された画像のいずれかが欠落している場合やエラーが返された場合に実行を中止します。デフォルト: false。 | BOOLEAN | いいえ | true / false |
| `seed` | 生成に使用するシード。デフォルト: 42。 | INT | いいえ | 0 to 2147483647 |
| `watermark` | 画像に「AI生成」の透かしを追加するかどうか。デフォルト: false。 | BOOLEAN | いいえ | true / false |
| `thinking` | モデルのプロンプト最適化推論（'thinking'）を有効にして、プロンプトへの適合性を高めます。生成時間が大幅に増加する可能性があります（特に Seedream 5.0 Pro）。テキストから画像を生成する場合にのみ無効にできます（参照画像が提供されている場合は無効にできません）。デフォルト: true。 | BOOLEAN | いいえ | true / false |

### Seedream 4.5 入力 (seedream-4-5-251128)

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 推奨サイズを選択します。下の幅と高さを使用するには「Custom」を選択します。デフォルト: このモデルの最初の推奨プリセット。 | COMBO | いいえ | Model-specific recommended size presets<br>"Custom" |
| `width` | 画像のカスタム幅。この値は `size_preset` が `Custom` に設定されている場合にのみ有効です。デフォルト: 2048。 | INT | いいえ | 1024 to 6240 (step 2) |
| `height` | 画像のカスタム高さ。この値は `size_preset` が `Custom` に設定されている場合にのみ有効です。デフォルト: 2048。 | INT | いいえ | 1024 to 4992 (step 2) |
| `max_images` | 生成する画像の最大数。1 の場合は正確に 1 枚の画像が生成されます。1 より大きい場合は、モデルは 1 枚から max_images 枚までの関連画像（例: ストーリーシーン、キャラクターのバリエーション）を生成します。画像の合計（入力 + 生成）は 15 を超えることはできません。デフォルト: 1。 | INT | いいえ | 1 to 10 |
| `fail_on_partial` | 有効にすると、要求された画像のいずれかが欠落している場合やエラーが返された場合に実行を中止します。デフォルト: false。 | BOOLEAN | いいえ | true / false |
| `seed` | 生成に使用するシード。デフォルト: 42。 | INT | いいえ | 0 to 2147483647 |
| `watermark` | 画像に「AI生成」の透かしを追加するかどうか。デフォルト: false。 | BOOLEAN | いいえ | true / false |
| `thinking` | モデルのプロンプト最適化推論（'thinking'）を有効にして、プロンプトへの適合性を高めます。生成時間が大幅に増加する可能性があります（特に Seedream 5.0 Pro）。テキストから画像を生成する場合にのみ無効にできます（参照画像が提供されている場合は無効にできません）。デフォルト: true。 | BOOLEAN | いいえ | true / false |

### Seedream 4.0 入力 (seedream-4-0-250828)

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 推奨サイズを選択します。下の幅と高さを使用するには「Custom」を選択します。デフォルト: このモデルの最初の推奨プリセット。 | COMBO | いいえ | Model-specific recommended size presets<br>"Custom" |
| `width` | 画像のカスタム幅。この値は `size_preset` が `Custom` に設定されている場合にのみ有効です。デフォルト: 2048。 | INT | いいえ | 1024 to 6240 (step 2) |
| `height` | 画像のカスタム高さ。この値は `size_preset` が `Custom` に設定されている場合にのみ有効です。デフォルト: 2048。 | INT | いいえ | 1024 to 4992 (step 2) |
| `max_images` | 生成する画像の最大数。1 の場合は正確に 1 枚の画像が生成されます。1 より大きい場合は、モデルは 1 枚から max_images 枚までの関連画像（例: ストーリーシーン、キャラクターのバリエーション）を生成します。画像の合計（入力 + 生成）は 15 を超えることはできません。デフォルト: 1。 | INT | いいえ | 1 to 10 |
| `fail_on_partial` | 有効にすると、要求された画像のいずれかが欠落している場合やエラーが返された場合に実行を中止します。デフォルト: false。 | BOOLEAN | いいえ | true / false |
| `seed` | 生成に使用するシード。デフォルト: 42。 | INT | いいえ | 0 to 2147483647 |
| `watermark` | 画像に「AI生成」の透かしを追加するかどうか。デフォルト: false。 | BOOLEAN | いいえ | true / false |
| `thinking` | モデルのプロンプト最適化推論（'thinking'）を有効にして、プロンプトへの適合性を高めます。生成時間が大幅に増加する可能性があります（特に Seedream 5.0 Pro）。テキストから画像を生成する場合にのみ無効にできます（参照画像が提供されている場合は無効にできません）。デフォルト: true。 | BOOLEAN | いいえ | true / false |

### 参照入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `images` | 拡張可能スロット: 画像間変換（image-to-image）または複数参照生成用のオプションの参照画像。1..N 枚の画像を接続します（例: `image_1`、`image_2`、...）。枚数の上限はモデルごとに異なります（下記の注記を参照）。接続した画像が画像のバッチを含む場合、そのバッチ内のすべての画像が上限にカウントされます。 | IMAGE | いいえ | 0 to 10 (Seedream 5.0 Pro, Seedream 4.5, Seedream 4.0)<br>0 to 14 (Seedream 5.0 Lite) |

**注記:**

- `prompt` は、前後の空白を除去した後も空であってはなりません。
- 参照画像の最大数: Seedream 5.0 Pro、Seedream 4.5、Seedream 4.0 では 10、Seedream 5.0 Lite では 14。
- 各参照画像のアスペクト比は 1:3 から 3:1 の間である必要があります。
- `max_images` が 1 より大きい場合（Seedream 5.0 Pro では使用不可）、参照画像と生成画像の合計は 15 を超えることはできません。
- `thinking` は、テキストから画像を生成する場合にのみ無効にできます。参照画像が提供されている場合、`thinking` は有効である必要があります。
- `width` と `height` は、`size_preset` が "Custom" に設定されている場合にのみ使用されます。
- `prompt_optimization` は Seedream 5.0 Pro でのみ使用できます。
- `max_images` と `fail_on_partial` は Seedream 5.0 Lite、Seedream 4.5、Seedream 4.0 でのみ使用できます。Seedream 5.0 Pro は常に単一の画像を要求します。
- 解像度の要件（幅 × 高さ）:
  - Seedream 5.0 Pro: 0.92MP（921,600 ピクセル）から 4.19MP（4,194,304 ピクセル）の間。
  - Seedream 5.0 Lite と Seedream 4.5: 最低 3.68MP（3,686,400 ピクセル）。
  - Seedream 4.0: 最低 0.92MP（921,600 ピクセル）。
  - Pro 以外のすべてのモデル: 最大 16.78MP（16,777,216 ピクセル）。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `image` | 生成された画像テンソル。複数の画像が生成された場合、単一のバッチ化された IMAGE テンソルに連結されます。 | IMAGE |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/ja.md)

---
**Source fingerprint (SHA-256):** `68dd23afdb5720491cef784b22ad66ff0baf80984ea652ea4c13e6c264c029ac`
