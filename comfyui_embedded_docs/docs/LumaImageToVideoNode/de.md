# Luma Bild zu Video

Erzeugt Videos synchron auf Basis eines Text-Prompts und optionaler Start-/Endbilder. Dieser Node verwendet die Luma API, um Videos zu erstellen. Sie können den Inhalt des Videos über einen Prompt definieren und optional das erste und/oder letzte Einzelbild angeben, um die Struktur des Videos zu steuern.

**Hinweis:** Dieser Node ist im Quellcode als veraltet gekennzeichnet. Luma entfernt die Endpunkte, die dieser Node aufruft, am 24. Oktober 2026. Verwenden Sie stattdessen die Luma Ray 3.2-Nodes.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt für die Videogenerierung (Standard: "") | STRING | Ja | - |
| `model` | Wählt das Videogenerierungsmodell aus den verfügbaren Luma-Modellen aus | COMBO | Ja | `"ray-1-6"`<br>`"ray-2"` |
| `resolution` | Ausgabeauflösung für das generierte Video (Standard: "540p"). Dieser Parameter wird ignoriert, wenn das Modell `ray-1-6` verwendet wird. | COMBO | Ja | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `duration` | Dauer des generierten Videos. Dieser Parameter wird ignoriert, wenn das Modell `ray-1-6` verwendet wird. | COMBO | Ja | `"5s"`<br>`"9s"` |
| `loop` | Gibt an, ob das generierte Video in einer Schleife wiedergegeben werden soll (Standard: False) | BOOLEAN | Ja | - |
| `seed` | Seed, um zu bestimmen, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Ja | 0 bis 18446744073709551615 |
| `first_image` | Erstes Einzelbild des generierten Videos. (optional) | IMAGE | Nein | - |
| `last_image` | Letztes Einzelbild des generierten Videos. (optional) | IMAGE | Nein | - |
| `luma_concepts` | Optionale Camera Concepts, um die Kamerabewegung über den Luma Concepts-Node vorzugeben. (optional) | CUSTOM | Nein | - |

**Hinweis:** Mindestens eines von `first_image` oder `last_image` muss angegeben werden. Der Node löst eine Ausnahme aus, wenn beide fehlen. Die Parameter `resolution` und `duration` werden ignoriert, wenn `model` auf `ray-1-6` gesetzt ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierte Videodatei | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `c69d09286aba39062faa292e054d313833d977888a3cc7188a5ea8fdc9e66913`
