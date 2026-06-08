以下是根據您的規則和要求，將英文技術文檔翻譯成繁體中文的結果：

Load3D 節點是用於載入和處理 3D 模型檔案的核心節點。載入節點時，它會自動從 `ComfyUI/input/3d/` 擷取可用的 3D 資源。您也可以使用上傳功能上傳支援的 3D 檔案進行預覽。

**支援的格式**
目前，此節點支援多種 3D 檔案格式，包括 `.gltf`、`.glb`、`.obj`、`.fbx` 和 `.stl`。

**3D 節點偏好設定**
3D 節點的一些相關偏好設定可以在 ComfyUI 的設定選單中進行配置。請參考以下文件進行對應設定：

[設定選單](https://docs.comfy.org/interface/settings/3d)

除了常規的節點輸出之外，Load3D 在畫布選單中還有許多與 3D 檢視相關的設定。

## 輸入

| 參數名稱 | 描述 | 類型 | 預設值 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型檔案` | 3D 模型檔案路徑，支援上傳，預設從 `ComfyUI/input/3d/` 讀取模型檔案 | 檔案選擇 | - | 支援的格式 |
| `寬度` | 畫布渲染寬度 | INT | 1024 | 1-4096 |
| `高度` | 畫布渲染高度 | INT | 1024 | 1-4096 |

## 輸出

| 參數名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `遮罩` | 畫布渲染的影像 | IMAGE |
| `網格路徑` | 包含當前模型位置的遮罩 | MASK |
| `法線` | 模型檔案路徑 | STRING |
| `相機資訊` | 法線貼圖 | IMAGE |
| `錄影` | 線稿影像輸出，可在畫布模型選單中調整對應的 `edge_threshold` | IMAGE |
| `3D 模型` | 相機資訊 | LOAD3D_CAMERA |
| `model_3d_info` | 錄製的影片（僅當存在錄製時） | VIDEO |

所有輸出預覽：
![檢視操作示範](./asset/load3d_outputs.webp)

## 畫布區域說明

Load3D 節點的畫布區域包含大量的檢視操作，包括：

- 預覽檢視設定（網格、背景顏色、預覽檢視）
- 相機控制：控制視野（FOV）、相機類型
- 全局照明強度：調整光照強度
- 影片錄製：錄製並匯出影片
- 模型匯出：支援 `GLB`、`OBJ`、`STL` 格式
- 以及更多

![Load 3D 節點 UI](./asset/load3d_ui.jpg)

1. 包含 Load 3D 節點的多個選單和隱藏選單
2. `調整預覽視窗大小` 和 `畫布影片錄製` 的選單
3. 3D 檢視操作軸
4. 預覽縮圖
5. 預覽尺寸設定，透過設定尺寸然後調整視窗大小來縮放預覽檢視顯示

### 1. 檢視操作

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  您的瀏覽器不支援影片播放。
</video>

檢視控制操作：

- 滑鼠左鍵 + 拖曳：旋轉檢視
- 滑鼠右鍵 + 拖曳：平移檢視
- 滑鼠中鍵滾輪或中鍵 + 拖曳：放大/縮小
- 座標軸：切換檢視

### 2. 左側選單功能

![選單](./asset/menu.webp)

在畫布中，某些設定隱藏在選單中。點擊選單按鈕可以展開不同的選單

- 1. 場景：包含預覽視窗網格、背景顏色、預覽設定
- 2. 模型：模型渲染模式、紋理材質、向上方向設定
- 3. 相機：在正交視圖和透視視圖之間切換，並設定透視角度大小
- 4. 光照：場景全局照明強度
- 5. 匯出：將模型匯出為其他格式（GLB、OBJ、STL）

#### 場景

![場景選單](./asset/menu_scene.webp)

場景選單提供了一些基本的場景設定功能

1. 顯示/隱藏網格
2. 設定背景顏色
3. 點擊上傳背景圖片
4. 隱藏預覽

#### 模型

![模型選單](./asset/menu_model.webp)

模型選單提供了一些與模型相關的功能

1. **向上方向**：確定模型的哪個軸是向上方向
2. **材質模式**：切換模型渲染模式 - 原始、法線、線框、線稿

#### 相機

![相機選單](./asset/menu_camera.webp)

此選單提供正交視圖和透視視圖之間的切換，以及透視角度大小的設定

1. **相機**：快速在正交視圖和透視視圖之間切換
2. **視野（FOV）**：調整視野角度

#### 光照

![光照選單](./asset/menu_light.webp)

透過此選單，您可以快速調整場景的全局照明強度

#### 匯出

![匯出選單](./asset/menu_export.webp)

此選單提供了快速轉換和匯出模型格式的功能

### 3. 右側選單功能

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  您的瀏覽器不支援影片播放。
</video>

右側選單有兩個主要功能：

1. **重置檢視比例**：點擊按鈕後，檢視將根據設定的寬度和高度調整畫布渲染區域的比例
2. **影片錄製**：允許您將當前的 3D 檢視操作錄製為影片，允許匯入，並可以作為 `recording_video` 輸出到後續節點

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3D/zh-TW.md)
