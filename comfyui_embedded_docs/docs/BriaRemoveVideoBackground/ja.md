# Bria 動画背景除去

このノードは、Bria AI サービスを使用して動画から背景を削除します。入力動画を処理し、元の背景を選択した単色に置き換えます。この操作は外部 API を介して実行され、結果は新しい動画ファイルとして返されます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `video` | 背景が削除される入力動画ファイル。 | VIDEO | はい | N/A |
| `background_color` | 出力動画の背景色。 | COMBO | はい | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `seed` | シードは、ノードを再実行するかどうかを制御します。シードに関係なく、結果は非決定的です。（デフォルト：0） | INT | はい | 0 から 2147483647 |

**注記：** 入力動画の長さは60秒以内である必要があります。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `output` | 背景が削除され、選択した色に置き換えられた処理済み動画ファイル。出力動画は H.264 の MP4 としてエンコードされます。 | VIDEO |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/ja.md)

---
**Source fingerprint (SHA-256):** `dbd6b7393f893be5a40322fc96b90bb3d5f1818bdda7b8109b28f48baac44d59`
