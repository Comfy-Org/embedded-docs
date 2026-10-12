# BriaEraseForeground

Dieser Node entfernt den Vordergrund eines Bildes mit Bria und generiert an dessen Stelle einen neuen Hintergrund. Alles, was Bria als Vordergrund identifiziert, wird entfernt, nicht nur Personen, und die unberührten Pixel bleiben erhalten. Das Ergebnis wird in einer Standardgröße von etwa 1 Megapixel neu gerendert.

Dies ist ein kostenpflichtiger API-Node, der auf dem Dienst von Bria ausgeführt wird, daher werden für jeden Durchlauf Ihre Comfy-API-Anmeldedaten verwendet.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Bild, dessen Vordergrund entfernt und durch einen generierten Hintergrund ersetzt wird. Es werden nur die Farbkanäle gesendet; ein etwaiger Alphakanal wird vor dem Hochladen verworfen. | IMAGE | Ja | - |
| `moderation` | Moderationseinstellungen. Wählen Sie `"false"`, um das Bild ohne Moderationsflags zu senden, oder `"true"`, um die unten stehenden Schalter für die Inhaltsmoderation einzublenden. Standard: `"false"`. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |

### `"false"` Eingaben

Keine zusätzlichen Eingaben. Die Anfrage wird ohne Flags für die Inhaltsmoderation gesendet.

### `"true"` Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Aktiviert die Inhaltsmoderation für das Eingabebild. Standard: false. | BOOLEAN | Ja | true<br>false |
| `visual_output_moderation` | Aktiviert die Inhaltsmoderation für das generierte Ausgabebild. Standard: false. | BOOLEAN | Ja | true<br>false |

### Hinweise

- Die Ausgabe wird in einer Standardgröße von etwa 1 Megapixel neu gerendert, daher kann das zurückgegebene Bild in den Abmessungen vom Eingabebild abweichen.
- Dieser Node ist ein kostenpflichtiger API-Node; jeder Durchlauf kostet ungefähr 0,0572 USD.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das Eingabebild mit gelöschtem Vordergrund und einem neu generierten Hintergrund an dessen Stelle. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseForeground/de.md)

---
**Source fingerprint (SHA-256):** `4d8c3c5eed97c648b1191ec41931c97caa17e98a8edd1c054ed63e80cc671b05`
