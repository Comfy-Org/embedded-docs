# Tripo: モデルのテクスチャリング

TripoTextureNode は、Tripo API を使用してテクスチャ付きの3Dモデルを生成します。モデルタスクIDを受け取り、PBRマテリアル、テクスチャ品質設定、アライメント方法、オプションのテキストガイダンスなど、さまざまなオプションでテクスチャ生成を適用します。ノードはTripo APIと通信してテクスチャ生成リクエストを処理し、結果のモデルファイルとタスクIDを返します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | テクスチャを適用するモデルのタスクID | MODEL_TASK_ID | はい | - |
| `texture` | テクスチャを生成するかどうか（デフォルト: True） | BOOLEAN | いいえ | - |
| `pbr` | PBR（フォトリアリスティックレンダリング）マテリアルを生成するかどうか（デフォルト: True） | BOOLEAN | いいえ | - |
| `texture_seed` | テクスチャ生成用のランダムシード（デフォルト: 42） | INT | いいえ | - |
| `texture_quality` | テクスチャ生成の品質レベル（デフォルト: "standard"）。"detailed" オプションは0.20米ドル、"standard" は0.10米ドルです。 | COMBO | いいえ | "standard"<br>"detailed" |
| `texture_alignment` | テクスチャの配置方法（デフォルト: "original_image"）。"original_image" は元の入力画像にテクスチャを合わせ、"geometry" は3Dジオメトリに合わせます。 | COMBO | いいえ | "original_image"<br>"geometry" |
| `texture_prompt` | テクスチャリングのためのオプションのテキストガイダンス。インポートしたモデル（Tripo: Import Model）では実際には必須です。ソース画像がないため、色を推測できないからです。（複数行テキストボックス、デフォルト: 空文字列） | STRING | いいえ | - |

*注: このノードは、システムによって自動的に処理される認証トークンとAPIキーを必要とします。*

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `model_file` | 適用されたテクスチャ付きの生成済みモデルファイル（後方互換性のため） | STRING |
| `model task_id` | テクスチャ生成プロセスを追跡するためのタスクID | MODEL_TASK_ID |
| `GLB` | 適用されたテクスチャ付きのGLB形式の生成済み3Dモデル | FILE3DGLB |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/ja.md)

---
**Source fingerprint (SHA-256):** `a0157b7fa2bb94d174ea5893d7389885180876794032a510642586e310ba30d4`
