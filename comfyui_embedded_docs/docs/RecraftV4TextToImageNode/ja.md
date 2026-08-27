# Recraft V4 テキストから画像生成

このノードは、Recraft V4 および V4.1 AI モデルを使用して、テキスト記述から画像を生成します。プロンプトを外部APIに送信し、生成された画像を返します。モデル、画像サイズ、生成する画像の数を指定することで、出力を制御できます。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | 生成に使用するモデルです。 | DYNAMIC_COMBO | はい | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | 画像生成のためのプロンプトです。最大10,000文字です。 | STRING | はい | N/A |
| `negative_prompt` | この入力は無視されます。ネガティブプロンプトは Recraft V4 および V4.1 モデルではサポートされていません。 | STRING | はい | N/A |
| `n` | 生成する画像の数です（デフォルト: 1）。 | INT | はい | 1〜6 |
| `seed` | ノードを再実行するかどうかを決定するためのシードです。実際の結果はシードに関係なく非決定的です（デフォルト: 0）。 | INT | はい | 0〜18446744073709551615 |
| `recraft_controls` | Recraft Controls ノードを使用した、生成に関する任意の追加コントロールです。 | CUSTOM | いいえ | N/A |

### recraftv4_1、recraftv4_1_utility、recraftv4 入力

`recraftv4_1`、`recraftv4_1_utility`、`recraftv4` で共有されます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成される画像のサイズです（デフォルト: "1024x1024"）。 | COMBO | はい | 複数のオプションが利用可能（標準の Recraft V4 サイズ、"1024x1024" を含む） |

### recraftv4_1_pro、recraftv4_1_utility_pro、recraftv4_pro 入力

`recraftv4_1_pro`、`recraftv4_1_utility_pro`、`recraftv4_pro` で共有されます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成される画像のサイズです（デフォルト: "2048x2048"）。 | COMBO | はい | 複数のオプションが利用可能（Pro の Recraft V4 サイズ、"2048x2048" を含む） |

**注記:** `size` パラメータは動的な入力であり、利用可能なオプションは選択した `model` に応じて変わります。`seed` の値は再現可能な画像出力を保証するものではありません。Infinite Style Library のスタイル ID を使用する場合は、それが Vector アートスタイルでないことを確認してください。Vector アートスタイルの場合、画像の代わりに SVG データが返される可能性があります。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `output` | 生成された画像、または画像のバッチです。 | IMAGE |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/ja.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
