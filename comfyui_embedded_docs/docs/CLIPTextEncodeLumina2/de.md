# CLIPTextEncodeLumina2

Dieser Node kodiert einen System-Prompt und einen User-Prompt mithilfe eines CLIP-Modells in ein Embedding, das zur Steuerung des Diffusionsmodells verwendet werden kann, um die Generierung spezifischer Bilder zu lenken. Er kombiniert einen vordefinierten Lumina 2 System-Prompt mit Ihrem benutzerdefinierten Text-Prompt und verarbeitet beide durch das CLIP-Modell, um Conditioning-Daten für die Bildgenerierung zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `system_prompt` | Lumina2 bietet zwei Arten von System-Prompts: Superior: Sie sind ein Assistent, der darauf ausgelegt ist, überlegene Bilder mit einem überlegenen Grad an Bild-Text-Ausrichtung basierend auf Text-Prompts oder User-Prompts zu generieren. Alignment: Sie sind ein Assistent, der darauf ausgelegt ist, hochwertige Bilder mit dem höchsten Grad an Bild-Text-Ausrichtung basierend auf Text-Prompts zu generieren. | COMBO | Ja | `"superior"`<br>`"alignment"` |
| `user_prompt` | Der zu kodierende Text. Unterstützt mehrzeilige Eingaben und dynamische Prompts. | STRING | Ja | N/A |
| `clip` | Das CLIP-Modell, das zur Kodierung des Textes verwendet wird. | CLIP | Ja | N/A |

**Hinweis:** Der Eingang `clip` ist erforderlich und darf nicht None sein. Wenn der Eingang `clip` ungültig ist, gibt der Node einen Fehler aus, der darauf hinweist, dass der Checkpoint möglicherweise kein gültiges CLIP- oder Text-Encoder-Modell enthält.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Ein Conditioning, das den eingebetteten Text enthält, der zur Steuerung des Diffusionsmodells verwendet wird. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/de.md)

---
**Source fingerprint (SHA-256):** `0c7540e6232c93b0f76c4903f5646e00a639ccb0b7720f70b5ac727513358a02`
