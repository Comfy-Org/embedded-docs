# WanMoveTracksFromCoords

Der Node WanMoveTracksFromCoords erstellt Bewegungs-Tracks aus einer JSON-formatierten Zeichenkette mit Koordinaten. Er konvertiert die Koordinatendaten in ein Track-Format, das von anderen Videoverarbeitungs-Nodes verwendet werden kann, und kann optional eine Maske anwenden, um die Sichtbarkeit der Tracks im zeitlichen Verlauf zu steuern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `track_coords` | Eine JSON-formatierte Zeichenkette, die die Koordinatendaten für die Tracks enthält. Der Standardwert ist eine leere Liste (`"[]"`). Dieser Eingang ist ein erzwungener Eingang und muss daher in der Benutzeroberfläche verbunden werden. | STRING | Nein | N/A |
| `track_mask` | Eine optionale Maske. Wenn sie bereitgestellt wird, verwendet der Node sie, um die Sichtbarkeit der Tracks pro Frame zu bestimmen: Tracks sind in Frames sichtbar, in denen die Maske mindestens einen Pixel ungleich Null enthält. Wenn sie nicht bereitgestellt wird, sind alle Tracks in allen Frames sichtbar. | MASK | Nein | N/A |

**Hinweis:** Der Eingang `track_coords` erwartet eine bestimmte JSON-Struktur. Es sollte eine Liste von Tracks sein, wobei jeder Track eine Liste von Frames ist und jeder Frame ein Objekt mit den Koordinaten `x` und `y` ist. Die Anzahl der Frames muss über alle Tracks hinweg konsistent sein, und mindestens ein Track muss bereitgestellt werden.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `tracks` | Die generierten Track-Daten, die die Pfadkoordinaten und Sichtbarkeitsinformationen für jeden Track enthalten. | TRACKS |
| `track_length` | Die Gesamtzahl der Frames in den generierten Tracks. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/de.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
