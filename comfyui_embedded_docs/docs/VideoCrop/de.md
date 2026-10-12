# Video zuschneiden

Dieser Node schneidet ein Video auf einen in Pixeln definierten rechteckigen Bereich zu und behält nur den Bereich innerhalb dieses Rechtecks bei. Er speichert eine temporäre MP4-Vorschau des zugeschnittenen Ergebnisses und gibt das zugeschnittene Video aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Das Quellvideo, das zugeschnitten wird. | VIDEO | Ja | Beliebiges Video |
| `crop` | Zuschneidebereich in Pixeln. Eine Breite/Höhe von 0 behält das vollständige Bild bei. Das Zuschneide-Rechteck liefert Werte für `x`, `y`, `width` und `height`, die alle standardmäßig 0 sind. | VIDEO_EDIT | Ja | `x` ≥ 0<br>`y` ≥ 0<br>`width` ≥ 0<br>`height` ≥ 0<br>Alle Werte haben den Standardwert 0 |

Hinweis: Der Zuschneidebereich wird in Pixelkoordinaten angegeben. Wenn Breite und Höhe 0 sind, wird kein Zuschnitt angewendet und der Node gibt das vollständige Eingabevideo aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das auf den ausgewählten rechteckigen Bereich zugeschnittene Video. Wenn die Breite und Höhe des Zuschnitts 0 sind, ist die Ausgabe das vollständige Eingabevideo. Das zugeschnittene Ergebnis wird außerdem als temporäre MP4-Datei gespeichert und als Videovorschau angezeigt. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoCrop/de.md)

---
**Source fingerprint (SHA-256):** `0c4ebd51027669fc232fe42a5e8840b5e4e95083b6794cd7b4c43123ddc0341b`
