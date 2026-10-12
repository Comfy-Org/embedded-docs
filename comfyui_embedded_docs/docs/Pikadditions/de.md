# Pikadditions

Der Pikadditions-Node ermöglicht es Ihnen, ein beliebiges Objekt oder Bild in Ihr Video einzufügen. Sie laden ein Video hoch und geben an, was Sie hinzufügen möchten, um ein nahtlos integriertes Ergebnis zu erzeugen. Dieser Node verwendet die Pika-API, um Bilder mit natürlich wirkender Integration in Videos einzufügen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Das Video, in das ein Bild eingefügt werden soll. | VIDEO | Ja | - |
| `image` | Das Bild, das in das Video eingefügt werden soll. | IMAGE | Ja | - |
| `prompt_text` | Textbeschreibung dessen, was dem Video hinzugefügt werden soll. | STRING | Ja | - |
| `negative_prompt` | Textbeschreibung dessen, was im Video vermieden werden soll. | STRING | Ja | - |
| `seed` | Zufälliger Seed-Wert für reproduzierbare Ergebnisse. | INT | Ja | 0 bis 4294967295 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Das verarbeitete Video mit dem eingefügten Bild. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/de.md)

---
**Source fingerprint (SHA-256):** `cf7bb4ee0a672e20c0ffc128fa95df43e05356aea03b2070f928a0263aff6234`
