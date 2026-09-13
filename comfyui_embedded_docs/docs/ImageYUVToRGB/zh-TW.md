# YUV 轉 RGB

ImageYUVToRGB 節點會將 YUV 色彩空間的影像轉換為 RGB 色彩空間。它接收三張分別代表 Y（亮度）、U（藍色投影）與 V（紅色投影）分量的輸入影像，並將它們合併為單一張 RGB 影像。

## 輸入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `Y` | Y（亮度）分量的輸入影像。若影像的通道數超過三個，僅會使用前三個通道，並將其平均為單一通道。 | IMAGE | 是 | - |
| `U` | U（藍色投影）分量的輸入影像。若影像的通道數超過三個，僅會使用前三個通道，並將其平均為單一通道。 | IMAGE | 是 | - |
| `V` | V（紅色投影）分量的輸入影像。若影像的通道數超過三個，僅會使用前三個通道，並將其平均為單一通道。 | IMAGE | 是 | - |

**注意：** 三張輸入影像（Y、U 與 V）必須同時提供，且必須具備相容的尺寸（高度、寬度與批次大小皆須相符），轉換才能成功。

## 輸出

| Output Name | Description | Data Type |
| --- | --- | --- |
| `output` | 轉換後的 RGB 影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/zh-TW.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
