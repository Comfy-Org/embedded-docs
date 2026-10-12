# LtxApi25ImageToVideo

Dieser Node erzeugt aus einem Startbild ein Video in professioneller Qualität mithilfe eines LTX 2.5-Modells. Sie beschreiben den Videoinhalt mit einem Text-Prompt, wählen eine Modellvariante aus und passen Dauer, Auflösung, Bildrate und Audiogenerierung an. Optional kann ein letztes Einzelbild angegeben werden, um das Ende des Videos festzulegen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Erstes Einzelbild, das für das Video verwendet werden soll. | IMAGE | Ja | Genau ein Bild |
| `model` | Gruppe der Modelleinstellungen. Wählt die zu verwendende LTX 2.5-Modellvariante aus. | COMBO | Ja | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `model.duration` | Länge des generierten Videos in Sekunden. | INT | Ja | Ganzzahl |
| `model.resolution` | Auflösung des generierten Videos. Die verfügbaren Optionen können vom ausgewählten Modell abhängen. | COMBO | Ja | "1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840" |
| `model.fps` | Bildrate des generierten Videos. | INT | Ja | Ganzzahl (Standard: 25) |
| `model.generate_audio` | Ob Audio für das Video generiert werden soll. | BOOLEAN | Ja | True<br>False (Standard: True) |
| `prompt` | Textbeschreibung des zu generierenden Videoinhalts. Muss zwischen 1 und 10000 Zeichen lang sein. | STRING | Ja | 1 bis 10000 Zeichen |
| `seed` | Seed-Wert für die reproduzierbare Generierung. Die Verwendung desselben Seeds mit denselben Einstellungen erzeugt dasselbe Ergebnis. | INT | Ja | Ganzzahl (Standard: 42) |
| `last_frame` | Letztes Einzelbild, das für das Video verwendet werden soll. | IMAGE | Nein | Genau ein Bild |

**Hinweis:** Für `image` wird nur ein Bild unterstützt. Wenn `last_frame` angegeben wird, muss es ebenfalls genau ein Bild enthalten. Die verfügbaren Optionen für `model.resolution` können je nach ausgewählter `model`-Variante variieren. Der Preis eines Durchlaufs hängt vom ausgewählten `model`, `model.duration` und `model.resolution` ab.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Video basierend auf dem bereitgestellten Startbild und den Generierungseinstellungen. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25ImageToVideo/de.md)

---
**Source fingerprint (SHA-256):** `13db42e5e0d4237424b30b960ec12f5dd16808d21b85e100e5861c095b351c79`
