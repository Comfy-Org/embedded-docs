# TextEncodeAceStepAudio1.5

TextEncodeAceStepAudio1.5 ノードは、AceStepAudio 1.5 モデルで使用するテキストおよび音声関連のメタデータを準備します。説明的なタグ、歌詞、音楽パラメータを受け取り、CLIP モデルを使用して、オーディオ生成に適したコンディショニング形式に変換します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `clip` | 入力テキストをトークン化およびエンコードするために使用されるCLIPモデル。 | CLIP | はい | N/A |
| `tags` | オーディオの説明的なタグ（ジャンル、ムード、楽器など）。複数行入力と動的プロンプトに対応しています。 | STRING | はい | N/A |
| `lyrics` | オーディオトラックの歌詞。複数行入力と動的プロンプトに対応しています。 | STRING | はい | N/A |
| `seed` | 再現可能な生成のためのランダムシード値。control_after_generate ウィジェットがあります。デフォルト: 0。 | INT | いいえ | 0 to 18446744073709551615 |
| `bpm` | 生成されるオーディオの1分間あたりの拍数（BPM）。デフォルト: 120。 | INT | いいえ | 10 to 300 |
| `duration` | オーディオの希望する長さ（秒）。デフォルト: 120.0。 | FLOAT | いいえ | 0.0 to 2000.0 |
| `timesignature` | 音楽の拍子記号。 | COMBO | いいえ | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | 入力テキストの言語。デフォルト: "en"。 | COMBO | いいえ | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | 音楽の調性とスケール（メジャーまたはマイナー）。 | COMBO | いいえ | `"C major"`<br>`"C# major"`<br>`"Db major"`<br>`"D major"`<br>`"D# major"`<br>`"Eb major"`<br>`"E major"`<br>`"F major"`<br>`"F# major"`<br>`"Gb major"`<br>`"G major"`<br>`"G# major"`<br>`"Ab major"`<br>`"A major"`<br>`"A# major"`<br>`"Bb major"`<br>`"B major"`<br>`"C minor"`<br>`"C# minor"`<br>`"Db minor"`<br>`"D minor"`<br>`"D# minor"`<br>`"Eb minor"`<br>`"E minor"`<br>`"F minor"`<br>`"F# minor"`<br>`"Gb minor"`<br>`"G minor"`<br>`"G# minor"`<br>`"Ab minor"`<br>`"A minor"`<br>`"A# minor"`<br>`"Bb minor"`<br>`"B minor"` |
| `generate_audio_codes` | オーディオコードを生成するLLMを有効にします。処理が遅くなる可能性がありますが、生成されるオーディオの品質は向上します。モデルにオーディオ参照を与える場合はオフにしてください。デフォルト: True。 | BOOLEAN | いいえ | N/A |
| `cfg_scale` | クラシファイアフリーガイダンススケール。値が大きいほど、出力がプロンプトにより厳密に従います。デフォルト: 2.0。 | FLOAT | いいえ | 0.0 to 100.0 |
| `temperature` | サンプリング温度。値が低いほど、出力はより決定的になります。デフォルト: 0.85。 | FLOAT | いいえ | 0.0 to 2.0 |
| `top_p` | ニュークリアスサンプリングの確率（top-p）。デフォルト: 0.9。 | FLOAT | いいえ | 0.0 to 2000.0 |
| `top_k` | 考慮する上位確率トークンの数（top-k）。デフォルト: 0。 | INT | いいえ | 0 to 100 |
| `min_p` | トークンサンプリングの最小確率しきい値（min-p）。デフォルト: 0.000。 | FLOAT | いいえ | 0.0 to 1.0 |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `CONDITIONING` | エンコードされたテキストとAceStepAudio 1.5モデル用のオーディオパラメータを含むコンディショニングデータ。 | CONDITIONING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/ja.md)

---
**Source fingerprint (SHA-256):** `4bc97ec6220514b71fafde610339f2dca4ded26f68b541ed43ea492f127321f8`
