> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/zh-TW.md)

根據提示和輸出設定同步生成影片。此節點使用文字描述和各種生成參數來創建影片內容，在生成過程完成後產生最終的影片輸出。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 影片生成的提示詞（預設：空字串） |
| `model` | COMBO | 是 | 多個選項可用 | 要使用的影片生成模型 |
| `aspect_ratio` | COMBO | 是 | 多個選項可用 | 生成影片的長寬比（預設：16:9） |
| `resolution` | COMBO | 是 | 多個選項可用 | 影片的輸出解析度（預設：540p） |
| `duration` | COMBO | 是 | 多個選項可用 | 生成影片的持續時間 |
| `loop` | BOOLEAN | 是 | - | 影片是否應該循環播放（預設：False） |
| `seed` | INT | 是 | 0 到 18446744073709551615 | 決定節點是否應重新執行的種子值；無論種子為何，實際結果都是非確定性的（預設：0） |
| `luma_concepts` | CUSTOM | 否 | - | 可選的攝影機概念，透過 Luma Concepts 節點來控制攝影機運動 |

**注意：** 當使用 `ray_1_6` 模型時，`duration` 和 `resolution` 參數會自動設為 None 且不影響生成過程。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案 |