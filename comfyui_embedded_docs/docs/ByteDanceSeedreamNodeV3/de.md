# ByteDanceSeedreamNodeV3

ByteDance Seedream 4.5 & 5.0 erzeugt Bilder aus einem Text-Prompt (Text-zu-Bild) oder generiert/bearbeitet Bilder, die durch optionale Referenzbilder gesteuert werden, unter Verwendung der Modelle ByteDance Seedream 4.0, 4.5 und 5.0 mit bis zu 4K-Auflösung. Der Node sendet den Prompt und alle Referenzbilder an die ByteDance-API, wartet, bis die Generierungsaufgabe abgeschlossen ist, und gibt den resultierenden Bildtensor oder die resultierenden Tensoren zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Text-Prompt zum Erstellen oder Bearbeiten eines Bildes. Darf nach dem Entfernen von Leerzeichen nicht leer sein. | STRING | Ja | Mehrzeiliger Text |
| `model` | Wählt das zu verwendende Seedream-Modell aus. Jedes Modell bietet unten einen eigenen Satz an Unterparametern und Limits. | DYNAMIC_COMBO | Ja | "seedream 5.0 pro"<br>"seedream 5.0 flash"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Seedream 5.0 Pro Eingaben (seedream 5.0 pro)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `size_preset` | Wählen Sie eine empfohlene Größe. Wählen Sie Custom, um die unten angegebene Breite und Höhe zu verwenden. Standard: erste empfohlene Voreinstellung für dieses Modell. | COMBO | Nein | Modellspezifische empfohlene Größen-Voreinstellungen<br>"Custom" |
| `width` | Benutzerdefinierte Breite für das Bild. Der Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 2048. | INT | Nein | 1024 bis 4514 (Schrittweite 2) |
| `height` | Benutzerdefinierte Höhe für das Bild. Der Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 2048. | INT | Nein | 1024 bis 4514 (Schrittweite 2) |
| `prompt_optimization` | Prompt-Optimierungsmodus, wenn Referenzbilder bereitgestellt werden: 'standard' liefert höhere Qualität, 'fast' eine kürzere Generierungszeit. Standard: "standard". | COMBO | Nein | "standard"<br>"fast" |
| `seed` | Seed für die Generierung. Standard: 42. | INT | Nein | 0 bis 2147483647 |
| `watermark` | Legt fest, ob dem Bild ein Wasserzeichen „AI generated“ hinzugefügt wird. Standard: false. | BOOLEAN | Nein | true / false |
| `thinking` | Aktiviert das Prompt-Optimierungs-Reasoning ('thinking') des Modells für bessere Prompt-Treue. Kann die Generierungszeit erheblich verlängern – insbesondere bei Seedream 5.0 Pro. Kann nur für Text-zu-Bild deaktiviert werden (nicht, wenn Referenzbilder bereitgestellt werden). Standard: true. | BOOLEAN | Nein | true / false |

### Seedream 5.0 Flash Eingaben (seedream 5.0 flash)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `size_preset` | Wählen Sie eine empfohlene Größe. Wählen Sie Custom, um die unten angegebene Breite und Höhe zu verwenden. Standard: erste empfohlene Voreinstellung für dieses Modell. | COMBO | Nein | Modellspezifische empfohlene Größen-Voreinstellungen<br>"Custom" |
| `width` | Benutzerdefinierte Breite für das Bild. Der Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 2048. | INT | Nein | 1024 bis 4514 (Schrittweite 2) |
| `height` | Benutzerdefinierte Höhe für das Bild. Der Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 2048. | INT | Nein | 1024 bis 4514 (Schrittweite 2) |
| `seed` | Seed für die Generierung. Standard: 42. | INT | Nein | 0 bis 2147483647 |
| `watermark` | Legt fest, ob dem Bild ein Wasserzeichen „AI generated“ hinzugefügt wird. Standard: false. | BOOLEAN | Nein | true / false |

