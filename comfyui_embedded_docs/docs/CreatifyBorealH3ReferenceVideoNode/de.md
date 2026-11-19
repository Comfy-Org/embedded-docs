# Creatify Boreal-H3 Reference to Video

Creatify Boreal-H3 Referenz-zu-Video erzeugt ein Video mit Ton, gesteuert durch Referenzbilder, -videos und -audio, unter Verwendung von Creatifys nachtrainiertem H3-Modell, das für Videoanzeigen entwickelt wurde. Benennen Sie die Referenzen im Prompt als `@Image1`, `@Video1` und `@Audio1`, um zu steuern, welchen Beitrag jede einzelne leistet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbarer Slot für bis zu 9 Referenzbilder (`image_1` ... `image_9`), die im Prompt in Verbindungsreihenfolge als `@Image1` ... `@Image9` referenziert werden. Mindestens ein Bild oder Video ist erforderlich, insgesamt höchstens 12 Referenzen. | IMAGE | Nein | Bis zu 9 Bilder |
| `reference_videos` | Erweiterbarer Slot für bis zu 3 Referenzvideos (`video_1` ... `video_3`), jeweils mindestens 1 Sekunde lang. Ihr Ton wird wiederverwendet, wenn der Prompt verlangt, ihn fortzusetzen; eine neue Zeile im Prompt ersetzt ihn. Insgesamt werden höchstens 15 Sekunden Referenzvideo abgerechnet. | VIDEO | Nein | Bis zu 3 Videos |
| `reference_audios` | Erweiterbarer Slot für bis zu 3 Referenzclips (`audio_1` ... `audio_3`). Sprache steuert eher die Stimme als die Wörter, und Instrumentalmusik kann zum Soundtrack werden. | AUDIO | Nein | Bis zu 3 Clips |
| `prompt` | Text-Prompt, der das Video beschreibt und auf die verbundenen Referenzen verweist. Muss mindestens ein Nicht-Leerzeichen enthalten. | STRING | Ja | Beliebiger nicht leerer Text |
| `resolution` | Auflösung des Ausgabevideos (Standard: `"768p"`). | COMBO | Ja | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. `"auto"` folgt dem ersten Referenzbild oder, wenn kein Bild verbunden ist, dem ersten Referenzvideo (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Länge des Videos in Sekunden (Standard: 5). Bei `"2k"` beträgt das Maximum 14 Sekunden. | INT | Ja | 1 bis 15 (Schritt: 1) |
| `prompt_enhancement` | Wie Creatify den Prompt vor dem Rendern umschreibt: `"auto"` und `"ads"` verwandeln ihn in einen Video-Ad-Prompt und können gesprochene Zeilen hinzufügen, `"general"` schreibt ihn für jedes andere Video um, `"none"` rendert ihn wie geschrieben (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt wird. Creatify wählt seine eigene Zufälligkeit, daher liefern dieselben Eingaben nur dann dasselbe Video, wenn `prompt_enhancement` auf `"none"` gesetzt ist (Standard: 42). | INT | Ja | 0 bis 2147483647 |

**Einschränkungen:** Verbinden Sie mindestens ein Referenzbild oder -video; Audio allein wird nicht akzeptiert. Ein Referenz-Tag, der über die Anzahl der verbundenen Referenzen dieser Art hinausgeht, löst einen Fehler aus, ebenso wie mehr als 12 Referenzen insgesamt. Bei `"1088p"` und `"auto"` ohne Referenzbild wird das Seitenverhältnis vom ersten Referenzvideo übernommen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das generierte Video mit Ton. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3ReferenceVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `c6e60b83a8e02262fcbae7c04f4f379cf665a9e25b2fa00836047fe56d0fa064`
