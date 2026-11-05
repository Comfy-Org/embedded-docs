# Pika H3 Flex Reference to Video

Dieser Node generiert oder bearbeitet ein Video mit synchronisiertem Audio, geleitet von Referenzbildern, Videos und Audioclips. Pika H3 Flex ist Pikas nachtrainiertes MiniMax-H3-Modell. Verbinden Sie Referenzen und adressieren Sie sie im Prompt in Verbindungsreihenfolge als `@Image1`, `@Video1` oder `@Audio1`. Mindestens ein Referenzbild oder -video ist erforderlich, und insgesamt können maximal 12 Referenzen verbunden werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Wertebereich |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Bis zu 9 Bilder, die im Prompt in Verbindungsreihenfolge als `@Image1` bis `@Image9` adressiert werden. Mindestens ein Bild oder Video ist erforderlich. | AUTOGROW | Nein | 0 bis 9 Bilder |
| `reference_videos` | Bis zu 3 Clips, die im Prompt in Verbindungsreihenfolge als `@Video1` bis `@Video3` adressiert werden. Jeder Clip muss 2 bis 15 Sekunden lang sein, und die Clips dürfen insgesamt höchstens 15 Sekunden lang sein. Abrechnung pro Sekunde. | AUTOGROW | Nein | 0 bis 3 Videos |
| `reference_audios` | Bis zu 3 Clips, die im Prompt als `@Audio1` bis `@Audio3` adressiert werden. Jeder Clip muss 2 bis 15 Sekunden lang sein, und die Clips dürfen insgesamt höchstens 15 Sekunden lang sein. Wenn sie in die Ausgabe kopiert werden, werden die Clips in Verbindungsreihenfolge abgespielt, vor dem Ton der verbundenen Videos. | AUTOGROW | Nein | 0 bis 3 Audioclips |
| `prompt` | Was generiert oder welche Bearbeitung vorgenommen werden soll. Referenzen werden als `@Image1`, `@Video1`, `@Audio1` oder als `<Picture 1>`, `<Video 1>`, `<Audio 1>` angegeben. Darf nicht leer sein. Standard: "" (leerer String). | STRING | Ja | 1 bis 8000 Zeichen |
| `reference_video_audio` | Den Ton verbundener Videos in die Ausgabe kopieren. Deaktivieren Sie dies für neue Hintergrundgeräusche oder für Bewegungstransfer mit neuer Musik. Ein Talking Head ohne Dialog im Prompt erhält dann eine erfundene Sprachausgabe. Standard: True. | BOOLEAN | Ja | true<br>false |
| `resolution` | Ausgabeauflösung. `"1080p"` und höher werden bei 768p gerendert und einmal hochskaliert. Derselbe Seed ergibt bei 480p ein anderes Video. Standard: `"768p"`. | COMBO | Ja | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `aspect_ratio` | Ausgabe-Seitenverhältnis. `"auto"` folgt einem Referenzvideo, andernfalls dem Prompt. Referenzbilder beeinflussen es nicht. Standard: `"auto"`. | COMBO | Ja | `"auto"`<br>`"21:9"`<br>`"16:9"`<br>`"3:2"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"9:21"` |
| `duration` | Clip-Länge in Sekunden. Die Ausgabelänge folgt einem Frame-Raster: 5 Sekunden ergeben 124 Frames, etwa 5,17 Sekunden. Standard: 5. | INT | Ja | 5 bis 15 Sekunden |
| `rewrite_prompt` | Lassen Sie Pika den Prompt zuerst erweitern. Derselbe Seed ergibt dann bei jedem Lauf ein anderes Video. Standard: False. | BOOLEAN | Ja | true<br>false |
| `seed` | Seed für das Sampling. Bei deaktiviertem `rewrite_prompt` wiederholt derselbe Seed das Video exakt, wobei ein lokaler Lauf mit demselben Seed ein anderes Ergebnis liefert. Standard: 42. | INT | Ja | 0 bis 2147483647 |

**Einschränkungen:**

* Mindestens ein Referenzbild oder -video ist erforderlich.
* Insgesamt können maximal 12 Referenzen verbunden werden, wobei Bilder, Videos und Audioclips zusammengezählt werden.
* Jedes Referenzvideo und jeder Audioclip muss 2 bis 15 Sekunden lang sein; die Videos dürfen insgesamt höchstens 15 Sekunden lang sein und die Audioclips höchstens 15 Sekunden.
* Der Prompt muss zwischen 1 und 8000 Zeichen lang sein.
* Das Referenzieren eines nicht verbundenen Slots, etwa `@Image3` bei nur zwei bereitgestellten Bildern, löst einen Fehler aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Der generierte oder bearbeitete Clip mit seinem synchronisierten Ton. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaH3FlexReferenceVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `c6d8700e3bb0c4ed7663aff55d477314af566568bd6db353fc21d6249ddd93bd`
