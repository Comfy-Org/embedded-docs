> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/ja.md)

Rodin3D_Gen2ノードは、Rodin APIを使用して3Dアセットを生成します。入力画像を受け取り、様々なマテリアルタイプとポリゴン数で3Dモデルに変換します。このノードは、タスクの作成、ステータスのポーリング、ファイルのダウンロードを含む生成プロセス全体を自動的に処理します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | はい | - | 3Dモデル生成に使用する入力画像 |
| `Seed` | INT | いいえ | 0-65535 | 生成用のランダムシード値（デフォルト: 0） |
| `Material_Type` | COMBO | いいえ | "PBR"<br>"Shaded" | 3Dモデルに適用するマテリアルのタイプ（デフォルト: "PBR"） |
| `Polygon_count` | COMBO | いいえ | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" | 生成される3Dモデルの目標ポリゴン数（デフォルト: "500K-Triangle"） |
| `TAPose` | BOOLEAN | いいえ | - | TAPose処理を適用するかどうか（デフォルト: False） |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | 生成された3Dモデルのファイルパス |
