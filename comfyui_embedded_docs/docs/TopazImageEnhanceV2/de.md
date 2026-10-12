# Topaz-Bildverbesserung

Topaz Image Enhance wendet branchenübliches Hochskalieren und Bildverbesserung auf ein einzelnes Eingabebild mit Topaz-Modellen an. Es sendet das Bild an die Topaz-API, verarbeitet es mit dem ausgewählten Modell und gibt das verbesserte Ergebnis zurück. Sie können aus drei Modellen wählen: Reimagine, Bloom 2 und Wonder 3.5.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das verbessert werden soll. Nur ein Eingabebild wird unterstützt. | IMAGE | Ja | Einzelnes Bild |
| `model` | Das zu verwendende Topaz-Verbesserungsmodell. Das ausgewählte Modell bestimmt, welche modellspezifischen Einstellungen angezeigt werden. | DYNAMIC_COMBO | Ja | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `output_width` | Der Wert Null bedeutet, automatisch zu berechnen (normalerweise entspricht dies der Originalgröße oder wird proportional zu `output_height` skaliert, falls angegeben). Wonder 3.5 unterstützt nur Skalierungsfaktoren von 1x bis 6x. Bloom 2 und Wonder 3.5 behalten das Seitenverhältnis der Eingabe bei und behandeln die angeforderte Größe als Ziel. (Standard: 0) | INT | Nein | 0 bis 32000 |
| `output_height` | Der Wert Null bedeutet, mit derselben Höhe wie das Original auszugeben oder proportional zu `output_width` skaliert zu werden, falls angegeben. Wonder 3.5 unterstützt nur Skalierungsfaktoren von 1x bis 6x. Bloom 2 und Wonder 3.5 behalten das Seitenverhältnis der Eingabe bei und behandeln die angeforderte Größe als Ziel. (Standard: 0) | INT | Nein | 0 bis 32000 |

### Reimagine Eingaben

Diese Einstellungen gelten, wenn `model` auf `"Reimagine"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Optionaler Text-Prompt als Anleitung für kreatives Hochskalieren. (Standard: "") | STRING | Ja | Beliebiger Text |
| `creativity` | Kreativitätsstufe für die Verbesserung. (Standard: 3) | INT | Ja | 1 bis 9 |
| `subject_detection` | Subjekterkennungsmodus (erweitert). | COMBO | Ja | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Gesichter (falls vorhanden) während der Verarbeitung verbessern. (Standard: True) | BOOLEAN | Ja | true<br>false |
| `face_enhancement_creativity` | Legen Sie die Kreativitätsstufe für die Gesichtsverbesserung fest. (Standard: 0.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `face_enhancement_strength` | Steuert, wie scharf verbesserte Gesichter im Verhältnis zum Hintergrund sind. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `face_preservation` | Bewahrt die Gesichtsidentität der Subjekte. (Standard: True) | BOOLEAN | Ja | true<br>false |
| `color_preservation` | Bewahrt die Originalfarben. (Standard: True) | BOOLEAN | Ja | true<br>false |
| `crop_to_fill` | Standardmäßig wird das Bild mit Letterbox versehen, wenn das Ausgabe-Seitenverhältnis abweicht. Aktivieren Sie diese Option, um das Bild zuzuschneiden, damit es die Ausgabeabmessungen ausfüllt. (Standard: False) | BOOLEAN | Ja | true<br>false |

### Bloom 2 Eingaben

Diese Einstellungen gelten, wenn `model` auf `"Bloom 2"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Optionaler Text-Prompt für die Generierung. Leer lassen, um automatisch einen Prompt aus dem Eingabebild zu generieren. (Standard: "") | STRING | Ja | Beliebiger Text |
| `creativity` | 1 ist zurückhaltende Verbesserung, 9 ist ausgeprägte Neuinterpretation mit neu generierten Details. (Standard: 3) | INT | Ja | 1 bis 9 |
| `seed` | Seed für reproduzierbare Generierung. (Standard: 2) | INT | Ja | 1 bis 2000 |
| `color_preservation` | Bewahrt die Originalfarben. (Standard: True) | BOOLEAN | Ja | true<br>false |
| `grain` | Fügt dem Ausgabebild Körnung hinzu. (Standard: False) | BOOLEAN | Ja | true<br>false |
| `grain_model` | Zu verwendendes Körnungsmodell. Wird ignoriert, wenn Körnung deaktiviert ist. | COMBO | Ja | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Stärke des Körnungseffekts. Wird ignoriert, wenn Körnung deaktiviert ist. (Standard: 0.5) | FLOAT | Ja | 0.0 bis 1.0 |
| `grain_size` | Größe der Körnungspartikel. Wird ignoriert, wenn Körnung deaktiviert ist. (Standard: 1.0) | FLOAT | Ja | 1.0 bis 5.0 |
| `grain_density` | Intensität des Körnungseffekts. Wird ignoriert, wenn Körnung deaktiviert ist. (Standard: 0.5) | FLOAT | Ja | 0.0 bis 1.0 |

### Wonder 3.5 Eingaben

Diese Einstellungen gelten, wenn `model` auf `"Wonder 3.5"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `enhancement_strength` | Verbesserungsstufe für unterschiedliche Eingabebedingungen. (Standard: "high") | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | Fügt dem Ausgabebild Körnung hinzu. (Standard: False) | BOOLEAN | Ja | true<br>false |
| `grain_model` | Zu verwendendes Körnungsmodell. Wird ignoriert, wenn Körnung deaktiviert ist. | COMBO | Ja | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Stärke des Körnungseffekts. Wird ignoriert, wenn Körnung deaktiviert ist. (Standard: 0.5) | FLOAT | Ja | 0.0 bis 1.0 |
| `grain_size` | Größe der Körnungspartikel. Wird ignoriert, wenn Körnung deaktiviert ist. (Standard: 1.0) | FLOAT | Ja | 1.0 bis 5.0 |
| `grain_density` | Intensität des Körnungseffekts. Wird ignoriert, wenn Körnung deaktiviert ist. (Standard: 0.5) | FLOAT | Ja | 0.0 bis 1.0 |

**Hinweis:** Nur ein Eingabebild wird unterstützt; der Node löst einen Fehler aus, wenn der Eingabe-Batch mehr als ein Bild enthält. Die Körnungseinstellungen (`grain_model`, `grain_strength`, `grain_size`, `grain_density`) werden ignoriert, sofern `grain` nicht aktiviert ist. Bei Bloom 2 wird durch Leerlassen von `prompt` automatisch ein Prompt aus dem Eingabebild generiert. Wonder 3.5 unterstützt nur Skalierungsfaktoren von 1x bis 6x; Bloom 2 und Wonder 3.5 behalten das Seitenverhältnis der Eingabe bei und behandeln die angeforderte Größe als Ziel.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das von der Topaz-API zurückgegebene verbesserte und hochskalierte Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/de.md)

---
**Source fingerprint (SHA-256):** `19bb03ca7354f1b0d1e559b742b83939678fce6d5f490b1030717b846043e0e6`
