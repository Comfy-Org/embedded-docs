> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/ja.md)

このドキュメントはAIによって生成されました。誤りや改善の提案がありましたら、ぜひご協力ください！

入力画像とテキストプロンプトに基づいて動画を生成します。このノードは画像を受け取り、指定されたモーションと品質設定を適用して、静止画像を動きのあるシーケンスに変換することでアニメーション動画を作成します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | はい | - | 動画に変換する入力画像 |
| `prompt` | STRING | はい | - | 動画生成のためのプロンプト |
| `quality` | COMBO | はい | `res_540p`<br>`res_1080p` | 動画品質の設定（デフォルト: res_540p） |
| `duration_seconds` | COMBO | はい | `dur_2`<br>`dur_5`<br>`dur_10` | 生成される動画の長さ（秒） |
| `motion_mode` | COMBO | はい | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` | 動画生成に適用されるモーションスタイル |
| `seed` | INT | はい | 0-2147483647 | 動画生成のシード値（デフォルト: 0） |
| `negative_prompt` | STRING | いいえ | - | 画像内で望ましくない要素を記述するオプションのテキスト |
| `pixverse_template` | CUSTOM | いいえ | - | PixVerseテンプレートノードで作成される、生成スタイルに影響を与えるオプションのテンプレート |

**注意:** 1080p品質を使用する場合、モーションモードは自動的にnormalに設定され、動画の長さは5秒に制限されます。5秒以外の長さの場合も、モーションモードは自動的にnormalに設定されます。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 入力画像とパラメータに基づいて生成された動画 |

---
**Source fingerprint (SHA-256):** `7630c662a2506fb0c8be0cb9c6bfdfcf0fc06d2b6f16b8636664d587affededc`
