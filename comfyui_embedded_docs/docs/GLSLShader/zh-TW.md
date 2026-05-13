> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/zh-TW.md)

GLSL 著色器節點可將自訂的 GLSL ES 片段著色器程式碼應用於輸入影像。它允許您編寫能夠處理多張影像並接受統一參數（浮點數、整數、布林值和曲線）的著色器程式，以建立複雜的視覺效果。輸出尺寸可由第一張輸入影像決定，或手動設定。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `片段著色器` | STRING | 是 | N/A | GLSL 片段著色器原始碼（相容 GLSL ES 3.00 / WebGL 2.0）。預設值：一個輸出第一張輸入影像的基本著色器。 |
| `尺寸模式` | COMBO | 是 | `"from_input"`<br>`"custom"` | 輸出尺寸：'from_input' 使用第一張輸入影像的尺寸，'custom' 允許手動設定尺寸。 |
| `width` | INT | 否 | 1 至 16384 | 當 `尺寸模式` 設為 `"custom"` 時，輸出影像的寬度。預設值：512。 |
| `height` | INT | 否 | 1 至 16384 | 當 `尺寸模式` 設為 `"custom"` 時，輸出影像的高度。預設值：512。 |
| `影像` | IMAGE | 是 | 1 至 8 張影像 | 要由著色器處理的輸入影像。在著色器程式碼中，影像可作為 `u_image0` 到 `u_image7`（sampler2D）使用。 |
| `浮點數` | FLOAT | 否 | 0 至 8 個浮點數 | 著色器的浮點數統一值。在著色器程式碼中，浮點數可作為 `u_float0` 到 `u_float7` 使用。預設值：0.0。 |
| `整數` | INT | 否 | 0 至 8 個整數 | 著色器的整數統一值。在著色器程式碼中，整數可作為 `u_int0` 到 `u_int7` 使用。預設值：0。 |
| `布林值` | BOOLEAN | 否 | 0 至 8 個布林值 | 著色器的布林統一值。在著色器程式碼中，布林值可作為 `u_bool0` 到 `u_bool7`（bool）使用。預設值：False。 |
| `曲線` | CURVE | 否 | 0 至 8 條曲線 | 著色器的曲線統一值。在著色器程式碼中，曲線可作為 `u_curve0` 到 `u_curve7`（sampler2D，1D LUT）使用。使用 `texture(u_curve0, vec2(x, 0.5)).r` 進行取樣。 |

**注意事項：**

* 僅在 `size_mode` 設為 `"custom"` 時，`width` 和 `height` 參數才為必要且可見。
* 至少需要一張輸入影像。
* 著色器程式碼始終可以存取包含輸出尺寸的 `u_resolution`（vec2）統一值。
* 最多可提供 8 張輸入影像、8 個浮點數統一值、8 個整數統一值、8 個布林統一值和 8 條曲線統一值。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `影像1` | IMAGE | 來自著色器的第一張輸出影像。可透過著色器程式碼中的 `layout(location = 0) out vec4 fragColor0` 使用。 |
| `影像2` | IMAGE | 來自著色器的第二張輸出影像。可透過著色器程式碼中的 `layout(location = 1) out vec4 fragColor1` 使用。 |
| `影像3` | IMAGE | 來自著色器的第三張輸出影像。可透過著色器程式碼中的 `layout(location = 2) out vec4 fragColor2` 使用。 |
| `IMAGE3` | IMAGE | 來自著色器的第四張輸出影像。可透過著色器程式碼中的 `layout(location = 3) out vec4 fragColor3` 使用。 |

---
**Source fingerprint (SHA-256):** `7830977409a5efab205b7c927eb83499a9e1e8299959b34643c9c3f1f586c058`
