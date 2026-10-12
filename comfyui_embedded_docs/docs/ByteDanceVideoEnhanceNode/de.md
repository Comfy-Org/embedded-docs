# ByteDanceVideoEnhanceNode

Dieser Node skaliert und restauriert Videos mit ByteDance vCube. Er kann die Auflösung auf bis zu 8K erhöhen, Kompressionsartefakte und Rauschen entfernen, Farbe und Schärfe verbessern und optional Frames für eine höhere Bildrate interpolieren. Das Video wird auf den vCube-Dienst hochgeladen, mit dem ausgewählten Verbesserungs-Preset verarbeitet und als verbesserte Videodatei zurückgegeben.

## Eingaben

### Gemeinsame Eingaben

Diese Eingaben sind immer sichtbar.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Zu verbesserndes Video. Die Quellauflösung darf höchstens 2560x1440 (2K) betragen; die Ausgabegröße wird durch die Eingabe `resolution` festgelegt. | VIDEO | Ja | Höchstens 2560x1440 (2K) |
| `tool_version` | 'standard' gleicht Geschwindigkeit und Qualität mit 10+ Verbesserungsalgorithmen aus. 'professional' verwendet 30+ Algorithmen für eine Restaurierung in Kinoqualität, dauert etwa 3-mal länger und kostet 10-mal mehr. | DYNAMIC_COMBO | Ja | "standard"<br>"professional" |
| `resolution` | Ausgabeauflösung. Die kurze Seite wird auf die gewählte Stufe gesetzt und die lange Seite folgt dem Seitenverhältnis der Quelle. 'source' behält die Quellgröße bei, 'custom' legt die kurze Seite in Pixeln fest. Quellen, die breiter oder höher als etwa 2,2:1 sind, werden eine Auflösungsstufe höher abgerechnet. | DYNAMIC_COMBO | Ja | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | Ausgabebildrate. Eine höhere Rate als die Quelle aktiviert KI-Frame-Interpolation; eine niedrigere verwirft Frames. 'source' behält die Quellrate bei, bis zu 120 fps. Raten über 30 fps kosten 2x, über 60 fps 4x. (Standard: "source") | COMBO | Ja | "source" (Standard)<br>Numerische Bildraten bis zu 120 fps |
| `bitrate_level` | Ziel-Bitrate der gelieferten Datei, skaliert auf die Ausgabeauflösung und Bildrate. (Standard: "medium") | COMBO | Ja | "low"<br>"medium"<br>"high" |

### Standard-Eingaben

Wird angezeigt, wenn `tool_version` auf "standard" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `scene` | Auf den Inhalt abgestimmtes Preset: 'aigc' für KI-generiertes Filmmaterial, 'common' für allgemeine Videos, 'ugc' für komprimierte Handyclips, 'short_series' für Dramen mit Gesichtern, 'old_film' für zerkratztes oder flackerndes Archivmaterial. (Standard: "aigc") | COMBO | Ja | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | 'hd' wendet eine schärfere Verbesserung an; 'natural' reduziert die Stärke für ein weicheres, weniger geschärftes Aussehen. (Standard: "hd") | COMBO | Ja | "hd"<br>"natural" |

### Professionelle Eingaben

Wird angezeigt, wenn `tool_version` auf "professional" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `enhance_style` | 'hd' wendet eine schärfere Verbesserung an; 'natural' reduziert die Stärke für ein weicheres, weniger geschärftes Aussehen. (Standard: "hd") | COMBO | Ja | "hd"<br>"natural" |

### Eingaben für benutzerdefinierte Auflösung

Wird angezeigt, wenn `resolution` auf "custom" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `short_side` | Kurze Seite der Ausgabe in Pixeln; die lange Seite folgt dem Seitenverhältnis der Quelle. (Standard: 1080) | INT | Ja | Standard 1080; begrenzt durch die minimalen und maximalen Grenzwerte für die kurze Seite von vCube |

### Hinweise

- Das Quellvideo darf höchstens 2560x1440 (2K) groß sein. Größere Videos werden abgelehnt und müssen vor der Verbesserung herunterskaliert werden.
- Die Dauer des Quellvideos ist auf die maximale Dauer begrenzt, die der vCube-Dienst unterstützt.
- Wenn `tool_version` auf "standard" gesetzt ist, sind sowohl `scene` als auch `enhance_style` verfügbar. Wenn es auf "professional" gesetzt ist, ist nur `enhance_style` verfügbar.
- Wenn `resolution` auf "custom" gesetzt ist, ist der Wert `short_side` erforderlich. Die Auflösungs-Presets und "source" verwenden `short_side` nicht.
- Wenn `resolution` auf "source" gesetzt ist und die kurze Seite der Quelle mindestens dem Mindestgrenzwert für die kurze Seite entspricht, behält die Ausgabe die Quellauflösung bei.
- Wenn `fps` auf "source" gesetzt ist, entspricht die Ausgabebildrate der Quellbildrate, bis zu 120 fps.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das verbesserte Video, hochskaliert und restauriert mit der angeforderten Auflösung und Bildrate. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/de.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`
