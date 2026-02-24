> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/ja.md)

GLSL Shaderノードは、カスタムGLSL ESフラグメントシェーダーコードを入力画像に適用します。複数の画像を処理し、浮動小数点や整数のuniformパラメータを受け取るシェーダープログラムを記述することで、複雑な視覚効果を作成できます。出力サイズは最初の入力画像から決定するか、手動で設定することができます。

## 入力

| パラメータ | データ型 | 必須 | 範囲 | 説明 |
|-----------|-----------|----------|-------|-------------|
| `fragment_shader` | STRING | はい | N/A | GLSLフラグメントシェーダーのソースコード（GLSL ES 3.00 / WebGL 2.0互換）。デフォルト: 最初の入力画像を出力する基本的なシェーダー。 |
| `size_mode` | COMBO | はい | `"from_input"`<br>`"custom"` | 出力サイズの決定方法: 'from_input'は最初の入力画像の寸法を使用、'custom'は手動でサイズを設定可能。 |
| `width` | INT | いいえ | 1 から 16384 | `size_mode`が`"custom"`に設定されている場合の出力画像の幅。デフォルト: 512。 |
| `height` | INT | いいえ | 1 から 16384 | `size_mode`が`"custom"`に設定されている場合の出力画像の高さ。デフォルト: 512。 |
| `images` | IMAGE | はい | 1 から 8 画像 | シェーダーによって処理される入力画像。画像はシェーダーコード内で`u_image0`から`u_image7`（sampler2D）として利用可能です。 |
| `floats` | FLOAT | いいえ | 0 から 8 浮動小数点数 | シェーダー用の浮動小数点uniform値。浮動小数点数はシェーダーコード内で`u_float0`から`u_float7`として利用可能です。デフォルト: 0.0。 |
| `ints` | INT | いいえ | 0 から 8 整数 | シェーダー用の整数uniform値。整数はシェーダーコード内で`u_int0`から`u_int7`として利用可能です。デフォルト: 0。 |

**注記:**
*   `width`および`height`パラメータは、`size_mode`が`"custom"`に設定されている場合にのみ必須となり、表示されます。
*   少なくとも1つの入力画像が必要です。
*   シェーダーコードは常に、出力寸法を含む`u_resolution`（vec2）uniformにアクセスできます。
*   最大で8つの入力画像、8つの浮動小数点uniform、8つの整数uniformを提供できます。

## 出力

| 出力名 | データ型 | 説明 |
|-------------|-----------|-------------|
| `IMAGE0` | IMAGE | シェーダーからの最初の出力画像。シェーダーコード内の`layout(location = 0) out vec4 fragColor0`で利用可能です。 |
| `IMAGE1` | IMAGE | シェーダーからの2番目の出力画像。シェーダーコード内の`layout(location = 1) out vec4 fragColor1`で利用可能です。 |
| `IMAGE2` | IMAGE | シェーダーからの3番目の出力画像。シェーダーコード内の`layout(location = 2) out vec4 fragColor2`で利用可能です。 |
| `IMAGE3` | IMAGE | シェーダーからの4番目の出力画像。シェーダーコード内の`layout(location = 3) out vec4 fragColor3`で利用可能です。 |