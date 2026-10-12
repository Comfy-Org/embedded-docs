# LumaRay32TextToVideoNode

Dieser Node generiert mithilfe von Lumas Ray 3.2-Modell ein Video aus einem Text-Prompt. Er sendet Ihren Prompt und die Videoeinstellungen an die Luma-API und gibt das generierte Video zusammen mit einer Generierungs-ID zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für die Videogenerierung. | STRING | Ja | 1 bis 6000 Zeichen |
| `aspect_ratio` | Das Seitenverhältnis des generierten Videos. | STRING | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `resolution` | Die Ausgabeauflösung des Videos (Standard: "720p"). | STRING | Ja | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Die Dauer des generierten Videos. | STRING | Ja | `"5s"`<br>`"10s"` |
| `loop` | Lässt das Video nahtlos wiederholen. Nur bei einer Dauer von 5s verfügbar. | BOOLEAN | Nein | True/False (Standard: False) |
| `seed` | Seed für reproduzierbare Generierung. | INT | Nein | 0 bis 2147483647 |

**Hinweis:** Der Parameter `loop` kann nur aktiviert werden, wenn `duration` auf "5s" eingestellt ist. Wenn Sie `duration` auf "10s" setzen und `loop` aktivieren, gibt der Node einen Fehler zurück.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Die generierte Videodatei. | VIDEO |
| `generation_id` | Die eindeutige Kennung für die Video-Generierungsanfrage. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32TextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `04358a872530e5a2622bf0f148a694f2c707ce8535586d8f860bdf9911e1fa6a`
