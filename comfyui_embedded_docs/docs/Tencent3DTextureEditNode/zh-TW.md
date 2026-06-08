此節點使用騰訊混元3D API來編輯3D模型的紋理。您提供一個3D模型以及所需變更的文字描述，節點會根據您的提示重新繪製紋理，並傳回模型的新版本。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_3d` | FBX格式的3D模型。模型面數應少於100000個。 | FILE3D | 是 | FBX, 任意 |
| `prompt` | 描述紋理編輯內容。最多支援1024個UTF-8字元。 | STRING | 是 |  |
| `seed` | 種子碼控制節點是否應重新執行；無論種子碼為何，結果皆非確定性。（預設值：0） | INT | 否 | 0 至 2147483647 |

**注意：** `model_3d` 輸入必須是FBX格式的檔案。此節點不支援其他3D檔案格式。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `OBJ` | 處理後的3D模型，格式為GLB。 | FILE3D |
| `texture_image` | 處理後的3D模型，格式為OBJ。 | FILE3D |
| `texture_image` | 為3D模型新生成的紋理影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c8e81fcfc24707746b8d1291d31aff325523cd93a627b896402ce1b5a96c7e87`
