# LTXV-Audio-Text-Encoder laden

Dieser Node lädt einen spezialisierten Textencoder für das LTXV-Audiomodell. Er kombiniert eine Textencoder-Datei mit einer Checkpoint-Datei, um ein CLIP-Modell zu erstellen, das zur Textkonditionierung in der Audiogenerierung verwendet wird. Laut Beschreibung des Nodes sollte der Textencoder ein Gemma 3 12B- oder ein passendes Gemma 4-Modell sein.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `text_encoder` | Der Dateiname des zu ladenden LTXV-Textencoder-Modells. Die verfügbaren Optionen werden aus dem Ordner `text_encoders` geladen. | COMBO | Ja | Mehrere Optionen verfügbar |
| `ckpt_name` | Der Dateiname des zu ladenden Checkpoints. Die verfügbaren Optionen werden aus dem Ordner `checkpoints` geladen. | COMBO | Ja | Mehrere Optionen verfügbar |
| `device` | Gibt das Gerät an, auf das das Modell geladen werden soll. Verwenden Sie `"cpu"`, um das Laden auf die CPU zu erzwingen. Das Standardverhalten (`"default"`) verwendet die automatische Gerätezuweisung des Systems (Standard: `"default"`). Dies ist ein erweiterter Parameter. | COMBO | Nein | `"default"`<br>`"cpu"` |

**Hinweis:** Die Parameter `text_encoder` und `ckpt_name` arbeiten zusammen. Der Node lädt beide angegebenen Dateien, um ein einzelnes, funktionsfähiges CLIP-Modell zu erstellen. Die Dateien müssen mit der LTXV-Architektur kompatibel sein, und der Textencoder sollte ein Gemma 3 12B- oder ein passendes Gemma 4-Modell sein.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `clip` | Das geladene LTXV-CLIP-Modell, bereit zur Verwendung für die Kodierung von Text-Prompts für die Audiogenerierung. | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/de.md)

---
**Source fingerprint (SHA-256):** `1f3df2c1791203ba849a87897de14052e0cb8370100dbca19df4cf30169a0a2a`
