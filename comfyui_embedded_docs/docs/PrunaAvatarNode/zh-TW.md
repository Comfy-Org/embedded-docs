# Pruna P-Video-2 Pro Avatar

使用 Pruna P-Video-2 Pro Avatar 將人像轉換成會說話的影片。你可以透過文字轉語音朗讀腳本，或連接自己的音訊，讓人物對嘴。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 影片起始所使用的人像。會保留 1:2 至 4:1 的長寬比；更極端的影像（例如 1:5）會裁切為 9:16 或 16:9。 | IMAGE | 是 | - |
| `語音` | 使用文字轉語音腳本或自己的音訊來驅動影片。選取選項後，其下方會顯示對應的輸入。 | DYNAMIC_COMBO | 是 | `"script"`<br>`"audio"` |
| `提示詞` | 描述影片內容（預設："The person is talking."）。最多 5000 個字元。 | STRING | 是 | 最多 5000 個字元 |
| `解析度` | 輸出解析度（預設：`"768p"`）。1080p、2k 和 4k 會將生成的 768p 影片進行放大。 | COMBO | 是 | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `enhance_prompt` | 將人像中可見的動態（例如背景、光線和身體動作）加入提示詞（預設：True）。進階設定。 | BOOLEAN | 是 | `True`<br>`False` |
| `seed` | 生成用的種子（預設：42）。只有在關閉 `enhance_prompt` 時，相同的種子才能精確重現結果。 | INT | 是 | 0 至 2147483647<br>步進值：1 |

### `"script"` 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `指令碼` | 人物所說的詞句。影片長度會與語音長度一致，超過 3 分鐘的語音會截斷至 3 分鐘。 | STRING | 是 | 任意文字 |
| `聲音` | 用於語音的嗓音（預設：`"Zephyr (Female)"`）。 | COMBO | 是 | 30 種預設語音 |
| `語言` | 腳本朗讀所用的語言（預設：`"English (US)"`）。 | COMBO | 是 | `"English (US)"`<br>`"English (UK)"`<br>`"Spanish"`<br>`"French"`<br>`"German"`<br>`"Italian"`<br>`"Portuguese (Brazil)"`<br>`"Japanese"`<br>`"Korean"`<br>`"Hindi"` |
| `voice_prompt` | 腳本的朗讀方式：語氣、節奏、口音、情緒（預設："Say the following."）。這段文字本身不會被朗讀。 | STRING | 是 | 任意文字 |

### `"audio"` 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `speech.audio` | 人物要對嘴的語音。影片長度會與其長度一致。 | AUDIO | 是 | 至少 1 秒 |

**注意事項：**

- 較大的輸出會限制音訊長度：2k 最多接受 150 秒的音訊，4k 最多接受 60 秒。在這些解析度下，較長的音訊會使節點停止並報錯，因此請使用較低的解析度或較短的片段。
- 人像的長寬比會決定輸出畫面的形狀。非常高或非常寬的人像會被裁切，而不是補邊，因此請讓主體遠離邊緣。
- 關閉 `enhance_prompt` 時，提示詞會完全依照原樣使用，這正是讓相同的 `seed` 能精確重現結果的原因。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `video` | 從人像生成的說話影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaAvatarNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `58efc7a110734f8da0a771371c5230908bf8226a946d69c5315e51e259630043`
