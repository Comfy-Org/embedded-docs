# HappyHorse Text zu Video

Erzeugt ein Video basierend auf einem Text-Prompt unter Verwendung des HappyHorse-Modells. Dieser Node sendet Ihren Prompt und Ihre Einstellungen an die HappyHorse-API, wartet auf die Generierung des Videos und lädt anschließend das Ergebnis herunter.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das für die Generierung verwendete HappyHorse-Modell zusammen mit seinen Unterparametern. Die Auswahl eines Modells bestimmt, welche Unterparameter verfügbar sind (siehe die Modellabschnitte unten). | DYNAMIC_COMBO | Ja | "happyhorse-1.1-t2v"<br>"happyhorse-1.0-t2v" |
| `seed` | Seed für die Generierung. Die Verwendung desselben Seeds mit denselben Eingaben führt zum selben Ergebnis. (Standard: 0). | INT | Ja | 0 bis 2147483647 |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll. (Standard: False). | BOOLEAN | Ja | True / False |

### happyhorse-1.1-t2v Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt, der die Elemente und visuellen Merkmale beschreibt. Unterstützt Englisch und Chinesisch. (Standard: ""). | STRING | Ja | - |
| `resolution` | Die Auflösung des Ausgabevideos. | COMBO | Ja | "720P"<br>"1080P" |
| `ratio` | Das Seitenverhältnis des Ausgabevideos. | COMBO | Ja | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21"<br>"5:4"<br>"4:5" |
| `duration` | Die Länge des Videos in Sekunden. (Standard: 5, min: 3, max: 15, Schritt: 1). | INT | Ja | 3 bis 15 |

### happyhorse-1.0-t2v Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt, der die Elemente und visuellen Merkmale beschreibt. Unterstützt Englisch und Chinesisch. (Standard: ""). | STRING | Ja | - |
| `resolution` | Die Auflösung des Ausgabevideos. | COMBO | Ja | "720P"<br>"1080P" |
| `ratio` | Das Seitenverhältnis des Ausgabevideos. | COMBO | Ja | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Die Länge des Videos in Sekunden. (Standard: 5, min: 3, max: 15, Schritt: 1). | INT | Ja | 3 bis 15 |

Hinweis: Der Prompt darf nicht leer sein; wenn kein Prompt angegeben wird, wird ein Fehler ausgegeben. Beide Modelle unterstützen Videolängen von 3 bis 15 Sekunden. Das Modell `happyhorse-1.1-t2v` bietet zusätzliche Seitenverhältnisse (`21:9`, `9:21`, `5:4`, `4:5`), die mit `happyhorse-1.0-t2v` nicht verfügbar sind.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/de.md)

---
**Source fingerprint (SHA-256):** `b60cfc3ce4935d7eb36bb28f9bd268446c4df5b437e06278b7e6d91d349d0238`
