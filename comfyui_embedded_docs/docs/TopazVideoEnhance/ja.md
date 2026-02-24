> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/ja.md)

Topaz Video Enhanceノードは、外部APIを使用して動画の品質を向上させます。動画解像度のアップスケール、補完によるフレームレートの向上、圧縮の適用が可能です。このノードは入力されたMP4動画を処理し、選択された設定に基づいて強化されたバージョンを返します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | はい | - | 強化する入力動画ファイル。 |
| `upscaler_enabled` | BOOLEAN | はい | - | 動画アップスケール機能を有効または無効にします（デフォルト: True）。 |
| `upscaler_model` | COMBO | はい | `"Proteus v3"`<br>`"Artemis v13"`<br>`"Artemis v14"`<br>`"Artemis v15"`<br>`"Gaia v6"`<br>`"Theia v3"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight (Astra) Optimized"`<br>`"Starlight (Astra) Balanced"`<br>`"Starlight (Astra) Quality"`<br>`"Starlight (Astra) Speed"` | 動画のアップスケールに使用するAIモデル。 |
| `upscaler_resolution` | COMBO | はい | `"FullHD (1080p)"`<br>`"4K (2160p)"` | アップスケール後の動画の目標解像度。 |
| `upscaler_creativity` | COMBO | いいえ | `"low"`<br>`"middle"`<br>`"high"` | 創造性レベル（Starlight (Astra) Creativeにのみ適用されます）。（デフォルト: "low"） |
| `interpolation_enabled` | BOOLEAN | いいえ | - | フレーム補完機能を有効または無効にします（デフォルト: False）。 |
| `interpolation_model` | COMBO | いいえ | `"apo-8"` | フレーム補完に使用するモデル（デフォルト: "apo-8"）。 |
| `interpolation_slowmo` | INT | いいえ | 1 から 16 | 入力動画に適用するスローモーション係数。例えば、2にすると出力が2倍遅くなり、再生時間が2倍になります。（デフォルト: 1） |
| `interpolation_frame_rate` | INT | いいえ | 15 から 240 | 出力フレームレート。（デフォルト: 60） |
| `interpolation_duplicate` | BOOLEAN | いいえ | - | 入力動画を分析し、重複フレームを除去します。（デフォルト: False） |
| `interpolation_duplicate_threshold` | FLOAT | いいえ | 0.001 から 0.1 | 重複フレームの検出感度。（デフォルト: 0.01） |
| `dynamic_compression_level` | COMBO | いいえ | `"Low"`<br>`"Mid"`<br>`"High"` | CQPレベル。（デフォルト: "Low"） |

**注意:** 少なくとも1つの強化機能が有効になっている必要があります。`upscaler_enabled`と`interpolation_enabled`の両方が`False`に設定されている場合、ノードはエラーを発生させます。入力動画はMP4形式である必要があります。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `video` | VIDEO | 強化された出力動画ファイル。 |