### Seedream 5.0 Lite Eingaben (seedream 5.0 lite)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `size_preset` | Wählen Sie eine empfohlene Größe. Wählen Sie Custom, um die unten angegebene Breite und Höhe zu verwenden. Standard: erste empfohlene Voreinstellung für dieses Modell. | COMBO | Nein | Modellspezifische empfohlene Größen-Voreinstellungen<br>"Custom" |
| `width` | Benutzerdefinierte Breite für das Bild. Der Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 2048. | INT | Nein | 1024 bis 6240 (Schrittweite 2) |
| `height` | Benutzerdefinierte Höhe für das Bild. Der Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 2048. | INT | Nein | 1024 bis 4992 (Schrittweite 2) |
| `max_images` | Maximale Anzahl zu generierender Bilder. Bei 1 wird genau ein Bild erzeugt. Bei >1 generiert das Modell zwischen 1 und max_images zusammenhängende Bilder (z. B. Story-Szenen, Charaktervarianten). Die Gesamtzahl der Bilder (Eingabe + generiert) darf 15 nicht überschreiten. Standard: 1. | INT | Nein | 1 bis 14 |
| `fail_on_partial` | Wenn aktiviert, wird die Ausführung abgebrochen, wenn angeforderte Bilder fehlen oder einen Fehler zurückgeben. Standard: false. | BOOLEAN | Nein | true / false |
| `seed` | Seed für die Generierung. Standard: 42. | INT | Nein | 0 bis 2147483647 |
| `watermark` | Legt fest, ob dem Bild ein Wasserzeichen „AI generated“ hinzugefügt wird. Standard: false. | BOOLEAN | Nein | true / false |
| `thinking` | Aktiviert das Prompt-Optimierungs-Reasoning ('thinking') des Modells für bessere Prompt-Treue. Kann die Generierungszeit erheblich verlängern – insbesondere bei Seedream 5.0 Pro. Kann nur für Text-zu-Bild deaktiviert werden (nicht, wenn Referenzbilder bereitgestellt werden). Standard: true. | BOOLEAN | Nein | true / false |

### Seedream 4.5 Eingaben (seedream-4-5-251128)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `size_preset` | Wählen Sie eine empfohlene Größe. Wählen Sie Custom, um die unten angegebene Breite und Höhe zu verwenden. Standard: erste empfohlene Voreinstellung für dieses Modell. | COMBO | Nein | Modellspezifische empfohlene Größen-Voreinstellungen<br>"Custom" |
| `width` | Benutzerdefinierte Breite für das Bild. Der Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 2048. | INT | Nein | 1024 bis 6240 (Schrittweite 2) |
| `height` | Benutzerdefinierte Höhe für das Bild. Der Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 2048. | INT | Nein | 1024 bis 4992 (Schrittweite 2) |
| `max_images` | Maximale Anzahl zu generierender Bilder. Bei 1 wird genau ein Bild erzeugt. Bei >1 generiert das Modell zwischen 1 und max_images zusammenhängende Bilder (z. B. Story-Szenen, Charaktervarianten). Die Gesamtzahl der Bilder (Eingabe + generiert) darf 15 nicht überschreiten. Standard: 1. | INT | Nein | 1 bis 10 |
| `fail_on_partial` | Wenn aktiviert, wird die Ausführung abgebrochen, wenn angeforderte Bilder fehlen oder einen Fehler zurückgeben. Standard: false. | BOOLEAN | Nein | true / false |
| `seed` | Seed für die Generierung. Standard: 42. | INT | Nein | 0 bis 2147483647 |
| `watermark` | Legt fest, ob dem Bild ein Wasserzeichen „AI generated“ hinzugefügt wird. Standard: false. | BOOLEAN | Nein | true / false |
| `thinking` | Aktiviert das Prompt-Optimierungs-Reasoning ('thinking') des Modells für bessere Prompt-Treue. Kann die Generierungszeit erheblich verlängern – insbesondere bei Seedream 5.0 Pro. Kann nur für Text-zu-Bild deaktiviert werden (nicht, wenn Referenzbilder bereitgestellt werden). Standard: true. | BOOLEAN | Nein | true / false |

