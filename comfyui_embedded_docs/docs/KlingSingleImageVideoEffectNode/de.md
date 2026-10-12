# KlingSingleImageVideoEffectNode

Der Kling Single Image Video Effect Node erstellt anhand eines einzelnen Referenzbildes Videos mit verschiedenen Spezialeffekten. Er wendet verschiedene visuelle Effekte und Szenen an, um statische Bilder in dynamische Videoinhalte umzuwandeln. Der Node unterstützt verschiedene Effektszenen, Modelloptionen und Videolängen, um das gewünschte visuelle Ergebnis zu erzielen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Referenzbild. URL oder Base64-kodierte Zeichenfolge (ohne data:image-Präfix). Die Dateigröße darf 10 MB nicht überschreiten, die Auflösung nicht unter 300x300 px liegen und das Seitenverhältnis muss zwischen 1:2.5 und 2.5:1 liegen | IMAGE | Ja | - |
| `effect_scene` | Der Typ der Spezialeffektszene, die auf die Videogenerierung angewendet werden soll. Einige Effekte können unterschiedliche Preise haben. | COMBO | Ja | `"dizzydizzy"`<br>`"bloombloom"`<br>`"neon"`<br>`"cartoon"`<br>`"sketch"`<br>`"oil"`<br>`"watercolor"`<br>`"3d"` |
| `model_name` | Die spezifische Modellversion, die zum Generieren des Videoeffekts verwendet werden soll. | COMBO | Ja | `"kling-v1-5"`<br>`"kling-v1-6"` |
| `duration` | Die Länge des generierten Videos in Sekunden. | COMBO | Ja | `"5"`<br>`"10"` |

**Hinweis:** Der Parameter `effect_scene` beeinflusst die Preisgestaltung des Nodes. Die Effekte `dizzydizzy` und `bloombloom` kosten 0,49 USD pro Generierung, während alle anderen Effekte 0,28 USD pro Generierung kosten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das generierte Video mit angewendeten Effekten | VIDEO |
| `video_id` | Die eindeutige Kennung für das generierte Video | STRING |
| `duration` | Die Dauer des generierten Videos | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/de.md)

---
**Source fingerprint (SHA-256):** `fb4a8b044daa99154a58d6926ff746bd2397b71ea32f1fafc851589f163ab51a`
