## 概述
LatentFlip 節點旨在透過垂直或水平翻轉來操控潛在表示。此操作允許轉換潛在空間，可能發掘資料中的新變化或視角。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `樣本` | 「samples」參數代表要進行翻轉的潛在表示。翻轉操作會根據「flip_method」參數，垂直或水平地改變這些表示，從而轉換潛在空間中的資料。 | `LATENT` |
| `翻轉方法` | 「flip_method」參數指定潛在樣本將沿哪個軸進行翻轉。可以是「x-axis: vertically」（x軸：垂直）或「y-axis: horizontally」（y軸：水平），決定翻轉的方向，進而決定應用於潛在表示的轉換性質。 | COMBO[STRING] |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `latent` | 輸出是輸入潛在表示的修改版本，已根據指定的方法進行翻轉。此轉換可以在潛在空間中引入新的變化。 | `LATENT` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFlip/zh-TW.md)
