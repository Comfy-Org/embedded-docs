# CLIP-Textkodierung (Controlnet)

Der Node CLIP Text Encode (Controlnet) kodiert einen Text-Prompt mit einem CLIP-Modell und fügt die resultierende Textkodierung vorhandenen Conditioning-Daten hinzu. Er speichert die Text-Embeddings als ControlNet-Cross-Attention-Parameter innerhalb jedes Conditioning-Eintrags, sodass das zurückgegebene Conditioning diese zusätzlichen ControlNet-Informationen enthält.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, das für die Text-Tokenisierung und -Kodierung verwendet wird | CLIP | Ja | - |
| `conditioning` | Vorhandene Conditioning-Daten, die mit der CLIP-Textkodierung kombiniert werden sollen | CONDITIONING | Ja | - |
| `text` | Der Text-Prompt, der vom CLIP-Modell verarbeitet werden soll. Unterstützt mehrzeiligen Text und dynamische Prompts | STRING | Ja | - |

**Hinweis:** Alle drei Eingaben (`clip`, `conditioning` und `text`) sind erforderlich, damit dieser Node funktioniert. Die Eingabe `text` unterstützt mehrzeiligen Text und dynamische Prompts für eine flexible Textverarbeitung. Dieser Node ist im Quellcode als experimentell gekennzeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Erweiterte Conditioning-Daten mit den zusätzlichen ControlNet-Cross-Attention-Parametern (`cross_attn_controlnet` und `pooled_output_controlnet`), die aus der CLIP-Textkodierung abgeleitet werden | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/de.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
