# FLUX 3 Image Layout Prompt

Erstellt die Layout-Tabelle, die FLUX 3 Image aus einem Prompt liest. Sie übernimmt die im Node Create Bounding Boxes gezeichneten Elemente und hängt sie als Liste von Boxen an Ihren Prompt an, jede mit einer ID, ihren Koordinaten und ihrer Beschreibung. Zitieren Sie eine Box im Prompt als `<obj_N>`, um Wörter an diesen Bereich zu binden, und verbinden Sie dann die Ausgabe mit dem prompt-Eingang des FLUX 3 Image-Node. Wenn keine Elemente verbunden sind, wird der Prompt unverändert zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `prompt` | Der Prompt-Text. Zitieren Sie Box N als `<obj_N>`, um Wörter daran zu binden. | STRING | Ja | - |
| `element` | Die Elemente, die im Layout platziert werden sollen, entnommen aus dem Node Create Bounding Boxes. Farbpaletten werden nicht verwendet, beschreiben Sie Farben stattdessen in der Beschreibung. | ARRAY | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `prompt` | Der Prompt mit angehängter Box-Layout-Tabelle, bereit zur Einspeisung in den FLUX 3 Image-Node. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3LayoutPrompt/de.md)

---
**Source fingerprint (SHA-256):** `ac8f61701c8da0a6fc8361aeebf7fc5e7aa338ce6ad8689718904caa9c53e3b8`
