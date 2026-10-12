# Flux3ImageToVideoNode

Flux 3 Image to Video animiert 1 bis 10 Bilder mit FLUX 3. Jedes Bild wird zu einem Frame des Clips: Ein Bild eröffnet ihn, zwei morphen vom ersten zum zweiten, und weitere werden über ihn verteilt oder an von Ihnen gewählte Zeitpunkte angeheftet.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `placement` | "spread across the clip" lässt FLUX 3 die Bilder platzieren (eines eröffnet den Clip, zwei werden zu dessen Anfang und Ende); "at times" heftet jedes Bild an eine von Ihnen gewählte Sekunde. | DYNAMIC_COMBO | Ja | `"spread across the clip"` (Standard)<br>`"at times"` |
| `prompt` | Wie sich die Szene bewegen und anhören soll; der Prompt wird vor der Generierung interpretiert und erweitert. Muss mindestens ein Zeichen enthalten. | STRING | Ja | Mehrzeiliger Text (Standard: leer) |
| `aspect_ratio` | Seitenverhältnis der Ausgabe. "auto" wählt eines anhand des Prompts und der Eingaben aus. | COMBO | Ja | `"auto"` (Standard)<br>weitere verfügbare Seitenverhältnisse |
| `duration` | Cliplänge in Sekunden. "auto" passt die Länge an den Inhalt an. | COMBO | Ja | `"auto"` (Standard)<br>weitere verfügbare Dauern |
| `resolution` | Auflösung der Ausgabe. | COMBO | Ja | `"720p"` (Standard)<br>`"1080p"` |
| `generate_audio` | Synchronisierten Ton generieren (Umgebung, Sprache, Effekte). Aus erzeugt ein Video ohne Audiospur. | BOOLEAN | Ja | true / false (Standard: true) |
| `safety_tolerance` | Moderationstoleranz, 0 ist am strengsten. Anfragen, die Bilder oder Videos senden, werden unabhängig von der hier festgelegten Einstellung auf 2 begrenzt. | INT | Ja | 0 bis 4 (Standard: 2, erweiterte Einstellung) |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; FLUX 3 wählt seinen eigenen Seed, daher sind die tatsächlichen Ergebnisse unabhängig von diesem Wert nicht deterministisch. | INT | Ja | 0 bis 4294967295 (Standard: 42, Steuerung nach der Generierung) |

### Eingaben für "spread across the clip"

Diese Platzierungsoption hat keine zusätzlichen Parameter.

### Eingaben für "at times"

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `times` | Ein Zeitpunkt in Sekunden pro Bild, durch Kommas getrennt und ansteigend, z. B. "0, 2.5, 5". Erscheint nur, wenn `placement` auf "at times" gesetzt ist; für jedes Keyframe-Bild ist ein Zeitpunkt erforderlich. | STRING | Nein | Durch Kommas getrennte Sekunden (Standard: "0") |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `keyframes` | Erweiterbarer Slot: Verbinden Sie 1 bis 10 Keyframe-Bilder in Wiedergabereihenfolge, z. B. `image_1`, `image_2` und so weiter. Jedes Bild wird zu einem Frame des Clips. Mindestens 256x256 Pixel pro Bild; das Seitenverhältnis darf nicht extremer als 64:1 sein. | IMAGE | Ja | 1 bis 10 Bilder |

Hinweis: `keyframes` muss mindestens ein Bild enthalten; der Node gibt einen Fehler aus, wenn keines verbunden ist. Jedes Keyframe-Bild muss mindestens 256x256 Pixel groß sein, und sein Seitenverhältnis darf nicht extremer als 64:1 sein.

Wenn `placement` auf "spread across the clip" gesetzt ist und 3 oder mehr Keyframes verbunden sind, muss `duration` auf einen expliziten Wert gesetzt werden, nicht auf "auto"; andernfalls gibt der Node einen Fehler aus.

Wenn `placement` auf "at times" gesetzt ist, muss `times` einen Zeitpunkt in Sekunden pro Bild angeben. Die Zeitpunkte müssen ansteigen, dürfen nicht negativ sein, und der letzte Zeitpunkt darf nicht nach dem Ende des Clips liegen (bis zu 20 Sekunden, wenn `duration` auf "auto" gesetzt ist).

Da dieser Node Bilder sendet, ist `safety_tolerance` unabhängig von dem von Ihnen festgelegten Wert auf 2 begrenzt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Der generierte Videoclip, der aus den Keyframe-Bildern mit dem gewählten Seitenverhältnis, der gewählten Dauer, Auflösung und Audioeinstellung erstellt wurde. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `1c49838dfa13adc2ed70a51094f0dd860df7207970b8dceab6bb273653d7161c`
