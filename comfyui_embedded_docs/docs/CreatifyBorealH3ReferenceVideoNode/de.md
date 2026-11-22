# Creatify Boreal-H3 Reference to Video

Creatify Boreal-H3 Reference to Video erzeugt ein Video mit Ton, gesteuert durch Referenzbilder, -videos und -audios, unter Verwendung von Creatifys nachtrainiertem H3-Modell, das für Videowerbung entwickelt wurde. Benennen Sie die Referenzen im Prompt als `@Image1`, `@Video1` und `@Audio1`, um zu steuern, welchen Beitrag jede einzelne leistet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Erweiterbarer Slot für bis zu 9 Referenzbilder (`image_1` ... `image_9`), die im Prompt in Verbindungsreihenfolge als `@Image1` ... `@Image9` referenziert werden. Mindestens ein Bild oder Video ist erforderlich, und insgesamt höchstens 12 Referenzen. | IMAGE | Nein | Bis zu 9 Bilder |
| `reference_videos` | Erweiterbarer Slot für bis zu 3 Referenzvideos (`video_1` ... `video_3`), jeweils mindestens 1 Sekunde lang. Ihr Ton wird wiederverwendet, wenn der Prompt darum bittet, ihn fortzusetzen; eine neue Zeile im Prompt ersetzt ihn. Insgesamt werden höchstens 15 Sekunden Referenzvideo abgerechnet. | VIDEO | Nein | Bis zu 3 Videos |
| `reference_audios` | Erweiterbarer Slot für bis zu 3 Referenzclips (`audio_1` ... `audio_3`). Sprache steuert eher die Stimme als die Wörter, und instrumentale Musik kann zum Soundtrack werden. | AUDIO | Nein | Bis zu 3 Clips |
| `Prompt` | Text-Prompt, der das Video beschreibt und auf die verbundenen Referenzen verweist. Muss mindestens ein Nicht-Leerzeichen-Zeichen enthalten. | STRING | Ja | Beliebiger nicht leerer Text |
| `Auflösung` | Auflösung des Ausgabevideos (Standard: `"768p"`). | COMBO | Ja | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Seitenverhältnis des Ausgabevideos. `"auto"` folgt dem ersten Referenzbild. Bei ausschließlich Referenzvideos mit `"1088p"` wählt der Node das nächstgelegene unterstützte Verhältnis zum ersten Video, das von dessen exaktem Verhältnis abweichen kann; bei anderen Auflösungen wird `"auto"` unverändert an Creatify übergeben (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `Dauer` | Länge des Videos in Sekunden (Standard: 5). Bei `"2k"` beträgt das Maximum 14 Sekunden. | INT | Ja | 1 bis 15 (Schritt 1) |
| `prompt_enhancement` | Wie Creatify den Prompt vor dem Rendern umschreibt: `"auto"` und `"ads"` verwandeln ihn in einen Videowerbe-Prompt und können gesprochene Zeilen hinzufügen, `"general"` schreibt ihn für jedes andere Video um, `"none"` rendert ihn wie geschrieben (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `Seed` | Der Seed steuert, ob der Node erneut ausgeführt wird. Boreal-H3 wird kein Seed übergeben, daher kann ein erneutes Ausführen mit denselben Eingaben ein anderes Video erzeugen (Standard: 42). | INT | Ja | 0 bis 2147483647 |

**Einschränkungen:** Verbinden Sie mindestens ein Referenzbild oder -video; Audio allein wird nicht akzeptiert. Ein Referenz-Tag, das über die Anzahl der verbundenen Referenzen dieser Art hinauszeigt, löst einen Fehler aus, ebenso wie mehr als 12 Referenzen insgesamt. Bei `"1088p"` und `"auto"` ohne Referenzbild wird das Seitenverhältnis vom ersten Referenzvideo übernommen.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das erzeugte Video mit Ton. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3ReferenceVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `c6e60b83a8e02262fcbae7c04f4f379cf665a9e25b2fa00836047fe56d0fa064`
