# Flux Video Upscale

Flux Video Upscale vergrößert ein Video mit FLUX-Superauflösung, entweder auf eine feste Frame-Größe von 1080p, 2K oder 4K oder um das 1,5- bis 3-Fache. Der Kreativ-Modus stellt feine Details wieder her und erfindet sie hinzu, was zu generiertem Material passt; der Präzise-Modus schärft die Quelle, ohne sie zu verändern, was zu Gesichtern, Produkten und echtem Filmmaterial passt. Der Clip wird hochgeladen, der BFL-Job wird abgefragt, und das fertige Video kommt mit 24 fps zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Quellclip von 1 bis 20 Sekunden, mindestens 64x64 Pixel, mit einem Seitenverhältnis zwischen 1:4 und 4:1. Die Ausgabe wird mit 24 fps gerendert und auf etwa 14,4 Megapixel pro Frame begrenzt. | VIDEO | Ja | 1 bis 20 Sekunden Dauer; Seitenverhältnis zwischen 1:4 und 4:1; mindestens 64x64 Pixel |
| `target_resolution` | Ausgabegröße. `"1080p"`, `"2K"` und `"4K"` passen das Ergebnis in 1920x1080, 2560x1440 oder 3840x2160 Pixel ein, bei Hochformat-Clips gedreht; `"by factor"` verwendet stattdessen `upscale_factor`. | DYNAMIC_COMBO | Ja | `"2K"`<br>`"4K"`<br>`"1080p"`<br>`"by factor"` |
| `mode` | `"creative"` stellt feine Details wieder her und erfindet sie hinzu, am besten für generiertes Material, Texturen und Landschaften. `"precise"` schärft die Quelle, ohne sie zu verändern, für Gesichter, Produkte und echtes Filmmaterial. (Standard: `"creative"`) | COMBO | Ja | `"creative"`<br>`"precise"` |
| `prompt` | Optionale Beschreibung des Clips, die die verbesserten Details lenkt. Leer lassen für ein neutrales Upscaling. (Standard: leer) | STRING | Ja | Mehrzeiliger Text |
| `auto_downscale` | Zu große Quellen herunterskalieren, anstatt sie abzulehnen: über 2560x1440 Pixel in der Fläche oder über zwei Drittel der Zielauflösung. Das Seitenverhältnis bleibt erhalten. (Standard: true) | BOOLEAN | Ja | true<br>false |
| `safety_tolerance` | Moderationstoleranz, 0 ist am strengsten. (Standard: 2, erweiterter Parameter) | INT | Ja | 0 bis 4 |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; FLUX wählt seinen eigenen Seed, daher sind die tatsächlichen Ergebnisse unabhängig von diesem Wert nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 4294967295 |

### by factor Eingaben

Diese Eingaben erscheinen, wenn `target_resolution` auf `"by factor"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `upscale_factor` | Ausgabegröße relativ zur Quelle. Sehr große Quellen werden wegen der Pro-Frame-Begrenzung um weniger als den angeforderten Faktor hochskaliert. (Standard: 2.0) | FLOAT | Ja | 1.5 bis 3.0 (Schritt 0.1) |

Eine Zielgröße wird als Upscale-Faktor angewendet, der auf 1,5–3,0 begrenzt ist. Eine Quelle, die zu klein ist, um bei 3x die Box zu füllen, fällt daher kleiner aus als die angeforderte Auflösung, und eine Quelle, die weniger als 1,5x benötigen würde, um in die Box zu passen, wird zuerst herunterskaliert. Ist `auto_downscale` ausgeschaltet, bricht der Node mit einem Fehler ab, anstatt herunterzuskalieren. Die Ausgabe hat 24 fps und ist auf etwa 14,4 Megapixel pro Frame begrenzt, sodass sehr große Quellen möglicherweise um weniger als den angeforderten Faktor hochskaliert werden.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Der hochskalierte Videoclip. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `bef6ef4614d75bc9e6bab977f5f19c45fe30d300907913462a058e6e7e7e4ac7`
