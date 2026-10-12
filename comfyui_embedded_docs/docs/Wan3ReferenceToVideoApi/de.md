# Wan3ReferenceToVideoApi

Dieser Node erzeugt mit dem Wan 3.0-Modell ein Video aus einem Text-Prompt und optionalen Referenzbildern, -videos und -audios. Referenzmedien können frei kombiniert und im Prompt als @Image1, @Video1 und @Audio1 referenziert werden. Der Node übermittelt die Generierungsanfrage an die Wan-API und gibt das fertige Video zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Wählt die für die Generierung verwendete Modellvariante von Wan 3.0 aus. | DYNAMIC_COMBO | Ja | `wan3.0-video`<br>`wan3.0-video-prime` |
| `seed` | Seed für die Generierung. Standard: 42. | INT | Ja | 0 bis 2147483647 |
| `watermark` | Gibt an, ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll. Standard: false. | BOOLEAN | Ja | true<br>false |

### Eingaben für wan3.0-video und wan3.0-video-prime

Beide Modelloptionen verwenden denselben Parametersatz.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Prompt, der die Elemente und visuellen Merkmale beschreibt. Unterstützt Englisch und Chinesisch. Verweisen Sie auf verbundene Referenzmedien als @Image1, @Video1, @Audio1, nummeriert pro Typ in Eingabereihenfolge. Standard: leer. | STRING | Ja | Bis zu 20.000 Zeichen |
| `resolution` | Auflösung des Ausgabevideos. | COMBO | Ja | "1080P"<br>"720P"<br>"480P" |
| `ratio` | Seitenverhältnis des Ausgabevideos. Bei "adaptive" werden die Ausgabeabmessungen aus den Eingabemedien abgeleitet. | COMBO | Ja | "adaptive"<br>"16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Ausgabedauer in Sekunden. Bei "auto" wählt das Modell eine Dauer, die zum Prompt und zu den Referenzmedien passt. Die kombinierte Dauer von Referenzvideos und Ausgabe darf 30 Sekunden nicht überschreiten. | COMBO | Ja | "auto"<br>"2" bis "30" (ganzzahlige Sekunden) |
| `audio` | Gibt an, ob das Ausgabevideo eine Audiospur enthält. Standard: true. | BOOLEAN | Ja | true<br>false |
| `prompt_extend` | Gibt an, ob der Prompt mit KI-Unterstützung erweitert werden soll. Standard: true. | BOOLEAN | Ja | true<br>false |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `reference_images` | Erweiterbarer Slot: Verbinden Sie 1 bis 10 Referenzbilder. Referenzen werden in Eingabereihenfolge als image1 bis image10 nummeriert. | IMAGE | Nein | 0 bis 10 Bilder |
| `reference_videos` | Erweiterbarer Slot: Verbinden Sie 1 bis 5 Referenzvideos. Referenzen werden in Eingabereihenfolge als video1 bis video5 nummeriert. | VIDEO | Nein | 0 bis 5 Videos |
| `reference_audios` | Erweiterbarer Slot: Verbinden Sie 1 bis 5 Referenzaudioclips. Referenzen werden in Eingabereihenfolge als audio1 bis audio5 nummeriert. | AUDIO | Nein | 0 bis 5 Audioclips |

**Einschränkungen:**

- Der Prompt muss mindestens ein nicht leeres Zeichen enthalten, oder es muss mindestens eine Referenzbild-, Video- oder Audioeingabe verbunden sein.
- Referenz-Tags im Prompt müssen mit den verbundenen Eingaben übereinstimmen. Zum Beispiel verweist @Image1 auf das erste verbundene Referenzbild, @Video2 auf das zweite verbundene Referenzvideo und @Audio1 auf das erste verbundene Referenzaudio. Tags werden pro Typ separat in Eingabereihenfolge nummeriert.
- Jedes verbundene Referenzbild muss genau ein Bild enthalten, keinen Batch.
- Jedes Referenzvideo darf höchstens 15 Sekunden lang sein. Die Gesamtdauer aller Referenzvideos darf 15 Sekunden nicht überschreiten.
- Jedes Referenzaudio darf höchstens 15 Sekunden lang sein. Die Gesamtdauer aller Referenzaudios darf 15 Sekunden nicht überschreiten.
- Wenn `duration` nicht "auto" ist, darf die Gesamtdauer aller Referenzvideos plus die ausgewählte Ausgabedauer 30 Sekunden nicht überschreiten.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `video` | Die generierte Videodatei. Enthält eine Audiospur, wenn der Parameter `audio` aktiviert ist. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ReferenceToVideoApi/de.md)

---
**Source fingerprint (SHA-256):** `09caa8142d71235417a3dfc5676c5f6accc2af1287fad3b7050844dd9453cc64`
