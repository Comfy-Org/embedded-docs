# Kling 文字口型同步影片

Kling Lip Sync Text to Video 節點會同步影片檔案中的嘴部動作，使其符合文字提示。此節點接收輸入影片並生成新的影片，其中角色的唇部動作會與提供的文字對齊。此節點使用語音合成來建立看起來自然的語音同步效果。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 用於唇形同步的輸入影片檔案。影片高度/寬度必須介於 720px 與 1920px 之間，時長必須介於 2s 與 10s 之間，且不得大於 100MB。 | VIDEO | 是 | - |
| `文字` | 用於唇形同步影片生成的文字內容。當模式為 text2video 時為必填。最大長度為 120 個字元。 | STRING | 是 | - |
| `語音` | 唇形同步音訊的語音選擇（預設："Melody"）。包含英文與中文語音選項。 | COMBO | 否 | "Melody"<br>"Sunny"<br>"Sage"<br>"Ace"<br>"Blossom"<br>"Peppy"<br>"Dove"<br>"Shine"<br>"Anchor"<br>"Lyric"<br>"Tender"<br>"Siren"<br>"Zippy"<br>"Bud"<br>"Sprite"<br>"Candy"<br>"Beacon"<br>"Rock"<br>"Titan"<br>"Grace"<br>"Helen"<br>"Lore"<br>"Crag"<br>"Prattle"<br>"Hearth"<br>"The Reader"<br>"Commercial Lady"<br>"阳光少年"<br>"懂事小弟"<br>"运动少年"<br>"青春少女"<br>"温柔小妹"<br>"元气少女"<br>"阳光男生"<br>"幽默小哥"<br>"文艺小哥"<br>"甜美邻家"<br>"温柔姐姐"<br>"职场女青"<br>"活泼男童"<br>"俏皮女童"<br>"稳重老爸"<br>"温柔妈妈"<br>"严肃上司"<br>"优雅贵妇"<br>"慈祥爷爷"<br>"唠叨爷爷"<br>"唠叨奶奶"<br>"和蔼奶奶"<br>"东北老铁"<br>"重庆小伙"<br>"四川妹子"<br>"潮汕大叔"<br>"台湾男生"<br>"西安掌柜"<br>"天津姐姐"<br>"新闻播报男"<br>"译制片男"<br>"撒娇女友"<br>"刀片烟嗓"<br>"乖巧正太" |
| `語速` | 語速。有效範圍：0.8~2.0，精確到小數點後一位。（預設：1） | FLOAT | 否 | 0.8-2.0 |

**影片需求：**

- 影片檔案不應大於 100MB
- 高度/寬度應介於 720px 與 1920px 之間
- 時長應介於 2s 與 10s 之間

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片，包含唇形同步音訊 | VIDEO |
| `video_id` | 生成影片的唯一識別碼 | STRING |
| `duration` | 生成影片的時長資訊 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `28a7be92d7e8a57efeb7e2913124e4373dfc75fbdba6ff7036fafb3a8ae43a60`
