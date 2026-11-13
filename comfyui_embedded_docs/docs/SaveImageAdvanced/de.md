# Bild speichern (Erweitert)

Der Node **Save Image (Advanced)** speichert die Eingabebilder im ComfyUI-Ausgabeverzeichnis mit erweiterter Kontrolle über Dateiformat, Bittiefe und Farbraum. Er unterstützt das Speichern als PNG-, EXR- oder AVIF-Dateien (einschließlich animierter AVIF-Dateien) und kann Workflow-Metadaten in die gespeicherten Dateien einbetten.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Die zu speichernden Bilder. | IMAGE | Ja | - |
| `filename_prefix` | Das Präfix für die zu speichernde Datei. Kann Formatierungstoken wie `%date:yyyy-MM-dd%` oder `%Empty Latent Image.width%` enthalten. (Standard: "ComfyUI") | STRING | Ja | - |
| `format` | Das Dateiformat, in dem das Bild gespeichert werden soll. Durch Auswahl eines Formats werden zusätzliche Optionen für dieses Format eingeblendet. | DYNAMIC_COMBO | Ja | `"png"`<br>`"exr"`<br>`"avif"` |

### PNG-Eingaben

Diese Optionen werden angezeigt, wenn `format` auf `"png"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `bit_depth` | Die Bittiefe für die gespeicherte PNG-Datei. (Standard: "8-bit") | COMBO | Ja (bedingt) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Farbraum des Eingabe-Tensors. Für das PNG-Format ist nur sRGB verfügbar. (Standard: "sRGB") | COMBO | Ja (bedingt) | `"sRGB"` |
| `channels` | Welche Kanäle in die PNG geschrieben werden. `"auto"` behält die Eingabekanäle bei, Graustufen wandelt RGB in Helligkeit um und verwirft Alpha, RGB speichert Farbe ohne Alpha, und RGBA behält Alpha bei oder fügt ein vollständig opakes Alpha hinzu. (Standard: `"auto"`) | COMBO | Nein | `"auto"`<br>`"grayscale (1 channel)"`<br>`"RGB (3 channels)"`<br>`"RGBA (4 channels)"` |

### EXR-Eingaben

Diese Optionen werden angezeigt, wenn `format` auf `"exr"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `bit_depth` | Die Bittiefe für die gespeicherte EXR-Datei. (Standard: "16-bit float") | COMBO | Ja (bedingt) | `"16-bit float"`<br>`"32-bit float"` |
| `input_color_space` | Farbraum des Eingabe-Tensors. Das EXR wird immer als szenenlinear im passenden Gamut geschrieben.<br>`"sRGB"` — Die Eingabe ist sRGB-kodiertes Rec.709; die inverse sRGB-EOTF wird angewendet.<br>`"HDR"` — Die Eingabe ist HLG-kodiertes Rec.2020 (BT.2100); die inverse HLG-OETF wird angewendet, um szenenlineares Licht zu erhalten.<br>`"linear"` — Die Eingabe ist bereits szenenlinear (Rec.709-Primärfarben); sie wird unverändert durchgeschrieben. Verwenden Sie dies für Renderer-/Compositor-Ausgaben.<br>`"linear ACEScg"` — Die Eingabe ist bereits szenenlinear ACEScg (AP1 / D60); sie wird unverändert mit ACEScg-Chromatizitäten durchgeschrieben. (Standard: "sRGB") | COMBO | Ja (bedingt) | `"sRGB"`<br>`"HDR"`<br>`"linear"`<br>`"linear ACEScg"` |

### AVIF-Eingaben

Diese Optionen werden angezeigt, wenn `format` auf `"avif"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `bit_depth` | Die Bittiefe für die gespeicherte AVIF-Datei. Automatisch verwendet 8-bit YUV420 für sRGB und 10-bit YUV420 für HDR. (Standard: "auto") | COMBO | Ja (bedingt) | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | Farbraum der Eingabebilder. HDR wählt BT.2020/HLG und HDR PQ wählt BT.2020/PQ. (Standard: "sRGB") | COMBO | Ja (bedingt) | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | Niedrigere Werte erzeugen höhere Qualität und größere Dateien. (Standard: 18) | INT | Ja (bedingt) | 1 bis 63 |
| `save_mode` | Der Speichermodus für die AVIF-Datei. `"still images"` speichert jedes Bild im Batch als separate Standbilddatei; `"animated"` speichert den gesamten Batch als eine einzelne animierte AVIF-Datei und blendet `fps` und `loop_count` ein. (Standard: "still images") | DYNAMIC_COMBO | Ja (bedingt) | `"still images"`<br>`"animated"` |

### AVIF-Animationsoptionen

Diese Optionen werden angezeigt, wenn `save_mode` auf `"animated"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `fps` | Die Bildrate der Animation. (Standard: 6.0) | FLOAT | Ja (bedingt) | 0.01 bis 1000.0 |
| `loop_count` | Anzahl der Wiederholungen der Animation. 0 wiederholt endlos. (Standard: 0) | INT | Ja (bedingt) | 0 bis 1000 |

**Hinweise zu Parameterabhängigkeiten:**
- Die formatspezifischen Parameter (`bit_depth`, `input_color_space` und bei AVIF zusätzlich `crf` und `save_mode`) sind nur verfügbar, wenn ein bestimmtes `format` ausgewählt ist.
- Für das PNG-Format sind nur die Bittiefen "8-bit" und "16-bit" sowie nur der Farbraum "sRGB" verfügbar.
- Für das EXR-Format sind die Bittiefen "16-bit float" und "32-bit float" mit den Farbräumen "sRGB", "HDR", "linear" oder "linear ACEScg" verfügbar. "16-bit float" ist der Standard und erzeugt kleinere Dateien.
- Für das AVIF-Format sind `fps` und `loop_count` nur verfügbar, wenn `save_mode` auf `"animated"` gesetzt ist.
- PNG- und EXR-Bilder müssen 1 (Graustufen), 3 (RGB) oder 4 (RGBA) Kanäle haben; andere Kanalanzahlen werden nicht unterstützt und lösen einen Fehler aus.
- AVIF unterstützt nur 1-kanalige Graustufenbilder und 3-kanalige RGB-Bilder; RGBA-Bilder (mit Alpha) werden nicht unterstützt und lösen einen Fehler aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Die Eingabebilder, unverändert durchgereicht. Die UI-Ausgabe des Nodes stellt eine Liste gespeicherter Bildergebnisse bereit, wobei jedes den Dateinamen, Unterordner und Typ ("output") enthält. Bei animiertem AVIF mit mehr als einem Bild enthält die UI-Ausgabe außerdem ein `animated`-Flag. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/de.md)

---
**Source fingerprint (SHA-256):** `4e8a92c5f1bba35bc4cdf8c858cc9a6fe57cf08436e2dc303d8204c726108216`
