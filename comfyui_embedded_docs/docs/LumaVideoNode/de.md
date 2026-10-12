# LumaVideoNode

Generiert Videos synchron auf Grundlage eines Text-Prompts und der Ausgabeeinstellungen. Dieser Node erstellt Videoinhalte anhand von Textbeschreibungen und verschiedenen Generierungsparametern und erzeugt die endgültige Videoausgabe, sobald der Generierungsprozess abgeschlossen ist.

**Hinweis:** Dieser Node ist im Quellcode als veraltet markiert. Luma entfernt die Endpunkte, die dieser Node aufruft, am 24. Oktober 2026; verwenden Sie stattdessen die Luma Ray 3.2-Nodes.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt für die Videogenerierung (Standard: leerer String). Muss mindestens 3 Zeichen lang sein. | STRING | Ja | - |
| `model` | Das zu verwendende Videogenerierungsmodell. | COMBO | Ja | `"ray-1-6"`<br>`"ray-2"` |
| `aspect_ratio` | Das Seitenverhältnis für das generierte Video (Standard: "16:9"). | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `resolution` | Die Ausgabeauflösung für das Video (Standard: "540p"). Dieser Parameter wird ignoriert, wenn das Modell `ray-1-6` verwendet wird. | COMBO | Ja | `"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Die Dauer des generierten Videos. Dieser Parameter wird ignoriert, wenn das Modell `ray-1-6` verwendet wird. | COMBO | Ja | `"5s"`<br>`"9s"` |
| `loop` | Ob das Video in einer Schleife wiedergegeben werden soll (Standard: False). | BOOLEAN | Ja | - |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0). | INT | Ja | 0 bis 18446744073709551615 |
| `luma_concepts` | Optionale Camera Concepts, um die Kamerabewegung über den Luma Concepts-Node festzulegen. | CUSTOM | Nein | - |

**Hinweis:** Bei Verwendung des Modells `ray-1-6` werden die Parameter `duration` und `resolution` automatisch ignoriert und haben keinen Einfluss auf die Generierung.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `86ebb2d035d35f142709546566d1041b66765ae3e0c2751e71c05df138a5ecf2`
