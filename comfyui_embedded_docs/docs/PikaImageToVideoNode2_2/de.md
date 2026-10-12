# PikaImageToVideoNode2_2

Der Node „Pika Image to Video“ sendet ein Bild und einen Text-Prompt an die Pika-API Version 2.2, um ein Video zu generieren. Er konvertiert Ihr Eingabebild basierend auf der bereitgestellten Beschreibung und den Einstellungen in ein Videoformat. Der Node übernimmt die API-Kommunikation und gibt das generierte Video als Ausgabe zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Bild, das in ein Video umgewandelt werden soll | IMAGE | Ja | - |
| `prompt_text` | Die Textbeschreibung, die die Videogenerierung steuert | STRING | Ja | - |
| `negative_prompt` | Text, der beschreibt, was im Video vermieden werden soll | STRING | Ja | - |
| `seed` | Zufälliger Seed-Wert für reproduzierbare Ergebnisse | INT | Ja | - |
| `resolution` | Einstellung für die Auflösung des Ausgabevideos | STRING | Ja | - |
| `duration` | Länge des generierten Videos in Sekunden | INT | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die generierte Videodatei | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/de.md)

---
**Source fingerprint (SHA-256):** `aaa8dc49b94f0fae2010a3b61a3fb41e212fa9d2946a934a1a7c651fdced81b3`
