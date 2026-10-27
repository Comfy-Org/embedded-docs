# Patina PBR Material Maps

從既有紋理影像衍生出一組 PBR 材質貼圖：basecolor、normal、roughness、metalness 與 height。僅啟用所需的貼圖，因為每張啟用的貼圖都會增加成本。可用於補全尚無材質貼圖的紋理，或重建單一損壞的貼圖。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 用來衍生 PBR 貼圖的照片或渲染圖。 | IMAGE | 是 | - |
| `basecolor` | 生成基礎色（albedo）貼圖。預設值：True。 | BOOLEAN | 是 | true<br>false |
| `normal` | 生成法線貼圖。預設值：True。 | BOOLEAN | 是 | true<br>false |
| `roughness` | 生成粗糙度貼圖。預設值：False。 | BOOLEAN | 是 | true<br>false |
| `metalness` | 生成金屬度貼圖。預設值：False。 | BOOLEAN | 是 | true<br>false |
| `height` | 生成高度（置換）貼圖。預設值：False。 | BOOLEAN | 是 | true<br>false |
| `seed` | 用於可重現去噪結果的種子。預設值：42。 | INT | 是 | 0 至 2147483646 |
| `safety_checker` | 對請求執行提供者的內容安全檢查。進階設定。預設值：False。 | BOOLEAN | 是 | true<br>false |
| `auto_downscale` | 自動將最長邊超過 2048 像素（模型輸入上限）的輸入影像縮小，同時維持長寬比；較小的影像則維持不變。停用此選項時，過大的影像將會引發錯誤。進階設定。預設值：True。 | BOOLEAN | 否 | true<br>false |

**限制與行為：**

* 至少必須啟用一張貼圖，否則執行會失敗。
* 輸入影像的最長邊限制為 2048 像素；請讓 `auto_downscale` 將其縮小，否則過大的影像會導致執行失敗。
* 每張已停用的貼圖仍會傳回一個輸出，但會是 1x1 的佔位影像，因此請只連接你實際生成的輸出。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `basecolor` | 生成的基礎色（albedo）貼圖；若該貼圖已停用，則為 1x1 佔位影像。 | IMAGE |
| `normal` | 生成的法線貼圖；若該貼圖已停用，則為 1x1 佔位影像。 | IMAGE |
| `roughness` | 生成的粗糙度貼圖；若該貼圖已停用，則為 1x1 佔位影像。 | IMAGE |
| `metalness` | 生成的金屬度貼圖；若該貼圖已停用，則為 1x1 佔位影像。 | IMAGE |
| `height` | 生成的高度（置換）貼圖；若該貼圖已停用，則為 1x1 佔位影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaPBRMapsNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `813c5bb3336c5ca54a9ca9ee95e84e7f27791170650248d0169acee39c4b3ce1`
