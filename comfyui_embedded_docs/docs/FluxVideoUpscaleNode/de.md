# Flux Video Upscale (Legacy)

Flux Video Upscale skaliert einen Videoclip mit FLUX-Superauflösung um das 1,5- bis 3-Fache hoch. Im Modus "creative" werden feine Details wiederhergestellt und erfunden; im Modus "precise" wird die Quelle geschärft, ohne sie zu verändern.

**Hinweis:** Dieser Node ist im Quellcode als veraltet markiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|-----------|--------------|---------|
| `video` | Quellclip von 1 bis 20 Sekunden mit einem Seitenverhältnis zwischen 1:4 und 4:1. Die Ausgabe wird mit 24 fps gerendert und auf etwa 14,4 Megapixel pro Frame begrenzt. | VIDEO | Ja | 1 bis 20 Sekunden Dauer; Seitenverhältnis zwischen 1:4 und 4:1; mindestens 64x64 Pixel |
| `upscale_factor` | Ausgabegröße relativ zur Quelle. Sehr große Quellen werden aufgrund der Obergrenze pro Frame um weniger als den angeforderten Faktor hochskaliert. (Standard: 2.0) | FLOAT | Ja | 1.5 bis 3.0 (Schrittweite 0.1) |
| `mode` | "creative" stellt feine Details wieder her und erfindet sie, am besten für generiertes Material, Texturen und Landschaften. "precise" schärft die Quelle, ohne sie zu verändern, für Gesichter, Produkte und echtes Filmmaterial. (Standard: "creative") | COMBO | Ja | "creative"<br>"precise" |
| `prompt` | Optionale Beschreibung des Clips, die die verbesserten Details steuert. Leer lassen für ein neutrales Upscaling. (Standard: leer) | STRING | Ja | Mehrzeiliger Text |
| `auto_downscale` | Quellen, die in der Fläche größer als 2560x1440 Pixel sind, automatisch herunterskalieren, um das Eingabelimit einzuhalten. Das Seitenverhältnis bleibt erhalten; kleinere Videos bleiben unverändert. (Standard: true) | BOOLEAN | Ja | true<br>false |
| `safety_tolerance` | Moderationstoleranz; 0 ist am strengsten. (Standard: 2, erweiterter Parameter) | INT | Ja | 0 bis 4 |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; FLUX wählt seinen eigenen Seed, daher sind die tatsächlichen Ergebnisse unabhängig von diesem Wert nicht deterministisch. (Standard: 42) | INT | Ja | 0 bis 4294967295 |

Hinweis: Das Quellvideo muss zwischen 1 und 20 Sekunden lang, mindestens 64x64 Pixel groß sein und ein Seitenverhältnis zwischen 1:4 und 4:1 haben. Wenn `auto_downscale` deaktiviert ist und die Videofläche 2560x1440 Pixel überschreitet, löst der Node einen Fehler aus. Das Ausgabevideo wird mit 24 fps gerendert und auf etwa 14,4 Megapixel pro Frame begrenzt; daher können sehr große Quellen um weniger als den angeforderten Faktor hochskaliert werden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|-----------|
| `video` | Der hochskalierte Videoclip. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/de.md)

---
**Source fingerprint (SHA-256):** `2eeac17c04b4a2cde76a7e0d58b42ba5622cc22119b7ddc3c730463b2eb5d8c1`
