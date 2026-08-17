# フォトメーカーを読み込む

PhotoMakerLoader ノードは、利用可能なモデルファイルから PhotoMaker モデルを読み込みます。指定されたモデルファイルを読み取り、IDベースの画像生成タスクで使用するための PhotoMaker IDエンコーダーを準備します。このノードは実験的機能としてマークされており、テスト目的で使用することを想定しています。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `photomaker_model_name` | 読み込むPhotoMakerモデルファイルの名前です。選択可能なオプションは、`photomaker`フォルダ内に存在するモデルファイルによって決まります。 | COMBO | はい | 複数のオプションから選択可能 |

注：選択したモデルファイルは`photomaker`フォルダ内に存在している必要があります。指定されたファイルが見つからない場合、ノードはエラーを発生させます。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `photomaker_model` | IDエンコーダーを含む読み込まれたPhotoMakerモデルです。IDエンコード操作で使用できる状態になっています。 | PHOTOMAKER |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/ja.md)

---
**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`
