# FluxProImageNode

Erzeugt Bilder synchron basierend auf Prompt und Auflösung. Dieser Node erstellt Bilder mit dem Flux 1.1 Pro-Modell, indem er Anfragen an einen API-Endpunkt sendet und auf die vollständige Antwort wartet, bevor das generierte Bild zurückgegeben wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt für die Bilderzeugung (Standard: leerer String) | STRING | Ja | - |
| `prompt_upsampling` | Ob ein Upsampling des Prompts durchgeführt werden soll. Wenn aktiviert, wird der Prompt automatisch für eine kreativere Generierung geändert, aber die Ergebnisse sind nicht deterministisch (derselbe Seed erzeugt nicht exakt dasselbe Ergebnis). (Standard: False) | BOOLEAN | Ja | - |
| `width` | Bildbreite in Pixeln (Standard: 1024, Schritt: 32) | INT | Ja | 256-1440 |
| `height` | Bildhöhe in Pixeln (Standard: 768, Schritt: 32) | INT | Ja | 256-1440 |
| `seed` | Der Zufalls-Seed, der zur Erzeugung des Rauschens verwendet wird. (Standard: 0) | INT | Ja | 0-18446744073709551615 |
| `image_prompt` | Optionales Referenzbild zur Steuerung der Generierung | IMAGE | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Das von der API zurückgegebene generierte Bild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProImageNode/de.md)

---
**Source fingerprint (SHA-256):** `89316d84f364854541157b5b60bae3d4e25024bd4af61a47a1748c6671b463c1`
