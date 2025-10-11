> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/ja.md)

プロンプトと出力サイズに基づいて動画を生成します。このノードはPixVerse APIを使用して2つの入力画像間のトランジション動画を作成し、動画の品質、長さ、モーションスタイル、生成パラメータを指定できます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `first_frame` | IMAGE | はい | - | 動画トランジションの開始画像 |
| `last_frame` | IMAGE | はい | - | 動画トランジションの終了画像 |
| `prompt` | STRING | はい | - | 動画生成のためのプロンプト（デフォルト：空文字列） |
| `quality` | COMBO | はい | PixVerseQuality enumから利用可能な品質オプション<br>デフォルト：res_540p | 動画品質設定 |
| `duration_seconds` | COMBO | はい | PixVerseDuration enumから利用可能な長さオプション | 動画の長さ（秒） |
| `motion_mode` | COMBO | はい | PixVerseMotionMode enumから利用可能なモーションモードオプション | トランジションのモーションスタイル |
| `seed` | INT | はい | 0 から 2147483647 | 動画生成のシード値（デフォルト：0） |
| `negative_prompt` | STRING | いいえ | - | 画像上で望ましくない要素のオプションのテキスト記述（デフォルト：空文字列） |

**注意:** 1080p品質を使用する場合、モーションモードは自動的にnormalに設定され、長さは5秒に制限されます。5秒以外の長さの場合も、モーションモードは自動的にnormalに設定されます。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成されたトランジション動画 |