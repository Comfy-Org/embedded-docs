# Bria画像編集

Bria FIBO Image Edit ノードを使用すると、テキストによる指示で既存の画像を変更できます。このノードは、画像とプロンプトを Bria API に送信し、Bria API が FIBO モデルを使用して、リクエストに基づいた新しい編集済み画像を生成します。マスクを指定して、編集を特定の領域に限定することもできます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | 画像編集に使用するモデルバージョン。 | COMBO | はい | `"FIBO"` |
| `image` | 編集したい入力画像。 | IMAGE | はい | - |
| `prompt` | 画像を編集するための指示（デフォルト: 空）。 | STRING | はい | - |
| `negative_prompt` | 編集後の画像に表示させたくない内容を説明するテキスト（デフォルト: 空）。 | STRING | はい | - |
| `structured_prompt` | JSON形式の構造化編集プロンプトを含む文字列。通常のプロンプトの代わりにこれを使用すると、正確でプログラムによる制御が可能です（デフォルト: 空）。 | STRING | はい | - |
| `seed` | ランダム生成を初期化するために使用される数値で、再現可能な結果を保証します（デフォルト: 1）。 | INT | はい | 1 〜 2147483647 |
| `guidance_scale` | 値が大きいほど、画像がプロンプトに忠実に従うようになります（デフォルト: 3.0）。 | FLOAT | はい | 3.0 〜 5.0 |
| `steps` | モデルが実行するノイズ除去ステップの数（デフォルト: 50）。 | INT | はい | 20 〜 50 |
| `moderation` | モデレーション設定。`"true"` を選択すると、プロンプト内容、視覚入力、視覚出力に関する追加のモデレーションオプションが表示されます。 | DYNAMICCOMBO | はい | `"false"`<br>`"true"` |
| `mask` | 省略した場合、編集は画像全体に適用されます。 | MASK | いいえ | - |

**重要な制約事項:**

- `prompt` または `structured_prompt` の少なくともいずれかを指定する必要があります。両方を空にすることはできません。
- `moderation` パラメータが `"true"` に設定されている場合、追加のブール入力が3つ利用可能になります: `prompt_content_moderation`（デフォルト: false）、`visual_input_moderation`（デフォルト: false）、`visual_output_moderation`（デフォルト: true）。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `IMAGE` | Bria API によって返された編集済み画像。 | IMAGE |
| `structured_prompt` | 編集プロセス中に使用または生成された構造化プロンプト。 | STRING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/ja.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
