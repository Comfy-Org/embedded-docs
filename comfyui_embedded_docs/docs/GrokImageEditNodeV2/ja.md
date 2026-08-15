# Grok Image Edit

テキストプロンプトに基づいて既存の画像を変更します。このノードは、画像とテキストによる説明をGrok APIに送信し、Grok APIが指示に従って画像を編集して結果を返します。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `モデル` | 使用するGrok画像モデル。下に表示されるサブパラメータは、選択したモデルによって異なります。 | MODEL | はい | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `プロンプト` | 画像の生成に使用するテキストプロンプト。（デフォルト: ""） | STRING | はい | N/A |
| `シード` | ノードを再実行するかどうかを決定するシード。実際の結果はシードに関係なく非決定的です。（デフォルト: 0） | INT | はい | 0〜2147483647 |

### grok-imagine-image-2.0 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `images` | 編集する参照画像。最大3枚まで。 | IMAGE | はい | 1〜3枚 |
| `resolution` | 編集後の画像の出力解像度。 | STRING | はい | "1K"<br>"2K" |
| `number_of_images` | 生成する編集後の画像の枚数。（デフォルト: 1） | INT | はい | 1〜10 |
| `quality` | 生成される画像の品質レベル。 | STRING | はい | "medium"<br>"low" |
| `aspect_ratio` | 編集後の画像のアスペクト比。（デフォルト: "auto"） | STRING | はい | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-quality と grok-imagine-image の入力

grok-imagine-image-quality と grok-imagine-image で共通です。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `images` | 編集する参照画像。最大3枚まで。 | IMAGE | はい | 1〜3枚 |
| `resolution` | 編集後の画像の出力解像度。 | STRING | はい | "1K"<br>"2K" |
| `number_of_images` | 生成する編集後の画像の枚数。（デフォルト: 1） | INT | はい | 1〜10 |
| `aspect_ratio` | 複数の画像が接続されている場合のみ許可されます。（デフォルト: "auto"） | STRING | はい | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-pro 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `images` | 編集する参照画像。 | IMAGE | はい | 1枚 |
| `resolution` | 編集後の画像の出力解像度。 | STRING | はい | "1K"<br>"2K" |
| `number_of_images` | 生成する編集後の画像の枚数。（デフォルト: 1） | INT | はい | 1〜10 |

### 参照入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `images` | 拡張可能スロット: 編集する参照画像を1枚以上接続します。`image_1`、`image_2`、`image_3` のような番号付きスロットを追加できます。最大画像数は選択したモデルに依存します（上記のモデルセクションを参照）。 | IMAGE | はい | モデルに応じて1〜3枚 |

**制約に関する注意:**

- `prompt` には空白以外の文字が少なくとも1文字含まれている必要があります。
- 編集には少なくとも1枚の参照画像が必要です。画像が接続されていない場合、ノードはエラーを発生させます。
- 入力画像の最大数は、`grok-imagine-image-pro` では1枚、`grok-imagine-image-2.0`、`grok-imagine-image-quality`、`grok-imagine-image` では3枚です。モデルがサポートする枚数より多く接続するとエラーが発生します。
- `grok-imagine-image-quality` と `grok-imagine-image` では、"auto" 以外のカスタム `aspect_ratio` は、複数の画像が接続されている場合にのみ許可されます。単一の画像の場合、`aspect_ratio` は "auto" である必要があります。
- `grok-imagine-image-2.0` では、単一の画像でも `aspect_ratio` を自由に設定できます。
- `quality` サブパラメータは、`grok-imagine-image-2.0` でのみ利用可能です。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `IMAGE` | Grok APIによって返された編集済み画像。単一の画像が生成された場合は、そのまま返されます。複数の画像が生成された場合は、単一のバッチテンソルに連結されます。 | IMAGE |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/ja.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
