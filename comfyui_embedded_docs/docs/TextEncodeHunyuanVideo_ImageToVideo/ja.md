# TextEncodeHunyuanVideo_ImageToVideo

TextEncodeHunyuanVideo_ImageToVideo ノードは、テキストプロンプトと画像埋め込みを組み合わせて、動画生成用のコンディショニングデータを作成します。CLIPモデルを使用してテキスト入力とCLIPビジョン出力からの視覚情報の両方を処理し、指定された画像インターリーブ設定に従ってこれら2つのソースをブレンドしたトークンを生成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `clip` | トークン化とエンコーディングに使用されるCLIPモデル。 | CLIP | はい | - |
| `clip_vision_output` | 画像コンテキストを提供するCLIPビジョンモデルからの視覚的埋め込み。 | CLIP_VISION_OUTPUT | はい | - |
| `prompt` | 動画生成をガイドするテキストの説明。複数行の入力と動的プロンプトをサポートします。プロンプトは、参照画像に基づいて動画を説明するようモデルに求めるテンプレートを使用してフォーマットされ、主な内容、オブジェクトの詳細、アクション、背景、カメラアングルなどの側面をカバーします。 | STRING | はい | - |
| `image_interleave` | テキストプロンプトに対する画像の影響の度合い。数値が大きいほどテキストプロンプトの影響が強くなります。（デフォルト: 2、高度なパラメータ） | INT | はい | 1-512 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `CONDITIONING` | テキストと画像情報を組み合わせて動画生成を行うためのコンディショニングデータ。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/ja.md)

---
**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`
