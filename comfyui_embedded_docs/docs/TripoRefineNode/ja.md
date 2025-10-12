> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/ja.md)

TripoRefineNodeは、特にv1.4 Tripoモデルによって作成されたドラフト3Dモデルを精緻化します。モデルタスクIDを受け取り、Tripo APIを通じて処理することで、モデルの改良版を生成します。このノードは、Tripo v1.4モデルによって生成されたドラフトモデル専用に設計されています。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | はい | - | v1.4 Tripoモデルである必要があります |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | いいえ | - | Comfy.org APIの認証トークン |
| `comfy_api_key` | API_KEY_COMFY_ORG | いいえ | - | Comfy.orgサービスのAPIキー |
| `unique_id` | UNIQUE_ID | いいえ | - | 操作の一意識別子 |

**注意:** このノードはTripo v1.4モデルによって作成されたドラフトモデルのみを受け付けます。他のバージョンのモデルを使用するとエラーが発生する可能性があります。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `model_file` | STRING | 精緻化されたモデルへのファイルパスまたは参照 |
| `model task_id` | MODEL_TASK_ID | 精緻化されたモデル操作のタスク識別子 |
