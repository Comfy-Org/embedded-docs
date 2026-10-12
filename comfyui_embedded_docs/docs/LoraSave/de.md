# LoraSave

Der LoraSave-Node extrahiert und speichert LoRA-Dateien (Low-Rank Adaptation) aus Modelldifferenzen. Er kann Differenzen von Diffusionsmodellen, Text-Encoder-Differenzen oder beides verarbeiten und sie in das LoRA-Format mit angegebenem Rang und Typ umwandeln. Die resultierende LoRA-Datei wird im Ausgabeverzeichnis zur späteren Verwendung gespeichert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `filename_prefix` | Das Präfix für den Ausgabedateinamen (Standard: "loras/ComfyUI_extracted_lora") | STRING | Ja | - |
| `rank` | Der Rangwert für das LoRA, der Größe und Komplexität steuert (Standard: 8) | INT | Ja | 1-4096 |
| `lora_type` | Der Typ des zu erstellenden LoRA. "standard" extrahiert niedrigrangige Matrizen über SVD; "full_diff" speichert die vollständige Gewichtsdifferenz (Standard: "standard") | COMBO | Ja | `"standard"`<br>`"full_diff"` |
| `bias_diff` | Ob Bias-Differenzen in die LoRA-Berechnung einbezogen werden (Standard: True) | BOOLEAN | Ja | - |
| `model_diff` | Die ModelSubtract-Ausgabe, die in ein LoRA umgewandelt werden soll | MODEL | Nein | - |
| `text_encoder_diff` | Die CLIPSubtract-Ausgabe, die in ein LoRA umgewandelt werden soll | CLIP | Nein | - |

**Hinweis:** Mindestens eines von `model_diff` oder `text_encoder_diff` muss angegeben werden, damit der Node funktioniert. Wenn beide weggelassen werden, erzeugt der Node keine Ausgabe.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| - | Dieser Node speichert eine LoRA-Datei im Ausgabeverzeichnis, gibt jedoch keine Daten über den Workflow zurück | - |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/de.md)

---
**Source fingerprint (SHA-256):** `642510bfe083130cb2724d7ae38d30d4694c85a43c7ce27230690ddd9fe76b79`
