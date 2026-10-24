# PixVerse V6 Bild zu Video

Dieser Node animiert ein Eingabebild mit dem PixVerse V6-Modell und gibt ein Video zurück, optional mit einer nativen Audiospur. Das Ausgabevideo behält das Seitenverhältnis des Eingabebilds bei.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das animiert werden soll. | IMAGE | Ja | Einzelnes Bild |
| `model` | Modell- und Generierungseinstellungen. | DYNAMIC_COMBO | Ja | "PixVerse V6"<br>"PixVerse V6 Max" |

### PixVerse V6 Eingaben

Diese Einstellungen erscheinen, wenn das Modell "PixVerse V6" ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt für die Videogenerierung (Standard: leer). | STRING | Ja | 1 bis 5000 Zeichen |
| `quality` | Ausgabeauflösung. Legt die lange Kante fest: 360p entspricht 640px, 540p 1024px, 720p 1280px, 1080p 1920px (Standard: "720p"). | COMBO | Ja | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Länge des generierten Videos in Sekunden (Standard: 5). | INT | Ja | 1 bis 15 |
| `generate_audio` | Erzeugt eine native Audiospur zusammen mit dem Video (Standard: true). | BOOLEAN | Ja | true oder false |
| `multi_clip` | Lässt das Modell das Video in mehrere Shots unterteilen, anstatt in einer durchgehenden Aufnahme (Standard: false). | BOOLEAN | Ja | true oder false |
| `seed` | Seed für die Videogenerierung. PixVerse zeichnet ihn auf, erzeugt damit jedoch keine reproduzierbare Ausführung (Standard: 42, Steuerung nach Generierung ist aktiviert). | INT | Ja | 0 bis 2147483647 |
| `negative_prompt` | Eine optionale Textbeschreibung unerwünschter Elemente im Video (Standard: leer). | STRING | Nein | Bis zu 2048 Zeichen |
| `style` | Ein optionaler visueller Stil, der auf das gesamte Video angewendet wird (Standard: keiner). | COMBO | Nein | Mehrere Optionen verfügbar (PixVerse V6-Stilvoreinstellungen) |

Hinweis: Der Prompt muss mindestens ein Nicht-Leerzeichen-Zeichen und höchstens 5000 Zeichen enthalten; der Negative Prompt darf, falls angegeben, höchstens 2048 Zeichen umfassen. Das Ausgabevideo entspricht immer dem Seitenverhältnis des Eingabebilds, daher ist keine Einstellung für das Seitenverhältnis erforderlich. Es wird nur ein einzelnes Eingabebild akzeptiert. PixVerse kann eine Anfrage ablehnen, wenn die Inhaltsmoderation fehlschlägt, wenn das Anbieterkonto keine Credits mehr hat oder wenn bereits die maximale Anzahl gleichzeitiger Generierungen läuft.

### PixVerse V6 Max Eingaben

Diese Einstellungen erscheinen, wenn das Modell "PixVerse V6 Max" ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt für die Videogenerierung (Standard: leer). | STRING | Ja | 1 bis 5000 Zeichen |
| `quality` | Ausgabeauflösung. Legt die lange Kante fest: 360p entspricht 640px, 540p 1024px, 720p 1280px, 1080p 1920px (Standard: "720p"). | COMBO | Ja | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Länge des generierten Videos in Sekunden (Standard: 5). | INT | Ja | 1 bis 15 |
| `generate_audio` | Erzeugt eine native Audiospur zusammen mit dem Video (Standard: true). | BOOLEAN | Ja | true oder false |
| `multi_clip` | Lässt das Modell das Video in mehrere Shots unterteilen, anstatt in einer durchgehenden Aufnahme (Standard: false). | BOOLEAN | Ja | true oder false |
| `seed` | Seed für die Videogenerierung. PixVerse zeichnet ihn auf, erzeugt damit jedoch keine reproduzierbare Ausführung (Standard: 42, Steuerung nach Generierung ist aktiviert). | INT | Ja | 0 bis 2147483647 |
| `negative_prompt` | Eine optionale Textbeschreibung unerwünschter Elemente im Video (Standard: leer). | STRING | Nein | Bis zu 2048 Zeichen |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Video, einschließlich der nativen Audiospur, wenn `generate_audio` aktiviert ist. Das Seitenverhältnis entspricht dem Eingabebild. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `276b4110c747c73c432cc406571a11b62863a25293615a4852e0dda947f4e48e`
