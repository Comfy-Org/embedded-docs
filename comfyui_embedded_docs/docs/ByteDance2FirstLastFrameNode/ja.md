# ByteDance Seedance 2.0 ファースト・ラストフレームから動画生成

このノードは、必須の先頭フレーム画像と任意の最終フレーム画像から、ByteDance Seedance モデルを使用して動画を生成します。テキストプロンプトで動画を記述します。先頭フレームは動画の開始を、最終フレームは終了を導きます。Seedance 2.5 と Seedance 2.0 ファミリー（Seedance 2.0、Seedance 2.0 Fast、Seedance 2.0 Mini）をサポートします。`Seedance 2.5 Draft` モデルを選択すると、代わりに高速な 480p プレビューをレンダリングします。得られた `draft_task_id` を ByteDance Seedance 2.5 Draft to Final Video ノードに接続して、1080p の最終版をレンダリングしてください。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `モデル` | `Seedance 2.5` は最新モデルで、最大 30 秒の動画と mp4/mov 出力に対応します。`Seedance 2.5 Draft` は高速な 480p プレビュー用で、その `draft_task_id` 出力を ByteDance Seedance 2.5 Draft to Final Video ノードで使用すると 1080p の最終版をレンダリングできます。`Seedance 2.0` は最高品質と 4k に対応します。`Fast` は速度最適化用です。`Mini` は最速かつ最低コストの生成用です。モデルを選択すると、以下にモデル固有の入力が表示されます。 | DYNAMIC_COMBO | はい | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `最初のフレーム` | 動画の先頭フレーム画像。 | IMAGE | いいえ | - |
| `最後のフレーム` | 動画の最終フレーム画像。 | IMAGE | いいえ | - |
| `first_frame_asset_id` | 先頭フレームとして使用する Seedance の asset_id。`first_frame` 画像入力とは同時に使用できません。デフォルトは空文字列です。 | STRING | いいえ | - |
| `last_frame_asset_id` | 最終フレームとして使用する Seedance の asset_id。`last_frame` 画像入力とは同時に使用できません。デフォルトは空文字列です。 | STRING | いいえ | - |
| `シード` | `seed` はノードを再実行するかどうかを制御します。seed に関係なく結果は非決定的です。デフォルトは 0 です。 | INT | はい | 0～2147483647 |
| `ウォーターマーク` | 動画に透かしを追加するかどうか。デフォルトは False です。 | BOOLEAN | はい | False<br>True |

### Seedance 2.5 入力

これらの入力は `Seedance 2.5` を選択したときに表示されます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 動画生成用のテキストプロンプトです。生成されるセリフを誘導するには、発話されるセリフを二重引用符で囲みます。 | STRING | はい | - |
| `resolution` | 出力動画の解像度。デフォルトは 720p です。 | COMBO | はい | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | 出力動画の長さ（秒、4～30）。デフォルトは 5 です。 | INT | はい | 4～30 |
| `generate_audio` | 出力動画の音声生成を有効にします。デフォルトは True です。 | BOOLEAN | はい | False<br>True |
| `output_format` | 出力動画のコンテナ形式。デフォルトは mp4 です。 | COMBO | はい | `"mp4"` |

### Seedance 2.5 Draft 入力

これらの入力は `Seedance 2.5 Draft` を選択したときに表示されます。パラメータセットは上記の Seedance 2.5 と同じですが、`resolution` で使用できる値が `"480p"` のみ（デフォルト `"480p"`）である点が異なります。

### Seedance 2.0 入力

これらの入力は `Seedance 2.0` を選択したときに表示されます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 動画生成用のテキストプロンプトです。 | STRING | はい | - |
| `resolution` | 出力動画の解像度。 | COMBO | はい | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 出力動画のアスペクト比。デフォルトは `adaptive` で、入力フレームのアスペクト比に最も近いサポート対象の比率を使用します。 | COMBO | はい | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 出力動画の長さ（秒、4～15）。デフォルトは 7 です。 | INT | はい | 4～15 |
| `generate_audio` | 出力動画の音声生成を有効にします。デフォルトは True です。 | BOOLEAN | はい | False<br>True |

### Seedance 2.0 Fast および Seedance 2.0 Mini 入力

`Seedance 2.0 Fast` と `Seedance 2.0 Mini` で共有されます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 動画生成用のテキストプロンプトです。 | STRING | はい | - |
| `resolution` | 出力動画の解像度。 | COMBO | はい | `"480p"`<br>`"720p"` |
| `ratio` | 出力動画のアスペクト比。デフォルトは `adaptive` で、入力フレームのアスペクト比に最も近いサポート対象の比率を使用します。 | COMBO | はい | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 出力動画の長さ（秒、4～15）。デフォルトは 7 です。 | INT | はい | 4～15 |
| `generate_audio` | 出力動画の音声生成を有効にします。デフォルトは True です。 | BOOLEAN | はい | False<br>True |

**パラメータ制約**

- 先頭フレームは、`first_frame` 画像または `first_frame_asset_id` のいずれかとして指定する必要があります。両方を指定するとエラーになり、どちらも指定しない場合もエラーになります。
- `last_frame` と `last_frame_asset_id` 入力は任意ですが、同じフレームに対して両方を指定することはできません。
- Asset ID は、存在する有効な Seedance Image アセットを参照している必要があります。
- `prompt` 入力は必須で、空にできません。
- `draft_task_id` 出力は `Seedance 2.5 Draft` でのみ生成されます。他のモデルでは未接続のままにする必要があり、そうしないと実行に失敗します。
- `Seedance 2.5` では、出力アスペクト比は常に adaptive で、先頭フレーム自体のアスペクト比に従うため、`ratio` 入力は表示されません。
- Seedance 2.0 ファミリーのモデルとローカルフレーム画像を使用する場合、生成前に画像は中央でクロップされ、ターゲットの出力解像度と比率にリサイズされます。`ratio` が `adaptive` の場合、入力画像に最も近いサポート対象の比率が使用されます。
- ローカルフレーム画像は、サポート対象のアスペクト比と寸法かどうか検証されます。大きすぎる画像はダウンスケールされます。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `output` | 生成された動画。 | VIDEO |
| `draft_task_id` | ドラフト実行のタスク ID。Seedance 2.5 Draft モデルのみが生成します。ByteDance Seedance 2.5 Draft to Final Video ノードに接続して、1080p の最終版をレンダリングしてください。 | STRING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/ja.md)

---
**Source fingerprint (SHA-256):** `363f1baac1685c2dada0e64a0b339f6ab2671161dccb002eb81f6b4f0d0aa243`
