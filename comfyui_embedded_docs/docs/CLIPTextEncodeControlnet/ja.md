> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/ja.md)

CLIPTextEncodeControlnetノードは、テキスト入力をCLIPモデルを使用して処理し、既存の調節データと組み合わせることで、controlnetアプリケーション向けの強化された調節出力を作成します。入力テキストをトークン化し、CLIPモデルを通じてエンコードし、結果の埋め込みを提供された調節データにcross-attention controlnetパラメータとして追加します。

## 入力

| パラメータ | データ型 | 入力タイプ | デフォルト | 範囲 | 説明 |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | 必須 | - | - | テキストのトークン化とエンコードに使用されるCLIPモデル |
| `conditioning` | CONDITIONING | 必須 | - | - | controlnetパラメータで強化する既存の調節データ |
| `text` | STRING | 複数行、動的プロンプト | - | - | CLIPモデルによって処理されるテキスト入力 |

**注意:** このノードは正常に機能するために`clip`と`conditioning`の両方の入力が必要です。`text`入力は、柔軟なテキスト処理のために動的プロンプトと複数行テキストをサポートしています。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | controlnet cross-attentionパラメータが追加された強化された調節データ |