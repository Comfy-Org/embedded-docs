# PikaStartEndFrameNode2_2

Der PikaFrames v2.2 Node erzeugt ein Video, indem er Ihr erstes und letztes Frame kombiniert. Sie laden zwei Bilder hoch, um Start- und Endpunkt zu definieren, und die KI erstellt einen fließenden Übergang zwischen ihnen, um ein vollständiges Video zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image_start` | Das erste zu kombinierende Bild. | IMAGE | Ja | - |
| `image_end` | Das letzte zu kombinierende Bild. | IMAGE | Ja | - |
| `prompt_text` | Prompt-Text, der den gewünschten Videoinhalt beschreibt. | STRING | Ja | - |
| `negative_prompt` | Text, der beschreibt, was im Video vermieden werden soll. | STRING | Ja | - |
| `seed` | Zufälliger Seed-Wert für Konsistenz der Generierung. | INT | Ja | - |
| `resolution` | Auflösung des Ausgabevideos. | STRING | Ja | - |
| `duration` | Dauer des generierten Videos. | INT | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Das generierte Video, das Start- und Endframe mit KI-Übergängen kombiniert. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/de.md)

---
**Source fingerprint (SHA-256):** `0a26f6db754c61d1f35e3fd9faceb631a8103ce9ff38190a5dd637991914e238`
