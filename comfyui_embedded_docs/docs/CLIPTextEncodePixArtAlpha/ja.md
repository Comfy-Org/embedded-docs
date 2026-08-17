# CLIPTextEncodePixArtAlpha

テキストをエンコードし、PixArt Alpha の解像度条件付けを設定します。このノードはテキスト入力を処理し、幅と高さの情報を追加して、PixArt Alpha モデル専用の条件付けデータを生成します。PixArt Sigma モデルには適用されません。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `width` | 解像度条件付けの幅の寸法（デフォルト: 1024） | INT | はい | 0 to MAX_RESOLUTION |
| `height` | 解像度条件付けの高さの寸法（デフォルト: 1024） | INT | はい | 0 to MAX_RESOLUTION |
| `text` | エンコードされるテキスト入力。複数行入力と動的プロンプトに対応しています | STRING | はい | - |
| `clip` | トークン化とエンコードに使用されるCLIPモデル | CLIP | はい | - |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `CONDITIONING` | テキストトークンと解像度情報を含む、エンコード済み条件付けデータ | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/ja.md)

---
**Source fingerprint (SHA-256):** `d25a4117d39e3528cd0f64bc34462cd7b4076c67cb4e454c77fcc66490f89be6`
