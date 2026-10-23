# Comfy Cloud MiniMax H3 Bild zu Video [BETA]

Führt den MiniMax H3 Image-to-Video-Workflow auf einer Comfy Cloud GPU aus und gibt ein Video mit passender Tonspur zurück. Das Standbild wird zum ersten Frame. Wird das Schlussbild eines Clips erneut eingespeist, wird die Sequenz fortgesetzt, sodass durch die Verkettung mehrerer Durchläufe eine längere Einstellung entsteht. Dies ist ein Beta-Node und wird pro GPU-Sekunde abgerechnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `erstes Bild` | Das Bild, von dem das Video ausgeht. Es wird vor dem Ausführen des Workflows mit bis zu 2048x2048 Pixeln hochgeladen. | IMAGE | Ja | - |
| `Prompt` | Die Textbeschreibung der Bewegung und der Klänge, die die Einstellung enthalten soll. Führende und nachfolgende Leerzeichen werden vor der Übermittlung entfernt. | STRING | Ja | 1 bis 4096 Zeichen |
| `Seed` | Zufälliger Seed, der das generierte Ergebnis steuert (Standard: 42). | INT | Ja | 0 bis 18446744073709551615 |
| `Seitenverhältnis` | Seitenverhältnis des generierten Videos (Standard: `"1:1"`). | COMBO | Ja | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `Auflösung` | Budget für die Bildgröße (Standard: `"480p"`). 720p kostet etwa doppelt so viele GPU-Sekunden wie 480p. | COMBO | Ja | `"480p"`<br>`"720p"` |
| `Dauer in Sekunden` | Länge in Sekunden (Standard: 5). Die Pipeline quantisiert auf 17-Frame-Schritte bei 24 fps, sodass der Clip innerhalb von etwa zwei Dritteln einer Sekunde um diesen Wert landet. | INT | Ja | 5 bis 15 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das generierte Video mit seiner Tonspur. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3ImageToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `d3657e266f2b9f789414a106ef66b6c64ec314d27c3b6a99c3a6a9b8584abf61`
