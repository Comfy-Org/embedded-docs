# ByteDance Seedance 2.5 Draft to Final Video

このノードは、Seedance 2.5 Draft の 1080p 最終動画をレンダリングします。ドラフトは高速な 480p プレビューです。Seedance 2.5 の動画ノード（テキストから動画、先頭・最終フレームから動画、参照から動画）で `model` を `Seedance 2.5 Draft` に設定して実行し、その `draft_task_id` 出力をここに接続します。最終版はドラフトのシーンと動きを維持し、ドラフトを生成したプロンプト、参照、継続時間、アスペクト比、音声設定を再利用します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `draft_task_id` | Seedance 2.5 Draft モデルで実行した Seedance 2.5 ノードの `draft_task_id` 出力、または貼り付けたドラフトタスク ID です。そのノードのシード制御を固定に設定してください。そうしないと、次回の実行で、確認したドラフトを再利用するのではなく、新しいドラフトが生成されます。 | STRING | はい | - |
| `watermark` | 動画にウォーターマークを追加するかどうか。デフォルトは False です。これは詳細設定です。 | BOOLEAN | いいえ | True / False |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `video` | レンダリングされた 1080p の最終動画です。レンダリングタスクが完了すると、プロバイダーからダウンロードされます。 | VIDEO |

**注意:** ドラフトは作成後 7 日間レンダリングできます。ドラフトタスク ID はドラフトを単独で識別するため、プロンプト、参照、継続時間、アスペクト比、音声設定を再度渡す必要はありません。

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/ja.md)

---
**Source fingerprint (SHA-256):** `c9a607826915f09ec199748964010a00a239b5efab3647a3b97fdceee6b04cde`
