# MediaPipe Face Landmarker を読み込む

このノードは、MediaPipe Face Landmarker v2 モデルを読み込みます。このモデルは、画像内の顔や顔のランドマーク（目、鼻、口など）を検出できます。読み込まれたモデルには、近距離用と全範囲用の2つの検出バリアント（short および full）に加えて、共有メッシュデータ、ブレンドシェイプ、顔分析用のカノニカルジオメトリが含まれています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | `models/detection/` ディレクトリ内の顔検出モデル。 | COMBO | はい | `models/detection/` ディレクトリ内で利用可能なモデルのリスト |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `FACE_DETECTION_MODEL` | 読み込まれた MediaPipe Face Landmarker モデルのオブジェクト。short/full の2つの検出バリアント、共有メッシュおよびブレンドシェイプデータ、カノニカルジオメトリ、顔のトポロジー接続セット、GPU管理用のモデルパッチャーが含まれています。 | FACE_DETECTION_MODEL |

**注:** この出力は複雑なオブジェクトであり、顔検出やランドマーク抽出タスクのために他のノードで使用できます。これには2つの検出バリアントが含まれています。近距離検出用の「short」と、全範囲検出用の「full」です。

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/ja.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
