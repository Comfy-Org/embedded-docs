# LTX Video SDR to HDR

Konvertiert ein SDR-Video in ein 10-Bit-HDR-Video in BT.2020 mit der HLG-Transferfunktion bei gleicher Auflösung. Audio wird nicht beibehalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Zu konvertierendes SDR-Video, maximal 3840x2160 in jeder Ausrichtung. Bis zu 273 Frames bei 1080p, 193 Frames bei 1440p und 65 Frames bei 4K. | VIDEO | Ja | - |
| `seed` | Steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Nein | 0 bis 4294967295 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das konvertierte 10-Bit-HDR-Video ohne Audio. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoSdrToHdr/de.md)

---
**Source fingerprint (SHA-256):** `e5c0ef901f504a9477f042b4aef24935f4b85da52ccfaddfc764e9efec490915`
