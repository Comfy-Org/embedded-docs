> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/ja.md)

このドキュメントはAIによって生成されました。誤りや改善の提案がありましたら、ぜひご協力ください！[GitHubで編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/en.md)

このノードは、3Dモデルに対してスマートリトポロジを実行します。これは、より低いポリゴン数で新しいクリーンなメッシュを自動生成するプロセスです。Tencent Hunyuan 3D APIに接続してモデルを処理し、GLBおよびOBJファイル形式をサポートします。ノードは処理済みモデルをOBJファイルとして返します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | はい | - | 入力3Dモデル（GLBまたはOBJ）。ファイルはGLBまたはOBJ形式である必要があり、200MBを超えることはできません。 |
| `polygon_type` | STRING | はい | `"triangle"`<br>`"quadrilateral"` | サーフェス構成タイプ。 |
| `face_level` | STRING | はい | `"medium"`<br>`"high"`<br>`"low"` | ポリゴン削減レベル。 |
| `seed` | INT | いいえ | 0～2147483647 | シードはノードを再実行するかどうかを制御します。結果はシードに関係なく非決定的です。（デフォルト：0） |

**注記：** `seed`パラメータはノードの再実行をトリガーするために使用されますが、同じシード値でも最終出力が同じになることは保証されません。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | 最適化されたトポロジを持つ処理済み3Dモデル。OBJ形式で返されます。 |