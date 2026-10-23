# Comfy Cloud MiniMax H3 Text zu Video [BETA]

Führt den MiniMax H3 Text-zu-Video-Workflow auf einer Comfy Cloud GPU aus und gibt ein Video mit passender Tonspur zurück. Bild und Audio entstehen im selben Durchlauf, anstatt nachträglich synchronisiert zu werden. Dies ist ein Beta-Node und wird pro GPU-Sekunde abgerechnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Prompt` | Die Textbeschreibung des Videos, einschließlich der Geräusche, die die Aufnahme enthalten soll. Führende und nachfolgende Leerzeichen werden vor der Übermittlung entfernt. | STRING | Ja | 1 bis 4096 Zeichen |
| `Seed` | Zufälliger Seed, der das generierte Ergebnis steuert (Standard: 42). | INT | Ja | 0 bis 18446744073709551615 |
| `Seitenverhältnis` | Seitenverhältnis des generierten Videos (Standard: `"16:9"`). | COMBO | Ja | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `Auflösung` | Budget für die Bildgröße (Standard: `"480p"`). 720p kostet etwa doppelt so viele GPU-Sekunden wie 480p. | COMBO | Ja | `"480p"`<br>`"720p"` |
| `Dauer in Sekunden` | Länge in Sekunden (Standard: 5). Die Pipeline quantisiert in 17-Frame-Schritten bei 24 fps, sodass der Clip innerhalb von etwa zwei Dritteln einer Sekunde um diesen Wert liegt. | INT | Ja | 5 bis 15 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `VIDEO` | Das generierte Video mit seiner Tonspur. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3TextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `bd1cbc80baa3b77ba48b529119495052252570b949676742b4c77cfe86b70ee2`
