# RunwayAleph2VideoToVideoNode

## Überblick

Dieser Node bearbeitet ein Video mithilfe eines Text-Prompts mit dem Aleph2-Modell von Runway. Er transformiert Ihr Material, indem er es umstilisiert, die Beleuchtung ändert, Elemente hinzufügt oder entfernt oder den Blickwinkel verändert, während die ursprüngliche Bewegung und das Timing erhalten bleiben. Die Ausgabeauflösung entspricht der des Eingabevideos.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Beschreibt, was in der Ausgabe erscheinen soll (1-1000 Zeichen). | STRING | Ja | 1-1000 Zeichen |
| `video` | Eingabevideo, das bearbeitet werden soll. Muss 2-30 Sekunden lang sein und 30 fps oder weniger haben. | VIDEO | Ja | 2-30 Sekunden Dauer, max. 30 fps |
| `seed` | Zufalls-Seed für die Generierung (Standard: 0). | INT | Ja | 0 bis 4294967295 |
| `public_figure_threshold` | Inhaltsmoderation für erkennbare öffentliche Personen (Standard: "low"). | COMBO | Ja | `"auto"`<br>`"low"` |
| `keyframes` | Steuerungsbilder, die am Eingabevideo verankert sind, aus Aleph2-Keyframe-Nodes (bis zu 5). Verwenden Sie `keyframes` oder `prompt_images`, nicht beides. | KEYFRAME | Nein | Bis zu 5 Elemente |
| `prompt_images` | Steuerungsbilder, die am Ausgabevideo verankert sind, aus Aleph2-Prompt-Image-Nodes (bis zu 5). Verwenden Sie `keyframes` oder `prompt_images`, nicht beides. | PROMPT_IMAGE | Nein | Bis zu 5 Elemente |

**Wichtige Einschränkungen:**
- Das Eingabevideo muss zwischen 2 und 30 Sekunden lang sein und eine Bildrate von 30 fps oder niedriger haben.
- Sie können entweder `keyframes` oder `prompt_images` zur Steuerung verwenden, aber nicht beides gleichzeitig.
- Jede Steuerungseingabe (Keyframes oder Prompt-Bilder) unterstützt maximal 5 Elemente.
- Zeitstempel für Keyframes und Prompt-Bilder dürfen die Dauer des Eingabevideos nicht überschreiten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das vom Aleph2-Modell generierte bearbeitete Video. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2VideoToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `bda4d0f49843c1a8f311ddbce5911a2a157cae798a26f7a183b31fe41686d0b7`
