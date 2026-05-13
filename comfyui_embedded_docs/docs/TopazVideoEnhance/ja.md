> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/ja.md)

以下が日本語翻訳です。

このドキュメントは AI によって生成されました。誤りや改善の提案がありましたら、ぜひご協力ください！ [GitHub で編集する](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/en.md)

Topaz Video Enhance ノードは、外部 API を使用して動画の品質を向上させます。動画の解像度をアップスケールしたり、フレーム補間によってフレームレートを向上させたり、圧縮を適用したりすることができます。このノードは入力された MP4 動画を処理し、選択された設定に基づいて品質が向上されたバージョンを返します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | はい | - | 品質を向上させる入力動画ファイルです。 |
| `upscaler_enabled` | BOOLEAN | はい | - | 動画のアップスケール機能を有効または無効にします（デフォルト: True）。 |
| `upscaler_model` | COMBO | はい | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` | 動画のアップスケールに使用する AI モデルです。 |
| `upscaler_resolution` | COMBO | はい | `"FullHD (1080p)"`<br>`"4K (2160p)"` | アップスケール後の動画の目標解像度です。 |
| `upscaler_creativity` | COMBO | いいえ | `"low"`<br>`"middle"`<br>`"high"` | 創造性のレベルです（Starlight (Astra) Creative にのみ適用されます）。（デフォルト: "low"） |
| `interpolation_enabled` | BOOLEAN | いいえ | - | フレーム補間機能を有効または無効にします（デフォルト: False）。 |
| `interpolation_model` | COMBO | いいえ | `"apo-8"` | フレーム補間に使用するモデルです（デフォルト: "apo-8"）。 |
| `interpolation_slowmo` | INT | いいえ | 1 から 16 | 入力動画に適用されるスローモーション係数です。例えば、2 を指定すると出力は 2 倍遅くなり、再生時間も 2 倍になります。（デフォルト: 1） |
| `interpolation_frame_rate` | INT | いいえ | 15 から 240 | 出力のフレームレートです。（デフォルト: 60） |
| `interpolation_duplicate` | BOOLEAN | いいえ | - | 入力から重複フレームを分析して削除します。（デフォルト: False） |
| `interpolation_duplicate_threshold` | FLOAT | いいえ | 0.001 から 0.1 | 重複フレームの検出感度です。（デフォルト: 0.01） |
| `dynamic_compression_level` | COMBO | いいえ | `"Low"`<br>`"Mid"`<br>`"High"` | CQP レベルです。（デフォルト: "Low"） |

**注意:** 少なくとも 1 つの品質向上機能を有効にする必要があります。`upscaler_enabled` と `interpolation_enabled` の両方が `False` に設定されている場合、ノードはエラーを発生させます。入力動画は MP4 形式である必要があります。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `video` | VIDEO | 品質が向上された出力動画ファイルです。 |

---
**Source fingerprint (SHA-256):** `70e1a6e0d7bd250f58c43beefe070fd83af19d11ac08cb9a6ac9655a9bfa839f`
