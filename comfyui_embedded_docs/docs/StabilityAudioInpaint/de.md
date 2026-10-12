# StabilityAudioInpaint

Transformiert einen Teil eines vorhandenen Audio-Samples mithilfe von Textanweisungen. Dieser Node ermöglicht es Ihnen, bestimmte Abschnitte des Audios durch beschreibende Prompts zu ändern, wodurch ausgewählte Teile effektiv per Inpainting bearbeitet oder neu generiert werden, während der Rest des Audios erhalten bleibt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Das KI-Modell, das für Audio-Inpainting verwendet werden soll. | STRING | Ja | `"stable-audio-2.5"` |
| `prompt` | Textbeschreibung, die angibt, wie das Audio transformiert werden soll (Standard: leer). Maximale Länge beträgt 10.000 Zeichen. | STRING | Ja |  |
| `audio` | Eingabe-Audiodatei, die transformiert werden soll. Audio muss zwischen 6 und 190 Sekunden lang sein. | AUDIO | Ja |  |
| `duration` | Steuert die Dauer des generierten Audios in Sekunden (Standard: 190). | INT | Nein | 1 bis 190 |
| `seed` | Der für die Generierung verwendete Zufalls-Seed (Standard: 0). | INT | Nein | 0 bis 4294967294 |
| `steps` | Steuert die Anzahl der Sampling-Schritte (Standard: 8). | INT | Nein | 4 bis 8 |
| `mask_start` | Startposition in Sekunden für den zu transformierenden Audioabschnitt (Standard: 30). | INT | Nein | 0 bis 190 |
| `mask_end` | Endposition in Sekunden für den zu transformierenden Audioabschnitt (Standard: 190). | INT | Nein | 0 bis 190 |

**Hinweis:** Der Wert `mask_end` muss größer als der Wert `mask_start` sein. Das Eingabe-Audio muss eine Dauer zwischen 6 und 190 Sekunden haben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `audio` | Die transformierte Audioausgabe, bei der der angegebene Abschnitt gemäß dem Prompt geändert wurde. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/de.md)

---
**Source fingerprint (SHA-256):** `3c180043c538311b1808cddd84b0c0ab22a6fa1d943b7f9ddc9edab0fb3413ad`
