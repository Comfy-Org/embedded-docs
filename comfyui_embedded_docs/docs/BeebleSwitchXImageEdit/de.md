# BeebleSwitchXImageEdit

Bearbeiten Sie ein einzelnes Bild mit Beeble SwitchX. Dieser Node kann alles in der Szene austauschen (Hintergrund, Beleuchtung, Kostüm), während die Pixel des ursprünglichen Motivs erhalten bleiben. Geben Sie ein Referenzbild und/oder einen Text-Prompt an, um das neue Aussehen zu beschreiben. Die maximale Auflösung beträgt etwa 2,77 Megapixel.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Quellbild, das bearbeitet werden soll. | IMAGE | Ja | - |
| `prompt` | Eine textliche Beschreibung des gewünschten neuen Aussehens (z. B. „ein Ritter in glänzender Rüstung“). | STRING | Ja | - |
| `alpha_mode` | Legt fest, wie mit der Alpha-Matte umgegangen wird. `"select"` verwendet ein Keyframe, um das Motiv auszuwählen, `"fill"` ersetzt das gesamte Bild ohne separate Matte, `"custom"` verwendet eine vom Benutzer bereitgestellte Maske. | COMBO | Ja | `"select"`<br>`"fill"`<br>`"custom"` |
| `max_resolution` | Die maximale Auflösung für das Ausgabebild. Eine höhere Auflösung kostet mehr Credits. | COMBO | Ja | `"1080p"`<br>`"720p"` |
| `seed` | Ein Seed-Wert für die Reproduzierbarkeit. | INT | Ja | - |
| `reference_image` | Ein optionales Referenzbild, um den Stil oder das Erscheinungsbild der neuen Szenenelemente zu steuern. | IMAGE | Nein | - |

**Hinweis zu `alpha_mode`:** Wenn `alpha_mode` auf `"select"` gesetzt ist, müssen Sie zusätzlich ein `alpha_keyframe` angeben (ein Keyframe-Bild, das zur Auswahl des Motivs verwendet wird). Wenn es auf `"custom"` gesetzt ist, müssen Sie ein `alpha_mask` bereitstellen (eine vom Benutzer erstellte Maske). Wenn es auf `"fill"` gesetzt ist, ist keine Alpha-Eingabe erforderlich.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das bearbeitete Bild mit ausgetauschten Szenenelementen. | IMAGE |
| `alpha` | Die von Beeble verwendete Alpha-Matte. Leer für den `"fill"`-Modus, der keine separate Matte hat. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXImageEdit/de.md)

---
**Source fingerprint (SHA-256):** `6fd10dff6ac4f1a15fd05de7a6ff6eda988e60dd4ef32bc8c792480fbbf0c92b`