### Seedream 4.0 Eingaben (seedream-4-0-250828)

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `size_preset` | Wählen Sie eine empfohlene Größe. Wählen Sie Custom, um die unten angegebene Breite und Höhe zu verwenden. Standard: erste empfohlene Voreinstellung für dieses Modell. | COMBO | Nein | Modellspezifische empfohlene Größen-Voreinstellungen<br>"Custom" |
| `width` | Benutzerdefinierte Breite für das Bild. Der Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 2048. | INT | Nein | 1024 bis 6240 (Schrittweite 2) |
| `height` | Benutzerdefinierte Höhe für das Bild. Der Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 2048. | INT | Nein | 1024 bis 4992 (Schrittweite 2) |
| `max_images` | Maximale Anzahl zu generierender Bilder. Bei 1 wird genau ein Bild erzeugt. Bei >1 generiert das Modell zwischen 1 und max_images zusammenhängende Bilder (z. B. Story-Szenen, Charaktervarianten). Die Gesamtzahl der Bilder (Eingabe + generiert) darf 15 nicht überschreiten. Standard: 1. | INT | Nein | 1 bis 10 |
| `fail_on_partial` | Wenn aktiviert, wird die Ausführung abgebrochen, wenn angeforderte Bilder fehlen oder einen Fehler zurückgeben. Standard: false. | BOOLEAN | Nein | true / false |
| `seed` | Seed für die Generierung. Standard: 42. | INT | Nein | 0 bis 2147483647 |
| `watermark` | Legt fest, ob dem Bild ein Wasserzeichen „AI generated“ hinzugefügt wird. Standard: false. | BOOLEAN | Nein | true / false |
| `thinking` | Aktiviert das Prompt-Optimierungs-Reasoning ('thinking') des Modells für bessere Prompt-Treue. Kann die Generierungszeit erheblich verlängern – insbesondere bei Seedream 5.0 Pro. Kann nur für Text-zu-Bild deaktiviert werden (nicht, wenn Referenzbilder bereitgestellt werden). Standard: true. | BOOLEAN | Nein | true / false |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `images` | Erweiterbarer Slot: optionale(s) Referenzbild(er) für Bild-zu-Bild- oder Multi-Referenz-Generierung. Verbinden Sie 1..N Bilder (z. B. `image_1`, `image_2`, ...); das Anzahllimit ist modellabhängig (siehe Hinweise unten). Wenn ein verbundenes Bild einen Batch von Bildern enthält, zählt jedes Bild im Batch zum Limit. | IMAGE | Nein | 0 bis 10 (Seedream 5.0 Pro, Seedream 5.0 Flash, Seedream 4.5, Seedream 4.0)<br>0 bis 14 (Seedream 5.0 Lite) |

**Hinweise:**

- Der `prompt` darf nach dem Entfernen von Leerzeichen nicht leer sein.
- Maximale Anzahl der Referenzbilder: 10 für Seedream 5.0 Pro, Seedream 5.0 Flash, Seedream 4.5 und Seedream 4.0; 14 für Seedream 5.0 Lite.
- Jedes Referenzbild muss ein Seitenverhältnis zwischen 1:16 und 16:1 haben.
- Wenn `max_images` größer als 1 ist (nicht verfügbar bei Seedream 5.0 Pro oder Seedream 5.0 Flash), darf die Gesamtzahl aus Referenzbildern plus generierten Bildern 15 nicht überschreiten.
- `thinking` kann nur für die Text-zu-Bild-Generierung deaktiviert werden. Wenn Referenzbilder bereitgestellt werden, muss `thinking` aktiviert sein. Seedream 5.0 Flash hat keinen `thinking`-Eingang.
- `width` und `height` werden nur verwendet, wenn `size_preset` auf "Custom" gesetzt ist.
- `prompt_optimization` ist nur bei Seedream 5.0 Pro verfügbar.
- `max_images` und `fail_on_partial` sind nur bei Seedream 5.0 Lite, Seedream 4.5 und Seedream 4.0 verfügbar; Seedream 5.0 Pro und Seedream 5.0 Flash fordern immer ein einzelnes Bild an.
- Auflösungsanforderungen (Breite x Höhe):
  - Seedream 5.0 Pro und Seedream 5.0 Flash: zwischen 0,92 MP (921.600 Pixel) und 4,62 MP (4.624.220 Pixel).
  - Seedream 5.0 Lite und Seedream 4.5: mindestens 3,68 MP (3.686.400 Pixel).
  - Seedream 4.0: mindestens 0,92 MP (921.600 Pixel).
  - Seedream 5.0 Lite, Seedream 4.5 und Seedream 4.0: höchstens 16,78 MP (16.777.216 Pixel).

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `image` | Der generierte Bildtensor. Wenn mehrere Bilder generiert werden, werden sie zu einem einzelnen gebündelten IMAGE-Tensor verkettet. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/de.md)

---
**Source fingerprint (SHA-256):** `1c1f40b202ccbb3e0f73cd072170e1c16b833e007f26e63505b54c42b004a8a6`
