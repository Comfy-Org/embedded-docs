# PixVerse V6 Fusion (Referenz zu Video)

PixVerse V6 Fusion (Referenz zu Video) erstellt mit PixVerse ein Video aus Referenzsubjekten, Referenzhintergründen und Referenzvideos. Platzieren Sie eine Referenz in der Szene, indem Sie sie im Prompt benennen, zum Beispiel '@Subject1 walks through @Background1'. Das Verbinden eines Referenzvideos schaltet das Modell in den Omni-Modus um, in dem die Ausgabelänge dem längsten Referenzvideo entspricht.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell- und Generierungseinstellungen. Wählt das Modell aus und zeigt seine Generierungseinstellungen unten an. Die einzige verfügbare Option ist "PixVerse V6". | DYNAMIC_COMBO | Ja | "PixVerse V6" |

### PixVerse V6 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt für die Videogenerierung. Verweisen Sie auf verbundene Referenzen als @Subject1, @Background1, @Video1. Standard: leer. | STRING | Ja | 1 bis 5000 Zeichen |
| `aspect_ratio` | Seitenverhältnis der Ausgabe. Die Option "auto" ist nur erlaubt, wenn mindestens ein Referenzvideo verbunden ist. | COMBO | Ja | "auto"<br>zuzüglich der vordefinierten PixVerse V6 Seitenverhältnisse |
| `quality` | Auflösung der Ausgabe. Legt die lange Kante fest: 360p entspricht 640px, 540p 1024px, 720p 1280px, 1080p 1920px. Standard: "720p". | COMBO | Ja | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Länge des generierten Videos in Sekunden. Wenn Referenzvideos verbunden sind, richtet sich die Ausgabelänge stattdessen nach dem längsten Referenzvideo und diese Einstellung wird ignoriert. Standard: 5. | INT | Ja | 1 bis 15 |
| `generate_audio` | Generiert eine native Audiospur zusammen mit dem Video. Standard: True. | BOOLEAN | Ja | True<br>False |
| `seed` | Seed für die Videogenerierung. PixVerse zeichnet ihn auf, reproduziert damit aber keinen Lauf. Standard: 42. | INT | Ja | 0 bis 2147483647 |
| `negative_prompt` | Eine optionale Textbeschreibung unerwünschter Elemente im Video. Standard: leer. | STRING | Nein | Bis zu 2048 Zeichen |
| `style` | Ein optionaler visueller Stil, der auf das gesamte Video angewendet wird. Standard: "none". | COMBO | Nein | "none"<br>zuzüglich der vordefinierten PixVerse V6 Stile |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `subjects` | Erweiterbarer Slot: Verbinden Sie Referenzbilder der Subjekte, die in der Szene platziert werden sollen. Slots heißen subject1 bis subject8; verweisen Sie im Prompt als @Subject1, @Subject2 usw. auf sie. | IMAGE | Nein | 0 bis 8 Bilder |
| `backgrounds` | Erweiterbarer Slot: Verbinden Sie Referenzbilder der Szene, in die die Subjekte platziert werden. Slots heißen background1 bis background2; verweisen Sie im Prompt als @Background1, @Background2 auf sie. | IMAGE | Nein | 0 bis 2 Bilder |
| `videos` | Erweiterbarer Slot: Verbinden Sie Referenzvideos, um Subjekte, Bewegung, Bildkomposition oder Stil daraus zu übernehmen. Slots heißen video1 bis video2; verweisen Sie im Prompt als @Video1, @Video2 auf sie. Jedes Video darf höchstens 15 Sekunden lang sein, und die Gesamtdauer darf 15 Sekunden nicht überschreiten. Das Verbinden mindestens eines Videos schaltet den Node in den Omni-Modus um. | VIDEO | Nein | 0 bis 2 Videos<br>max. 15 Sekunden je<br>15 Sekunden insgesamt |

Hinweis: Verbinden Sie mindestens ein Subjekt, einen Hintergrund oder ein Referenzvideo. Referenz-Tags im Prompt (zum Beispiel @Subject1, @Background1, @Video1) müssen mit verbundenen Slots übereinstimmen, andernfalls wird die Anfrage abgelehnt. Wenn mindestens ein Referenzvideo verbunden ist (Omni-Modus), entspricht die Ausgabelänge dem längsten Referenzvideo, `duration_seconds` wird ignoriert, `aspect_ratio` kann auf "auto" gesetzt werden, und es werden bis zu 10 Referenzbilder akzeptiert. Ohne Referenzvideo werden höchstens 7 Referenzbilder (Subjekte und Hintergründe zusammen) akzeptiert, und das Seitenverhältnis "auto" ist nicht erlaubt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Fusion-Video, heruntergeladen von PixVerse. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FusionVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `a83ef07f6f1918921e93fa67c2eca351754794f629aa216ccff21ce80901aebd`
