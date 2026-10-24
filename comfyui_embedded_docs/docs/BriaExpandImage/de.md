# Bria Bild erweitern

Bria Expand Image erweitert ein Bild über seine ursprünglichen Ränder hinaus, indem mit Bria neue Inhalte generiert werden. Es ermöglicht Ihnen, ein Ziel-Seitenverhältnis, ein benutzerdefiniertes Verhältnis zu wählen oder eine Leinwand mit manueller Platzierung des Originalbilds zu definieren. Die Erweiterung kann mit einem Text-Prompt gesteuert werden; bleibt der Prompt leer, generiert Bria automatisch einen.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das erweitert werden soll. | IMAGE | Ja | — |
| `expand_mode` | Zielform des erweiterten Bildes: ein voreingestelltes Seitenverhältnis, ein benutzerdefiniertes Verhältnis oder manuelle Platzierung des Originalbildes auf einer Leinwand. Manuell ist der einzige Modus, der eine Leinwand erreichen kann, die höher als 1:2 ist. Die Auswahl von `custom_ratio` blendet `ratio_width` und `ratio_height` ein. Die Auswahl von `manual` blendet die Parameter für Leinwand und Bildplatzierung ein. | DYNAMIC_COMBO | Ja | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"custom_ratio"`<br>`"manual"` |
| `prompt` | Optionale Beschreibung der erweiterten Szene; wenn leer, generiert Bria eine aus dem Bild. Standard: leerer String. | STRING | Ja | Beliebige Zeichenkette |
| `negative_prompt` | Ein optionaler negativer Prompt für die Erweiterung. Standard: leerer String. | STRING | Ja | Beliebige Zeichenkette |
| `seed` | Seed für den zufälligen Generierungsprozess. Standard: 42. | INT | Ja | 1–2147483647 |
| `moderation` | Moderationseinstellungen. Wenn auf `true` gesetzt, werden zusätzliche Moderationsoptionen angezeigt. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |

### Eingaben für benutzerdefiniertes Verhältnis

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `ratio_width` | Breitenseite des Zielverhältnisses: 21 und 9 ergeben 21:9. Standard: 21. | INT | Ja | 1–100 |
| `ratio_height` | Höhenseite des Zielverhältnisses: 21 und 9 ergeben 21:9. Bria akzeptiert nur Breite/Höhe zwischen 0.5 und 3.0, daher benötigt alles, was höher als 1:2 ist, den manuellen Modus. Standard: 9. | INT | Ja | 1–100 |

### Manuelle Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `canvas_width` | Breite der Ausgabeleinwand in Pixeln. Standard: 1000. | INT | Ja | 64–5000 |
| `canvas_height` | Höhe der Ausgabeleinwand in Pixeln. Standard: 1000. | INT | Ja | 64–5000 |
| `image_width` | Breite des Originalbildes innerhalb der Leinwand. Standard: 500. | INT | Ja | 1–5000 |
| `image_height` | Höhe des Originalbildes innerhalb der Leinwand. Standard: 500. | INT | Ja | 1–5000 |
| `image_x` | X-Position der oberen linken Ecke des Bildes innerhalb der Leinwand; kann außerhalb der Leinwand liegen, wodurch das Bild zugeschnitten wird. Standard: 250. | INT | Ja | -5000–5000 |
| `image_y` | Y-Position der oberen linken Ecke des Bildes innerhalb der Leinwand; kann außerhalb der Leinwand liegen, wodurch das Bild zugeschnitten wird. Standard: 250. | INT | Ja | -5000–5000 |

### Moderationseingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Wenn aktiviert, wird der Prompt-Inhalt moderiert. Standard: false. Nur verfügbar, wenn `moderation` `true` ist. | BOOLEAN | Ja | true/false |
| `visual_input_moderation` | Wenn aktiviert, wird die visuelle Eingabe moderiert. Standard: false. Nur verfügbar, wenn `moderation` `true` ist. | BOOLEAN | Ja | true/false |
| `visual_output_moderation` | Wenn aktiviert, wird die visuelle Ausgabe moderiert. Standard: false. Nur verfügbar, wenn `moderation` `true` ist. | BOOLEAN | Ja | true/false |

Voreingestellte Seitenverhältnis-Optionen (`1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`) haben keine zusätzlichen Eingaben.

Wenn `expand_mode` auf `custom_ratio` gesetzt ist, definieren `ratio_width` und `ratio_height` ein Ziel-Seitenverhältnis. Bria akzeptiert nur Breite-zu-Höhe-Verhältnisse zwischen 0.5 und 3.0. Liegt das Verhältnis außerhalb dieses Bereichs, wird ein Fehler ausgelöst und stattdessen sollte der Modus `manual` verwendet werden. Die erweiterte Leinwand ist auf 25 Megapixel begrenzt; wenn das Ergebnis eine größere Leinwand bräuchte, löst der Node einen Fehler aus, also das Bild zuerst verkleinern.

Wenn `expand_mode` auf `manual` gesetzt ist, wird das Originalbild mit der angegebenen Größe und Position auf einer Leinwand platziert. Das Bild kann über die Leinwand hinausragen; in diesem Fall wird der außerhalb liegende Teil zugeschnitten. Das Bild muss einen Teil der Leinwand frei lassen: deckt es die ganze Leinwand ab, löst der Node einen Fehler aus, weil es nichts zu erweitern gibt.

Wenn `moderation` auf `true` gesetzt ist, werden die drei Moderations-Booleschen Werte an Bria gesendet. Wenn `moderation` auf `false` gesetzt ist, werden sie ignoriert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das von Bria generierte erweiterte Bild. | IMAGE |
| `prompt` | Der für die Erweiterung verwendete Prompt; automatisch von Bria generiert, wenn die Prompt-Eingabe leer ist. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaExpandImage/de.md)

---
**Source fingerprint (SHA-256):** `939b51e420f13ccea058d9cf36172148db55d9878975b5f0251a90773f6d6105`
