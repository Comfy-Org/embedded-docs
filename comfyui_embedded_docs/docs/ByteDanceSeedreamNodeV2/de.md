# ByteDanceSeedreamNodeV2

Dieser Node erzeugt oder bearbeitet Bilder mit den Seedream-Modellen von ByteDance (Versionen 4.0, 4.5, 5.0 Lite und 5.0 Pro). Er bietet einheitliche Text-zu-Bild-Generierung und präzise Bildbearbeitung mit einem einzigen Satz bei bis zu 4K-Auflösung. Dies ist die Legacy-Version (V2) des Seedream-Nodes.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Die Seedream-Modellversion, die für die Generierung verwendet werden soll. Jedes Modell hat unterschiedliche Fähigkeiten und Preise. | DYNAMIC_COMBO | Ja | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | Text-Prompt zum Erstellen oder Bearbeiten eines Bildes (Standard: leerer String). | STRING | Ja | N/A |
| `seed` | Seed für die Generierung (Standard: 0). | INT | Ja | 0 bis 2147483647 |
| `watermark` | Ob dem Bild ein "AI generated"-Wasserzeichen hinzugefügt werden soll (Standard: False). | BOOLEAN | Ja | True / False |
| `thinking` | Aktiviert den Prompt-Optimierungs-Denkprozess ('thinking') des Modells für bessere Prompt-Treue. Kann die Generierungszeit erheblich verlängern – insbesondere bei Seedream 5.0 Pro. Kann nur für Text-zu-Bild deaktiviert werden (nicht, wenn Referenzbilder bereitgestellt werden) (Standard: True). | BOOLEAN | Nein | True / False |

### `seedream 5.0 pro` Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Wählen Sie eine empfohlene Größe. Wählen Sie `Custom`, um die untenstehende Breite und Höhe zu verwenden. | COMBO | Ja | Mehrere modellspezifische Voreinstellungen verfügbar, einschließlich `Custom` |
| `width` | Benutzerdefinierte Breite für das Bild. Der Wert wirkt nur, wenn `size_preset` auf `Custom` gesetzt ist (Standard: 2048). | INT | Ja | 1024 bis 3136 (Schrittweite 2) |
| `height` | Benutzerdefinierte Höhe für das Bild. Der Wert wirkt nur, wenn `size_preset` auf `Custom` gesetzt ist (Standard: 2048). | INT | Ja | 1024 bis 2496 (Schrittweite 2) |

### `seedream 5.0 lite` Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Wählen Sie eine empfohlene Größe. Wählen Sie `Custom`, um die untenstehende Breite und Höhe zu verwenden. | COMBO | Ja | Mehrere modellspezifische Voreinstellungen verfügbar, einschließlich `Custom` |
| `width` | Benutzerdefinierte Breite für das Bild. Der Wert wirkt nur, wenn `size_preset` auf `Custom` gesetzt ist (Standard: 2048). | INT | Ja | 1024 bis 6240 (Schrittweite 2) |
| `height` | Benutzerdefinierte Höhe für das Bild. Der Wert wirkt nur, wenn `size_preset` auf `Custom` gesetzt ist (Standard: 2048). | INT | Ja | 1024 bis 4992 (Schrittweite 2) |
| `max_images` | Maximale Anzahl der zu generierenden Bilder. Bei 1 wird genau ein Bild erzeugt. Bei >1 generiert das Modell zwischen 1 und `max_images` zusammenhängende Bilder (z. B. Story-Szenen, Charaktervariationen). Die Gesamtzahl der Bilder (Eingabe + generiert) darf 15 nicht überschreiten. (Standard: 1) | INT | Ja | 1 bis 14 |
| `fail_on_partial` | Wenn aktiviert, bricht die Ausführung ab, falls angeforderte Bilder fehlen oder ein Fehler zurückgegeben wird. (Standard: False) | BOOLEAN | Ja | True / False |

