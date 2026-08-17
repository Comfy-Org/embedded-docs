# 学習データセットを保存

このノードは、準備されたトレーニングデータセットをコンピュータのハードドライブに保存します。画像の潜在変数（latents）と対応するテキスト条件付けを含むエンコードデータを受け取り、管理しやすいようにシャードと呼ばれる複数の小さなファイルに整理します。このノードは、datasetsディレクトリ内にフォルダを自動的に作成し、シャードデータファイルと、データセットを説明するメタデータファイルの両方を保存します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `latents` | MakeTrainingDataset からの潜在変数辞書のリスト。 | LATENT | はい | N/A |
| `conditioning` | MakeTrainingDataset からの条件付けリストのリスト。 | CONDITIONING | はい | N/A |
| `folder_name` | データセットを保存するフォルダ名（datasetsディレクトリ内）。`'project/run1'` のようなサブフォルダも指定できます。（デフォルト: `"training_dataset"`） | STRING | はい | N/A |
| `shard_size` | シャードファイルあたりのサンプル数。（デフォルト: 1000） | INT | はい | 1 ～ 100000 |

**注:** `latents` リストの項目数は、`conditioning` リストの項目数と正確に一致している必要があります。一致しない場合、ノードはエラーを発生させます。`folder_name` は datasets ディレクトリのサブフォルダを指定する必要があります。datasets ルートフォルダ自体や、それを外れるパス（`..` や絶対パスなど）は拒否されます。

## 出力

このノードは出力データを生成しません。データセットは、選択したフォルダ内に番号付きシャードファイル（例：`shard_0000.pkl`）と `metadata.json` ファイルとして、datasets ディレクトリ内に保存されます。

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/ja.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
