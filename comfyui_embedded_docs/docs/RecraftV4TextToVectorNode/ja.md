# Recraft V4 テキストからベクター生成

以下に、翻訳したドキュメントを示します。

---

Recraft V4 Text to Vector ノードは、テキストの説明から Scalable Vector Graphics（SVG）イラストを生成します。Recraft API に接続し、Recraft V4 および V4.1 モデルを使用して画像を生成し、プロンプトに基づいて 1 つ以上の SVG ファイルを出力します。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | 生成に使用するモデル。モデルを選択すると、利用可能な `size` オプションが変わります。 | DYNAMIC_COMBO | はい | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | 画像生成のためのプロンプト。最大 10,000 文字。 | STRING | はい | N/A |
| `negative_prompt` | この入力は無視されます。Recraft V4 および V4.1 モデルはネガティブプロンプトをサポートしていません。 | STRING | はい | N/A |
| `n` | 生成する画像の数（デフォルト: 1）。 | INT | はい | 1〜6 |
| `seed` | ノードを再実行するかどうかを決定するシード。実際の結果はシードに関係なく非決定的です（デフォルト: 0）。 | INT | はい | 0〜18446744073709551615 |
| `recraft_controls` | Recraft Controls ノードによる生成の追加オプションの制御。 | CUSTOM | いいえ | N/A |

### recraftv4_1_vector、recraftv4_1_utility_vector、および recraftv4 入力

これらのモデルは同じ `size` オプションを共有します。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成される画像のサイズ。デフォルトは `"1024x1024"` です。 | COMBO | はい | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### recraftv4_1_pro_vector、recraftv4_1_utility_pro_vector、および recraftv4_pro 入力

これらのモデルは同じ `size` オプションを共有します。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成される画像のサイズ。デフォルトは `"2048x2048"` です。 | COMBO | はい | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

**注:** `size` パラメータは動的入力であり、利用可能なオプションは選択した `model` によって変わります。`seed` の値によって、外部 API からの再現可能な結果が保証されるわけではありません。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `output` | 生成された Scalable Vector Graphics（SVG）画像。 | SVG |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/ja.md)

---
**Source fingerprint (SHA-256):** `822f6b9fef67ef6beb1eba099c41c72570a1f79e316612201c81f6e5eb91408d`
