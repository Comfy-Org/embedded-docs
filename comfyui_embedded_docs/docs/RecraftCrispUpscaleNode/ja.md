> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/ja.md)

画像を同期的にアップスケールします。「crisp upscale」ツールを使用して指定されたラスター画像を強化し、画像解像度を向上させ、画像をよりシャープでクリーンにします。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `画像` | IMAGE | はい | - | アップスケールする入力画像 |
| `auth_token` | STRING | いいえ | - | Recraft APIの認証トークン |
| `comfy_api_key` | STRING | いいえ | - | Comfy.orgサービスのAPIキー |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `画像` | IMAGE | 解像度と明瞭度が向上したアップスケール画像 |
