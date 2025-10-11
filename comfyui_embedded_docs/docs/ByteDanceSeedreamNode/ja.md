> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/ja.md)

ByteDance Seedream 4ノードは、最大4K解像度での統一されたテキストから画像への生成機能と、精密な単一文による編集機能を提供します。テキストプロンプトから新しい画像を作成したり、テキスト指示を使用して既存の画像を編集したりすることができます。このノードは、単一画像の生成と、複数の関連画像の連続生成の両方をサポートしています。

## 入力

| パラメータ | データ型 | 入力タイプ | デフォルト | 範囲 | 説明 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | "seedream-4-0-250828" | ["seedream-4-0-250828"] | モデル名 |
| `prompt` | STRING | STRING | "" | - | 画像の作成または編集のためのテキストプロンプト。 |
| `image` | IMAGE | IMAGE | - | - | 画像から画像への生成のための入力画像。単一または複数参照生成のための1〜10枚の画像リスト。 |
| `size_preset` | STRING | COMBO | RECOMMENDED_PRESETS_SEEDREAM_4の最初のプリセット | RECOMMENDED_PRESETS_SEEDREAM_4のすべてのラベル | 推奨サイズを選択します。カスタムを選択すると、以下の幅と高さを使用します。 |
| `width` | INT | INT | 2048 | 1024-4096 (ステップ64) | 画像のカスタム幅。この値は `size_preset` が `Custom` に設定されている場合にのみ有効です。 |
| `height` | INT | INT | 2048 | 1024-4096 (ステップ64) | 画像のカスタム高さ。この値は `size_preset` が `Custom` に設定されている場合にのみ有効です。 |
| `sequential_image_generation` | STRING | COMBO | "disabled" | ["disabled", "auto"] | グループ画像生成モード。'disabled' は単一画像を生成します。'auto' はモデルに複数の関連画像（例：ストーリーシーン、キャラクターバリエーション）を生成するかどうかを決定させます。 |
| `max_images` | INT | INT | 1 | 1-15 | sequential_image_generation='auto' の場合に生成する画像の最大数。総画像数（入力＋生成）は15を超えることはできません。 |
| `seed` | INT | INT | 0 | 0-2147483647 | 生成に使用するシード値。 |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 画像に「AI生成」の透かしを追加するかどうか。 |
| `fail_on_partial` | BOOLEAN | BOOLEAN | True | - | 有効にすると、要求された画像の一部が欠落している場合やエラーが返された場合に実行を中止します。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 入力パラメータとプロンプトに基づいて生成された画像 |