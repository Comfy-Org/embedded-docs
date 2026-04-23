> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/ja.md)

このノードは、ByteDanceのSeedance 2.0モデルを使用して動画を生成します。テキストプロンプトと必須の最初のフレーム画像に基づいて動画を作成します。オプションで最後のフレーム画像を指定することで、動画シーケンスの終了をガイドできます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | はい | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | 動画生成に使用するモデルです。Seedance 2.0は最高品質を追求し、Seedance 2.0 Fastは速度を最適化しています。モデルを選択すると、`prompt`、`resolution`、`ratio`、`duration`、`generate_audio`の追加入力項目が表示されます。 |
| `first_frame` | IMAGE | いいえ | - | 動画の最初のフレームとして使用する画像です。 |
| `last_frame` | IMAGE | いいえ | - | 動画の最後のフレームとして使用する画像です。 |
| `first_frame_asset_id` | STRING | いいえ | - | 最初のフレームとして使用するSeedanceのasset_idです。`first_frame`画像入力と同時に使用することはできません。デフォルトは空の文字列です。 |
| `last_frame_asset_id` | STRING | いいえ | - | 最後のフレームとして使用するSeedanceのasset_idです。`last_frame`画像入力と同時に使用することはできません。デフォルトは空の文字列です。 |
| `seed` | INT | いいえ | 0～2147483647 | シード値です。このシードを変更するとノードが再実行されますが、結果は非決定的です。デフォルトは0です。 |
| `watermark` | BOOLEAN | いいえ | - | 生成された動画に透かしを追加するかどうかです。デフォルトはFalseです。 |

**パラメータの制約：**
*   `first_frame`画像**または**`first_frame_asset_id`の**いずれか**を指定する必要があります。両方を指定するとエラーが発生します。
*   同じフレームに対して`last_frame`画像と`last_frame_asset_id`の両方を指定することはできません。
*   `model`入力は動的なコンボボックスです。モデルを選択した後、表示された`prompt`フィールド（テキストによる説明）を入力し、その他の表示されたパラメータ（`resolution`、`ratio`、`duration`、`generate_audio`）を設定する必要があります。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成された動画です。 |