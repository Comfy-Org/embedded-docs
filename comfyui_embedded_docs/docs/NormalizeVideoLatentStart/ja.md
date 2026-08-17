# NormalizeVideoLatentStart

このノードは、ビデオ潜在表現の最初の数フレームを調整し、後続のフレームにより近づけます。後続の基準フレーム群から平均とばらつきを計算し、それらの特性を開始フレームに適用します。これにより、ビデオの冒頭でより滑らかで一貫性のある視覚的遷移が生まれます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `latent` | 処理するビデオ潜在表現。 | LATENT | はい | - |
| `start_frame_count` | 先頭から数えた正規化する潜在フレーム数（デフォルト: 4）。 | INT | はい | 1 to 16384 (max resolution) |
| `reference_frame_count` | 開始フレームの後に基準として使用する潜在フレーム数（デフォルト: 5）。 | INT | はい | 1 to 16384 (max resolution) |

**注:** `reference_frame_count` は、開始フレームの後に利用可能なフレーム数を超えないよう自動的に制限されます。ビデオ潜在表現がわずか1フレームしかない場合、正規化は実行されず、元の潜在表現がそのまま返されます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `latent` | 開始フレームが正規化された処理済みのビデオ潜在表現。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/ja.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
