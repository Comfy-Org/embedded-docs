# GrokVideoReferenceNode

Der Grok Reference-to-Video-Node erzeugt aus einem Text-Prompt ein Video und verwendet bis zu sieben Referenzbilder, um Stil und Inhalt der Ausgabe zu steuern. Mit dem Modell `grok-imagine-video-1.5` können Sie außerdem bis zu drei voreingestellte Stimmreferenzen anhängen und im Prompt mithilfe der Tags `@ImageN` und `@AudioN` direkt auf Bilder und Stimmen verweisen. Der Node sendet die Anfrage an eine externe API, wartet auf den Abschluss der Generierung und lädt das resultierende Video herunter.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Modell, das für die Videogenerierung verwendet werden soll. | DYNAMIC_COMBO | Ja | `"grok-imagine-video-1.5"`<br>`"grok-imagine-video"` |
| `prompt` | Textbeschreibung des gewünschten Videos. Muss eine nicht leere Zeichenkette sein. | STRING | Ja | N/A |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt wird; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Ja | 0 bis 2147483647 |

### Grok Imagine Video 1.5 Eingaben

Verfügbar, wenn `model` auf `grok-imagine-video-1.5` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `voice_1` | Optionale voreingestellte Stimmreferenz; verweisen Sie im Prompt als @Audio1 darauf. Die API unterstützt nur diese voreingestellten Stimmen, kein benutzerdefiniertes Audio (Standard: none). | COMBO | Nein | Voreingestellte Stimmenoptionen, einschließlich `"none"` |
| `voice_2` | Optionale zweite Stimmreferenz; @Audio2 im Prompt (Standard: none). | COMBO | Nein | Voreingestellte Stimmenoptionen, einschließlich `"none"` |
| `voice_3` | Optionale dritte Stimmreferenz; @Audio3 im Prompt (Standard: none). | COMBO | Nein | Voreingestellte Stimmenoptionen, einschließlich `"none"` |
| `resolution` | Die Auflösung des Ausgabevideos. | COMBO | Ja | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Das Seitenverhältnis des Ausgabevideos. | COMBO | Ja | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Die Dauer des Ausgabevideos in Sekunden (Standard: 6). | INT | Ja | 1 bis 15 |

### Grok Imagine Video Eingaben

Verfügbar, wenn `model` auf `grok-imagine-video` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `resolution` | Die Auflösung des Ausgabevideos. | COMBO | Ja | `"480p"`<br>`"720p"` |
| `aspect_ratio` | Das Seitenverhältnis des Ausgabevideos. | COMBO | Ja | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Die Dauer des Ausgabevideos in Sekunden (Standard: 6). | INT | Ja | 2 bis 10 |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbarer Slot: Verbinden Sie 1 bis 7 Referenzbilder, um die Videogenerierung zu steuern. Mit `grok-imagine-video-1.5` verweisen Sie im Prompt als @Image1 ... @Image7 darauf; nummeriert in Eingabereihenfolge; eine gebündelte Eingabe zählt einmal pro Bild. | IMAGE | Ja | 1 bis 7 Bilder |

**Hinweis:** Die angezeigten Unterparameter hängen vom ausgewählten `model` ab; `grok-imagine-video-1.5` fügt die Eingaben `voice_1`, `voice_2` und `voice_3` hinzu. Mindestens ein Referenzbild ist erforderlich, und die Gesamtzahl ist auf 7 begrenzt (eine gebündelte Eingabe zählt einmal pro Bild). Mit `grok-imagine-video-1.5` kann der Prompt verbundene Bilder als `@Image1` ... `@Image7` und Voice-Slots als `@Audio1`, `@Audio2`, `@Audio3` referenzieren; ein nicht nummeriertes `@image` oder `@audio` verweist auf das jeweils erste. `@AudioN` verweist auf das Widget `voice_N`, nicht auf die Reihenfolge der aktivierten Stimmen. Das Verweisen auf ein nicht verbundenes Bild oder einen auf `none` gesetzten Voice-Slot verursacht einen Fehler. Die API unterstützt nur voreingestellte Stimmen, kein benutzerdefiniertes Audio.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/de.md)

---
**Source fingerprint (SHA-256):** `e584c450563eaa7fcb7751d2325f9ef847fa34a4342df01f2bd9ce2e4ff8f2c3`
