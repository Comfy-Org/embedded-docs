# MiniMax H3 Text zu Video

Dieser Node generiert ein Video aus einem Text-Prompt unter Verwendung der MiniMax H3-Modellfamilie: MiniMax H3, MiniMax H3 Max und MiniMax H3 Max Turbo. Sie wählen das Modell aus, geben einen Text-Prompt ein und passen Einstellungen wie Auflösung, Seitenverhältnis und Dauer an. Der Node sendet die Anfrage an die MiniMax-API, wartet auf den Abschluss der Generierungsaufgabe und gibt das resultierende Video zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell, das für die Videogenerierung verwendet wird (Standard: "MiniMax H3"). Wenn Sie ein Modell auswählen, werden außerdem die modellspezifischen Einstellungen angezeigt, die in den folgenden Abschnitten beschrieben sind. | DYNAMIC_COMBO | Ja | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `seed` | Zufälliger Seed. Die gleiche Anfrage mit demselben Seed liefert ähnliche, aber nicht garantiert identische Ergebnisse (Standard: 42). | INT | Ja | 0 bis 4294967295 |
| `watermark` | Ob dem Video ein AIGC-Wasserzeichen hinzugefügt wird (Standard: false). Wenn aktiviert, wird nur das Modell "MiniMax H3" unterstützt. | BOOLEAN | Nein | true<br>false |

### MiniMax H3 Eingaben

Diese Einstellungen werden angezeigt, wenn das Modell "MiniMax H3" ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. Muss mindestens ein Nicht-Leerzeichen-Zeichen enthalten. | STRING | Ja | Beliebiger Text |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | "768P"<br>"2K" |
| `ratio` | Seitenverhältnis des Ausgabevideos (Standard: "16:9"). | COMBO | Ja | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Dauer des Ausgabevideos in Sekunden (4-15) (Standard: 5). | INT | Ja | 4 bis 15 |

### MiniMax H3 Max und MiniMax H3 Max Turbo Eingaben

Diese Einstellungen werden von den Modellen "MiniMax H3 Max" und "MiniMax H3 Max Turbo" gemeinsam verwendet und erscheinen, wenn eines der beiden Modelle ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. Muss mindestens ein Nicht-Leerzeichen-Zeichen enthalten und darf bis zu 50.000 Zeichen lang sein. | STRING | Ja | Bis zu 50000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos (Standard: "768P"). | COMBO | Ja | "480P"<br>"768P" |
| `ratio` | Seitenverhältnis des Ausgabevideos (Standard: "16:9"). | COMBO | Ja | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Dauer des Ausgabevideos in Sekunden (5-15) (Standard: 5). | INT | Ja | 5 bis 15 |
| `prompt_expansion_mode` | Wie viel Aufwand betrieben wird, um den Prompt vor der Generierung umzuschreiben (Standard: "balanced"). | COMBO | Ja | "balanced"<br>"quality" |

### Hinweise

- Für alle Modelle muss der Prompt mindestens ein Nicht-Leerzeichen-Zeichen enthalten.
- Die Einstellung `watermark` wird nur von "MiniMax H3" unterstützt. Wenn sie mit "MiniMax H3 Max" oder "MiniMax H3 Max Turbo" aktiviert wird, verursacht dies einen Fehler.
- Die Modelle "MiniMax H3 Max" und "MiniMax H3 Max Turbo" begrenzen den Prompt auf 50.000 Zeichen.
- Auflösungs- und Dauerlimits hängen vom ausgewählten Modell ab: "MiniMax H3" unterstützt "768P"- und "2K"-Auflösung sowie Videos mit 4-15 Sekunden, während "MiniMax H3 Max" und "MiniMax H3 Max Turbo" "480P"- und "768P"-Auflösung sowie Videos mit 5-15 Sekunden unterstützen.
- Der für diesen Node angezeigte geschätzte Preis wird aus dem ausgewählten Modell, der Auflösung und der Dauer berechnet.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das aus dem bereitgestellten Text-Prompt erzeugte Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `4d3de190d18de4370aff878279755e881841d2ada28320a7c1d7c52061071c05`
