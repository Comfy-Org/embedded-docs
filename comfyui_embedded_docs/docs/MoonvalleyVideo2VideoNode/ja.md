> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/ja.md)

Moonvalley Marey Video to Videoノードは、入力された動画をテキスト記述に基づいて新しい動画に変換します。このノードはMoonvalley APIを使用して、元の動画から動きやポーズの特徴を保持しながら、プロンプトに一致する動画を生成します。テキストプロンプトと各種生成パラメータを通じて、出力動画のスタイルや内容を制御できます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | はい | - | 生成する動画を記述します（複数行入力可能） |
| `negative_prompt` | STRING | いいえ | - | ネガティブプロンプトテキスト（デフォルト：広範なネガティブ記述子のリスト） |
| `seed` | INT | はい | 0-4294967295 | 乱数シード値（デフォルト：9） |
| `video` | VIDEO | はい | - | 出力動画の生成に使用される参照動画。最低5秒以上の長さが必要です。5秒より長い動画は自動的にトリミングされます。MP4形式のみサポートされています。 |
| `control_type` | COMBO | いいえ | "Motion Transfer"<br>"Pose Transfer" | 制御タイプの選択（デフォルト："Motion Transfer"） |
| `motion_intensity` | INT | いいえ | 0-100 | control_typeが'Motion Transfer'の場合にのみ使用されます（デフォルト：100） |
| `steps` | INT | はい | 1-100 | 推論ステップ数（デフォルト：33） |

**注意:** `motion_intensity`パラメータは、`control_type`が"Motion Transfer"に設定されている場合にのみ適用されます。"Pose Transfer"を使用する場合、このパラメータは無視されます。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成された動画の出力 |
