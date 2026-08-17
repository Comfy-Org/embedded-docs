# ReferenceTimbreAudio

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `conditioning` | 参照オーディオ情報が添付されるコンディショニングデータです。 | CONDITIONING | はい |  |
| `latent` | 参照オーディオのオプションの潜在表現です。指定すると、そのサンプルがコンディショニングに追加されます。 | LATENT | いいえ |  |

`latent` が指定された場合、そのサンプルはコンディショニングの参照オーディオ音色潜在変数に追加されます。`latent` が指定されない場合は、元のコンディショニングが変更されずにそのまま渡されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `conditioning` | 変更されたコンディショニングデータです。オプションの `latent` 入力が指定された場合、参照オーディオの音色潜在変数が含まれます。`latent` が指定されない場合は、元のコンディショニングが変更されずにそのまま返されます。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/ja.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
