# MiniMax Hailuo 動画

MiniMax Hailuo-02 モデルを使用して、テキストプロンプトから動画を生成します。オプションで、開始画像を最初のフレームとして提供すると、その画像から続く動画を作成できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `prompt_text` | 動画生成を導くテキストプロンプト。 | STRING | はい | - |
| `seed` | ノイズ生成に使用されるランダムシード（デフォルト: 0）。 | INT | いいえ | 0 to 18446744073709551615 |
| `first_frame_image` | 動画生成の最初のフレームとして使用するオプションの画像。 | IMAGE | いいえ | - |
| `prompt_optimizer` | 必要に応じてプロンプトを最適化し、生成品質を向上させます（デフォルト: True）。 | BOOLEAN | いいえ | - |
| `duration` | 出力動画の長さ（秒）（デフォルト: 6）。 | COMBO | いいえ | `6`<br>`10` |
| `resolution` | 動画表示の解像度。1080p は 1920x1080、768p は 1366x768（デフォルト: "768P"）。 | COMBO | いいえ | `"768P"`<br>`"1080P"` |

**注意事項:**
- `first_frame_image` が提供されていない場合、`prompt_text` は空でない文字列である必要があります。
- MiniMax-Hailuo-02 モデルを 1080P 解像度で使用する場合、動画の長さは 6 秒に制限されます。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `output` | 生成された動画ファイル。 | VIDEO |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/ja.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
