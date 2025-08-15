ConditioningConcatノードは、条件付けベクトルを連結するために設計されており、特に'conditioning_from'ベクトルを'conditioning_to'ベクトルに統合します。この操作は、2つのソースからの条件付け情報を単一の統一された表現に結合する必要があるシナリオで基本的です。

## 入力

| パラメータ             | Comfy dtype        | 説明 |
|-----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | 'conditioning_from'ベクトルが連結される主要な条件付けベクトルのセットを表します。連結プロセスの基礎として機能します。 |
| `conditioning_from`   | `CONDITIONING`     | 'conditioning_to'ベクトルに連結される条件付けベクトルで構成されています。このパラメータは、既存のセットに追加の条件付け情報を統合することを可能にします。 |

## 出力

| パラメータ            | Comfy dtype        | 説明 |
|----------------------|--------------------|-------------|
| `conditioning`       | `CONDITIONING`     | 'conditioning_from'ベクトルを'conditioning_to'ベクトルに連結した結果としての統一された条件付けベクトルのセットです。 |