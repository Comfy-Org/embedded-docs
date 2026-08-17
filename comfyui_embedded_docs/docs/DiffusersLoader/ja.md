# ディフューザーを読み込む

```markdown
DiffusersLoader ノードは非推奨です。このノードは、Hugging Face diffusers 形式で保存された事前学習済みモデルを読み込み、パイプラインに必要な3つの標準コンポーネント（MODEL、CLIP、VAE）を返します。ノードは設定された diffusers フォルダーを自動的にスキャンし、有効なモデルディレクトリ（`model_index.json` ファイルを含むフォルダー）を探して、読み込むモデルを選択できます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model_path` | 読み込む diffusers モデルディレクトリへのパス。ノードは設定された diffusers フォルダーをスキャンし、`model_index.json` ファイルを含むすべてのディレクトリを一覧表示します。 | COMBO | はい | 自動入力（設定された diffusers フォルダー内の、`model_index.json` ファイルを含むすべてのサブディレクトリ） |

注：選択したパスは、検出されたモデルのリストに対して検証されます。パスがリストに含まれていない場合、またはモデルディレクトリが見つからない場合は、エラーで読み込みが失敗します。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `MODEL` | diffusers 形式から読み込まれたモデルコンポーネント | MODEL |
| `CLIP` | diffusers 形式から読み込まれた CLIP テキストエンコーディングモデルコンポーネント | CLIP |
| `VAE` | diffusers 形式から読み込まれた VAE（変分オートエンコーダー）コンポーネント | VAE |
```

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/ja.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
