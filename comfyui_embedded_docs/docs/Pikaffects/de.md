# Pikaffects

Der Pikaffects-Node generiert Videos mit verschiedenen visuellen Effekten, die auf ein Eingabebild angewendet werden. Er verwendet Pikas Video-Generierungs-API, um statische Bilder in animierte Videos mit spezifischen Effekten wie Schmelzen, Explodieren oder Schweben zu verwandeln. Der Node benötigt einen API-Schlüssel und ein Authentifizierungstoken, um auf den Pika-Dienst zuzugreifen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Referenzbild, auf das der Pikaffect angewendet werden soll. | IMAGE | Ja | - |
| `pikaffect` | Der spezifische visuelle Effekt, der auf das Bild angewendet wird (Standard: "Cake-ify"). | COMBO | Ja | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" |
| `prompt_text` | Textbeschreibung, die die Videogenerierung steuert. | STRING | Ja | - |
| `negative_prompt` | Textbeschreibung dessen, was im generierten Video vermieden werden soll. | STRING | Ja | - |
| `seed` | Zufälliger Seed-Wert für reproduzierbare Ergebnisse. | INT | Ja | 0 bis 4294967295 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Das generierte Video mit dem angewendeten Pikaffect. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/de.md)

---
**Source fingerprint (SHA-256):** `68ebbee465763d463bf73678254eed38d37ebacb1c62d386bbe66961deffd5a8`
