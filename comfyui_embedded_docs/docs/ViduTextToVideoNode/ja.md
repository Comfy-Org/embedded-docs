> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/ja.md)

Vidu Text To Video Generationノードは、テキストの記述から動画を作成します。様々な動画生成モデルを使用して、テキストプロンプトを動画コンテンツに変換し、再生時間、アスペクト比、視覚的なスタイルについてカスタマイズ可能な設定を提供します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | はい | `vidu_q1`<br>*その他のVideoModelNameオプション* | モデル名（デフォルト: vidu_q1） |
| `prompt` | STRING | はい | - | 動画生成のためのテキストによる記述 |
| `duration` | INT | いいえ | 5-5 | 出力動画の長さ（秒単位）（デフォルト: 5） |
| `seed` | INT | いいえ | 0-2147483647 | 動画生成のためのシード値（0でランダム）（デフォルト: 0） |
| `aspect_ratio` | COMBO | いいえ | `r_16_9`<br>*その他のAspectRatioオプション* | 出力動画のアスペクト比（デフォルト: r_16_9） |
| `resolution` | COMBO | いいえ | `r_1080p`<br>*その他のResolutionオプション* | サポートされる値はモデルと再生時間によって異なる場合があります（デフォルト: r_1080p） |
| `movement_amplitude` | COMBO | いいえ | `auto`<br>*その他のMovementAmplitudeオプション* | フレーム内のオブジェクトの動きの振幅（デフォルト: auto） |

**注意:** `prompt` フィールドは必須であり、空にすることはできません。`duration` パラメータは現在5秒に固定されています。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `output` | VIDEO | テキストプロンプトに基づいて生成された動画 |
