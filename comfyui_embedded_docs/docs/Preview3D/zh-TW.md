> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3D/zh-TW.md)

Preview3D 節點主要用於預覽 3D 模型輸出。此節點接受兩個輸入：一個是來自 Load3D 節點的 `camera_info`，另一個是 3D 模型檔案的路徑。模型檔案路徑必須位於 `ComfyUI/output` 資料夾中。

**支援的格式**
目前，此節點支援多種 3D 檔案格式，包括 `.gltf`、`.glb`、`.obj`、`.fbx` 和 `.stl`。

**3D 節點偏好設定**
3D 節點的相關偏好設定可以在 ComfyUI 的設定選單中配置。請參考以下文件進行相應設定：
[設定選單](https://docs.comfy.org/interface/settings/3d)

## 輸入

| 參數名稱 | 類型 | 說明 |
| -------------- | -------------- | -------------------------------------------- |
| `camera_info` | LOAD3D_CAMERA | 相機資訊 |
| `model_file` | LOAD3D_CAMERA | `ComfyUI/output/` 下的模型檔案路徑 |

## 畫布區域說明

目前，ComfyUI 前端中與 3D 相關的節點共享同一個畫布元件，因此它們的基本操作除了部分功能差異外，大多保持一致。

> 以下內容與介面主要基於 Load3D 節點，具體功能請以實際節點介面為準。

畫布區域包含多種視圖操作，例如：

- 預覽視圖設定（網格、背景顏色、預覽視圖）
- 相機控制：FOV、相機類型
- 全局照明強度：調整光照
- 模型匯出：支援 `GLB`、`OBJ`、`STL` 格式
- 等等。

![Load 3D 節點 UI](./asset/preview3d_canvas.jpg)

1. 包含 Load 3D 節點的多個選單及隱藏選單
2. 3D 視圖操作軸

### 1. 視圖操作

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  您的瀏覽器不支援影片播放。
</video>

視圖控制操作：

- 滑鼠左鍵 + 拖曳：旋轉視圖
- 滑鼠右鍵 + 拖曳：平移視圖
- 滑鼠中鍵滾輪或中鍵 + 拖曳：放大/縮小
- 座標軸：切換視圖

### 2. 左側選單功能

![選單](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

在預覽區域中，部分視圖操作選單隱藏在選單中。點擊選單按鈕可展開不同的選單。

- 1. 場景：包含預覽視窗網格、背景顏色、縮圖設定
- 2. 模型：模型渲染模式、紋理材質、向上方向設定
- 3. 相機：切換正交視圖與透視視圖，設定透視角度
- 4. 光照：場景全局照明強度
- 5. 匯出：將模型匯出為其他格式（GLB、OBJ、STL）

#### 場景

![場景選單](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

場景選單提供了一些基本的場景設定功能：

1. 顯示/隱藏網格
2. 設定背景顏色
3. 點擊上傳背景圖片
4. 隱藏預覽縮圖

#### 模型

![選單_場景](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

模型選單提供了一些與模型相關的功能：

1. **向上方向**：決定模型的哪個軸為向上方向
2. **材質模式**：切換模型渲染模式 - 原始、法線、線框、線稿

#### 相機

![選單_模型_相機](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

此選單提供正交視圖與透視視圖的切換，以及透視角度大小的設定：

1. **相機**：快速切換正交視圖與透視視圖
2. **FOV**：調整 FOV 角度

#### 光照

![選單_模型_相機](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

透過此選單，您可以快速調整場景的全局照明強度

#### 匯出

![選單_匯出](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

此選單提供快速轉換和匯出模型格式的功能