# フォトメーカーエンコード

PhotoMakerEncodeは、参照画像とテキストプロンプトを組み合わせることで、AI画像生成用のconditioningデータを作成します。テキストプロンプト内で「photomaker」という単語を検索し、見つかった場合、PhotoMakerモデルを使用して、プロンプト内のその位置に参照画像の視覚的特徴を適用します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `photomaker` | 参照画像の処理と画像ベースの埋め込みの生成に使用されるPhotoMakerモデル | PHOTOMAKER | はい | - |
| `image` | conditioning用の視覚的特徴を提供する参照画像 | IMAGE | はい | - |
| `clip` | テキストのトークン化とエンコードに使用されるCLIPモデル | CLIP | はい | - |
| `text` | conditioning生成用のテキストプロンプト。複数行と動的プロンプトに対応（デフォルト: "photograph of photomaker"） | STRING | はい | - |

**注:** 画像ベースのconditioningを適用するには、テキストプロンプト内に「photomaker」という単語が独立した単語として含まれている必要があります（大文字と小文字は区別されます）。存在する場合、画像の特徴はプロンプト内のその位置に注入されます。「photomaker」が見つからない場合、ノードは画像の影響を受けない標準的なテキストconditioningを返します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `CONDITIONING` | 画像生成を導くための画像およびテキスト埋め込みと、CLIPテキストエンコーダーからのプールされた出力を含むconditioningデータ | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/ja.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
