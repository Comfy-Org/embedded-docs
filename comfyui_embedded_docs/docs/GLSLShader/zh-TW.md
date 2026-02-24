> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/zh-TW.md)

GLSL Shader 節點將自訂的 GLSL ES 片段著色器程式碼套用至輸入圖像。它允許您編寫能夠處理多個圖像並接受統一參數（浮點數和整數）的著色器程式，以創造複雜的視覺效果。輸出尺寸可以由第一個輸入圖像決定或手動設定。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `fragment_shader` | STRING | 是 | N/A | GLSL 片段著色器原始碼（相容於 GLSL ES 3.00 / WebGL 2.0）。預設值：一個輸出第一個輸入圖像的基本著色器。 |
| `size_mode` | COMBO | 是 | `"from_input"`<br>`"custom"` | 輸出尺寸模式：'from_input' 使用第一個輸入圖像的尺寸，'custom' 允許手動設定尺寸。 |
| `width` | INT | 否 | 1 至 16384 | 當 `size_mode` 設定為 `"custom"` 時，輸出圖像的寬度。預設值：512。 |
| `height` | INT | 否 | 1 至 16384 | 當 `size_mode` 設定為 `"custom"` 時，輸出圖像的高度。預設值：512。 |
| `images` | IMAGE | 是 | 1 至 8 個圖像 | 要由著色器處理的輸入圖像。圖像在著色器程式碼中作為 `u_image0` 到 `u_image7` (sampler2D) 使用。 |
| `floats` | FLOAT | 否 | 0 至 8 個浮點數 | 提供給著色器的浮點數統一參數值。浮點數在著色器程式碼中作為 `u_float0` 到 `u_float7` 使用。預設值：0.0。 |
| `ints` | INT | 否 | 0 至 8 個整數 | 提供給著色器的整數統一參數值。整數在著色器程式碼中作為 `u_int0` 到 `u_int7` 使用。預設值：0。 |

**注意事項：**

* `width` 和 `height` 參數僅在 `size_mode` 設定為 `"custom"` 時才需要且可見。
* 至少需要一個輸入圖像。
* 著色器程式碼始終可以存取一個包含輸出尺寸的 `u_resolution` (vec2) 統一參數。
* 最多可以提供 8 個輸入圖像、8 個浮點數統一參數和 8 個整數統一參數。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE0` | IMAGE | 來自著色器的第一個輸出圖像。在著色器程式碼中可透過 `layout(location = 0) out vec4 fragColor0` 存取。 |
| `IMAGE1` | IMAGE | 來自著色器的第二個輸出圖像。在著色器程式碼中可透過 `layout(location = 1) out vec4 fragColor1` 存取。 |
| `IMAGE2` | IMAGE | 來自著色器的第三個輸出圖像。在著色器程式碼中可透過 `layout(location = 2) out vec4 fragColor2` 存取。 |
| `IMAGE3` | IMAGE | 來自著色器的第四個輸出圖像。在著色器程式碼中可透過 `layout(location = 3) out vec4 fragColor3` 存取。 |
