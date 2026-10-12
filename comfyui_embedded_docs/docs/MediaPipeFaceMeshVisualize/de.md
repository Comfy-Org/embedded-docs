# Gesichtslandmarken visualisieren (MediaPipe)

## Überblick

Zeichnet Gesichts-Landmark-Punkte und Verbindungslinien (ein Gesichtsnetz) über ein Eingabebild. Dieser Node verwendet die Landmark-Daten, die von einem Gesichtserkennungs-Node erzeugt wurden, um die erkannten Gesichtsmerkmale wie Augen, Nase, Mund und Gesichtsumriss zu visualisieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `face_landmarks` | Die Gesichts-Landmark-Daten von einem Erkennungs-Node. | FACE_LANDMARKS | Ja |  |
| `image` | Das Bild, auf das das Netz gezeichnet werden soll. Wenn nicht verbunden, wird eine schwarze Leinwand derselben Größe wie das Erkennungsergebnis verwendet. | IMAGE | Nein |  |
| `connections` | Legt fest, welche Teile des Gesichtsnetzes gezeichnet werden. `"all"` zeichnet das vollständige Netz (Gesichtsumriss, Augen, Brauen, Lippen, Iris, Nase). `"fill"` zeichnet ein solides Polygon des Gesichtsumrisses (Silhouettenmaske). `"custom"` ermöglicht es, jedes Merkmal einzeln ein- oder auszuschalten. (Standard: `"all"`) | COMBO | Ja | `"all"`<br>`"fill"`<br>`"custom"` |
| `color` | Die Farbe der Netzlinien und -punkte. (Standard: `#00ff00`) | COLOR | Ja |  |
| `thickness` | Die Dicke der Netzlinien in Pixeln. Wenn dies auf 0 gesetzt wird, wird das Zeichnen von Linien deaktiviert. (Standard: 1) | INT | Ja | 0 to 8 |
| `point_size` | Der Radius der Landmark-Punkte in Pixeln. Wenn dies auf 0 gesetzt wird, wird das Zeichnen von Punkten deaktiviert. (Standard: 2) | INT | Ja | 0 to 16 |

**Hinweis zum Parameter `connections`:** Wenn `"custom"` ausgewählt ist, erscheinen zusätzliche boolesche Eingaben für jedes Gesichtsmerkmal (z. B. `face_oval`, `lips`, `left_eye`, `right_eye`, `left_eyebrow`, `right_eyebrow`, `left_iris`, `right_iris`, `nose`, `tesselation`). Nur die von Ihnen aktivierten Merkmale werden gezeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Das Eingabebild mit dem darauf gezeichneten Gesichts-Landmark-Netz. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMeshVisualize/de.md)

---
**Source fingerprint (SHA-256):** `fb5437d73378b0c8daa68669c2e19058ccb7133ed68fc51c8d4c5bab8662f243`
