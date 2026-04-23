> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/ja.md)

以下が翻訳結果です。

## 概要

ByteDance Seedance 2.0 参照動画ノードは、Seedance 2.0 AIモデルを使用して、テキストプロンプトと提供された参照素材に基づき、動画の作成、編集、または延長を行います。画像、動画、音声を参照として使用して生成プロセスをガイドし、動画編集や延長などのタスクをサポートします。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | はい | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | 使用するAIモデル。Seedance 2.0は最高品質向け、Seedance 2.0 Fastは速度最適化向けです。モデルを選択すると、`prompt`、`resolution`、`duration`、`ratio`、`generate_audio`の必須入力と、`reference_images`、`reference_videos`、`reference_audios`、`reference_assets`、`auto_downscale`のオプション入力が追加で表示されます。 |
| `seed` | INT | いいえ | 0 ～ 2147483647 | ノードを再実行するかどうかを制御するための数値。シード値に関係なく結果は非決定的です（デフォルト：0）。 |
| `watermark` | BOOLEAN | いいえ | `True` / `False` | 生成された動画に透かしを追加するかどうか（デフォルト：False）。 |

**重要な制約事項：**
*   ノードを動作させるには、少なくとも1つの参照画像または動画（`reference_images`、`reference_videos`、または`reference_assets`入力で提供）が必要です。
*   各参照動画は少なくとも1.8秒の長さが必要です。すべての参照動画の合計時間は15.1秒を超えてはなりません。
*   各参照音声クリップは少なくとも1.8秒の長さが必要です。すべての参照音声の合計時間は15.1秒を超えてはなりません。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `video` | VIDEO | 生成された動画ファイル。 |