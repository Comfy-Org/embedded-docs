# Pruna P-Video-2 Pro Reference to Video

Generieren Sie ein Video aus einem Prompt, das durch Referenzbilder, -videos und -audios mit Pruna P-Video-2 Pro Reference to Video gesteuert wird. Verweisen Sie im Prompt anhand der Nummer auf jede Referenz, und das Modell überträgt deren Motiv, Stil oder Bewegung in das Ergebnis.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `Modell` | Zu verwendendes Pruna-Videomodell. Bei Auswahl eines Modells werden dessen Eingaben unten eingeblendet. | DYNAMIC_COMBO | Ja | `"p-video-2-pro-reference"` |

### P-Video-2 Pro Reference Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.images` | Erweiterbarer Slot für Referenzbilder (`image_1`, `image_2`, ...), im Prompt in Verbindungsreihenfolge als `@Image1` bis `@Image9` referenziert. Bis zu 9 Bilder, einschließlich des ersten und letzten Frames. | AUTOGROW | Nein | 0 bis 9 Bilder |
| `model.videos` | Erweiterbarer Slot für Referenzvideos (`video_1`, `video_2`, ...), referenziert als `@Video1` bis `@Video3`. Jedes 2 bis 15 Sekunden bei bis zu 60 fps, insgesamt 15 Sekunden. Videos über 1080p werden herunterskaliert. | AUTOGROW | Nein | 0 bis 3 Videoclips |
| `model.audios` | Erweiterbarer Slot für Referenzaudio (`audio_1`, `audio_2`, ...), referenziert als `@Audio1` bis `@Audio3`. Insgesamt bis zu 15 Sekunden. | AUTOGROW | Nein | 0 bis 3 Audioclips |
| `Prompt` | Beschreibt das Video. Referenzieren Sie die Referenzen als `@Image1`, `@Video1` oder `@Audio1` (Standard: leer). Bis zu 5000 Zeichen. | STRING | Ja | 1 bis 5000 Zeichen |
| `model.first_frame` | Bild, mit dem das Video beginnt. Zählt zum Limit von 9 Bildern. | IMAGE | Nein | - |
| `model.last_frame` | Bild, mit dem das Video endet. Zählt zum Limit von 9 Bildern. | IMAGE | Nein | - |
| `model.keep_audio` | Verwendet das verbundene Audio als Soundtrack und generiert das Video passend dazu (Standard: False). Erfordert genau ein Audio: Bei kürzerem Audio folgt generierter Ton, längeres Audio wird auf die Dauer gekürzt. | BOOLEAN | Ja | `True`<br>`False` |
| `Dauer` | Länge des Videos in Sekunden (Standard: `"5"`). | COMBO | Ja | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"` |
| `Auflösung` | Ausgabauflösung (Standard: `"768p"`). 1080p, 2k und 4k skalieren das generierte 768p-Video hoch. | COMBO | Ja | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `Modus` | `"cost"` ist günstiger, `"speed"` rendert schneller (Standard: `"speed"`). | COMBO | Ja | `"cost"`<br>`"speed"` |
| `model.aspect_ratio` | Seitenverhältnis des Ausgabevideos (Standard: `"16:9"`). `"adaptive"` verwendet das häufigste Seitenverhältnis unter den Referenzen, und bei aktiviertem `enhance_prompt` wählt stattdessen der umgeschriebene Prompt das Verhältnis aus. | COMBO | Ja | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"1:1"` |
| `model.enhance_prompt` | Schreibt den Prompt vor der Generierung detaillierter um; `"max"` ist langsamer (Standard: `"turbo"`). Lassen Sie es aktiviert, wenn der Prompt Referenzen anhand der Nummer referenziert; bei einem ersten oder letzten Frame wird immer `"turbo"` verwendet. Erweiterte Einstellung. | COMBO | Ja | `"off"`<br>`"turbo"`<br>`"max"` |
| `Seed` | Seed für die Generierung (Standard: 42). Derselbe Seed reproduziert ein Ergebnis nur dann exakt, wenn `model.enhance_prompt` deaktiviert ist. | INT | Ja | 0 bis 2147483647<br>Schritt: 1 |

**Hinweise:**

- Verbinden Sie mindestens ein Referenzbild, -video, einen ersten oder letzten Frame, andernfalls bricht der Node mit einem Fehler ab.
- 9 Bilder sind einschließlich des ersten und letzten Frames erlaubt, und insgesamt 12 Referenzen über Bilder, Frames, Videos und Audio hinweg.
- Referenzvideo und Referenzaudio sind jeweils auf insgesamt 15 Sekunden begrenzt, und jedes einzelne Referenzvideo muss 2 bis 15 Sekunden lang sein bei bis zu 60 fps.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das generierte Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaReferenceToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `d6e295b394984c924386ea6432532c7653b4512c646b1f86793be9b98583eef3`
