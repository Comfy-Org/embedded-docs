# ByteDance Seedance 2.0 テキストから動画生成

このノードは、ByteDance の Seedance 2.5 または 2.0 モデルを使用して、テキストプロンプトから動画を生成します。選択したモデルにプロンプトを送信し、動画の処理が完了するまで待機して、生成された動画ファイルを返します。`Seedance 2.5 Draft` モデルを選択すると、代わりに高速な 480p プレビューをレンダリングします。生成された `draft_task_id` を ByteDance Seedance 2.5 Draft to Final Video ノードに接続して、1080p の最終出力をレンダリングしてください。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `モデル` | 動画生成に使用する Seedance モデル。Seedance 2.5 は最新モデルで、最大30秒の動画と mp4/mov 出力に対応します。Seedance 2.5 Draft は高速な 480p プレビューをレンダリングし、その `draft_task_id` 出力を使って ByteDance Seedance 2.5 Draft to Final Video ノードで 1080p の最終出力をレンダリングします。Seedance 2.0 は最高品質と 4k 向けです。Seedance 2.0 Fast は速度最適化向けです。Seedance 2.0 Mini は最速かつ最低コストの生成向けです。モデルを選択すると、プロンプト、解像度、アスペクト比、長さ、音声生成の追加入力が表示されます。 | DYNAMIC_COMBO | はい | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `シード` | ノードを再実行するかどうかを制御します。seed に関係なく結果は非決定的です。（デフォルト: 0） | INT | いいえ | 0〜2147483647 |
| `ウォーターマーク` | 動画にウォーターマークを追加するかどうか。（デフォルト: False）これは高度な設定です。 | BOOLEAN | いいえ | True / False |

### Seedance 2.5 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 動画生成用のテキストプロンプト。発話するセリフを二重引用符で囲むと、生成される対話を誘導できます。 | STRING | はい | — |
| `resolution` | 出力動画の解像度。（デフォルト: `"720p"`） | COMBO | はい | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | 出力動画のアスペクト比。（デフォルト: `"16:9"`） | COMBO | はい | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 出力動画の長さ（秒単位）。（デフォルト: 5） | INT | はい | 4〜30 |
| `generate_audio` | 出力動画の音声生成を有効にします。（デフォルト: True） | BOOLEAN | はい | True / False |
| `output_format` | 出力動画のコンテナ形式。（デフォルト: `"mp4"`） | COMBO | はい | `"mp4"` |

### Seedance 2.5 Draft 入力

これらの入力は `Seedance 2.5 Draft` を選択したときに表示されます。パラメータセットは上記の Seedance 2.5 と同じですが、`resolution` が `"480p"` のみ（デフォルト `"480p"`）である点が異なります。

### Seedance 2.0 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 動画生成用のテキストプロンプト。 | STRING | はい | — |
| `resolution` | 出力動画の解像度。 | COMBO | はい | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 出力動画のアスペクト比。（デフォルト: `"16:9"`） | COMBO | はい | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 出力動画の長さ（秒単位）。（デフォルト: 7） | INT | はい | 4〜15 |
| `generate_audio` | 出力動画の音声生成を有効にします。（デフォルト: True） | BOOLEAN | はい | True / False |

### Seedance 2.0 Fast および Seedance 2.0 Mini 入力

Seedance 2.0 Fast と Seedance 2.0 Mini で共有されます。どちらのモデルも同じパラメータを公開します。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 動画生成用のテキストプロンプト。 | STRING | はい | — |
| `resolution` | 出力動画の解像度。 | COMBO | はい | `"480p"`<br>`"720p"` |
| `ratio` | 出力動画のアスペクト比。（デフォルト: `"16:9"`） | COMBO | はい | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 出力動画の長さ（秒単位）。（デフォルト: 7） | INT | はい | 4〜15 |
| `generate_audio` | 出力動画の音声生成を有効にします。（デフォルト: True） | BOOLEAN | はい | True / False |

**注:** `model` セレクターは動的です。各モデルセクションの下に表示される入力は、そのモデルを選択したときに表示されます。プロンプトは空白を除去した後、少なくとも1文字以上である必要があります。解像度と長さの制限は選択したモデルによって異なります。Seedance 2.5 は 480p/720p/1080p および 4～30秒に対応し、Seedance 2.0 は 480p/720p/1080p/4k および 4～15秒に対応します。また、Seedance 2.0 Fast と Seedance 2.0 Mini は 480p/720p のみおよび 4～15秒に対応します。Seedance 2.5 Draft は 480p のみおよび 4～30秒に対応します。`draft_task_id` 出力は Seedance 2.5 Draft によってのみ生成されるため、他のモデルでは未接続のままにする必要があります。そうしないと実行が失敗します。`seed` の値はノードを再実行するかどうかを制御するだけで、結果を決定的にはしません。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `video` | 生成された動画ファイル。 | VIDEO |
| `draft_task_id` | ドラフト実行のタスク ID。Seedance 2.5 Draft モデルのみがこれを生成します。ByteDance Seedance 2.5 Draft to Final Video ノードに接続して、1080p の最終出力をレンダリングします。 | STRING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/ja.md)

---
**Source fingerprint (SHA-256):** `2abad0c4eab5a1286c8da9237bcec52b275c40188b3b7dc9eede5d5f4cbb11d3`
