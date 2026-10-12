# BriaReseason

Dieser Node versetzt ein Bild mithilfe von Bria in eine andere Jahreszeit. Die gesamte Szene wird neu gerendert, sodass sich die Umgebung über die Jahreszeit selbst hinaus ändern kann. Bria rendert das gesamte Bild mit etwa 1 Megapixel neu, daher ist das Ergebnis nicht pixelgenau am Eingabebild ausgerichtet.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Bild, das in eine andere Jahreszeit versetzt werden soll. Ein etwaiger Alphakanal wird entfernt, bevor das Bild gesendet wird. | IMAGE | Ja | - |
| `season` | Die anzuwendende Jahreszeit. | COMBO | Ja | `"spring"`<br>`"summer"`<br>`"autumn"`<br>`"winter"` |
| `moderation` | Moderationseinstellungen. Legt fest, ob Inhaltsmoderationsoptionen für diese Anfrage konfiguriert werden. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |

### Moderationseingaben

Diese Optionen werden angezeigt, wenn `moderation` auf `"true"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Aktiviert die Inhaltsmoderation für das Eingabebild (Standard: false). | BOOLEAN | Nein | true<br>false |
| `visual_output_moderation` | Aktiviert die Inhaltsmoderation für das generierte Ausgabebild (Standard: false). | BOOLEAN | Nein | true<br>false |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das neu gerenderte Bild in der ausgewählten Jahreszeit. | IMAGE |
| `structured_prompt` | Strukturierte Beschreibung des bearbeiteten Bildes für eine nachfolgende Bearbeitung mit Bria FIBO Image Edit. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReseason/de.md)

---
**Source fingerprint (SHA-256):** `3bb9ee1c00c91759cc6f972e2ba8708ae73a186f4b66bf6669937e561efad0a4`
