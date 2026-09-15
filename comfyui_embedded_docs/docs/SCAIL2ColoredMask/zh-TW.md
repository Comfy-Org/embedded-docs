# 建立 SCAIL-2 彩色遮罩

此節點將 SAM3 追蹤資料渲染為彩色遮罩，供 WanSCAILToVideo 節點使用。它會處理來自驅動姿態影片的追蹤資料，以及可選的參考影像，並為兩個輸出中的每位被追蹤人物指派一致的顏色。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `驅動追蹤資料` | 驅動姿態影片的 SAM3 追蹤資料。將渲染到 `pose_video_mask` 輸出。 | SAM3_TRACK_DATA | 是 | - |
| `參考追蹤資料` | 參考影像的 SAM3 追蹤資料（每個物件一個身分，依批次順序上色），或參考主體的純 MASK（渲染為單一身分）。 | SAM3_TRACK_DATA or MASK | 否 | - |
| `物件索引` | 以逗號分隔的要包含的人物索引清單（例如 '0,2,3'）。同時套用於參考和姿態影片遮罩。空白 = 全部。（預設值：""） | STRING | 是 | - |
| `排序方式` | 調色盤顏色指派給被追蹤物件的順序（同時套用於參考和姿態影片，讓每個身分保持相同顏色）。出現在較早影格中的物件一律優先；在同一影格內，left_to_right = 最左側物件（依首次出現時的質心）取得第一個顏色，area = 最大物件（依首次出現時的遮罩面積）取得第一個顏色；none = 保持 SAM3 的順序。（預設值："left_to_right"） | COMBO | 是 | `"none"`<br>`"left_to_right"`<br>`"area"` |
| `替換模式` | False = 動畫模式（`pose_video_mask` 為黑色背景，`reference_image_mask` 為白色背景）。True = 替換模式（`pose_video_mask` 為白色背景，`reference_image_mask` 為黑色背景）。（預設值：False） | BOOLEAN | 是 | False<br>True |

注意：`object_indices` 僅接受以逗號分隔的數字；非數字項目和超出範圍的索引會被忽略。當未提供 `ref_track_data` 時，`reference_image_mask` 輸出會使用參考背景色純色填滿（動畫模式為白色，替換模式為黑色）。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `pose_video_mask` | 從驅動姿態影片追蹤資料渲染而成的彩色遮罩。背景顏色依 `replacement_mode` 設定。 | IMAGE |
| `reference_image_mask` | 從參考影像追蹤資料渲染而成的彩色遮罩。背景在替換模式為黑色，在動畫模式為白色。如果未提供參考資料，則傳回符合參考背景色的純色填滿。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ce0669ad0ed3c76cc18ef0ee7b620f5aa6eaa1e5b96c189941c0a5b744c3351f`
