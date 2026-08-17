# Topaz画像強化

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | 画像強調に使用するAIモデルです。 | COMBO | はい | `"Reimagine"` |
| `image` | 強調する入力画像です。サポートされる画像は1枚のみです。 | IMAGE | はい | - |
| `prompt` | 創造的なアップスケーリングを導くためのオプションのテキストプロンプトです（デフォルト：空）。 | STRING | いいえ | - |
| `subject_detection` | 強調処理が画像のどの部分に焦点を当てるかを制御します（デフォルト："All"）。 | COMBO | いいえ | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | 処理中に顔（存在する場合）を強調します（デフォルト：True）。 | BOOLEAN | いいえ | - |
| `face_enhancement_creativity` | 顔強調の創造性レベルを設定します（デフォルト：0.0）。 | FLOAT | いいえ | 0.0 - 1.0 |
| `face_enhancement_strength` | 強調された顔の、背景に対する鮮明さを制御します（デフォルト：1.0）。 | FLOAT | いいえ | 0.0 - 1.0 |
| `crop_to_fill` | デフォルトでは、出力アスペクト比が異なる場合に画像がレターボックス化されます。出力サイズに合わせて画像を切り抜くには、これを有効にします（デフォルト：False）。 | BOOLEAN | いいえ | - |
| `output_width` | ゼロの場合は自動計算します（通常は元のサイズか、指定されていれば`output_height`になります）（デフォルト：0）。 | INT | いいえ | 0 - 32000 |
| `output_height` | ゼロの場合は元の高さか、`output_width`と同じ高さで出力します（デフォルト：0）。 | INT | いいえ | 0 - 32000 |
| `creativity` | 強調処理全体の創造性レベルを制御します（デフォルト：3）。 | INT | いいえ | 1 - 9 |
| `face_preservation` | 被写体の顔の同一性を保持します（デフォルト：True）。 | BOOLEAN | いいえ | - |
| `color_preservation` | 元の色を保持します（デフォルト：True）。 | BOOLEAN | いいえ | - |

**注記：** このノードは単一の入力画像のみ処理できます。複数の画像をバッチで提供するとエラーが発生します。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `image` | 強調処理された出力画像です。 | IMAGE |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/ja.md)

---
**Source fingerprint (SHA-256):** `a4b622ced661dd1dd1c57d4536359874d2203c8d4064c76fa684b9935e265085`
