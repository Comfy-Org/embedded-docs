# Comfy Cloud MiniMax H3 Erstes-letztes-Frame-zu-Video [BETA]

Führt den MiniMax H3 First-Last-Frame-Workflow auf einer Comfy Cloud GPU aus und gibt die Bewegung zwischen zwei Keyframes mit passender Tonspur zurück. Übergeben Sie ihm das Anfangs- und das Endbild, und das Modell füllt die Aufnahme dazwischen aus. Das Endbild ist optional: Lassen Sie es weg, läuft die Bewegung stattdessen vom ersten Bild weg. Dies ist ein Beta-Node und wird pro GPU-Sekunde abgerechnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Erstes Frame` | Das Bild, von dem das Video startet. Es wird mit bis zu 2048x2048 Pixeln hochgeladen, bevor der Workflow ausgeführt wird. | IMAGE | Ja | - |
| `letztes Bild` | Optionales Endbild. Wenn verbunden, endet die generierte Bewegung auf diesem Bild; ohne dieses Bild läuft die Bewegung vom `first_frame` weg. | IMAGE | Nein | - |
| `Prompt` | Die Textbeschreibung der Bewegung und der Geräusche, die die Aufnahme enthalten soll. Führende und nachfolgende Leerzeichen werden vor der Übermittlung entfernt. | STRING | Ja | 1 bis 4096 Zeichen |
| `Seed` | Zufälliger Seed, der das generierte Ergebnis steuert (Standard: 42). | INT | Ja | 0 bis 18446744073709551615 |
| `Seitenverhältnis` | Seitenverhältnis des generierten Videos (Standard: `"1:1"`). | COMBO | Ja | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `Auflösung` | Budget für die Bildgröße (Standard: `"480p"`). 720p kostet etwa doppelt so viele GPU-Sekunden wie 480p. | COMBO | Ja | `"480p"`<br>`"720p"` |
| `Dauer in Sekunden` | Länge in Sekunden (Standard: 5). Die Pipeline quantisiert auf 17-Frame-Schritte bei 24 fps, daher liegt der Clip innerhalb von etwa zwei Dritteln einer Sekunde um diesen Wert. | INT | Ja | 5 bis 15 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das generierte Video mit seiner Tonspur. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3FirstLastFrameToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `5b9d1a2155951fb953e94726f0c6ca7720a805ab5d3015adaa5cc496acaa0de3`
