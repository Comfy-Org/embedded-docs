# Topaz Video Enhance

Der **Topaz Video Enhance V2**-Node verleiht Videos mit leistungsstarker Upscaling- und Wiederherstellungstechnologie neues Leben. Er kann die Auflösung eines Videos mithilfe verschiedener Topaz-Upscaler-Modelle erhöhen, die Bildrate durch Frame-Interpolation anpassen und kreative oder realistische Verbesserungseinstellungen anwenden.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Das zu verarbeitende Eingabevideo. Muss im MP4-Containerformat vorliegen. | VIDEO | Ja | - |
| `upscaler_model` | Das KI-Modell, das zum Hochskalieren des Videos verwendet wird. Die verfügbaren Unterparameter hängen vom ausgewählten Modell ab. Wenn `"Disabled"` ausgewählt wird, wird das Upscaling deaktiviert. | DYNAMIC_COMBO | Ja | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` |
| `interpolation_model` | Das KI-Modell, das für die Frame-Interpolation verwendet wird. Die verfügbaren Unterparameter hängen vom ausgewählten Modell ab. Wenn `"Disabled"` ausgewählt wird, wird die Interpolation deaktiviert. | DYNAMIC_COMBO | Ja | `"Disabled"`<br>`"apo-8"` |
| `dynamic_compression_level` | CQP-Stufe für die Videokomprimierung (Standard: `"Low"`). | COMBO | Nein | `"Low"`<br>`"Mid"`<br>`"High"` |

In den folgenden Abschnitten werden die Unterparameter beschrieben, die für jede Option der Selektoren `upscaler_model` und `interpolation_model` angezeigt werden. Die Optionen `"Disabled"` zeigen keine zusätzlichen Parameter an.

### Astra 2 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Ziel-Ausgabeauflösung des Upscalings. | COMBO | Ja (wenn "Astra 2" ausgewählt ist) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Kreative Stärke des Upscalings (Standard: 0.5). | FLOAT | Nein | 0.0 bis 1.0 (Schritt 0.1) |
| `upscaler_model.prompt` | Optionaler beschreibender (nicht anweisender) Szenen-Prompt. Begrenzt die Eingabe auf 450 Frames (~15 s bei 30 fps), wenn gesetzt (Standard: leer). | STRING | Nein | - |
| `upscaler_model.sharp` | Schärfe vor der Verbesserung: 0.0=Gaußscher Weichzeichner, 0.5=Durchleitung (Standard), 1.0=USM-Schärfung. | FLOAT | Nein | 0.0 bis 1.0 (Schritt 0.01) |
| `upscaler_model.realism` | Zieht die Ausgabe in Richtung fotografischen Realismus. Bei 0 belassen für den Modellstandard (Standard: 0.0). | FLOAT | Nein | 0.0 bis 1.0 (Schritt 0.01) |

### Starlight (Astra) Fast Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Ziel-Ausgabeauflösung des Upscalings. | COMBO | Ja (wenn dieses Modell ausgewählt ist) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### Starlight (Astra) Creative Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Ziel-Ausgabeauflösung des Upscalings. | COMBO | Ja (wenn dieses Modell ausgewählt ist) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Kreative Stärke des Upscalings (Standard: `"low"`). | COMBO | Nein | `"low"`<br>`"middle"`<br>`"high"` |

### Starlight Precise 2.5 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Ziel-Ausgabeauflösung des Upscalings. | COMBO | Ja (wenn dieses Modell ausgewählt ist) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### apo-8 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `interpolation_model.interpolation_frame_rate` | Ausgabe-Bildrate (Standard: 60). | INT | Ja (wenn "apo-8" ausgewählt ist) | 15 bis 240 |
| `interpolation_model.interpolation_slowmo` | Auf das Eingabevideo angewendeter Zeitlupenfaktor. Zum Beispiel macht 2 die Ausgabe doppelt so langsam und verdoppelt die Dauer (Standard: 1). | INT | Nein | 1 bis 16 |
| `interpolation_model.interpolation_duplicate` | Analysiert die Eingabe auf doppelte Frames und entfernt sie (Standard: False). | BOOLEAN | Nein | True<br>False |
| `interpolation_model.interpolation_duplicate_threshold` | Erkennungsempfindlichkeit für doppelte Frames (Standard: 0.01). | FLOAT | Nein | 0.001 bis 0.1 (Schritt 0.001) |

**Wichtige Einschränkungen:**

- Mindestens einer der Parameter `upscaler_model` oder `interpolation_model` muss aktiviert sein. Wenn beide auf `"Disabled"` gesetzt sind, löst der Node einen Fehler aus, da nichts zu verarbeiten ist.
- Die Eingabe `video` muss im MP4-Containerformat vorliegen.
- Das Modell `"Astra 2"` ist auf 9000 Eingabe-Frames begrenzt. Wenn ein `prompt` gesetzt ist, liegt das Limit bei 450 Eingabe-Frames (~15 Sekunden bei 30 fps). Der Node löst einen Fehler aus, wenn das Video das zutreffende Limit überschreitet.
- `upscaler_model.upscaler_resolution` ist erforderlich, wann immer ein anderes Upscaler-Modell als `"Disabled"` ausgewählt ist. `"FullHD (1080p)"` zielt auf ein 1080p-Ergebnis und `"4K (2160p)"` auf ein 2160p-Ergebnis ab; die genaue Ausgabebreite und -höhe werden aus dem Seitenverhältnis der Eingabe berechnet, auf eine maximale lange Seite von 1920 bzw. 3840 Pixeln begrenzt und auf eine gerade Zahl gerundet.
- `interpolation_model.interpolation_frame_rate` ist erforderlich, wann immer `interpolation_model` `"apo-8"` ist.
- Sehr große Dateien werden derzeit nicht unterstützt; Uploads sind auf einen einzelnen Teil begrenzt, andernfalls löst der Node einen Fehler aus.
- Mehrere Parameter (`sharp`, `realism`, `interpolation_slowmo`, `interpolation_duplicate`, `interpolation_duplicate_threshold`) sind in der UI als erweitert markiert und können standardmäßig ausgeblendet sein.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das verbesserte Video nach Anwendung der ausgewählten Upscaling- und/oder Interpolationsfilter. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/de.md)

---
**Source fingerprint (SHA-256):** `14627dc772a6a46a645517bd34b545e0986a84561e24bdfe810b67f791ee47e3`
