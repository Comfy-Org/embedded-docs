# Beeble SwitchX Video Edit

Bearbeiten Sie ein Video mit Beeble SwitchX. Dieser Node kann alles in der Szene austauschen (Hintergrund, Beleuchtung, Kostüm), während die Pixel und die Bewegung des ursprünglichen Motivs erhalten bleiben. Geben Sie ein Referenzbild und/oder einen Text-Prompt an, um das neue Aussehen zu beschreiben. Maximal 240 Frames, maximal ca. 2,77 Megapixel pro Frame.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Das Eingabevideo, das bearbeitet werden soll. | VIDEO | Ja | N/A |
| `prompt` | Eine Textbeschreibung des gewünschten neuen Aussehens für die Szene. | STRING | Ja | N/A |
| `alpha_mode` | Der Alpha-Matte-Modus. Der Modus "fill" hat keine separate Matte und füllt den gesamten Frame. Der Modus "select" verwendet ein einzelnes Keyframe-Bild, um den zu bearbeitenden Bereich festzulegen. Der Modus "custom" verwendet ein vollständiges Alpha-Video, um den zu bearbeitenden Bereich Frame für Frame festzulegen. | COMBO | Ja | `"fill"`<br>`"select"`<br>`"custom"` |
| `max_resolution` | Die maximale Auflösung für das Ausgabevideo (Standard: "1080p"). | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `seed` | Ein Seed-Wert für die Reproduzierbarkeit. Die Verwendung desselben Seeds mit denselben Eingaben erzeugt dasselbe Ergebnis. | INT | Ja | 0 to 2147483647 |
| `reference_image` | Ein optionales Referenzbild, das das gewünschte neue Aussehen für die Szene beschreibt. | IMAGE | Nein | N/A |

### Details zum Alpha-Modus

Der Parameter `alpha_mode` steuert, welche Teile des Videos bearbeitet werden:

- **fill**: Der gesamte Videoframe wird bearbeitet. Es wird keine separate Alpha-Matte erzeugt.
- **select**: Sie stellen ein einzelnes Keyframe-Bild bereit, das den zu bearbeitenden Bereich definiert. Der Node verwendet dieses, um zu bestimmen, welche Teile des Videos geändert werden.
- **custom**: Sie stellen ein vollständiges Alpha-Video bereit, das den zu bearbeitenden Bereich Frame für Frame definiert. Dies gibt Ihnen präzise Kontrolle darüber, welche Teile jedes Frames bearbeitet werden.

Bei Verwendung des Modus `select` müssen Sie das Bild `alpha_keyframe` bereitstellen. Bei Verwendung des Modus `custom` müssen Sie das Video `alpha_mask` bereitstellen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das bearbeitete Video mit den angewendeten Szenenänderungen. | VIDEO |
| `alpha` | Die von Beeble verwendete Alpha-Matte. Für den Modus "fill" ist diese leer, da keine separate Matte vorhanden ist. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXVideoEdit/de.md)

---
**Source fingerprint (SHA-256):** `a92e78e6a08ac01466d953562a250b812eb8b1a5fb37efce6fddd7aa1ef380a2`
