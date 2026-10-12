# FoV aus MoGe-Geometrie abrufen

Dieser Node leitet das Sichtfeld und die Brennweite aus den Kamera-Intrinsics ab, die in einem MoGe-Geometrieobjekt gespeichert sind. Er kann den vertikalen, horizontalen oder diagonalen FOV zurückgeben, in Grad oder Bogenmaß. Die vertikale FOV-Ausgabe kann beispielsweise verwendet werden, um den Node SAM3DBody_Predict zu versorgen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `moge_geometry` | Das MoGe-Geometrieobjekt. Es muss eine Intrinsics-Matrix und mindestens eines der Daten `image`, `points` oder `depth` enthalten, die zum Auslesen der Pixelhöhe für die Brennweitenumrechnung verwendet werden. | MOGE_GEOMETRY | Ja | — |
| `axis` | Die Achse, entlang derer der FOV berechnet wird: „vertical“ (fov_y), „horizontal“ (fov_x) oder „diagonal“ (Standard: „vertical“). | COMBO | Ja | "vertical"<br>"horizontal"<br>"diagonal" |
| `unit` | Ausgabeeinheit für den FOV (Standard: „degrees“). | COMBO | Ja | "degrees"<br>"radians" |

Hinweis: Der Node löst einen Fehler aus, wenn `moge_geometry` keine Intrinsics enthält (Panorama-Geometrie enthält keine) oder wenn es weder `image`-, `points`- noch `depth`-Daten enthält.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `fov` | Das Sichtfeld entlang der ausgewählten Achse, in der ausgewählten Einheit („degrees“ oder „radians“). | FLOAT |
| `focal_pixels` | Die Brennweite des Objektivs in Pixeln, abgeleitet aus dem vertikalen Intrinsik-Wert und der Pixelhöhe. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/de.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`