### `seedream-4-5-251128` Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Wählen Sie eine empfohlene Größe. Wählen Sie `Custom`, um die untenstehende Breite und Höhe zu verwenden. | COMBO | Ja | Mehrere modellspezifische Voreinstellungen verfügbar, einschließlich `Custom` |
| `width` | Benutzerdefinierte Breite für das Bild. Der Wert wirkt nur, wenn `size_preset` auf `Custom` gesetzt ist (Standard: 2048). | INT | Ja | 1024 bis 6240 (Schrittweite 2) |
| `height` | Benutzerdefinierte Höhe für das Bild. Der Wert wirkt nur, wenn `size_preset` auf `Custom` gesetzt ist (Standard: 2048). | INT | Ja | 1024 bis 4992 (Schrittweite 2) |
| `max_images` | Maximale Anzahl der zu generierenden Bilder. Bei 1 wird genau ein Bild erzeugt. Bei >1 generiert das Modell zwischen 1 und `max_images` zusammenhängende Bilder (z. B. Story-Szenen, Charaktervariationen). Die Gesamtzahl der Bilder (Eingabe + generiert) darf 15 nicht überschreiten. (Standard: 1) | INT | Ja | 1 bis 10 |
| `fail_on_partial` | Wenn aktiviert, bricht die Ausführung ab, falls angeforderte Bilder fehlen oder ein Fehler zurückgegeben wird. (Standard: False) | BOOLEAN | Ja | True / False |

### `seedream-4-0-250828` Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Wählen Sie eine empfohlene Größe. Wählen Sie `Custom`, um die untenstehende Breite und Höhe zu verwenden. | COMBO | Ja | Mehrere modellspezifische Voreinstellungen verfügbar, einschließlich `Custom` |
| `width` | Benutzerdefinierte Breite für das Bild. Der Wert wirkt nur, wenn `size_preset` auf `Custom` gesetzt ist (Standard: 2048). | INT | Ja | 1024 bis 6240 (Schrittweite 2) |
| `height` | Benutzerdefinierte Höhe für das Bild. Der Wert wirkt nur, wenn `size_preset` auf `Custom` gesetzt ist (Standard: 2048). | INT | Ja | 1024 bis 4992 (Schrittweite 2) |
| `max_images` | Maximale Anzahl der zu generierenden Bilder. Bei 1 wird genau ein Bild erzeugt. Bei >1 generiert das Modell zwischen 1 und `max_images` zusammenhängende Bilder (z. B. Story-Szenen, Charaktervariationen). Die Gesamtzahl der Bilder (Eingabe + generiert) darf 15 nicht überschreiten. (Standard: 1) | INT | Ja | 1 bis 10 |
| `fail_on_partial` | Wenn aktiviert, bricht die Ausführung ab, falls angeforderte Bilder fehlen oder ein Fehler zurückgegeben wird. (Standard: False) | BOOLEAN | Ja | True / False |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Erweiterbarer Slot: Verbinden Sie 1..N Elemente (z. B. `image_1`, `image_2`, ...); die Anzahlbegrenzung hängt vom ausgewählten Modell ab (siehe Modellabschnitte). Optionale Referenzbilder für Bild-zu-Bild- oder Multi-Referenz-Generierung. Ohne Referenzbilder arbeitet der Node im Text-zu-Bild-Modus. | IMAGE | Nein | 0 bis 10 Bilder (`seedream 5.0 pro`, `seedream-4-5-251128`, `seedream-4-0-250828`)<br>0 bis 14 Bilder (`seedream 5.0 lite`) |

### Hinweise zu Einschränkungen

- `width` und `height` wirken nur, wenn `size_preset` auf `Custom` gesetzt ist.
- Die Gesamtzahl aus Referenzbildern plus generierten Bildern darf 15 nicht überschreiten.
- `thinking` kann nur für die Text-zu-Bild-Generierung deaktiviert werden, nicht wenn Referenzbilder bereitgestellt werden.
- Seedream 5.0 Pro unterstützt keine Batch-Generierung: Es erzeugt immer ein einzelnes Bild, daher sind `max_images` und `fail_on_partial` für dieses Modell nicht verfügbar.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das generierte oder bearbeitete Bild als Tensor. Wenn mehrere Bilder angefordert wurden, werden sie zu einem einzelnen Batch zusammengefügt. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `f1a84171d94c602ec5417e43857ddf511ab1e54caa089b1928f740d3a38423f8`
