# ビデオスライス

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `video` | スライスする入力ビデオ。 | VIDEO | はい | - |
| `start_time` | 開始時間（秒）。デフォルトは 0.0。 | FLOAT | いいえ | -1e5〜1e5 |
| `duration` | 長さ（秒）。0 の場合は無制限（デフォルト: 0.0）。 | FLOAT | いいえ | 0.0 以上 |
| `strict_duration` | True の場合、指定した長さで切り取れないときにエラーが発生します（デフォルト: False）。 | BOOLEAN | いいえ | - |

注: `duration` が 0 の場合、ノードは `start_time` からビデオの終わりまでをスライスします。要求されたセグメントを作成できない場合（たとえば、`start_time` がビデオの終わりを超えている場合）、ノードはエラーを発生させます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `video` | 切り取られたビデオセグメント。 | VIDEO |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/ja.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
