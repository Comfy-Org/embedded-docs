# PikaTextToVideoNode2_2

Der Node Pika Text2Video v2.2 sendet einen Text-Prompt an die Pika-API-Version 2.2, um ein Video zu generieren. Er wandelt Ihre Textbeschreibung mithilfe des KI-Videogenerierungsdienstes von Pika in ein Video um. Der Node ermöglicht es Ihnen, verschiedene Aspekte des Videogenerierungsprozesses anzupassen, darunter Seitenverhältnis, Dauer und Auflösung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `prompt_text` | Die Haupttextbeschreibung, die beschreibt, was im Video generiert werden soll | STRING | Ja | - |
| `negative_prompt` | Text, der beschreibt, was im generierten Video nicht erscheinen soll | STRING | Ja | - |
| `seed` | Eine Zahl, die die Zufälligkeit der Generierung für reproduzierbare Ergebnisse steuert | INT | Ja | - |
| `resolution` | Die Auflösungseinstellung für das Ausgabevideo | STRING | Ja | - |
| `duration` | Die Länge des Videos in Sekunden | INT | Ja | - |
| `aspect_ratio` | Seitenverhältnis (Breite / Höhe) (Standard: 1.7777777777777777) | FLOAT | Nein | 0.4 - 2.5 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die generierte Videodatei, die von der Pika-API zurückgegeben wird | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/de.md)

---
**Source fingerprint (SHA-256):** `b4287519f5d4cc4a1077a58fb13aa99697e3be038a0b382c4b4c9b0e53a0d8a8`
