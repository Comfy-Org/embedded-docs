# DA3Render

Dieser Node rendert eine Visualisierung aus Depth Anything 3-Geometriedaten. Je nach ausgewähltem Ausgabemodus können Tiefenkarten, Konfidenzkarten oder Himmelsmasken ausgegeben werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | Das Depth Anything 3-Geometriedatenpaket, das Tiefe und optional Himmels- und Konfidenztensoren enthält | DA3_GEOMETRY | Ja | - |
| `output` | Der Typ der zu rendernden Visualisierung.<br>- depth: normalisiertes Graustufen-Tiefenbild.<br>- depth_colored: Tiefe, abgebildet über die Turbo-Colormap.<br>- sky_mask: Himmelwahrscheinlichkeit in [0, 1] (nur für Mono/Metric-Modelle).<br>- confidence: normalisierte Tiefenkonfidenz (nur für Small/Base-Modelle). | COMBO | Ja | "depth"<br>"depth_colored"<br>"sky_mask"<br>"confidence" |

### Unterparameter für `output`-Optionen

Wenn `output` auf `"depth"` oder `"depth_colored"` gesetzt ist:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `normalization` | Verfahren zur Tiefennormalisierung.<br>- v2_style: Mittelwert-/Std.-Normalisierung für perzeptuell ausgewogene Ergebnisse (Standard).<br>- min_max: streckt den gesamten Tiefenbereich auf [0, 1] für maximalen Kontrast.<br>- raw: keine Skalierung, behält metrische Einheiten für das Metric-Modell bei. | COMBO | Ja | "v2_style"<br>"min_max"<br>"raw" |
| `apply_sky_clip` | Begrenzt die Tiefe des Himmelsbereichs vor der Normalisierung auf das 99. Perzentil der Vordergrundtiefe. Erfordert einen Sky-Schlüssel in der Eingabe `da3_geometry` (nur für Mono/Metric-Modelle). Standard: False | BOOLEAN | Ja | True<br>False |

Wenn `output` auf `"sky_mask"` gesetzt ist:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `colored` | Wendet die Turbo-Colormap auf die Himmelsmaske an. Standard: False | BOOLEAN | Ja | True<br>False |

Wenn `output` auf `"confidence"` gesetzt ist:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `colored` | Wendet die Turbo-Colormap auf die Konfidenzkarte an. Standard: False | BOOLEAN | Ja | True<br>False |

### Parametereinschränkungen

- Wenn `apply_sky_clip` auf True gesetzt ist, muss die Eingabe `da3_geometry` einen Sky-Tensor enthalten. Dies ist nur verfügbar, wenn Mono- oder Metric-Modelle verwendet werden. Wenn der Sky-Tensor fehlt, löst der Node einen Fehler aus.
- Die Ausgabeoption `sky_mask` erfordert einen Sky-Tensor in der Eingabe `da3_geometry`. Dies ist nur mit Mono- oder Metric-Modellen verfügbar.
- Die Ausgabeoption `confidence` erfordert einen Konfidenztensor in der Eingabe `da3_geometry`. Dies ist nur mit Small- oder Base-Modellen verfügbar.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Die gerenderte Visualisierung als Bildtensor. Für Tiefenausgaben wird eine Graustufen- oder farbige Tiefenkarte zurückgegeben. Für sky_mask und confidence wird abhängig vom Parameter `colored` entweder eine Graustufen- oder eine farbige Visualisierung zurückgegeben. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Render/de.md)

---
**Source fingerprint (SHA-256):** `54d4cde95a916cac26c8a2e19c5623e794d46c0d7652f1c8204f9f2a0deabe0c`
