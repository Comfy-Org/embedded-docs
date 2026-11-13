# HeyGen Video 1.0 Referenz zu Video

Erzeugen Sie mit HeyGen Video 1.0 ein Video mit synchronisiertem Dialog und Ton aus einem Text-Prompt, optional geleitet durch verbundenes Referenzmaterial. Bilder von Personen, Produkten oder Orten, Videos zur Wiederverwendung und Audioclips, die eine Stimme bereitstellen, können alle als Referenzen verwendet werden. Nennen Sie jede Referenz im Prompt als @Image1, @Video1 oder @Audio1, nummeriert pro Typ in der Reihenfolge, in der die Eingaben verbunden werden: Diese Tags werden in die von HeyGen erwarteten Bezeichnungen umgeschrieben, und ein Tag, das auf eine nicht verbundene Referenz verweist, löst einen Fehler aus. Ohne Referenzbild oder Referenzvideo läuft der Node als Text-zu-Video-Generierung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modellversion, die für die Generierung verwendet wird. (Standard: `"heygen-video-1"`) | DYNAMIC_COMBO | Ja | `"heygen-video-1"` |
| `prompt` | Beschreibung des Videos, einschließlich etwaigem Dialog. Verweisen Sie auf verbundene Referenzen als @Image1, @Video1, @Audio1, nummeriert pro Typ in Eingabereihenfolge. (Standard: leere Zeichenkette) | STRING | Ja | 1 bis 16000 Zeichen |
| `duration` | Dauer des Ausgabevideos in Sekunden. Mehr als 15 Sekunden sind nur ohne Referenzbilder und -videos verfügbar. (Standard: 5) | INT | Ja | 5 bis 30 |
| `resolution` | Ausgabeauflösung. 1080p und 2k erfordern das Seitenverhältnis 16:9 oder 9:16; 'auto' funktioniert bei diesen Auflösungen nur ohne Referenzen. (Standard: `"768p"`) | COMBO | Ja | `"768p"`<br>`"480p"`<br>`"1080p"`<br>`"2k"` |
| `aspect_ratio` | Ausgabeseitenverhältnis. `"auto"` ist 16:9, wenn keine Referenzen verbunden sind; andernfalls folgt es dem ersten Referenzbild oder, wenn keine Bilder verbunden sind, dem ersten Referenzvideo. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `seed` | Seed für die Generierung. Ergebnisse können zwischen Läufen mit demselben Seed weiterhin variieren. (Standard: 42) | INT | Ja | 0 bis 4294967295 |
| `reference_images` | Erweiterbarer Slot: Bilder von Personen, Produkten oder Orten, die im Video verwendet werden sollen (`image_1` ... `image_9`); verweisen Sie darauf als @Image1, @Image2, ... Jede Eingabe muss genau ein Bild enthalten, und jedes Bild muss ein Seitenverhältnis zwischen 1:4 und 4:1 haben. | IMAGE | Nein | 0 bis 9 Bilder |
| `reference_videos` | Erweiterbarer Slot: Videos, die als Referenzen verwendet werden sollen (`video_1` ... `video_3`); verweisen Sie darauf als @Video1, @Video2, ... Insgesamt werden höchstens 15 Sekunden Filmmaterial verwendet. | VIDEO | Nein | 0 bis 3 Videos |
| `reference_audios` | Erweiterbarer Slot: Audioclips wie etwa eine Stimme für einen Sprecher (`audio_1` ... `audio_3`); verweisen Sie darauf als @Audio1, @Audio2, ... Erfordert mindestens ein Referenzbild oder -video. Eine Stimmenreferenz benötigt einige Sekunden klarer Sprache, und Clips, die kürzer als etwa 2 Sekunden sind, werden normalerweise ignoriert. | AUDIO | Nein | 0 bis 3 Audioclips |
| `auto_duration` | Wenn aktiviert, folgt die Videolänge dem im Prompt in Anführungszeichen gesetzten Dialog (8 bis 30 Sekunden oder 8 bis 15 mit Referenzbildern oder -videos) und `duration` wird ignoriert. (Standard: `"disabled"`) | COMBO | Nein | `"disabled"`<br>`"enabled"` |

### Parameterbeschränkungen

- **Referenzlimit:** höchstens 15 Referenzen insgesamt: bis zu 9 Bilder, 3 Videos und 3 Audioclips. Wenn mehr verbunden werden, wird ein Fehler ausgelöst.
- **Audio benötigt Bild oder Video:** Referenzaudio wird abgelehnt, wenn weder ein Referenzbild noch ein Referenzvideo verbunden ist.
- **Regeln für Referenzbilder:** Jede Eingabe `reference_images` muss genau ein Bild enthalten (ein Batch wird abgelehnt), und jedes Bild muss ein Seitenverhältnis zwischen 1:4 und 4:1 haben.
- **Prompt-Tags:** `@ImageN`, `@VideoN` und `@AudioN` werden ohne Beachtung der Groß-/Kleinschreibung abgeglichen. Die Nummer darf die Anzahl der verbundenen Referenzen dieses Typs nicht überschreiten, und der Prompt muss nach dem Entfernen von Leerraum nicht leer sein.
- **Modus:** Mit mindestens einem Referenzbild oder -video ist die Anfrage ein Referenz-zu-Video-Lauf; ohne eines ist es ein reiner Text-zu-Video-Lauf.
- **1080p- und 2k-Auflösung:** `resolution` `"1080p"` oder `"2k"` erfordert `aspect_ratio` `"16:9"` oder `"9:16"`; `"auto"` wird bei diesen Auflösungen nur akzeptiert, wenn weder ein Referenzbild noch ein Referenzvideo verbunden ist.
- **Dauer:** Mit Referenzbildern oder -videos bleibt das generierte Video bei 15 Sekunden oder weniger. Längere Videos erfordern keine Referenzbilder oder -videos; `auto_duration` bewirkt nur, dass `duration` ignoriert wird (8 bis 30 Sekunden aus dem Dialog, 8 bis 15 mit Referenzen), es hebt diese Obergrenze nicht an.
- **Seed:** Der Seed entscheidet nur, ob der Node erneut ausgeführt wird; Ergebnisse sind mit demselben Seed nicht reproduzierbar.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das generierte Video mit synchronisiertem Dialog und Ton. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenReferenceToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `415ffca1c385936e35bdb0451a23f03756e936b3b871d8d6a958da1ef8c56c36`
