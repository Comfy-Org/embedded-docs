# Compose Camera Angle Prompt

此節點會選擇主體周圍的相機角度，並將該選擇轉換為兩項內容：可供 3D 節點渲染的 `camera_info` 結構，以及可直接貼入提示詞的英文鏡頭描述。主體位於場景原點，下游 3D 節點會將其模型置中於此，因此你在此選擇的角度會與預覽相符。

用它來在生成前為渲染取景，或為影像或影片模型描述視角，例如 `front view eye-level shot medium shot`。節點中的 3D 預覽會顯示產生的相機位置。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `horizontal_angle` | 圍繞主體的方位角，以度為單位：0 是正面、90 是右側、180 是背面。（預設值：0） | INT | 是 | 0 至 360 |
| `vertical_angle` | 仰角，以度為單位。負值表示從下方向上看，正值表示從上方向下看。（預設值：0） | INT | 是 | -30 至 60 |
| `zoom` | 鏡頭對主體的變焦：0 是廣角鏡頭，10 是特寫。此值也會帶入 `camera_info.zoom`。（預設值：5.0） | FLOAT | 是 | 0.0 至 10.0 （步進值：0.1） |
| `image` | 選用的參考影像，會顯示在 3D 預覽中主體立方體的正面。 | IMAGE | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `camera_info` | 供 3D 節點使用的相機資訊：位置、注視目標、變焦倍率、相機類型與視野。相機維持固定的 35 度視野，並放置在距離目標 6 單位處。 | LOAD3DCAMERA |
| `prompt` | 根據角度、仰角和距離建立的簡短鏡頭描述，例如 `front view eye-level shot medium shot`。 | STRING |

## 鏡頭描述術語

`prompt` 輸出會從下列各組中分別取一個詞彙組合而成。數值會先限制在小工具範圍內。

- 水平角度分為八個 45 度區段：`front view`、`front-right quarter view`、`right side view`、`back-right quarter view`、`back view`、`back-left quarter view`、`left side view`、`front-left quarter view`。
- 垂直角度低於 -15 度時為 `low-angle shot`；否則低於 15 度時為 `eye-level shot`；否則低於 45 度時為 `elevated shot`；45 度（含）以上則為 `high-angle shot`。
- 變焦低於 2 時為 `wide shot`；否則低於 6 時為 `medium shot`；6 或以上則為 `close-up`。

`camera_info.zoom` 倍率會將小工具數值縮放到 1.0 至 1.875，因此 `zoom` 為 0 時得到 1.0，`zoom` 為 10 時得到 1.875。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CameraAngle/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8ed2cd186bc6ca02dbc8da006b2e9156245ef691a2257f286f6e32ffa480fd5d`
