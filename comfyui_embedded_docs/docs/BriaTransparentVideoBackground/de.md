# Bria Videohintergrund entfernen (transparent)

Dieser Node entfernt den Hintergrund aus einem Video mithilfe des KI-Dienstes von Bria und gibt die freigestellten Frames zusammen mit einer Alpha-Maske aus. Verbinden Sie beide Ausgaben mit einem Compositing-Node oder führen Sie sie einem Save WEBM-Node zu, um ein transparentes Video zu schreiben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `video` | Das Eingabevideo, das verarbeitet werden soll. Das Video muss 60 Sekunden oder kürzer sein. | VIDEO | Ja | - |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0) | INT | Ja | 0 bis 2147483647 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `images` | Die Videoframes mit entferntem Hintergrund als RGB-Bilder im Bereich 0,0 bis 1,0 | IMAGE |
| `mask` | Die Alpha-Maske für die Videoframes, entsprechend der Load Image-Konvention, bei der 1 transparent bedeutet | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/de.md)

---
**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`
