# スプラットのプレビュー

`PreviewGaussianSplat` ノードを使用すると、3Dガウシアンスプラットファイルを出力ディレクトリに保存することなく、ComfyUI インターフェース上で直接プレビューできます。ファイルは一時フォルダに一時的に保存され、3Dプレビューウィンドウに表示されます。また、モデルデータ、カメラ情報、プレビューサイズは他のノードにそのまま渡されます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | ガウシアンスプラットの3Dファイル。 | FILE3D | はい | splat, ply, spz, ksplat |
| `model_3d_info` | 3Dモデルに関するオプションのメタデータ情報。 | LOAD3DMODELINFO | いいえ | - |
| `viewport_state` | カメラおよびモデル情報を含む、3Dビューポートの現在の状態。 | LOAD3D | はい | - |
| `camera_info` | プレビュー用のオプションのカメラ情報。 | LOAD3DCAMERA | いいえ | - |
| `width` | プレビューレンダリングの幅（ピクセル単位、デフォルト: 1024）。 | INT | はい | 1 から 4096 |
| `height` | プレビューレンダリングの高さ（ピクセル単位、デフォルト: 1024）。 | INT | はい | 1 から 4096 |

注：`camera_info` または `model_3d_info` が指定されていない場合、ノードは代わりに `viewport_state` の対応する値を使用します。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `model_3d` | 入力された3Dガウシアンスプラットファイルを、変更せずにそのまま渡します。 | FILE3D |
| `model_3d_info` | 入力またはビューポート状態のいずれかからの、3Dモデルに関するメタデータ情報。 | LOAD3DMODELINFO |
| `camera_info` | 入力またはビューポート状態のいずれかからの、プレビュー用のカメラ情報。 | LOAD3DCAMERA |
| `width` | プレビューレンダリングの幅。 | INT |
| `height` | プレビューレンダリングの高さ。 | INT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/ja.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
