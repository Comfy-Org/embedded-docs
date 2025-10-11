> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/ja.md)

TripoRigNodeは、元のモデルのタスクIDからリギングされた3Dモデルを生成します。Tripo APIにリクエストを送信し、Tripo仕様を使用してGLB形式のアニメーションリグを作成し、リグ生成タスクが完了するまでAPIをポーリングします。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID | はい | - | リギング対象の元の3DモデルのタスクID |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | いいえ | - | Comfy.org APIアクセスのための認証トークン |
| `comfy_api_key` | API_KEY_COMFY_ORG | いいえ | - | Comfy.orgサービス認証のためのAPIキー |
| `unique_id` | UNIQUE_ID | いいえ | - | 操作を追跡するための一意の識別子 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 生成されたリギング済み3Dモデルファイル |
| `rig task_id` | RIG_TASK_ID | リグ生成プロセスを追跡するためのタスクID |