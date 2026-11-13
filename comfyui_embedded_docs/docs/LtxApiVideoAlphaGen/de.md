# LTX Video AlphaGen

Extrahiert eine Graustufen-Alpha-Matte, weiß für den Vordergrund, die dem Eingabevideo Bild für Bild entspricht. Geben Sie die Matte an Get Video Components und Image To Mask weiter, um sie in eine Maske umzuwandeln. Audio wird nicht beibehalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Video, das als Matte extrahiert werden soll, bis zu 10 Sekunden und 3840x2160 in beliebiger Ausrichtung. | VIDEO | Ja | - |
| `seed` | Steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 42. | INT | Nein | 0 bis 4294967295 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `matte` | Die Alpha-Matte als Video, ein Frame pro Eingabeframe und ohne Audio. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoAlphaGen/de.md)

---
**Source fingerprint (SHA-256):** `54a8304c2d092a736ad7fb86c8497aceda6340886beb81b6068a3de5a387a746`
