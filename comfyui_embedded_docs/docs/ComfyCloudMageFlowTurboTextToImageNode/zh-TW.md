# ComfyCloudMageFlowTurboTextToImageNode

此 Comfy Cloud 節點會使用 Mage-Flow Turbo 工作流程（`mage-flow-turbo/text-to-image`）從文字提示生成圖像。它執行 Mage-Flow 模型的蒸餾版本，以 cfg 值為 1 的設定在 4 個步驟內生成圖像，所需 GPU 時間約為完整 Mage-Flow 過程的七分之一，因此此變體旨在快速迭代。

## 輸入

節點類別本身並未在可用原始碼中宣告輸入小工具；其輸入結構繼承自共用基底類別 `_ComfyCloudMageFlowNode`，而該類別的定義未包含在原始碼快照中。根據節點摘要與文字轉圖像工作流程名稱，此節點接收一段描述要生成圖像的文字提示。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成之圖像的文字提示。確切參數名稱由繼承的 `_ComfyCloudMageFlowNode` 基底結構設定，可能與此標籤不同。 | STRING | 是 | 自由文字 |

注意：繼承的基底節點定義中可能存在其他輸入參數，而該定義未包含在所提供的原始碼中。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 從文字提示生成的圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTurboTextToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8d867a0c906028597ef52c75f5c9a994fdc00211c7aae410ffca8204943f0c34`
