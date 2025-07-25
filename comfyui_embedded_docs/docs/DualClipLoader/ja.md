DualCLIPLoaderノードは、2つのCLIPモデルを同時にロードするために設計されており、両モデルの特徴を統合または比較する操作を容易にします。

## 入力

| パラメータ    | Data Type | 説明 |
|--------------|--------------|-------------|
| `clip_name1` | COMBO[STRING] | ロードする最初のCLIPモデルの名前を指定します。このパラメータは、利用可能なCLIPモデルの事前定義リストから正しいモデルを識別し取得するために重要です。 |
| `clip_name2` | COMBO[STRING] | ロードする2番目のCLIPモデルの名前を指定します。このパラメータは、最初のモデルと並行して比較または統合分析のために2番目の異なるCLIPモデルをロードすることを可能にします。 |
| `type`       | `option`        | "sdxl", "sd3", "flux" から選択して異なるモデルに適応します。 |

* ロードの順序は出力効果に影響を与えません

## 出力

| パラメータ | データ型 | 説明 |
|-----------|--------------|-------------|
| `clip`    | `CLIP`       | 出力は、指定された2つのCLIPモデルの特徴または機能を統合した結合CLIPモデルです。 |

## ワークフロー例

元のワークフロー引用元 <https://openart.ai/workflows/seal_harmful_40/flux/UGHBjoJgN8tLnhr7FKOP>
