> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/zh-TW.md)

此節點主要用於獨立載入 CLIP 文字編碼器模型。
模型檔案可以在以下路徑中偵測到：

- "ComfyUI/models/text_encoders/"
- "ComfyUI/models/clip/"

> 如果在 ComfyUI 啟動後儲存了模型，您需要重新整理 ComfyUI 前端以取得最新的模型檔案路徑清單

支援的模型格式：

- `.ckpt`
- `.pt`
- `.pt2`
- `.bin`
- `.pth`
- `.safetensors`
- `.pkl`
- `.sft`

有關最新模型檔案載入的更多詳細資訊，請參閱 [folder_paths](https://github.com/comfyanonymous/ComfyUI/blob/master/folder_paths.py)

## 輸入參數

| 參數名稱      | 資料類型        | 描述 |
|---------------|---------------|-------------|
| `clip_name`   | COMBO[STRING] | 指定要載入的 CLIP 模型名稱。此名稱用於在預先定義的目錄結構中定位模型檔案。 |
| `type`        | COMBO[STRING] | 決定要載入的 CLIP 模型類型。隨著 ComfyUI 支援更多模型，新的類型將會新增至此。詳細資訊請查閱 [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py) 中的 `CLIPLoader` 類別定義。 |
| `device`      | COMBO[STRING] | 選擇載入 CLIP 模型的裝置。`default` 會在 GPU 上執行模型，而選擇 `CPU` 則會強制在 CPU 上載入。 |

### 裝置選項說明

**何時選擇 "default"：**

- 擁有足夠的 GPU 記憶體
- 想要最佳效能
- 讓系統自動最佳化記憶體使用

**何時選擇 "cpu"：**

- GPU 記憶體不足
- 需要為其他模型（如 UNet）保留 GPU 記憶體
- 在低 VRAM 環境中執行
- 除錯或特殊用途需求

**效能影響**

在 CPU 上執行會比 GPU 慢很多，但可以為其他更重要的模型元件節省寶貴的 GPU 記憶體。在記憶體受限的環境中，將 CLIP 模型放在 CPU 上是常見的最佳化策略。

### 支援的組合

| 模型類型 | 對應編碼器 |
|------------|---------------------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl/ clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |

隨著 ComfyUI 更新，這些組合可能會擴展。詳細資訊請參閱 [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py) 中的 `CLIPLoader` 類別定義

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
|-----------|-----------|-------------|
| `clip`    | CLIP      | 已載入的 CLIP 模型，準備好用於下游任務或進一步處理。 |

## 補充說明

CLIP 模型在 ComfyUI 中作為文字編碼器扮演核心角色，負責將文字提示轉換為擴散模型能夠理解的數值表示。您可以將它們視為翻譯器，負責將您的文字翻譯成大型模型能夠理解的語言。當然，不同的模型有自己的「方言」，因此不同架構之間需要不同的 CLIP 編碼器來完成文字編碼過程。