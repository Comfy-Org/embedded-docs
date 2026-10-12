# Videoliste mischen

Dieser Node nimmt eine Liste von Videos entgegen und ordnet sie zufällig neu an. Er verwendet einen Zufalls-Seed, um die Mischung reproduzierbar zu machen, sodass derselbe Seed stets dieselbe Ausgabereihenfolge erzeugt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `videos` | Liste der zu mischenden Videos. | VIDEO | Ja | Liste der Video-Eingaben |
| `seed` | Zufalls-Seed für das Mischen (Standard: 0). | INT | Nein | 0 bis 18446744073709551615 |

Hinweis: Der Wert von `seed` wird vor der Verwendung modulo 4294967295 (2^32 - 1) reduziert. Daher erzeugen Seeds, die sich um ein Vielfaches von 4294967295 unterscheiden, dieselbe Ausgabereihenfolge.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `videos` | Gemischte Liste von Videos in zufälliger Reihenfolge. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoDataset/de.md)

---
**Source fingerprint (SHA-256):** `0bd32b664197d3bbd4c53f65e29ef38fba836579f07f05cb7fb85f3b8a1024ac`
