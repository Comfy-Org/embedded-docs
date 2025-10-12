> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/ja.md)

TripoRetargetNodeは、事前定義されたアニメーションを3Dキャラクターモデルに適用するために、モーションデータのリターゲティングを行います。このノードは、以前に処理された3Dモデルを受け取り、いくつかのプリセットアニメーションのいずれかを適用して、アニメーション付きの3Dモデルファイルを出力として生成します。ノードはTripo APIと通信して、アニメーションリターゲティング操作を処理します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | RIG_TASK_ID | はい | - | アニメーションを適用する、以前に処理された3DモデルのタスクID |
| `animation` | STRING | はい | "preset:idle"<br>"preset:walk"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn" | 3Dモデルに適用するアニメーションプリセット |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | いいえ | - | Comfy.org APIアクセスのための認証トークン |
| `comfy_api_key` | API_KEY_COMFY_ORG | いいえ | - | Comfy.orgサービスアクセスのためのAPIキー |
| `unique_id` | UNIQUE_ID | いいえ | - | 操作を追跡するための一意の識別子 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成されたアニメーション付き3Dモデルファイル |
| `retarget task_id` | RETARGET_TASK_ID | リターゲティング操作を追跡するためのタスクID |
