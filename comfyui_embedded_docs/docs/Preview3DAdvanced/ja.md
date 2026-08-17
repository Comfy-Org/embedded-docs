# 3Dプレビュー（詳細）

このノードは、カメラ情報とモデル情報の出力を備えた高度な3Dモデルプレビューを提供します。ComfyUIの出力ディレクトリに保存せずに3Dモデルファイルをプレビューし、モデルを一時ファイルに書き込んでUIに表示します。モデルデータ、モデル情報、カメラ情報、ビューポート寸法も下流の処理のためにそのまま渡されます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 上流の3Dノードからの3Dモデルファイルです。 | FILE3D | はい | GLB, GLTF, FBX, OBJ, STL, USDZ, or any supported 3D format |
| `model_3d_info` | オプションのモデル情報メタデータです。 | LOAD3DMODELINFO | いいえ | - |
| `viewport_state` | カメラとモデル情報を含む現在のビューポート状態です。 | LOAD3D | はい | - |
| `camera_info` | 3Dビュー用のオプションのカメラ設定です。 | LOAD3DCAMERA | いいえ | - |
| `width` | プレビューの幅（ピクセル単位）です。 | INT | はい | 1 to 4096 (default: 1024) |
| `height` | プレビューの高さ（ピクセル単位）です。 | INT | はい | 1 to 4096 (default: 1024) |

注：`camera_info`が接続されていない場合、ノードは`viewport_state`から`camera_info`の値を使用します。`model_3d_info`が接続されていない場合、ノードは`viewport_state`から`model_3d_info`の値を使用します。ビューポート状態にそれが含まれていない場合は、空のリストを使用します。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `model_3d` | 入力からそのまま渡される3Dモデルファイルです。 | FILE3D |
| `model_3d_info` | 入力またはビューポート状態からのモデル情報メタデータです。 | LOAD3DMODELINFO |
| `camera_info` | 入力またはビューポート状態からのカメラ設定です。 | LOAD3DCAMERA |
| `width` | プレビューの幅（ピクセル単位）です。 | INT |
| `height` | プレビューの高さ（ピクセル単位）です。 | INT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/ja.md)

---
**Source fingerprint (SHA-256):** `eda8c8fdd6ce7c39caf00c3054fc58e6dcab124fc3774d17af2deae651fbbf2e`
