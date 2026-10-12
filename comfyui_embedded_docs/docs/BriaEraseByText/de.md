# Bria Per Text löschen

Dieser Node entfernt mit Bria ein in Klartext beschriebenes Objekt aus einem Bild. Bria rendert das gesamte Bild mit etwa 1 Megapixel neu, sodass das Ergebnis nicht pixelgenau am Eingangsbild ausgerichtet ist.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Bild, aus dem das benannte Objekt entfernt werden soll. | IMAGE | Ja | - |
| `object_name` | Name des zu entfernenden Objekts, wie z. B. 'the lamp'. Es können mehrere Objekte gleichzeitig benannt werden, wie z. B. 'the phone and the pencils'. Wenn etwas benannt wird, das nicht auf dem Bild ist, wird trotzdem ein neu gerendertes Bild zurückgegeben, und die Anfrage wird weiterhin abgerechnet. Muss mindestens 1 Zeichen lang sein (Standard: leer). | STRING | Ja | - |
| `moderation` | Moderationseinstellungen. Wählt aus, ob die optionalen Moderationselemente angezeigt werden. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |

### Moderationseingaben

Diese Parameter erscheinen, wenn `moderation` auf `"true"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Aktiviert die Inhaltsmoderation für das Eingabebild (Standard: false). | BOOLEAN | Nein | true<br>false |
| `visual_output_moderation` | Aktiviert die Inhaltsmoderation für das generierte Ausgabebild (Standard: false). | BOOLEAN | Nein | true<br>false |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das neu gerenderte Bild, aus dem das benannte Objekt entfernt wurde. | IMAGE |
| `structured_prompt` | Strukturierte Beschreibung des bearbeiteten Bildes für eine nachfolgende Bearbeitung mit Bria FIBO Image Edit. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseByText/de.md)

---
**Source fingerprint (SHA-256):** `51ac362bea731251c99905172c41cdebb5165e7564c508f13aa43cf9072964ef`
