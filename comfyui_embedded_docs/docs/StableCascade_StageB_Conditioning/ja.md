# 安定カスケード_ステージB条件付け

StableCascade_StageB_Conditioning ノードは、既存のコンディショニング情報とステージ C の事前潜在表現を組み合わせることで、Stable Cascade ステージ B 生成用のコンディショニングデータを準備します。各コンディショニングエントリにステージ C の潜在サンプルが含まれるように変更し、生成プロセスが事前情報を活用して、より一貫性のある出力を生成できるようにします。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `conditioning` | ステージ C の事前情報で変更されるコンディショニングデータです。 | CONDITIONING | はい | - |
| `stage_c` | コンディショニング用の事前サンプルを含む、ステージ C からの潜在表現です。 | LATENT | はい | - |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `CONDITIONING` | ステージ C の事前情報が統合された、変更済みのコンディショニングデータです。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/ja.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
