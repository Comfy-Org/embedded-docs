# MediaPipeFaceMask

## Überblick

Dieser Node erstellt eine binäre Maske (ein Schwarz-Weiß-Bild) basierend auf Gesichts-Landmarken, die von MediaPipe erkannt wurden. Er zeichnet gefüllte Polygonformen für jede erkannte Gesichtsregion und erzeugt eine Maske pro Frame in einem Batch. Wenn mehrere Gesichter im selben Frame erkannt werden, werden ihre Masken zu einer einzigen Maske zusammengeführt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `face_landmarks` | Die Gesichts-Landmarken-Daten von einem MediaPipe-Gesichtserkennungs-Node. | FACE_LANDMARKS | Ja | - |
| `regions` | Wählt aus, welche Gesichtsregionen in die Maske aufgenommen werden. `"all"` erstellt eine Maske aus der Vereinigung aller Gesichtsregionen (Gesichtsoval, Lippen, Augen, Iris). `"custom"` ermöglicht das individuelle Ein-/Ausschalten jeder Region. Standard: `"all"` | COMBO | Ja | `"all"`<br>`"custom"` |

Wenn `regions` auf `"custom"` gesetzt ist, werden die folgenden zusätzlichen booleschen Parameter verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `face_oval` | Die Gesichtsoval-Region in die Maske aufnehmen. Standard: True | BOOLEAN | Nein | True/False |
| `lips` | Die Lippenregion in die Maske aufnehmen. Standard: True | BOOLEAN | Nein | True/False |
| `eyes` | Die Augenregion in die Maske aufnehmen. Standard: True | BOOLEAN | Nein | True/False |
| `irises` | Die Irisregion in die Maske aufnehmen. Standard: True | BOOLEAN | Nein | True/False |

**Hinweis:** Bei Verwendung des Modus `"all"` enthält die Maske alle Regionen kombiniert. Da das Gesichtsoval die anderen Regionen umschließt, führt die Auswahl von `"all"` effektiv zum selben Ergebnis wie die Auswahl nur des Gesichtovals.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MASK` | Ein binärer Masken-Tensor, bei dem Gesichtsregionen weiß (Wert 1.0) und der Hintergrund schwarz (Wert 0.0) sind. Die Maske hat dieselben Abmessungen wie das Eingabebild und enthält eine Maske pro Frame im Batch. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMask/de.md)

---
**Source fingerprint (SHA-256):** `92270002a42ed59bc75e676a6881e1899186d3c8a1bb4dd4c0d39b3762b5bb66`
