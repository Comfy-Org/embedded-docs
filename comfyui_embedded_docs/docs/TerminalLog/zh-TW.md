> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TerminalLog/zh-TW.md)

Terminal Log (Manager) 節點主要用於在 ComfyUI 介面內的終端機中顯示 ComfyUI 的執行資訊。使用時需要將 `mode` 設定為 **logging** 模式，這樣它就能在圖片生成任務中記錄相應的日誌資訊。如果將 `mode` 設定為 **stop** 模式，則不會記錄日誌資訊。
當您透過遠端連線或區域網路連線存取和使用 ComfyUI 時，Terminal Log (Manager) 節點就顯得特別有用。它讓您能夠直接在 ComfyUI 介面中查看來自 CMD 的錯誤訊息，更方便地了解 ComfyUI 目前的執行狀態。