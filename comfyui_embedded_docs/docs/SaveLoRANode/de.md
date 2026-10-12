# SaveLoRANode

Der Node SaveLoRA speichert LoRA-Modelle (Low-Rank Adaptation) in Ihrem Ausgabeverzeichnis. Er nimmt ein LoRA-Modell als Eingabe entgegen und erstellt eine safetensors-Datei mit einem automatisch generierten Dateinamen. Sie können das Dateinamenpräfix anpassen und optional die Anzahl der Trainingsschritte im Dateinamen angeben, um eine bessere Organisation zu ermöglichen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `lora` | Das zu speichernde LoRA-Modell. Verwenden Sie nicht das Modell mit LoRA-Schichten. | LORA_MODEL | Ja | - |
| `prefix` | Das Präfix, das für die gespeicherte LoRA-Datei verwendet werden soll (Standard: "loras/ComfyUI_trained_lora"). | STRING | Ja | - |
| `steps` | Optional: Die Anzahl der Schritte, für die das LoRA-Modell trainiert wurde; wird zum Benennen der gespeicherten Datei verwendet. | INT | Nein | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| *None* | Dieser Node gibt keine Ausgaben zurück, sondern speichert das LoRA-Modell im Ausgabeverzeichnis. | - |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/de.md)

---
**Source fingerprint (SHA-256):** `06a1067433aa4b720b51050b09fbad4870caf12c5e92f788d44ea022a39efef4`
