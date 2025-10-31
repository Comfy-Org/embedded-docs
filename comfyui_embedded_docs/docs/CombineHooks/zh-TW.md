> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks/zh-TW.md)

{heading_overview}

Combine Hooks [2] 節點將兩個掛鉤群組合併為單一的組合掛鉤群組。它接受兩個可選的掛鉤輸入，並使用 ComfyUI 的掛鉤組合功能將它們合併。這讓您可以整合多個掛鉤配置，以實現更流暢的處理流程。

{heading_inputs}

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | 可選 | 無 | - | 要合併的第一個掛鉤群組 |
| `hooks_B` | HOOKS | 可選 | 無 | - | 要合併的第二個掛鉤群組 |

**注意：** 兩個輸入都是可選的，但必須提供至少一個掛鉤群組節點才能正常運作。如果只提供一個掛鉤群組，它將保持不變地返回。

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `hooks` | HOOKS | 包含兩個輸入群組中所有掛鉤的組合掛鉤群組 |