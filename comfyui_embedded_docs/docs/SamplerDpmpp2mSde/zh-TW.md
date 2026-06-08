此節點專為生成 DPMPP_2M_SDE 模型的取樣器而設計，可根據指定的求解器類型、雜訊等級及計算裝置偏好來建立樣本。它抽象化了取樣器配置的複雜性，提供簡潔的介面以自訂設定生成樣本。

## 輸入

| 參數名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `solver_type` | 指定取樣過程中使用的求解器類型，提供 'midpoint'（中點法）與 'heun'（赫恩法）兩種選項。此選擇會影響取樣時應用的數值積分方法。 | COMBO[STRING] |
| `eta` | 決定數值積分中的步長，影響取樣過程的細緻程度。數值越高表示步長越大。 | `FLOAT` |
| `s_noise` | 控制取樣過程中引入的雜訊等級，影響生成樣本的變異性。 | `FLOAT` |
| `noise_device` | 指定執行雜訊生成程序的計算裝置（'gpu' 或 'cpu'），影響效能與效率。 | COMBO[STRING] |

## 輸出

| 參數名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sampler` | 輸出為根據指定參數配置的取樣器，可直接用於生成樣本。 | `SAMPLER` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmpp2mSde/zh-TW.md)
