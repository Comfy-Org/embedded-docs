# Luma Ray 3.2 Keyframes zu Video

Dieser Node erzeugt ein Video, das durch eine Sequenz von Leitbildern interpoliert, wobei jedes an einer bestimmten Position auf der Zeitachse verankert ist, unter Verwendung von Luma Ray 3.2. Erstellen Sie die Keyframe-Sequenz mit Luma Ray 3.2 Keyframe-Nodes, indem Sie mindestens 2 Keyframes verbinden, um die Animation zu definieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung (Standard: leerer String). | STRING | Ja | 1 bis 6000 Zeichen |
| `resolution` | Die Ausgabeauflösung des generierten Videos (Standard: "720p"). | STRING | Ja | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Die Dauer des generierten Videos (Standard: "5s"). | STRING | Ja | `"5s"`<br>`"10s"` |
| `seed` | Seed für die Zufallszahlengenerierung zur Steuerung der Reproduzierbarkeit. | INT | Ja | 0 bis 4294967295 |
| `keyframes` | Keyframe-Sequenz aus Luma Ray 3.2 Keyframe-Nodes (mindestens 2). | LUMA_RAY32_KEYFRAME | Ja | 2 bis 64 Keyframes |

**Hinweis:** Die Keyframe-Sequenz muss mindestens 2 Keyframes und höchstens 64 Keyframes enthalten. Jeder Keyframe muss eine eindeutige Position auf der Zeitachse haben. Keyframe-Positionen werden basierend auf der ausgewählten Dauer in Ausgabe-Frame-Indizes aufgelöst (120 Frames für 5s, 240 Frames für 10s). Keyframe-Positionen im Sekundenmodus dürfen die Gesamtdauer des Videos nicht überschreiten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Die generierte Videoausgabe. | VIDEO |
| `generation_id` | Die eindeutige Kennung für die Generierungsanfrage. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframesToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `28099e5990942860a20e23cfd5c71a36b23a6264b44097ca617f8bdd06e7857a`
