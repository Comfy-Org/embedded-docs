> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3D/zh-TW.md)

## 節點概述

Preview3D 節點主要用於預覽 3D 模型輸出。此節點接收兩個輸入：一個是來自 Load3D 節點的 `camera_info`，另一個是 3D 模型檔案的路徑。模型檔案路徑必須位於 `ComfyUI/output` 資料夾內。

**支援格式**
目前此節點支援多種 3D 檔案格式，包括 `.gltf`、`.glb`、`.obj`、`.fbx` 和 `.stl`。

**3D 節點偏好設定**
部分 3D 節點的相關偏好設定可在 ComfyUI 的設定選單中進行配置。請參考以下文件進行相應設定：
[設定選單](https://docs.comfy.org/interface/settings/3d)

## 輸入參數

| 參數名稱      | 類型           | 描述                                  |
| ------------- | -------------- | ------------------------------------- |
| camera_info   | LOAD3D_CAMERA  | 攝影機資訊                            |
| model_file    | LOAD3D_CAMERA  | `ComfyUI/output/` 下的模型檔案路徑    |

## 畫布區域說明

目前 ComfyUI 前端中的 3D 相關節點共用同一個畫布元件，因此除了部分功能差異外，其基本操作大多一致。

> 以下內容與介面主要以 Load3D 節點為基礎，具體功能請以實際節點介面為準。

畫布區域包含多種視圖操作，例如：

- 預覽視圖設定（網格、背景顏色、預覽視圖）
- 攝影機控制：FOV、攝影機類型
- 全域光照強度：調整照明
- 模型匯出：支援 `GLB`、`OBJ`、`STL` 格式
- 等

![Load 3D 節點介面](./asset/preview3d_canvas.jpg)

1. 包含 Load3D 節點的多個選單和隱藏選單
2. 3D 視圖操作軸

### 1. 視圖操作

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/view_operations.mp4" type="video/mp4">
  您的瀏覽器不支援影片播放。
</video>

視圖控制操作：

- 左鍵點擊 + 拖曳：旋轉視圖
- 右鍵點擊 + 拖曳：平移視圖
- 中鍵滾輪滾動或中鍵點擊 + 拖曳：縮放視圖
- 座標軸：切換視圖

### 2. 左側選單功能

![選單](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

在預覽區域中，部分視圖操作選單隱藏在選單中。點擊選單按鈕可展開不同選單。

- 1. 場景：包含預覽視窗網格、背景顏色、縮略圖設定
- 2. 模型：模型渲染模式、紋理材質、上方向設定
- 3. 攝影機：切換正交與透視視圖，設定透視角度
- 4. 光源：場景全域光照強度
- 5. 匯出：將模型匯出為其他格式（GLB、OBJ、STL）

#### 場景

![場景選單](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

場景選單提供一些基本場景設定功能：

1. 顯示/隱藏網格
2. 設定背景顏色
3. 點擊上傳背景圖片
4. 隱藏預覽縮略圖

#### 模型

![模型選單](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

模型選單提供一些模型相關功能：

1. **上方向**：決定模型的哪個軸是上方向
2. **材質模式**：切換模型渲染模式 - 原始、法線、線框、線稿

#### 攝影機

![攝影機選單](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

此選單提供正交與透視視圖的切換，以及透視角度大小設定：

1. **攝影機**：快速切換正交與透視視圖
2. **FOV**：調整 FOV 角度

#### 光源

![光源選單](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

透過此選單，可以快速調整場景的全域光照強度

#### 匯出

![匯出選單](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

此選單提供快速轉換和匯出模型格式的功能