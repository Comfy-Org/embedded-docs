# Video zuschneiden (temporal)

Dieser Node schneidet einen fortlaufenden Bereich von Frames aus einem Video aus. Er arbeitet vollständig lazy, d. h. er verarbeitet nur den ausgewählten Teil des Videos, wenn er später im Workflow benötigt wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Eingabevideo. | VIDEO | Ja | – |
| `start_frame` | Index des Start-Frames (Standard: 0). | INT | Ja | 0 bis 99999 |
| `length` | Anzahl der beizubehaltenden Frames (Standard: 16). | INT | Ja | 1 bis 99999 |

Hinweis: `start_frame` ist auf den letzten Frame des Videos begrenzt, und `length` wird reduziert, wenn es über die verfügbaren Frames hinausgehen würde.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Zugeschnittenes Video (lazy). | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTemporalCrop/de.md)

---
**Source fingerprint (SHA-256):** `1d28a55399c9fe7ca47f0aaa872751ac89c5419a6f6be6636fbf7f020a02749d`
