# Comfy Cloud Mage Flow Turbo 文字轉影像 [測試版]

此 Comfy Cloud 節點使用 Mage-Flow Turbo 工作流程（`mage-flow-turbo/text-to-image`）從文字提示生成影像。它執行 Mage-Flow 模型的蒸餾版本，以 4 步且 `cfg` 值為 1 生成影像，約只需完整執行一次 Mage-Flow 的 GPU 時間的七分之一，這使其成為專為快速迭代設計的變體。

## 輸入

節點類別本身在可取得的原始碼中並未宣告輸入小工具；其輸入結構定義繼承自共享基底類別 `_ComfyCloudMageFlowNode`，而該類別的定義未包含在原始碼快照中。根據節點摘要與 text-to-image 工作流程名稱，此節點接收一段描述要生成影像的文字提示。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 用於描述要生成影像的文字提示。確切的參數名稱由繼承的 `_ComfyCloudMageFlowNode` 基底結構定義設定，可能與此標籤不同。 | STRING | 是 | 自由文字 |

注意：繼承的基底節點定義中可能還有其他輸入參數，但提供的原始碼中並未包含該定義。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 根據文字提示生成的影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTurboTextToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8d867a0c906028597ef52c75f5c9a994fdc00211c7aae410ffca8204943f0c34`
