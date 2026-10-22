# Text Encode MOSS-Image Edit

MOSS-Image 編集 LoRA 用のコンディショニングへ、編集指示と参照画像をまとめてエンコードします。出力をポジティブコンディショニングとして接続し、同じ参照を使って 2 つ目のインスタンスを実行してネガティブ側にしてください。参照は届いたサイズのまま使用されるため、接続前にスケーリングしてください。このノードは ComfyUI で実験的としてマークされています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `clip` | 指示をトークン化してエンコードする CLIP モデルです。 | CLIP | はい | - |
| `prompt` | 編集内容を記述する指示です。複数行テキストと動的プロンプトをサポートします。 | STRING | はい | 任意のテキスト |
| `vae` | 参照画像を参照 Latent にエンコードするために使用する VAE です。 | VAE | はい | - |
| `edit_format` | 編集 LoRA の学習に使用されたレイアウトです。参照 Latent の方式と、テキストエンコーダーが参照も見るかどうかを選択します。 | COMBO | はい | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | 拡張可能なスロット: 1 つ以上の参照画像（`image_1`、`image_2`、...）を接続します。各画像は届いたサイズのまま使用され、アルファチャンネルが削除され、VAE によって参照 Latent にエンコードされます。 | IMAGE | はい | 1 枚以上の画像 |

**注:** `"ai-toolkit"` と `"ai-toolkit (kv_cache off)"` では、テキストエンコーダーもすべての参照を参照します。各参照は最大 384x384 ピクセルに縮小され、プロンプト内で `Picture N:` マーカーが前に付けられるため、指示から番号で参照できます。`"Moss-Image-Edit"` では、参照は参照 Latent としてのみモデルに渡され、テキストエンコーダーは指示だけを参照します。さらに `"ai-toolkit (kv_cache off)"` は、参照が生成中の画像にアテンションし続けるように保持するため、各サンプリングステップで再計算されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `conditioning` | エンコードされた指示に、参照 Latent と対応する参照 Latent 方式が付加されたもの。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/ja.md)

---
**Source fingerprint (SHA-256):** `30e4edbb129f647cdce4ec95f78c002ecdc9a4f8fc5a45f1477fdc555b541dae`
