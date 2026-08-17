# RT-DETR 偵測

RT-DETR Detect 節點使用 RT-DETR 模型對輸入圖像執行物體偵測。它會在圖像中找出物體，並傳回每個偵測結果的邊界框座標，標記對應的 COCO 資料集類別。您可以透過置信度和物體類別篩選結果，並限制每張圖像傳回的偵測總數。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於物體偵測的 RT-DETR 模型。 | MODEL | 是 | N/A |
| `image` | 要偵測物體的輸入圖像。此節點會以最多 32 張圖像為一批進行處理，並在內部調整大小以進行偵測。 | IMAGE | 是 | N/A |
| `threshold` | 偵測結果必須達到的最低置信度，才會納入結果（預設值：0.5）。 | FLOAT | 是 | N/A |
| `class_name` | 依類別篩選偵測結果。設為 'all' 以停用篩選（預設值："all"）。 | COMBO | 是 | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `max_detections` | 每張圖像傳回的最大偵測數目。依置信度遞減順序排列（預設值：100）。 | INT | 是 | N/A |

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `bboxes` | 每個輸入圖像的邊界框列表。每個框包含座標（x, y, width, height）、類別標籤和置信度分數。 | BOUNDINGBOX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/zh-TW.md)

---
**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`
