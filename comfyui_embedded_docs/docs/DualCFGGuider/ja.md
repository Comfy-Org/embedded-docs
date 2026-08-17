# デュアルCFGガイダー

DualCFGGuiderノードは、デュアル分類器フリーガイダンスサンプリングのためのガイダンスシステムを作成します。2つのポジティブ条件付け入力と1つのネガティブ条件付け入力を組み合わせ、各条件付けペアに異なるガイダンススケールを適用して、各プロンプトが生成出力に与える影響の強さを制御します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | ガイダンスに使用するモデル。 | MODEL | はい | - |
| `cond1` | 1つ目のポジティブ条件付け入力。 | CONDITIONING | はい | - |
| `cond2` | 2つ目のポジティブ条件付け入力で、中間条件付けとして扱われます。 | CONDITIONING | はい | - |
| `negative` | ネガティブ条件付け入力。 | CONDITIONING | はい | - |
| `cfg_conds` | `cond1` と `cond2` の間に適用されるガイダンススケール（デフォルト: 8.0）。 | FLOAT | はい | 0.0 - 100.0 |
| `cfg_cond2_negative` | `cond2` とネガティブ条件付けの間に適用されるガイダンススケール（デフォルト: 8.0）。 | FLOAT | はい | 0.0 - 100.0 |
| `style` | 適用するガイダンススタイル（デフォルト: "regular"）。"regular" は両方のガイダンススケールを1つのステップで組み合わせます。"nested" は最初に `cfg_conds` を適用し、その結果をネガティブ条件付けに対して `cfg_cond2_negative` でスケーリングします。 | COMBO | はい | "regular"<br>"nested" |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `GUIDER` | サンプリングで使用する準備が整った構成済みガイダンスシステム。 | GUIDER |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/ja.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
