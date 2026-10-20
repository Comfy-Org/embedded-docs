# FLUX 3 Max Image to Video

FLUX 3 Max Image to Video animiert 1 bis 10 Bilder mit FLUX 3 Max. Jedes Bild wird zu einem Frame des Clips: Ein Bild eröffnet ihn, zwei werden zu seinem ersten und letzten Frame, und mehr werden über den Clip verteilt oder an von Ihnen gewählten Zeitpunkten fixiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Wie sich die Szene bewegen und klingen soll (Standard: leer). | STRING | Ja | Mehrzeiliger Text |
| `keyframes` | Erweiterbarer Slot: Verbinden Sie 1 bis 10 Keyframe-Bilder in Wiedergabereihenfolge, z. B. `image_1`, `image_2` und so weiter. Jedes Bild wird zu einem Frame des Clips. | IMAGE | Ja | 1 bis 10 Bilder |
| `placement` | `"spread across the clip"` platziert das erste Bild am Anfang, das letzte am Ende und die übrigen gleichmäßig dazwischen; `"at times"` fixiert jedes Bild auf eine von Ihnen gewählte Sekunde (Standard: `"spread across the clip"`). | DYNAMIC_COMBO | Ja | `"spread across the clip"`<br>`"at times"` |
| `aspect_ratio` | Ausgabe-Seitenverhältnis. `"auto"` folgt dem ersten Keyframe-Bild (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Cliplänge in Sekunden (Standard: `"5"`). | COMBO | Ja | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `resolution` | Ausgabeauflösung (Standard: `"720p"`). | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `reasoning_level` | Wie stark das Modell den Prompt vor der Generierung durchdenkt und erweitert. `"high"` dauert länger; der Preis ist derselbe (Standard: `"high"`). | COMBO | Ja | `"low"`<br>`"high"` |
| `generate_audio` | Synchronisiertes Audio generieren. Aus erzeugt ein Video ohne Audiospur (Standard: true). | BOOLEAN | Ja | `true`<br>`false` |
| `seed` | Seed, der steuert, ob der Node erneut ausgeführt wird. Die Ergebnisse sind unabhängig von diesem Wert nicht deterministisch (Standard: 42). | INT | Ja | 0 bis 2147483646 |

### at times Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `times` | Ein Zeitpunkt in Sekunden pro Bild, durch Kommas getrennt und ansteigend, z. B. "0, 2.5, 5". Erscheint nur, wenn `placement` auf `"at times"` gesetzt ist. | STRING | Nein | Durch Kommas getrennte Sekunden (Standard: "0") |

Hinweis: `prompt` muss mindestens ein Zeichen enthalten. `keyframes` muss mindestens ein Bild enthalten und darf nicht mehr als 10 enthalten; eine gebatchte Eingabe zählt einmal pro Bild.

Wenn `placement` auf `"spread across the clip"` gesetzt ist, werden ein oder zwei Bilder als Startbild und ein optionales Endbild gesendet, während drei oder mehr auf Keyframes platziert werden, die bei 24 fps gleichmäßig über den Clip verteilt sind.

Wenn `placement` auf `"at times"` gesetzt ist, muss `times` einen Wert pro Bild angeben, und diese Werte müssen ansteigen, dürfen nicht negativ sein, und der letzte Zeitpunkt darf nicht nach dem Ende des Clips liegen.

Der angezeigte Preis basiert auf `resolution` und `duration`: 720p wird bis zum 7. November 2026 mit 0,060775 $ pro Sekunde und 1080p mit 0,103675 $ pro Sekunde berechnet, nach diesem Datum mit 0,2431 $ bzw. 0,4147 $ pro Sekunde. Die geschätzten Gesamtkosten für den Clip werden in der Benutzeroberfläche angezeigt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Der generierte Videoclip, der aus den Keyframe-Bildern mit dem gewählten Seitenverhältnis, der Dauer, Auflösung und Audioeinstellung erstellt wurde. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3MaxImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `fd8bbd627022f86d3ecb3482530a6c8c37d4225e32db36c35185eac318ed4c75`
