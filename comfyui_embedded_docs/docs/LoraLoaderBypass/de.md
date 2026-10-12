# LoraLoaderBypass

Der Node LoraLoaderBypass wendet eine LoRA (Low-Rank Adaptation) auf ein Diffusionsmodell und ein CLIP-Modell in einem speziellen „Bypass“-Modus an. Im Gegensatz zu einem Standard-LoRA-Loader werden die Gewichte des Basismodells bei dieser Methode nicht dauerhaft verändert. Stattdessen wird das Ergebnis berechnet, indem der Beitrag der LoRA zum normalen Forward-Pass des Modells addiert wird. Das ist nützlich für das Training oder bei der Arbeit mit Modellen, deren Gewichte ausgelagert sind.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, auf das die LoRA angewendet wird. | MODEL | Ja | - |
| `clip` | Das CLIP-Modell, auf das die LoRA angewendet wird. | CLIP | Ja | - |
| `lora_name` | Der Name der LoRA. Verfügbare LoRA-Dateien werden aus dem Ordner `loras` geladen. | COMBO | Ja | Liste der verfügbaren LoRA-Dateien |
| `strength_model` | Wie stark das Diffusionsmodell verändert wird. Dieser Wert kann negativ sein (Standard: 1.0). | FLOAT | Ja | -100.0 bis 100.0 (Schritt: 0.01) |
| `strength_clip` | Wie stark das CLIP-Modell verändert wird. Dieser Wert kann negativ sein (Standard: 1.0). | FLOAT | Ja | -100.0 bis 100.0 (Schritt: 0.01) |

**Hinweis:** Wenn sowohl `strength_model` als auch `strength_clip` auf 0 gesetzt sind, gibt der Node die ursprünglichen, unveränderten Eingaben `model` und `clip` zurück, ohne sie zu verarbeiten.

**Hinweis:** Die ausgewählte LoRA-Datei wird nach dem ersten Laden zwischengespeichert. Sie wird nur dann erneut von der Festplatte gelesen, wenn ein anderer `lora_name` ausgewählt wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL` | Das modifizierte Diffusionsmodell. | MODEL |
| `CLIP` | Das modifizierte CLIP-Modell. | CLIP |

**Hinweis:** Dieser Node ist als experimentell gekennzeichnet.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/de.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
