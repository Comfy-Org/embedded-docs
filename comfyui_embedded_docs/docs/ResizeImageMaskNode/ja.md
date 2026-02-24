> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/ja.md)

Resize Image/Maskノードは、入力画像またはマスクの寸法を変更するための複数の方法を提供します。倍率によるスケーリング、特定の寸法の設定、別の入力のサイズに合わせる、またはピクセル数に基づいて調整することができ、品質のために様々な補間方法を使用します。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `input` | IMAGE または MASK | はい | N/A | リサイズする画像またはマスク。 |
| `resize_type` | COMBO | はい | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` | 新しいサイズを決定するために使用する方法。必要なパラメータは選択したタイプに基づいて変化します。 |
| `multiplier` | FLOAT | いいえ | 0.01 から 8.0 | スケーリング係数。`resize_type`が`SCALE_BY`の場合に必要です（デフォルト: 1.00）。 |
| `width` | INT | いいえ | 0 から 8192 | ターゲットの幅（ピクセル単位）。`resize_type`が`SCALE_DIMENSIONS`または`SCALE_WIDTH`の場合に必要です（デフォルト: 512）。 |
| `height` | INT | いいえ | 0 から 8192 | ターゲットの高さ（ピクセル単位）。`resize_type`が`SCALE_DIMENSIONS`または`SCALE_HEIGHT`の場合に必要です（デフォルト: 512）。 |
| `crop` | COMBO | いいえ | `"disabled"`<br>`"center"` | 寸法がアスペクト比に一致しない場合に適用するクロップ方法。`resize_type`が`SCALE_DIMENSIONS`または`MATCH_SIZE`の場合にのみ利用可能です（デフォルト: "center"）。 |
| `longer_size` | INT | いいえ | 0 から 8192 | 画像の長辺のターゲットサイズ。`resize_type`が`SCALE_LONGER_DIMENSION`の場合に必要です（デフォルト: 512）。 |
| `shorter_size` | INT | いいえ | 0 から 8192 | 画像の短辺のターゲットサイズ。`resize_type`が`SCALE_SHORTER_DIMENSION`の場合に必要です（デフォルト: 512）。 |
| `megapixels` | FLOAT | いいえ | 0.01 から 16.0 | ターゲットの総メガピクセル数。`resize_type`が`SCALE_TOTAL_PIXELS`の場合に必要です（デフォルト: 1.0）。 |
| `match` | IMAGE または MASK | いいえ | N/A | 入力のリサイズ先となる寸法を持つ画像またはマスク。`resize_type`が`MATCH_SIZE`の場合に必要です。 |
| `scale_method` | COMBO | はい | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` | スケーリングに使用される補間アルゴリズム（デフォルト: "area"）。 |

**注意:** `crop`パラメータは、`resize_type`が`SCALE_DIMENSIONS`または`MATCH_SIZE`に設定されている場合にのみ利用可能で関連性があります。`SCALE_WIDTH`または`SCALE_HEIGHT`を使用する場合、もう一方の寸法は元のアスペクト比を維持するために自動的にスケーリングされます。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `resized` | IMAGE または MASK | リサイズされた画像またはマスク。入力のデータ型と一致します。 |
