# Bria Objekt ersetzen

Ersetzt ein Objekt in einem Bild durch ein anderes, das in Klartext beschrieben wird, unter Verwendung von Brias textgesteuerter Bildbearbeitung. Bria rendert das gesamte Bild mit etwa 1 Megapixel neu, daher ist das Ergebnis nicht pixelgenau am Eingabebild ausgerichtet.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Bild, das das zu ersetzende Objekt enthält. Der Alphakanal wird entfernt, bevor das Bild hochgeladen wird. | IMAGE | Ja | - |
| `instruction` | Was wodurch ersetzt werden soll, z. B. "Ersetze den roten Apfel durch eine grüne Birne". Muss mindestens 1 Zeichen lang sein. | STRING | Ja | Mehrzeiliger Text; Standard: "" (leer) |
| `seed` | Bria verwendet hier keinen Seed und erzeugt die Bearbeitung bei jedem Aufruf neu, sodass wiederholte Ausführungen abweichen können. Der Wert wird nie übermittelt: Er ändert nur den Cache-Schlüssel dieses Nodes, sodass ein ansonsten identischer Graph die Bearbeitung erneut ausführt, anstatt das zwischengespeicherte Ergebnis zurückzugeben. | INT | Ja | 0 bis 2147483647, Schritt 1; Standard: 42; Steuerung nach Generierung aktiviert |

### Moderationseingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `moderation` | Moderationseinstellungen. Wenn "true" ausgewählt wird, werden die untenstehenden Moderationsunteroptionen eingeblendet, die andernfalls nicht angezeigt werden. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |
| `visual_input_moderation` | Aktiviert die Moderation des Eingabebilds. Nur verfügbar, wenn `moderation` auf "true" gesetzt ist. | BOOLEAN | Nein | `true` / `false`; Standard: false |
| `visual_output_moderation` | Aktiviert die Moderation des generierten Ausgabebilds. Nur verfügbar, wenn `moderation` auf "true" gesetzt ist. | BOOLEAN | Nein | `true` / `false`; Standard: false |

Hinweis: `instruction` wird validiert, bevor die Anfrage gesendet wird, und muss mindestens 1 Zeichen enthalten. Der `seed`-Wert wird nicht an Bria übertragen; er beeinflusst nur, ob der Node die Bearbeitung erneut ausführt oder ein zwischengespeichertes Ergebnis zurückgibt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|-------------|-----------|
| `image` | Das bearbeitete Bild mit der beschriebenen Objekt-Ersetzung. | IMAGE |
| `structured_prompt` | Strukturierte Beschreibung des bearbeiteten Bildes für eine Folgebearbeitung mit Bria FIBO Image Edit. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceObject/de.md)

---
**Source fingerprint (SHA-256):** `75a45d5c0d6cde96a1e961db627edc1a59c07cc37b974402745cefc62864cc26`
