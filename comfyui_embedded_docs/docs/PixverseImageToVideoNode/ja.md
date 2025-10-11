> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/ja.md)

入力画像とテキストプロンプトに基づいて動画を生成します。このノードは画像を受け取り、指定されたモーションと品質設定を適用して、静止画像を動画シーケンスに変換します。

## 入力パラメータ

| パラメータ名 | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | はい | - | 動画に変換する入力画像 |
| `prompt` | STRING | はい | - | 動画生成用のプロンプト |
| `quality` | COMBO | はい | `res_540p`<br>`res_1080p` | 動画品質設定（デフォルト: res_540p） |
| `duration_seconds` | COMBO | はい | `dur_2`<br>`dur_5`<br>`dur_10` | 生成動画の長さ（秒単位） |
| `motion_mode` | COMBO | はい | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` | 動画生成に適用されるモーションスタイル |
| `seed` | INT | はい | 0-2147483647 | 動画生成用のシード値（デフォルト: 0） |
| `negative_prompt` | STRING | いいえ | - | 画像上で望ましくない要素のオプションのテキスト記述 |
| `pixverse_template` | CUSTOM | いいえ | - | 生成スタイルに影響を与えるオプションのテンプレート（PixVerse Templateノードで作成） |

**注意:** 1080p品質を使用する場合、モーションモードは自動的にnormalに設定され、長さは5秒に制限されます。5秒以外の長さの場合も、モーションモードは自動的にnormalに設定されます。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 入力画像とパラメータに基づいて生成された動画 |