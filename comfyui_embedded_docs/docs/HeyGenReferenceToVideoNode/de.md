# HeyGenReferenceToVideoNode

Erzeugen Sie mit HeyGen Video 1.0 ein Video mit synchronisiertem Dialog und Ton aus einem Text-Prompt, optional durch verbundenes Referenzmaterial geleitet. Bilder von Personen, Produkten oder Orten, Videos zur Wiederverwendung und Audioclips, die eine Stimme bereitstellen, können alle als Referenzen verwendet werden. Erwähnen Sie jede Referenz im Prompt als @Image1, @Video1 oder @Audio1, nummeriert pro Typ in der Reihenfolge, in der die Eingaben verbunden sind: Diese Tags werden in die von HeyGen erwarteten Labels umgeschrieben, und ein Tag, das auf eine nicht verbundene Referenz verweist, löst einen Fehler aus. Ohne Referenzbild oder -video läuft der Node als Text-zu-Video-Generierung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Für die Generierung verwendete Modellversion. (Standard: `"heygen-video-1"`) | DYNAMIC_COMBO | Ja | `"heygen-video-1"` |
| `prompt` | Beschreibung des Videos, einschließlich etwaigen Dialogs. Verweisen Sie auf verbundene Referenzen als @Image1, @Video1, @Audio1, nummeriert pro Typ in Eingabereihenfolge. (Standard: leerer String) | STRING | Ja | 1 bis 32000 Zeichen |
| `duration` | Dauer des Ausgabevideos in Sekunden. (Standard: 5) | INT | Ja | 5 bis 15 |
| `resolution` | Ausgabeauflösung. 2k erfordert das Seitenverhältnis 16:9 oder 9:16; 'auto' funktioniert bei 2k nur ohne Referenzen. (Standard: `"768p"`) | COMBO | Ja | `"768p"`<br>`"480p"`<br>`"2k"` |
| `aspect_ratio` | Ausgabeseitenverhältnis. `"auto"` ist 16:9, wenn keine Referenzen verbunden sind; andernfalls folgt es dem ersten Referenzbild oder, wenn keine Bilder verbunden sind, dem ersten Referenzvideo. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `seed` | Seed für die Generierung. Ergebnisse können zwischen Durchläufen mit demselben Seed weiterhin variieren. (Standard: 42) | INT | Ja | 0 bis 4294967295 |
| `reference_images` | Erweiterbarer Slot: Bilder von Personen, Produkten oder Orten zur Verwendung im Video (`image_1` ... `image_9`); verweisen Sie auf sie als @Image1, @Image2, ... Jede Eingabe muss genau ein Bild enthalten, und jedes Bild muss ein Seitenverhältnis zwischen 1:4 und 4:1 haben. | IMAGE | Nein | 0 bis 9 Bilder |
| `reference_videos` | Erweiterbarer Slot: Videos zur Verwendung als Referenzen (`video_1` ... `video_3`); verweisen Sie auf sie als @Video1, @Video2, ... | VIDEO | Nein | 0 bis 3 Videos |
| `reference_audios` | Erweiterbarer Slot: Audioclips wie eine Stimme für einen Sprecher (`audio_1` ... `audio_3`); verweisen Sie auf sie als @Audio1, @Audio2, ... Erfordert mindestens ein Referenzbild oder -video. Eine Stimmreferenz benötigt ein paar Sekunden klarer Sprache, und Clips, die kürzer als etwa 2 Sekunden sind, werden normalerweise ignoriert. | AUDIO | Nein | 0 bis 3 Audioclips |

### Parametereinschränkungen

- **Referenzlimit:** höchstens 12 Referenzen insgesamt über `reference_images`, `reference_videos` und `reference_audios`; das Verbinden weiterer Referenzen löst einen Fehler aus.
- **Audio benötigt Bild oder Video:** Referenzaudio wird abgelehnt, wenn weder ein Referenzbild noch ein Referenzvideo verbunden ist.
- **Regeln für Referenzbilder:** Jede `reference_images`-Eingabe muss genau ein Bild enthalten (ein Batch wird abgelehnt), und jedes Bild muss ein Seitenverhältnis zwischen 1:4 und 4:1 haben.
- **Prompt-Tags:** `@ImageN`, `@VideoN` und `@AudioN` werden ohne Beachtung der Groß-/Kleinschreibung abgeglichen. Die Nummer darf die Anzahl der verbundenen Referenzen dieses Typs nicht überschreiten, und der Prompt darf nach dem Entfernen von Leerraum nicht leer sein.
- **Modus:** Mit mindestens einem Referenzbild oder -video ist die Anfrage ein Referenz-zu-Video-Lauf; ohne ist es ein reiner Text-zu-Video-Lauf.
- **2k-Auflösung:** `resolution` `"2k"` erfordert `aspect_ratio` `"16:9"` oder `"9:16"`; `"auto"` wird bei 2k nur akzeptiert, wenn weder ein Referenzbild noch ein Referenzvideo verbunden ist.
- **Seed:** Der Seed entscheidet nur, ob der Node erneut ausgeführt wird; Ergebnisse sind mit demselben Seed nicht reproduzierbar.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das generierte Video mit synchronisiertem Dialog und Ton. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenReferenceToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `f3fae5dce59c90d65ad8eff2c992819f29a71e3a3e13fa91c1e7479a9cd6fcdc`
