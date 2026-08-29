# PixVerse V6 融合（參考資料轉影片）

PixVerse V6 Fusion（Reference to Video）使用 PixVerse 根據參考主體、背景與影片組合成一部影片。透過在提示詞中命名參考對象來將其放入場景，例如：'@Subject1 walks through @Background1'。連接參考影片會將模型切換為 Omni 模式，此模式下的輸出長度會對齊最長的參考影片。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 模型與生成設定。選擇模型並在下方顯示其生成設定。唯一可用的選項是「PixVerse V6」。 | DYNAMIC_COMBO | 是 | "PixVerse V6" |

### PixVerse V6 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的提示詞。引用已連接的參考內容時使用 @Subject1、@Background1、@Video1。預設值：空。 | STRING | 是 | 1 至 5000 個字元 |
| `aspect_ratio` | 輸出縱橫比。僅當至少連接一個參考影片時，才允許使用「auto」選項。 | COMBO | 是 | "auto"<br>加上預先定義的 PixVerse V6 縱橫比 |
| `quality` | 輸出解析度。設定長邊：360p 為 640px，540p 為 1024px，720p 為 1280px，1080p 為 1920px。預設值：「720p」。 | COMBO | 是 | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | 生成影片的長度（秒）。當連接參考影片時，輸出長度改為對齊最長的參考影片，並忽略此設定。預設值：5。 | INT | 是 | 1 至 15 |
| `generate_audio` | 與影片一同生成原生音訊軌道。預設值：True。 | BOOLEAN | 是 | True<br>False |
| `seed` | 影片生成的種子。PixVerse 會記錄此種子，但不會用它來重現一次執行。預設值：42。 | INT | 是 | 0 至 2147483647 |
| `negative_prompt` | 影片中不希望出現元素的選用文字描述。預設值：空。 | STRING | 否 | 最多 2048 個字元 |
| `style` | 套用至整部影片的選用視覺風格。預設值：「none」。 | COMBO | 否 | "none"<br>加上預先定義的 PixVerse V6 風格 |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `主體` | 可擴充插槽：連接要放入場景中的主體參考影像。插槽命名為 subject1 至 subject8；在提示詞中以 @Subject1、@Subject2 等來引用它們。 | IMAGE | 否 | 0 至 8 張影像 |
| `背景` | 可擴充插槽：連接主體所在場景的參考影像。插槽命名為 background1 至 background2；在提示詞中以 @Background1、@Background2 來引用它們。 | IMAGE | 否 | 0 至 2 張影像 |
| `影片` | 可擴充插槽：連接參考影片，以從中借用主體、動作、構圖或風格。插槽命名為 video1 至 video2；在提示詞中以 @Video1、@Video2 來引用它們。每部影片的長度最多 15 秒，且總時長不得超過 15 秒。至少連接一部影片會將節點切換為 Omni 模式。 | VIDEO | 否 | 0 至 2 部影片<br>每部最多 15 秒<br>總計最多 15 秒 |

注意：請至少連接一個主體、背景或參考影片。提示詞中的參考標籤（例如 @Subject1、@Background1、@Video1）必須對應已連接的插槽，否則請求將被拒絕。當至少連接一個參考影片時（Omni 模式），輸出長度對齊最長的參考影片，`duration_seconds` 會被忽略，`aspect_ratio` 可設為「auto」，並接受最多 10 張參考影像。若沒有參考影片，則最多接受 7 張參考影像（主體與背景合計），且不允許使用「auto」縱橫比。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的融合影片，從 PixVerse 下載。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FusionVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a83ef07f6f1918921e93fa67c2eca351754794f629aa216ccff21ce80901aebd`
