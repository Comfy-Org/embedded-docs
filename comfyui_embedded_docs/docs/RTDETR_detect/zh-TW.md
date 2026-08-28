# RT-DETR 偵測

RT-DETR Detect 節點使用 RT-DETR 模型對輸入影像執行物體偵測。它會識別物體、傳回包圍它們的邊界框，並根據 COCO 資料集類別為它們標記。您可以透過信心分數、物體類別來篩選結果，並限制偵測總數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於物體偵測的 RT-DETR 模型。 | MODEL | 是 | N/A |
| `圖像` | 要偵測物體的輸入影像。此節點會以每批最多 32 張影像的方式處理。 | IMAGE | 是 | N/A |
| `閾值` | 偵測必須達到的最低信心分數，才能納入結果（預設：0.5）。 | FLOAT | 否 | N/A |
| `類別名稱` | 依類別篩選偵測。設為 'all' 以停用篩選（預設："all"）。 | COMBO | 否 | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `最大偵測數` | 每張影像要傳回的最大偵測數。依信心分數遞減排序（預設：100）。 | INT | 否 | N/A |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `bboxes` | 每個輸入影像的邊界框清單。每個框包含座標 (x, y, width, height)、類別標籤和信心分數。 | BOUNDINGBOX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/zh-TW.md)

---
**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`
