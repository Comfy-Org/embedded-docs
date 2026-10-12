# Vidu2TextToVideoNode

Der Node „Vidu2 Text-to-Video Generation“ erstellt ein Video aus einer Textbeschreibung. Er verbindet sich mit einer externen API, um Videoinhalte basierend auf Ihrem Prompt zu generieren, sodass Sie Länge, visuellen Stil und Format des Videos steuern können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das KI-Modell, das für die Videogenerierung verwendet werden soll. Derzeit ist nur ein Modell verfügbar. | COMBO | Ja | `"viduq2"` |
| `prompt` | Eine Textbeschreibung für die Videogenerierung mit einer maximalen Länge von 2000 Zeichen. | STRING | Ja | - |
| `duration` | Die Länge des generierten Videos in Sekunden. Der Wert kann über einen Schieberegler angepasst werden (Standard: 5). | INT | Nein | 1 bis 10 |
| `seed` | Eine Zahl, die verwendet wird, um die Zufälligkeit der Generierung zu steuern, wodurch reproduzierbare Ergebnisse ermöglicht werden. Sie kann nach der Generierung gesteuert werden (Standard: 1). | INT | Nein | 0 bis 2147483647 |
| `aspect_ratio` | Das proportionale Verhältnis zwischen Breite und Höhe des Videos. | COMBO | Nein | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `resolution` | Die Pixelabmessungen des generierten Videos. Dies ist ein erweiterter Parameter. | COMBO | Nein | `"720p"`<br>`"1080p"` |
| `background_music` | Ob dem generierten Video Hintergrundmusik hinzugefügt werden soll (Standard: False). Dies ist ein erweiterter Parameter. | BOOLEAN | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `27b7c05ae1b3b23d07e775f67474ecef1ffc0bd8240f4aa2219e15949d854f27`
