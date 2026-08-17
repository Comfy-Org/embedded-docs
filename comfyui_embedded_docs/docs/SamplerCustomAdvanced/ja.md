# カスタムサンプラー（高度）

SamplerCustomAdvanced ノードは、カスタムノイズ、ガイダンス、およびサンプリング設定を使用して、高度な潜在空間サンプリングを実行します。カスタマイズ可能なノイズ生成とシグマスケジュールを使用したガイド付きサンプリングプロセスを通じて潜在画像を処理し、利用可能な場合には、最終的なサンプリング出力とノイズ除去されたバージョンの両方を生成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `noise` | サンプリングプロセスの初期ノイズパターンとシードを提供するノイズジェネレーターです。 | NOISE | Yes | - |
| `guider` | サンプリングプロセスを望ましい出力へ導くガイダンスモデルです。 | GUIDER | Yes | - |
| `sampler` | 生成中に潜在空間をどのように移動するかを定義するサンプリングアルゴリズムです。 | SAMPLER | Yes | - |
| `sigmas` | サンプリングステップ全体のノイズレベルを制御するシグマスケジュールです。 | SIGMAS | Yes | - |
| `latent_image` | サンプリングの開始点となる初期の潜在表現です。選択的なノイズ除去のためのオプションの `noise_mask` と、高度な潜在処理のためのオプションの `downscale_ratio_spacial` および `downscale_ratio_temporal` キーをサポートします。 | LATENT | Yes | - |

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `output` | サンプリングプロセス完了後の最終的なサンプリング済み潜在表現です。入力潜在に含まれる `downscale_ratio_spacial` または `downscale_ratio_temporal` キーは、この出力から削除されます。 | LATENT |
| `denoised_output` | サンプリングプロセスが中間のクリーンな予測（x0）を生成する場合、出力のノイズ除去版です。それ以外の場合は出力と同じものを返します。利用可能な場合、これは各ステップにおけるクリーンな潜在表現のモデルによる最良の推定値を表します。 | LATENT |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/ja.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
