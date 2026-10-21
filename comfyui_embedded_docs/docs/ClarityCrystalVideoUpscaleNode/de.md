# Clarity AI Crystal Video Upscale

Skalieren Sie ein Video mit dem Crystal Video Upscaler von Clarity AI hoch, einem hochpräzisen Upscaler, der quellentreu bleibt. Der Clip wird hochgeladen, um den von Ihnen festgelegten Faktor hochskaliert und als Video zurückgegeben. Die Ausgabe ist auf 9 Megapixel pro Einzelbild (zum Beispiel 4000x2250) und auf 360 Megapixelsekunden pro Clip begrenzt, sodass große oder lange Clips mit einer niedrigeren Auflösung zurückkommen, als es der Faktor verlangt.

Die Auswahl eines `model` blendet die für dieses Modell spezifischen Parameter ein.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. Die Auswahl eines Modells blendet die dafür spezifischen Parameter ein: `video` und `scale_factor`. | DYNAMIC_COMBO | Ja | `"crystal-video-upscaler"` |
| `video` | Das hochzuskalierende Video. | VIDEO | Ja | N/A |
| `scale_factor` | Faktor, mit dem die Breite und Höhe des Videos multipliziert werden. Die Ausgabe ist auf 9 Megapixel pro Einzelbild und 360 Megapixelsekunden pro Clip begrenzt, sodass große oder lange Videos weniger stark hochskaliert werden; der Faktor wird erneut verringert, wenn dadurch eine Seite über 5120 Pixel hinausgehen würde (Standard: 2.0). | FLOAT | Ja | 1.0 bis 200.0 (Schritt 0.1) |

**Hinweis:** Der Clip darf an jeder Seite höchstens 5120 Pixel und pro Einzelbild höchstens 9 Megapixel groß sein. Die maximale Länge hängt von der Bildgröße und der Bildrate ab: Sie ergibt sich aus 360 Megapixelsekunden geteilt durch die Pixel pro Einzelbild und durch die auf ein Vielfaches von 30 fps aufgerundete Bildrate, sodass ein 1080p-Clip bei 30 fps bis zu etwa 173 Sekunden lang sein kann. Clips über 30 fps kosten das 2-Fache, über 60 fps das 3-Fache und so weiter.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das hochskalierte Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalVideoUpscaleNode/de.md)

---
**Source fingerprint (SHA-256):** `ca44ed6591474421edaf7e4e99e6da62e0c2e4e66964b7dac51d45758150aaa8`
