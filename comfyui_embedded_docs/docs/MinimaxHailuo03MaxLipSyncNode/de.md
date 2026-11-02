# MiniMax H3 Max Lip Sync

Dieser Node animiert ein Standbild so, dass die Mundbewegungen einer bereitgestellten Audiospur folgen. Bild und Audio werden hochgeladen, der Hailuo 03 Max Lip-Sync-Job wird abgefragt, und das sprechende Video kommt in der von Ihnen gewählten Auflösung zurück. Das Ausgabevideo ist so lang wie das Audio.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Modell zur Videogenerierung. | DYNAMIC_COMBO | Ja | "MiniMax H3 Max" |

### MiniMax H3 Max Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Zu animierendes Bild, mindestens 256x256 Pixel. Das Seitenverhältnis muss zwischen 0,4 und 2,5 liegen. | IMAGE | Ja | Einzelnes Bild |
| `audio` | Audio für das Lip-Sync, 5 bis 899 Sekunden lang. | AUDIO | Ja | 5 bis 899 Sekunden |
| `resolution` | Ausgabeauflösung (Standard: "768P"). Das Seitenverhältnis ist das unterstützte, das dem Bild am nächsten kommt. | COMBO | Ja | "480P"<br>"768P"<br>"1080P"<br>"2K" |
| `transcription` | Das Audio transkribieren, um die Lippensynchronisation zu steuern (Standard: false). | BOOLEAN | Nein | true<br>false |
| `seed` | Zufälliger Seed. Dieselbe Anfrage mit demselben Seed liefert ähnliche, aber nicht garantiert identische Ergebnisse (Standard: 42). | INT | Ja | 0 bis 2147483647 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das sprechende Video, so lang wie das eingegebene Audio. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxLipSyncNode/de.md)

---
**Source fingerprint (SHA-256):** `0af4166f9f3237cacc3506d6c6544c0374a330cf998f8bd2ef1f4f7162e2f9ab`
