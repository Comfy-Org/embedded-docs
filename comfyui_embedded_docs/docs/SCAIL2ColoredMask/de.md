# SCAIL2ColoredMask

Dieser Node rendert SAM3-Tracking-Daten in farbige Masken, die vom WanSCAILToVideo-Node verwendet werden. Er verarbeitet Tracking-Daten aus einem Driving-Pose-Video und optional einem Referenzbild und weist jeder verfolgten Person über beide Ausgaben hinweg konsistente Farben zu.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `driving_track_data` | SAM3-Track des Driving-Pose-Videos. Wird in die Ausgabe `pose_video_mask` gerendert. | SAM3_TRACK_DATA | Ja | - |
| `ref_track_data` | SAM3-Track des/der Referenzbildes/-bilder (eine Identität pro Objekt, in Batch-Reihenfolge eingefärbt), oder eine einfache MASK des Referenzsubjekts (als einzelne Identität gerendert). | SAM3_TRACK_DATA oder MASK | Nein | - |
| `object_indices` | Kommagetrennte Liste der einzubeziehenden Personenindizes (z. B. '0,2,3'). Wird sowohl auf Referenz- als auch auf Pose-Video-Masken angewendet. Leer = alle. (Standard: "") | STRING | Ja | - |
| `sort_by` | Reihenfolge, in der Palettenfarben den verfolgten Objekten zugewiesen werden (wird sowohl auf Referenz als auch auf Pose-Video angewendet, damit jede Identität dieselbe Farbe behält). Objekte, die in früheren Frames erscheinen, kommen immer zuerst; innerhalb eines Frames: left_to_right = das am weitesten links liegende Objekt (nach Schwerpunkt beim ersten Erscheinen) erhält die erste Farbe, area = das größte Objekt (nach Maskenfläche beim ersten Erscheinen) erhält die erste Farbe; none = SAM3-Reihenfolge beibehalten. (Standard: "left_to_right") | COMBO | Ja | `"none"`<br>`"left_to_right"`<br>`"area"` |
| `replacement_mode` | False = Animationsmodus (pose_video_mask hat schwarzen Hintergrund, reference_image_mask hat weißen Hintergrund). True = Ersetzungsmodus (pose_video_mask hat weißen Hintergrund, reference_image_mask hat schwarzen Hintergrund). (Standard: False) | BOOLEAN | Ja | False<br>True |

Hinweis: `object_indices` akzeptiert nur kommagetrennte Ziffern; nicht numerische Einträge und Indizes außerhalb des gültigen Bereichs werden ignoriert. Wenn `ref_track_data` nicht angegeben ist, ist die Ausgabe `reference_image_mask` eine Vollfüllung mit der Hintergrundfarbe der Referenz (weiß im Animationsmodus, schwarz im Ersetzungsmodus).

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `pose_video_mask` | Farbige Maske, gerendert aus den Tracking-Daten des Driving-Pose-Videos. Die Hintergrundfarbe folgt der Einstellung replacement_mode. | IMAGE |
| `reference_image_mask` | Farbige Maske, gerendert aus den Tracking-Daten des Referenzbildes. Der Hintergrund ist schwarz im Ersetzungsmodus, weiß im Animationsmodus. Wenn keine Referenzdaten bereitgestellt werden, wird eine Vollfüllung zurückgegeben, die der Hintergrundfarbe der Referenz entspricht. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/de.md)

---
**Source fingerprint (SHA-256):** `ce0669ad0ed3c76cc18ef0ee7b620f5aa6eaa1e5b96c189941c0a5b744c3351f`
