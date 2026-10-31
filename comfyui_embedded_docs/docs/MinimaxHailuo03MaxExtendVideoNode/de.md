# MiniMax H3 Max Extend Video

Dieser Node setzt ein Video mit neuen Aufnahmen fort, gesteuert durch einen Prompt und optionale Audioreferenzen. Das Quellvideo wird hochgeladen, die Fortsetzung wird generiert, und das Ergebnis wird entweder als das gesamte neu gerenderte Video oder als nur die neuen Aufnahmen zurückgegeben. Es stehen zwei Modelle zur Verfügung: „MiniMax H3 Max“ und „MiniMax H3 Max Turbo“, wobei letzteres pro Einheit günstiger ist.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Modell, das zum Fortsetzen des Videos verwendet wird. Beide Modelle stellen unten dieselben Eingaben bereit. | DYNAMIC_COMBO | Ja | "MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |

### Modelleingaben

Diese Eingaben gelten für beide Modelle.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Video, das verlängert werden soll, 1.625 bis 60 Sekunden lang, bis zu 50 MB. Das Seitenverhältnis muss zwischen 0.4 und 2.5 liegen. | VIDEO | Ja | 1.625 bis 60 Sekunden |
| `prompt` | Was als Nächstes passiert. Beschreiben Sie die Fortsetzung, nicht die Quelle. Verweisen Sie auf die Referenzaudios als `@Audio1`..`@Audio3`, zum Beispiel „@Audio1 für die Stimme“. | STRING | Ja | 1 bis 50000 Zeichen |
| `reference_audios` | Erweiterbarer Slot: Verbinden Sie bis zu 3 Audioclips (`audio_1`...`audio_3`) für die neuen Aufnahmen, jeweils mindestens 2 Sekunden und insgesamt höchstens 14.5 Sekunden. | AUDIO | Nein | 0 bis 3 Clips |
| `duration` | Sekunden neuer Aufnahmen, die hinzugefügt werden sollen (Standard: 5). | INT | Ja | 1 bis 15 |
| `resolution` | Auflösung des Ausgabevideos (Standard: "768P"). | COMBO | Ja | "480P"<br>"768P"<br>"1080P"<br>"2K" |
| `aspect_ratio` | Seitenverhältnis der Ausgabe. "auto" folgt dem Quellvideo; die anderen Werte beschneiden das Video auf das ausgewählte Verhältnis (Standard: "auto"). | COMBO | Ja | "auto"<br>"21:9"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16" |
| `output` | „extended“ gibt das gesamte Video zurück, neu gerendert in der ausgewählten Auflösung, mit den neuen Aufnahmen. „continuation“ gibt nur die neuen Aufnahmen zurück, beginnend mit einer 1.6 Sekunden langen Wiederholung des Endes des Quellvideos (Standard: "extended"). | COMBO | Ja | "extended"<br>"continuation" |
| `prompt_expansion` | Den Prompt anhand des Quellvideos umschreiben, um die Fortsetzung konsistent zu halten. Deaktivieren Sie dies, um reproduzierbare Ergebnisse für denselben Seed zu erhalten (Standard: true). | BOOLEAN | Nein | true<br>false |
| `seed` | Zufälliger Seed. Dieselbe Anfrage mit demselben Seed liefert ähnliche, aber nicht garantiert identische Ergebnisse (Standard: 42). | INT | Ja | 0 bis 4294967295 |

### Parametereinschränkungen

- Bei 2K-Auflösung ist die Ausgabe „extended“ auf insgesamt 45 Sekunden begrenzt, Quellvideo plus neue Aufnahmen. Verwenden Sie „continuation“ oder eine niedrigere Auflösung für längere Clips.
- Jeder Referenzaudio-Clip muss mindestens 2 Sekunden lang sein, und alle zusammen dürfen 14.5 Sekunden nicht überschreiten.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das verlängerte Video oder nur die neuen Aufnahmen, je nach Einstellung von `output`. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxExtendVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `db41a14db392fa450689c8d0d73d38b4ce9ea59ee30cfe4d6d2b0501cf0fc9a8`
