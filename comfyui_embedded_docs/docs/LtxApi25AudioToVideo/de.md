# LtxApi25AudioToVideo

Dieser Node erzeugt ein Video, das einer Audiospur folgt, unter Verwendung des LTX 2.5-Modells. Die Audiodauer bestimmt die Videolänge (zwischen 2 und 20 Sekunden); optional kann ein Bild als erstes Frame angegeben werden. Das Video wird über den LTX 2.5-API-Dienst generiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `audio` | Audiospur, die das Video steuert. Ihre Länge (2-20 Sekunden) legt die Videodauer fest. | AUDIO | Ja | 2-20 Sekunden |
| `model` | Die zu verwendende LTX 2.5-Modellversion. Bei Auswahl eines Modells wird außerdem die Unteroption `resolution` für dieses Modell eingeblendet. | COMBO | Ja | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `resolution` | Die Ausgabeauflösung des generierten Videos. Diese Unteroption wird unter dem ausgewählten `model` angezeigt (Standard: "1920x1080"). Beide Modelle bieten dieselben Auflösungsoptionen. | COMBO | Ja | "1920x1080"<br>"1080x1920" |
| `prompt` | Eine Textbeschreibung, die den Inhalt des generierten Videos steuert (Standard: ""). Muss mindestens 1 Zeichen und höchstens 10000 Zeichen enthalten. | STRING | Ja | 1-10000 Zeichen |
| `seed` | Eine Zahl, die die Zufälligkeit der Generierung steuert. Derselbe Seed erzeugt dasselbe Ergebnis (Standard: 42). | INT | Ja | Beliebige Ganzzahl |
| `image` | Optionales erstes Frame, das für das Video verwendet wird. Es wird nur ein Bild unterstützt. | IMAGE | Nein | Einzelnes Bild |

Hinweise zu Einschränkungen:
- Die Audiodauer muss zwischen 2 und 20 Sekunden liegen; der Node gibt einen Fehler aus, wenn sie außerhalb dieses Bereichs liegt.
- Der Prompt ist erforderlich und darf nicht leer sein; er muss zwischen 1 und 10000 Zeichen lang sein.
- Wenn `image` angegeben wird, wird nur ein einzelnes Eingabebild akzeptiert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `video` | Das generierte Video, das durch die bereitgestellte Audiospur gesteuert wird. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25AudioToVideo/de.md)

---
**Source fingerprint (SHA-256):** `ae0d0123c0421f645448496d30a53a21aba1728310180719a4c4599eca8351c5`
