# LoraModelLoader

Der Node LoraModelLoader wendet trainierte LoRA-Gewichte (Low-Rank Adaptation) auf ein Diffusionsmodell an. Er modifiziert das Basismodell, indem er LoRA-Gewichte aus einem trainierten LoRA-Modell lädt und deren Einflussstärke anpasst. Dadurch können Sie das Verhalten von Diffusionsmodellen anpassen, ohne sie von Grund auf neu zu trainieren, einschließlich eines Bypass-Modus, der die Gewichte des Basismodells unverändert lässt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, auf das die LoRA angewendet wird. | MODEL | Ja | - |
| `lora` | Das LoRA-Modell, das auf das Diffusionsmodell angewendet wird. | LORA_MODEL | Ja | - |
| `strength_model` | Wie stark das Diffusionsmodell verändert wird. Dieser Wert kann negativ sein (Standard: 1.0). | FLOAT | Ja | -100.0 bis 100.0 |
| `bypass` | Wenn aktiviert, wird LoRA im Bypass-Modus angewendet, ohne die Gewichte des Basismodells zu verändern. Nützlich für das Training und wenn Modellgewichte ausgelagert (offloaded) sind (Standard: False). | BOOLEAN | Ja | True or False |

**Hinweis:** Wenn `strength_model` auf 0 gesetzt ist, gibt der Node das ursprüngliche Modell zurück, ohne LoRA-Änderungen anzuwenden.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Diffusionsmodell mit angewendeten LoRA-Gewichten. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/de.md)

---
**Source fingerprint (SHA-256):** `81eb2a9b0376fe7453f6e7e422414472e80a3d1b92bb6874b91df6de8aed0d9a`
