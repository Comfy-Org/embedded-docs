> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/ja.md)

制御画像（canny）を使用して画像を生成します。このノードは制御画像を受け取り、プロンプトに基づいて新しい画像を生成すると同時に、制御画像で検出されたエッジ構造に従います。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `control_image` | IMAGE | はい | - | Cannyエッジ検出制御に使用する入力画像 |
| `prompt` | STRING | いいえ | - | 画像生成のためのプロンプト（デフォルト：空文字列） |
| `prompt_upsampling` | BOOLEAN | いいえ | - | プロンプトに対してアップサンプリングを実行するかどうか。有効にすると、より創造的な生成のためにプロンプトを自動的に変更しますが、結果は非決定的になります（同じシードでも全く同じ結果にはなりません）。（デフォルト：False） |
| `canny_low_threshold` | FLOAT | いいえ | 0.01 - 0.99 | Cannyエッジ検出の低閾値；skip_processingがTrueの場合は無視されます（デフォルト：0.1） |
| `canny_high_threshold` | FLOAT | いいえ | 0.01 - 0.99 | Cannyエッジ検出の高閾値；skip_processingがTrueの場合は無視されます（デフォルト：0.4） |
| `skip_preprocessing` | BOOLEAN | いいえ | - | 前処理をスキップするかどうか；control_imageが既にcanny処理済みの場合はTrueに、生画像の場合はFalseに設定します。（デフォルト：False） |
| `guidance` | FLOAT | いいえ | 1 - 100 | 画像生成プロセスのガイダンス強度（デフォルト：30） |
| `steps` | INT | いいえ | 15 - 50 | 画像生成プロセスのステップ数（デフォルト：50） |
| `seed` | INT | いいえ | 0 - 18446744073709551615 | ノイズ生成に使用するランダムシード（デフォルト：0） |

**注意:** `skip_preprocessing`がTrueに設定されている場合、`canny_low_threshold`と`canny_high_threshold`パラメータは無視されます。これは制御画像が既にcannyエッジ画像として処理済みであると仮定するためです。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output_image` | IMAGE | 制御画像とプロンプトに基づいて生成された画像 |
