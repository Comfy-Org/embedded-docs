# LoRAの読み込み（バイパス）（デバッグ用）

LoraLoaderBypass ノードは、特別なバイパスモードで拡散モデルとCLIPモデルにLoRA（Low-Rank Adaptation）を適用します。標準のLoRAローダーとは異なり、ベースモデルの重みを永続的に変更しません。代わりに、モデルの通常のフォワードパスにLoRAの効果を追加します。これは、トレーニング時や重みがオフロードされたモデルを扱う場合に役立ちます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `model` | LoRAが適用される拡散モデルです。 | MODEL | はい | N/A |
| `clip` | LoRAが適用されるCLIPモデルです。 | CLIP | はい | N/A |
| `lora_name` | 適用するLoRAファイルの名前です。オプションは`loras`フォルダから読み込まれます。 | COMBO | はい | 利用可能なLoRAファイルのリスト |
| `strength_model` | 拡散モデルを変更する強さです。負の値を指定できます（デフォルト: 1.0）。 | FLOAT | はい | -100.0 to 100.0 |
| `strength_clip` | CLIPモデルを変更する強さです。負の値を指定できます（デフォルト: 1.0）。 | FLOAT | はい | -100.0 to 100.0 |

**注記：** `strength_model` と `strength_clip` の両方が0に設定されている場合、ノードは処理を行わずに元の未変更の`model`および`clip`入力を返します。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `MODEL` | バイパスモードでLoRAが適用された拡散モデルです。 | MODEL |
| `CLIP` | バイパスモードでLoRAが適用されたCLIPモデルです。 | CLIP |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/ja.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
