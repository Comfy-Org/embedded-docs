# Bilderliste mischen

Der Node Shuffle Dataset nimmt eine Liste von Bildern entgegen und ändert deren Reihenfolge zufällig. Er verwendet einen Seed-Wert, um die Zufälligkeit zu steuern, wodurch sichergestellt wird, dass dieselbe Shuffle-Reihenfolge reproduziert werden kann. Dies ist nützlich, um die Reihenfolge der Bilder in einem Dataset vor der Verarbeitung zu randomisieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Die Liste der Bilder, die gemischt werden sollen. | IMAGE | Ja | - |
| `seed` | Zufälliger Seed. (Standard: 0) | INT | Nein | 0 bis 18446744073709551615 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Dieselbe Liste von Bildern, aber in einer neuen, zufällig gemischten Reihenfolge. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleDataset/de.md)

---
**Source fingerprint (SHA-256):** `6cde5dcf15817ab98f35f7b2e40fe79a5451c86dba93c0e3cd2622d1cec76c36`
