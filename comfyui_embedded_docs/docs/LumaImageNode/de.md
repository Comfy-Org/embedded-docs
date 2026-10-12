# LumaImageNode

Erzeugt Bilder synchron anhand eines Text-Prompts und eines Seitenverhältnisses. Dieser Node erstellt Bilder mithilfe von Textbeschreibungen und ermöglicht es Ihnen, die Bildabmessungen und den Stil über verschiedene Referenzeingaben zu steuern, einschließlich Charakter- und Stilbildern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt für die Bilderzeugung (Standard: leerer String). Muss mindestens 3 Zeichen lang sein. | STRING | Ja | - |
| `model` | Modellauswahl für die Bilderzeugung. Verschiedene Modelle haben unterschiedliche Kosten. | COMBO | Ja | `photon-flash-1`<br>`photon-1`<br>`photon` |
| `aspect_ratio` | Seitenverhältnis für das generierte Bild (Standard: `16:9`) | COMBO | Ja | `16:9`<br>`1:1`<br>`4:3`<br>`3:2`<br>`21:9`<br>`9:16`<br>`3:4`<br>`2:3`<br>`9:21` |
| `seed` | Seed, um zu bestimmen, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0) | INT | Ja | 0 bis 18446744073709551615 |
| `style_image_weight` | Gewichtung des Stilbilds. Wird ignoriert, wenn kein `style_image` angegeben ist (Standard: 1.0) | FLOAT | Nein | 0.0 bis 1.0 |
| `image_luma_ref` | Verbindung zum Luma Reference-Node, um die Generierung durch Eingabebilder zu beeinflussen; es können bis zu 4 Bilder berücksichtigt werden. | LUMA_REF | Nein | - |
| `style_image` | Stil-Referenzbild; es wird nur 1 Bild verwendet. | IMAGE | Nein | - |
| `character_image` | Charakter-Referenzbilder; kann ein Batch aus mehreren sein, bis zu 4 Bilder können berücksichtigt werden. | IMAGE | Nein | - |

**Parametereinschränkungen:**

- Der `prompt` muss nach dem Entfernen von Leerzeichen mindestens 3 Zeichen lang sein.
- Der Parameter `image_luma_ref` kann bis zu 4 Referenzbilder akzeptieren.
- Der Parameter `character_image` kann bis zu 4 Charakter-Referenzbilder akzeptieren.
- Der Parameter `style_image` akzeptiert nur 1 Stil-Referenzbild.
- Der Parameter `style_image_weight` wird nur verwendet, wenn `style_image` angegeben ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Das generierte Bild basierend auf den Eingabeparametern. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode/de.md)

---
**Source fingerprint (SHA-256):** `cde0fc1ace28523d658b757d7f829b0d20071bed391964d2d8caa81801265b46`
