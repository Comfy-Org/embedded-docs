# Tripo: 重新定位骨架模型

`TripoRetargetNode` 會將預設動畫套用到既有的已綁定骨架 3D 模型。它會取得先前已綁定骨架模型的任務 ID，向 Tripo API 傳送重新定向要求，並下載產生的動畫檔案。動畫模型可以 GLB 或 FBX 格式傳回，並可選擇是否包含網格幾何，以及是否進行原地播放。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | 要重新定向的先前已綁定骨架 3D 模型的任務 ID。所引用的任務必須是骨架綁定任務。 | RIG_TASK_ID | 是 | - |
| `animation` | 要套用到已綁定骨架模型的動畫預設。`preset:*` 動畫可用於兩種骨架模型。`preset:biped:*` 動畫是為 model v1.0-20240301 的骨架所製作；v2.5 骨架僅接受 chop、climb、dive、fall、hurt、idle、jump、run、shoot、slash、turn 和 walk。 | COMBO | 是 | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>以及使用者介面中顯示的其他 `"preset:biped:*"` 選項 |
| `out_format` | 輸出檔案格式；結果會出現在對應的輸出。(預設：glb) | COMBO | 否 | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | 匯出時包含網格；關閉時僅匯出動畫骨架。(預設：True) | BOOLEAN | 否 | True<br>False |
| `animate_in_place` | 在原處播放動畫，不進行根節點位移。(預設：False) | BOOLEAN | 否 | True<br>False |
| `auth_token_comfy_org` | 用於 Comfy.org API 存取的驗證權杖（隱藏參數）。 | AUTH_TOKEN_COMFY_ORG | 否 | - |
| `api_key_comfy_org` | 用於 Comfy.org 服務存取的 API 金鑰（隱藏參數）。 | API_KEY_COMFY_ORG | 否 | - |
| `unique_id` | 用於追蹤操作的唯一識別碼（隱藏參數）。 | UNIQUE_ID | 否 | - |

注意：`preset:*` 群組中的動畫可用於兩種骨架模型。`preset:biped:*` 群組中的動畫是為 model v1.0-20240301 的骨架所製作；v2.5 骨架僅接受 chop、climb、dive、fall、hurt、idle、jump、run、shoot、slash、turn 和 walk。如果引用的骨架是使用 Mixamo 規格與開頭為 `v1.0` 的模型版本所建立，重新定向呼叫會失敗並發生錯誤。要求的輸出格式必須是 GLB 或 FBX；如果服務傳回任何其他檔案類型，此節點會引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 產生的動畫 3D 模型檔案（僅供回溯相容使用）。 | STRING |
| `retarget task_id` | 用於追蹤重新定向操作的任務 ID。 | RETARGET_TASK_ID |
| `GLB` | GLB 格式的動畫 3D 模型。當 `out_format` 為 glb 時填入。 | FILE3DGLB |
| `FBX` | FBX 格式的動畫 3D 模型。當 `out_format` 為 fbx 時填入。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`
