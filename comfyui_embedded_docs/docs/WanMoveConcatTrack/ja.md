# WanMoveConcatTrack

WanMoveConcatTrack ノードは、2つのモーショントラッキングデータセットを1つの長いシーケンスに結合します。これは、入力トラックからのトラックパスと可視性マスクを、それぞれの次元に沿って結合することで機能します。トラック入力が1つだけ提供された場合、そのデータを変更せずにそのまま出力に渡します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `tracks_1` | 結合する最初のモーショントラッキングデータセット。 | TRACKS | はい |  |
| `tracks_2` | オプションの2番目のモーショントラッキングデータセット。提供されない場合、`tracks_1` がそのまま出力に渡されます。 | TRACKS | いいえ |  |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `tracks` | 結合されたモーショントラッキングデータ。入力からの `track_path` と `track_visibility` を結合したものを含みます。 | TRACKS |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/ja.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`
