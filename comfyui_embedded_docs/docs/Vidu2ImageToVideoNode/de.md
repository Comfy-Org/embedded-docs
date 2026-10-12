# Vidu2 Bild-zu-Video-Generierung

Der Node Vidu2 Image-to-Video Generation erstellt eine Videosequenz, die von einem einzelnen Eingabebild ausgeht. Er verwendet ein angegebenes Vidu2-Modell, um die Szene anhand eines optionalen Text-Prompts zu animieren, und steuert dabei die Länge, Auflösung und Bewegungsintensität des Videos.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Das Vidu2-Modell, das für die Videogenerierung verwendet wird. Verschiedene Modelle bieten unterschiedliche Kompromisse zwischen Geschwindigkeit und Qualität. | COMBO | Ja | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` |
| `image` | Ein Bild, das als Startframe des generierten Videos verwendet wird. Es ist nur ein Bild erlaubt. | IMAGE | Ja | - |
| `prompt` | Ein optionaler Text-Prompt für die Videogenerierung (maximal 2000 Zeichen). Standard ist eine leere Zeichenkette. | STRING | Nein | - |
| `duration` | Die Länge des generierten Videos in Sekunden. Standard ist 5. | INT | Ja | 1 bis 10 |
| `seed` | Ein Seed-Wert für die Zufallszahlengenerierung, um reproduzierbare Ergebnisse sicherzustellen. Standard ist 1. | INT | Nein | 0 bis 2147483647 |
| `resolution` | Die Ausgabauflösung des generierten Videos. Dies ist ein erweiterter Parameter. | COMBO | Ja | `"720p"`<br>`"1080p"` |
| `movement_amplitude` | Die Bewegungsamplitude von Objekten im Frame. Dies ist ein erweiterter Parameter. | COMBO | Ja | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Einschränkungen:**

- Die Eingabe `image` muss genau ein Bild enthalten.
- Das Seitenverhältnis des Eingabebilds muss zwischen 1:4 und 4:1 liegen.
- Der Text für `prompt` ist auf maximal 2000 Zeichen begrenzt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `output` | Die generierte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `4cf56654286561f3d211ce50d0dce141880fe0e0a63aa45ab41ae0ff5ab6ccc3`
