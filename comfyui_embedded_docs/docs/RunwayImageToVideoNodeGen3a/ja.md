# Runway 画像から動画生成 (Gen3a Turbo)

Runway Image to Video (Gen3a Turbo) ノードは、Runway の Gen3a Turbo モデルを使用して、単一の開始フレームからビデオを生成します。テキストプロンプトと初期画像フレームを受け取り、指定された長さとアスペクト比に基づいてビデオシーケンスを作成します。このノードは Runway の API に接続して、リモートで生成を処理します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 生成用のテキストプロンプト（デフォルト："") | STRING | はい | N/A |
| `start_frame` | ビデオに使用される開始フレーム | IMAGE | はい | N/A |
| `duration` | ビデオの長さ（秒）（デフォルト："5"） | COMBO | はい | `"5"`<br>`"10"` |
| `ratio` | 生成されたビデオのアスペクト比（デフォルト："768:1280"） | COMBO | はい | `"768:1280"`<br>`"1280:768"` |
| `seed` | 生成用のランダムシード（デフォルト：0） | INT | いいえ | 0 から 4294967295 |

**パラメータ制約：**

- `start_frame` の寸法は 7999x7999 ピクセルを超えてはなりません。
- `start_frame` のアスペクト比は 0.5 から 2.0 の間でなければなりません。
- `prompt` は少なくとも1文字以上含まれている必要があります（空にできません）。

**注記：**

- このノードは非推奨です。
- 生成前に、Runway はベストプラクティスガイドの確認を推奨しています： https://help.runwayml.com/hc/en-us/articles/33927968552339-Creating-with-Act-One-on-Gen-3-Alpha-and-Turbo

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `output` | 生成されたビデオシーケンス | VIDEO |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/ja.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
