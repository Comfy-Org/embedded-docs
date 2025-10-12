> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/ja.md)

StableCascade_EmptyLatentImageノードは、Stable Cascadeモデル用の空の潜在テンソルを作成します。このノードは、入力解像度と圧縮設定に基づいて適切な次元を持つ、ステージC用とステージB用の2つの別々の潜在表現を生成します。このノードは、Stable Cascade生成パイプラインの開始点を提供します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `幅` | INT | はい | 256 から MAX_RESOLUTION | 出力画像の幅（ピクセル単位）（デフォルト: 1024, ステップ: 8） |
| `高さ` | INT | はい | 256 から MAX_RESOLUTION | 出力画像の高さ（ピクセル単位）（デフォルト: 1024, ステップ: 8） |
| `圧縮` | INT | はい | 4 から 128 | ステージCの潜在次元を決定する圧縮係数（デフォルト: 42, ステップ: 1） |
| `バッチサイズ` | INT | いいえ | 1 から 4096 | バッチで生成する潜在サンプルの数（デフォルト: 1） |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `ステージB` | LATENT | 次元が[batch_size, 16, height//compression, width//compression]のステージC潜在テンソル |
| `stage_b` | LATENT | 次元が[batch_size, 4, height//4, width//4]のステージB潜在テンソル |