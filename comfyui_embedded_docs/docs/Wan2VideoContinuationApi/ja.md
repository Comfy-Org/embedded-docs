# Wan 2.7 ビデオ継続生成

Wan 2.7 Video Continuation ノードは、入力ビデオクリップの終端から継続する新しいビデオセグメントを生成します。Wan 2.7 モデルを使用してテキストプロンプトに基づいて継続部分を合成し、オプションで終端を特定のターゲットフレームへ誘導することもできます。

## 入力

### 共通入力

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | 使用するビデオ生成モデル。 | DYNAMIC_COMBO | はい | `"wan2.7-i2v"` |
| `first_clip` | 継続元となる入力ビデオ。長さ: 2秒〜10秒。出力のアスペクト比はこのビデオから取得されます。 | VIDEO | はい | 2秒〜10秒 |
| `last_frame` | 最後のフレーム画像。継続部分はこのフレームに向かって遷移します。 | IMAGE | いいえ | - |
| `seed` | 生成に使用するシード値。(デフォルト: 0) | INT | はい | 0 〜 2147483647 |
| `prompt_extend` | AI支援でプロンプトを拡張するかどうか。(デフォルト: True) | BOOLEAN | はい | - |
| `watermark` | 結果にAI生成ウォーターマークを追加するかどうか。(デフォルト: False) | BOOLEAN | はい | - |

### wan2.7-i2v 入力

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model.prompt` | 要素と視覚的特徴を説明するプロンプト。英語と中国語に対応しています。(デフォルト: 空文字列) | STRING | はい | - |
| `model.negative_prompt` | 避けるべき内容を説明するネガティブプロンプト。(デフォルト: 空文字列) | STRING | はい | - |
| `model.resolution` | 出力ビデオの解像度。 | COMBO | はい | `"720P"`<br>`"1080P"` |
| `model.duration` | 出力全体の長さ（秒）。モデルは、入力クリップ後の残り時間を埋める継続部分を生成します。(デフォルト: 5) | INT | はい | 2 〜 15 |

**注:** 入力ビデオ `first_clip` の長さは2秒から10秒の間である必要があります。

## 出力

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | 生成されたビデオの継続部分。 | VIDEO |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/ja.md)

---
**Source fingerprint (SHA-256):** `591e551676969bc1fedb5f820f6866512c132bb98ee8ef1766d1e0b389e2dc11`
