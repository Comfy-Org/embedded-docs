# FlashVSR-Video-Upscaling

Der WavespeedFlashVSRNode ist ein schneller, hochwertiger Video-Upscaler, der die Auflösung erhöht und die Klarheit von niedrig aufgelöstem oder unscharfem Filmmaterial wiederherstellt. Er verarbeitet eine Videoeingabe und gibt ein neues Video in einer vom Benutzer ausgewählten höheren Auflösung aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Die Eingabevideodatei, die hochskaliert werden soll. Muss im MP4-Containerformat vorliegen und eine Dauer zwischen 5 Sekunden und 10 Minuten haben. | VIDEO | Ja | N/A |
| `target_resolution` | Die gewünschte Auflösung für das hochskalierte Ausgabevideo. | STRING | Ja | `"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |

**Einschränkungen für Eingaben:**

- Die Eingabedatei `video` muss im MP4-Containerformat vorliegen.
- Die Dauer des Eingabevideos `video` muss zwischen 5 Sekunden und 10 Minuten (600 Sekunden) liegen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die hochskalierte Videodatei in der ausgewählten Zielauflösung. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedFlashVSRNode/de.md)

---
**Source fingerprint (SHA-256):** `d7885eeb2dacfc2bc398d1bc991620be479f45d8edbdca7eb046a21500581529`
