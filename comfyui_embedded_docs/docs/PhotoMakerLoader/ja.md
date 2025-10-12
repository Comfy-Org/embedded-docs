> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/ja.md)

PhotoMakerLoaderノードは、利用可能なモデルファイルからPhotoMakerモデルを読み込みます。指定されたモデルファイルを読み取り、IDベースの画像生成タスクで使用するためのPhotoMaker IDエンコーダを準備します。このノードは実験的としてマークされており、テスト目的で使用されることを意図しています。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `photomakerモデル名` | STRING | はい | 複数のオプションが利用可能 | 読み込むPhotoMakerモデルファイルの名前。利用可能なオプションは、photomakerフォルダ内に存在するモデルファイルによって決定されます。 |

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `photomaker_model` | PHOTOMAKER | 読み込まれたPhotoMakerモデル。IDエンコーディング操作で使用する準備が整ったIDエンコーダを含みます。 |