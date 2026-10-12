# Luma-Referenz

Dieser Node enthält ein Bild und einen Gewichtungswert zur Verwendung mit dem Luma Generate Image-Node. Er erstellt eine Referenzkette, die an andere Luma-Nodes übergeben werden kann, um die Bilderzeugung zu beeinflussen. Der Node kann entweder eine neue Referenzkette starten oder einer vorhandenen hinzufügen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Bild, das als Referenz verwendet wird. | IMAGE | Ja | - |
| `weight` | Gewichtung der Bildreferenz (Standard: 1.0). | FLOAT | Ja | 0.0 - 1.0 |
| `luma_ref` | Optionale vorhandene Luma-Referenzkette, zu der hinzugefügt wird. | LUMA_REF | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `luma_ref` | Die Luma-Referenzkette, die das Bild und die Gewichtung enthält. | LUMA_REF |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/de.md)

---
**Source fingerprint (SHA-256):** `f7e7789f2f19cac41cb9e55d21f10fef3012b10dcdbd59eb79f97fe5c2a944b7`
