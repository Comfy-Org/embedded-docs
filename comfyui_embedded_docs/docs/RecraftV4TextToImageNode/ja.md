# Recraft V4 テキストから画像生成

このノードは、Recraft V4 および V4.1 AI モデルを使用して、テキスト記述から画像を生成します。プロンプトと生成設定を Recraft 画像生成サービスに送信し、生成された画像（複数可）を返します。モデル、画像サイズ、生成枚数を選択できます。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | 生成に使用するモデル。モデルを選択すると、利用可能な `size` オプションが決まります。 | DYNAMIC_COMBO | Yes | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | 画像生成用のプロンプト。最大10,000文字です。 | STRING | Yes | 1〜10000文字 |
| `negative_prompt` | この入力は無視されます。Recraft V4 および V4.1 モデルではネガティブプロンプトはサポートされていません。 | STRING | Yes | N/A |
| `n` | 生成する画像の数（デフォルト: 1）。 | INT | Yes | 1〜6 |
| `seed` | ノードを再実行するかどうかを決定するシード。実際の結果はシードに関係なく非決定論的です（デフォルト: 0）。 | INT | Yes | 0〜18446744073709551615 |
| `recraft_controls` | Recraft Controls ノードによる生成のオプションの追加コントロール。 | CUSTOM | No | N/A |

### recraftv4_1、recraftv4_1_utility、および recraftv4 入力

`recraftv4_1`、`recraftv4_1_utility`、`recraftv4` モデルで共有されます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成される画像のサイズ（デフォルト: 1024x1024）。 | COMBO | Yes | 利用可能な複数のオプション（標準の Recraft V4 サイズ） |

### recraftv4_1_pro、recraftv4_1_utility_pro、および recraftv4_pro 入力

`recraftv4_1_pro`、`recraftv4_1_utility_pro`、`recraftv4_pro` モデルで共有されます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成される画像のサイズ（デフォルト: 2048x2048）。 | COMBO | Yes | 利用可能な複数のオプション（Pro の Recraft V4 サイズ） |

**注記：**

- `size` 入力はモデルを選択すると表示され、利用可能なオプションはモデルによって異なります。標準モデル（`recraftv4_1`、`recraftv4_1_utility`、`recraftv4`）は同じサイズセットを共有し、Pro モデル（`recraftv4_1_pro`、`recraftv4_1_utility_pro`、`recraftv4_pro`）は別のサイズセットを共有します。
- `negative_prompt` 入力は UI に表示されますが、モデルには送信されません。Recraft V4 および V4.1 モデルではネガティブプロンプトはサポートされていません。
- `seed` の値は、値が変更されたときにノードが再実行されるかどうかを決定するだけです。実際の画像結果はシードに関係なく非決定論的です。
- Recraft Controls 入力を通じて Infinite Style Library のスタイル ID を使用する場合は、それが Vector アートスタイルではないことを確認してください。画像の代わりに SVG データが返される可能性があります。

## 出力

| 出力名 | 説明 | データ型 |
|--------|-------------|-----------|
| `output` | 生成された画像、または画像のバッチ。 | IMAGE |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/ja.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
