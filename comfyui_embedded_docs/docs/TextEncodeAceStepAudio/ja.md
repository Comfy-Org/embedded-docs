# TextEncodeAceStepAudio

TextEncodeAceStepAudio ノードは、タグと歌詞をトークンに結合し、調整可能な歌詞強度でエンコードすることで、オーディオ条件付け用のテキスト入力を処理します。CLIP モデルとテキスト記述、歌詞を受け取り、それらをまとめてトークン化し、オーディオ生成タスクに適した条件付けデータを生成します。このノードでは、歌詞の影響を最終出力に反映させる強度パラメータを通じて、歌詞の影響を微調整できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `clip` | トークン化とエンコードに使用される CLIP モデル | CLIP | はい | - |
| `tags` | オーディオ条件付け用のテキストタグまたは説明（複数行入力と動的プロンプトに対応） | STRING | はい | - |
| `lyrics` | オーディオ条件付け用の歌詞テキスト（複数行入力と動的プロンプトに対応） | STRING | はい | - |
| `lyrics_strength` | 条件付け出力に対する歌詞の影響の強さを制御します（デフォルト: 1.0、ステップ: 0.01） | FLOAT | いいえ | 0.0 - 10.0 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `conditioning` | 処理されたテキストトークンと適用された歌詞強度を含むエンコード済み条件付けデータ | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/ja.md)

---
**Source fingerprint (SHA-256):** `2226c9f25dd26bf454bcce2e298d6d261dace5a9bbed164a2fcf0e1204d7c3f4`
