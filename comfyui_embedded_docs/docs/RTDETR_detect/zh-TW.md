> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/zh-TW.md)

RT-DETR Detect 節點使用 RT-DETR 模型對輸入圖像進行物件偵測。它能識別物件、繪製邊界框，並根據 COCO 資料集的類別進行標註。您可以透過置信度分數、物件類別來篩選結果，並限制偵測到的總數。

## 輸入參數

| 參數 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | N/A | 用於物件偵測的 RT-DETR 模型。 |
| `image` | IMAGE | 是 | N/A | 要進行物件偵測的輸入圖像。此節點最多以 32 張圖像為一批進行處理。 |
| `threshold` | FLOAT | 否 | N/A | 偵測結果必須達到的最低置信度分數才能被納入結果中（預設值：0.5）。 |
| `class_name` | COMBO | 否 | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` | 按類別篩選偵測結果。設定為 'all' 以停用篩選（預設值："all"）。 |
| `max_detections` | INT | 否 | N/A | 每張圖像返回的最大偵測數量。按置信度分數降序排列（預設值：100）。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `bboxes` | BOUNDINGBOX | 每個輸入圖像的邊界框列表。每個框包含座標 (x, y, width, height)、類別標籤和置信度分數。 |