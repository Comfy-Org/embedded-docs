# Creatify Aurora 2.0 Avatar

Creatify Aurora 2.0 Avatar verwandelt ein Foto zusammen mit einem Sprach- oder Gesangsclip in ein sprechendes oder singendes Video. Das Video ist so lang wie das verbundene Audio und behält dieses Audio unverändert bei.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Foto der zu animierenden Person. Mindestens 256 Pixel pro Seite und ein Seitenverhältnis zwischen 1:4 und 4:1; das Video behält das Seitenverhältnis des Fotos bei. | IMAGE | Ja | - |
| `audio` | Sprache oder Gesang, die den Mund und die Länge des Videos steuert. Bis zu 60 Sekunden oder 14 Sekunden bei `"2k"`; Abrechnung pro angefangener Sekunde. | AUDIO | Ja | Bis zu 60 Sekunden |
| `resolution` | Auflösung des Ausgabevideos (Standard: `"720p"`). | COMBO | Ja | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"2k"` |
| `text_prompt` | Szene, Kamera, Beleuchtung, Ausdruck oder Bewegung für die Aufnahme. Leer lässt das Foto unverändert (Standard: leerer String). | STRING | Ja | Beliebiger Text |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt wird. Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 42). | INT | Ja | 0 bis 2147483647 |

**Einschränkungen:** Ein Foto, das an einer Seite kleiner als 256 Pixel ist oder ein Seitenverhältnis außerhalb von 1:4 bis 4:1 hat, führt zu einem Fehler. Audio, das länger als das Limit für die gewählte Auflösung ist, wird abgelehnt: normalerweise 60 Sekunden und 14 Sekunden bei `"2k"`.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das sprechende oder singende Video mit dem verbundenen Audio. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyAurora2AvatarNode/de.md)

---
**Source fingerprint (SHA-256):** `29c83246ebed4bc7a9f3daf3612cd6f34bf2d5a2f1fde7612614a2da6a5010be`
