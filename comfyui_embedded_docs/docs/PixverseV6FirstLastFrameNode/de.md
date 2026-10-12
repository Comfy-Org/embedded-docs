# PixverseV6FirstLastFrameNode

PixVerse V6 First-Last-Frame to Video erzeugt mithilfe von PixVerse ein Video, das von einem ersten Frame zu einem letzten Frame übergeht, optional mit nativem Audio. Die beiden bereitgestellten Bilder werden an die PixVerse API gesendet, die das Übergangsvideo erzeugt und als Videodatei zurückgibt. Die Ausgabe behält das Seitenverhältnis des ersten Frames bei.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | Das Startbild des Videos. | IMAGE | Ja | — |
| `last_frame` | Das Endbild des Videos. | IMAGE | Ja | — |
| `model` | Modell- und Generierungseinstellungen. Wählt das PixVerse-Modell aus und zeigt dessen Generierungsparameter an. | DYNAMIC_COMBO | Ja | "PixVerse V6" |

### PixVerse V6 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt, der den Übergang beschreibt. | STRING | Ja | Bis zu 5000 Zeichen |
| `quality` | Ausgabeauflösung. Legt die lange Kante fest: 360p entspricht 640px, 540p 1024px, 720p 1280px, 1080p 1920px. (Standard: 720p) | COMBO | Ja | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Länge des generierten Videos in Sekunden. (Standard: 5) | INT | Ja | 1 bis 15 |
| `generate_audio` | Erzeugt eine native Audiospur zusammen mit dem Video. (Standard: true) | BOOLEAN | Ja | true<br>false |
| `seed` | Seed für die Videogenerierung. PixVerse zeichnet ihn auf, reproduziert damit aber keinen Lauf. (Standard: 42) | INT | Ja | 0 bis 2147483647 |
| `negative_prompt` | Eine optionale Textbeschreibung unerwünschter Elemente im Video. | STRING | Nein | Bis zu 2048 Zeichen |
| `style` | Ein optionaler visueller Stil, der auf das gesamte Video angewendet wird. (Standard: none) | COMBO | Nein | Mehrere Optionen verfügbar (Standard: "none") |

Hinweis: Der Prompt darf nach Entfernen von Leerzeichen nicht leer sein und ist auf 5000 Zeichen begrenzt. Der Negative Prompt ist, sofern angegeben, auf 2048 Zeichen begrenzt. Die Dauer muss zwischen 1 und 15 Sekunden liegen. Das Ausgabevideo behält das Seitenverhältnis des ersten Frames bei.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das generierte Video, das vom ersten Frame zum letzten Frame übergeht, einschließlich einer Audiospur, wenn `generate_audio` aktiviert ist. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FirstLastFrameNode/de.md)

---
**Source fingerprint (SHA-256):** `cdb5e45e9de2b429b9d43bbff90b6529af246911ecae8c2809c8abd539101aaa`
