# Kling 開始-終了フレームから動画生成

このノードは、指定された開始画像と終了画像の間を遷移するビデオシーケンスを作成します。最初のフレームから最後のフレームへの滑らかな変形を生成するため、間のすべてのフレームを生成します。このノードは image-to-video API を呼び出しますが、`image_tail` リクエストフィールドで動作する入力オプションのみをサポートしています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | 参照画像 - URL または Base64 エンコード文字列。10MB を超えることはできません。解像度は 300*300px 以上。アスペクト比は 1:2.5 ~ 2.5:1 の間。Base64 には data:image プレフィックスを含めないでください。 | IMAGE | はい | - |
| `end_frame` | 参照画像 - 終了フレーム制御。URL または Base64 エンコード文字列。10MB を超えることはできません。解像度は 300*300px 以上。Base64 には data:image プレフィックスを含めないでください。 | IMAGE | はい | - |
| `prompt` | ポジティブテキストプロンプト | STRING | はい | - |
| `negative_prompt` | ネガティブテキストプロンプト | STRING | はい | - |
| `cfg_scale` | プロンプトガイダンスの強さを制御します（デフォルト: 0.5） | FLOAT | いいえ | 0.0-1.0 |
| `aspect_ratio` | 生成されるビデオのアスペクト比（デフォルト: "16:9"） | COMBO | いいえ | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | ビデオ生成に使用する設定。形式は mode / duration / model_name に従います。（デフォルト: "pro mode / 5s duration / kling-v2-5-turbo"）。利用可能なすべてのオプションは pro mode と kling-v2-5-turbo モデルを使用し、ビデオの長さのみが異なります。 | COMBO | いいえ | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**画像の制約:**

- `start_frame` と `end_frame` の両方を指定する必要があり、ファイルサイズは 10MB を超えることはできません。
- 最小解像度: 両画像とも 300×300 ピクセル。
- `start_frame` のアスペクト比は 1:2.5 から 2.5:1 の間でなければなりません。
- Base64 エンコードされた画像には "data:image" プレフィックスを含めないでください。

**プロンプトの制約:**

- ポジティブプロンプトは空にすることはできません。
- ポジティブおよびネガティブプロンプトはどちらも 500 文字に制限されています。
- `negative_prompt` が空のままの場合、リクエストから省略されます。

**料金:**

- "pro mode / 5s duration / kling-v2-5-turbo": 生成あたり $0.35 USD
- "pro mode / 10s duration / kling-v2-5-turbo": 生成あたり $0.70 USD

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `output` | 生成されたビデオシーケンス | VIDEO |
| `video_id` | 生成されたビデオの一意の識別子 | STRING |
| `duration` | 生成されたビデオの長さ | STRING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/ja.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
