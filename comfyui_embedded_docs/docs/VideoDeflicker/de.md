# Video Deflicker

Entfernt zeitliches Flackern aus einem verarbeiteten Video, sodass jedes Einzelbild seine eigenen Details behält und gleichzeitig der Bewegung seiner Nachbarbilder folgt. Es ist für Aufnahmen gedacht, die nach dem Hochskalieren oder der Verarbeitung Bild für Bild pulsieren: Verbinden Sie das Optical-Flow-Modell und die flackernden Einzelbilder und optional eine stabile Kopie der Quelle als Führung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `optical_flow` | Optisches Flussmodell vom Load Optical Flow Model-Node (torchvision RAFT-large). | OPTICAL_FLOW | Ja | - |
| `images` | Flackernde Einzelbilder, die stabilisiert werden sollen, zum Beispiel ein Video, das hochskaliert oder Bild für Bild verarbeitet wurde. | IMAGE | Ja | - |
| `guide` | Stabile Quellbilder, deren Bewegung verfolgt wird, in beliebiger Auflösung. Standardmäßig `images`, wodurch weniger Flackern entfernt wird. | IMAGE | Nein | - |
| `strength` | Wie stark jedes Einzelbild seinen Nachbarbildern folgt (Standard: 1.0). Höhere Werte entfernen mehr Flackern und glätten mehr feine Details; 0 gibt die Einzelbilder unverändert zurück. | FLOAT | Ja | 0.0 bis 100.0 (Schritt: 0.1) |
| `direction` | Richtung des Durchlaufs. `bidirectional` mittelt einen Vorwärts- und einen Rückwärtsdurchlauf, wodurch ein Nachziehen hinter der Bewegung vermieden wird; `forward` führt einen einzelnen Durchlauf aus. (Standard: `bidirectional`) | COMBO | Ja | `"bidirectional"`<br>`"forward"` |
| `threshold` | Änderungen, die zwischen einem Einzelbild und seinem bewegungskompensierten Nachbarbild größer als dieser Wert sind, werden als real behandelt und weniger geglättet (Standard: 0.1). 0 glättet jede Änderung gleichermaßen. | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |

**Hinweise:**

- Die Führung liefert nur die Bewegung, nicht die Pixel: Der Optical Flow wird auf einer verkleinerten Kopie berechnet, sie muss also nicht dieselbe Größe wie `images` haben.
- Einzelbilder jenseits des kürzeren von `images` und `guide` werden nicht entrauscht. Ist `guide` kürzer, kommen die restlichen Einzelbilder unverändert zurück.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Entflackerte Einzelbilder mit derselben Größe und Bildanzahl wie `images`. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoDeflicker/de.md)

---
**Source fingerprint (SHA-256):** `d9937a67b0ac33ef3b326017e7d7990474705917902f1097cfeb06d9f83322a1`
