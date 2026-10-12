# Wan 3.0 Bild-zu-Video

Dieser Node generiert mithilfe des Wan 3.0-Modells ein Video aus einem Startbild. Optional können Sie ein Endbild angeben, um zu steuern, wie das Video endet; das Modell erstellt dann ein Video, das vom ersten zum letzten Frame übergeht.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Wählt die zu verwendende Wan 3.0-Modellvariante aus und legt fest, welche modellspezifischen Einstellungen unten angezeigt werden. | DYNAMIC_COMBO | Ja | "wan3.0-video"<br>"wan3.0-video-prime" |
| `first_frame` | Startbild. Es ist genau ein Bild erforderlich. | IMAGE | Ja | Einzelnes Bild |
| `last_frame` | Endbild. Das Modell generiert ein Video, das vom ersten zum letzten Frame übergeht. Optional; falls angegeben, ist genau ein Bild erforderlich. | IMAGE | Nein | Einzelnes Bild |
| `seed` | Seed für die Generierung (Standard: 42). | INT | Ja | 0 - 2147483647 |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll (Standard: false). | BOOLEAN | Ja | true<br>false |

### wan3.0-video und wan3.0-video-prime Eingaben

Diese modellspezifischen Einstellungen gelten für beide Modelloptionen gemeinsam und werden angezeigt, wenn ein Modell ausgewählt wurde.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt, der die Elemente und visuellen Merkmale beschreibt. Unterstützt Englisch und Chinesisch. Kann leer gelassen werden (Standard: leer). | STRING | Ja | Bis zu 20000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | "1080P"<br>"720P"<br>"480P" |
| `ratio` | Seitenverhältnis des Ausgabevideos. Bei „adaptive“ werden die Ausgabedimensionen vom ersten Frame abgeleitet. | COMBO | Ja | "adaptive"<br>"16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Ausgabedauer in Sekunden. Bei „auto“ wählt das Modell eine Dauer, die zum Prompt passt. | COMBO | Ja | "auto"<br>"2" - "30" |
| `audio` | Ob das Ausgabevideo eine Audiospur enthält (Standard: true). | BOOLEAN | Ja | true<br>false |
| `prompt_extend` | Ob der Prompt mit KI-Unterstützung erweitert werden soll (Standard: true). | BOOLEAN | Ja | true<br>false |

Hinweis: Der Node akzeptiert genau ein `first_frame`-Bild und optional ein `last_frame`-Bild. Wenn mehr als ein Bild mit einem der beiden Eingaben verbunden ist, wird ein Fehler ausgelöst. Wenn `last_frame` angegeben wird, geht das generierte Video vom ersten zum letzten Frame über. Der `prompt` ist auf 20.000 Zeichen begrenzt. Der Preis eines Durchlaufs hängt vom ausgewählten `model`, `resolution` und `duration` ab.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Video. Enthält eine Audiospur, wenn die Option `audio` aktiviert ist. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ImageToVideoApi/de.md)

---
**Source fingerprint (SHA-256):** `ff9fce554fa7aa5fc8729b5f84b2f8bf89e8e7772ce1c32b1307d0dc4882200c`
