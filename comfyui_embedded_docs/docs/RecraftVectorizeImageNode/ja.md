> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/ja.md)

入力画像からSVGを同期的に生成します。このノードはラスター画像をベクターグラフィックス形式に変換し、入力バッチ内の各画像を処理して結果を単一のSVG出力に結合します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `画像` | IMAGE | はい | - | SVG形式に変換する入力画像 |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | いいえ | - | APIアクセスのための認証トークン |
| `comfy_api_key` | API_KEY_COMFY_ORG | いいえ | - | Comfy.orgサービスのためのAPIキー |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `SVG` | SVG | 処理されたすべての画像を結合した生成ベクターグラフィックス出力 |
