> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/ja.md)

# Topaz Video Enhance V2

**Topaz Video Enhance V2** ノードを使用すると、Topaz Labs の AI モデルを活用して動画のアップスケールと画質向上が可能です。解像度の向上、フレーム補間によるフレームレートの調整、クリエイティブまたは写実的なエンハンスメントを適用することで、動画素材に新たな命を吹き込むことができます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | はい | - | 処理する入力動画です。MP4 コンテナ形式である必要があります。 |
| `upscaler_model` | COMBO | はい | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` | 動画のアップスケールに使用する AI モデルです。"Disabled" を選択すると、アップスケールは適用されません。 |
| `upscaler_model.upscaler_resolution` | COMBO | 条件付き | `"FullHD (1080p)"`<br>`"4K (2160p)"` | アップスケーラーの目標出力解像度です。このパラメータは、アップスケーラーモデルが選択されている場合（"Disabled" 以外）に必須となります。 |
| `upscaler_model.creativity` | FLOAT | 条件付き | 0.0 ～ 1.0（ステップ 0.1） | アップスケールのクリエイティブ強度です。"Astra 2" および "Starlight (Astra) Creative" モデルでのみ利用可能です。デフォルト値：Astra 2 は 0.5、Starlight Creative は "low"。 |
| `upscaler_model.prompt` | STRING | いいえ | - | オプションの説明的（指示的ではない）シーンプロンプトです。"Astra 2" モデルでのみ利用可能です。設定時は最大 500 入力フレーム（30fps で約 15 秒）に制限されます。デフォルト：空。 |
| `upscaler_model.sharp` | FLOAT | いいえ | 0.0 ～ 1.0（ステップ 0.01） | 事前エンハンスメントのシャープネスです。0.0=ガウスぼかし、0.5=パススルー（デフォルト）、1.0=USM シャープニングです。"Astra 2" モデルでのみ利用可能です。デフォルト：0.5。 |
| `upscaler_model.realism` | FLOAT | いいえ | 0.0 ～ 1.0（ステップ 0.01） | 出力を写真のようなリアリズムに引き寄せます。モデルのデフォルトを使用する場合は 0 のままにします。"Astra 2" モデルでのみ利用可能です。デフォルト：0.0。 |
| `interpolation_model` | COMBO | はい | `"Disabled"`<br>`"apo-8"` | フレーム補間に使用する AI モデルです。"Disabled" を選択すると、補間は適用されません。 |
| `interpolation_model.interpolation_frame_rate` | INT | 条件付き | 15 ～ 240 | 出力フレームレートです。補間モデルが "apo-8" の場合に必須です。デフォルト：60。 |
| `interpolation_model.interpolation_slowmo` | INT | いいえ | 1 ～ 16 | 入力動画に適用するスローモーション係数です。例えば、2 を設定すると出力の速度が半分になり、長さが 2 倍になります。デフォルト：1。 |
| `interpolation_model.interpolation_duplicate` | BOOLEAN | いいえ | True/False | 入力の重複フレームを分析して削除します。デフォルト：False。 |
| `interpolation_model.interpolation_duplicate_threshold` | FLOAT | いいえ | 0.001 ～ 0.1（ステップ 0.001） | 重複フレームの検出感度です。デフォルト：0.01。 |
| `dynamic_compression_level` | COMBO | いいえ | `"Low"`<br>`"Mid"`<br>`"High"` | 動画圧縮の CQP レベルです。デフォルト："Low"。 |

**重要な制約事項：**
- `upscaler_model` または `interpolation_model` の少なくとも一方が有効（"Disabled" 以外）である必要があります。そうでない場合はエラーが発生します。
- 入力動画は MP4 コンテナ形式である必要があります。
- プロンプト付きの "Astra 2" モデルは、最大 500 入力フレーム（30fps で約 15 秒）に制限されます。プロンプトがない場合は、より多くのフレームに制限されます。
- `upscaler_model` が "Disabled" 以外の場合、`upscaler_resolution` サブパラメータが必須です。
- `interpolation_model` が "Disabled" 以外の場合、`interpolation_frame_rate` サブパラメータが必須です。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `video` | VIDEO | 選択されたアップスケールおよび/または補間フィルターを適用した後の、画質が向上した動画出力です。 |