> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/zh-TW.md)

PorterDuffImageComposite 節點專門用於執行基於 Porter-Duff 合成運算元的影像合成。它允許根據不同的混合模式組合來源影像和目標影像，透過創意性地操作影像透明度和疊加方式，實現複雜的視覺效果。

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
| --------- | ------------ | ----------- |
| `source`  | `IMAGE`     | 將要合成到目標影像上方的來源影像張量。根據所選的合成模式，它對最終視覺效果起著關鍵作用。 |
| `source_alpha` | `MASK` | 來源影像的 Alpha 通道，用於指定來源影像中每個像素的透明度。它會影響來源影像與目標影像的混合方式。 |
| `destination` | `IMAGE` | 作為背景的目標影像張量，來源影像將合成於其上方。根據混合模式的不同，它會對最終合成影像產生影響。 |
| `destination_alpha` | `MASK` | 目標影像的 Alpha 通道，用於定義目標影像像素的透明度。它會影響來源影像和目標影像的混合效果。 |
| `模式` | COMBO[STRING] | 要套用的 Porter-Duff 合成模式，此模式決定了來源影像和目標影像的混合方式。每種模式都會產生不同的視覺效果。 |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
| --------- | ------------ | ----------- |
| `image`   | `IMAGE`     | 套用指定 Porter-Duff 模式後產生的合成影像。 |
| `mask`    | `MASK`      | 合成影像的 Alpha 通道，用於指示每個像素的透明度。 |