# Comfy Cloud MiniMax Music 3 Text zu Audio [BETA]

Führt den Workflow MiniMax Music 3 auf einer Comfy Cloud GPU aus und gibt einen generierten Song zurück. Der Prompt gibt Stil, Instrumentierung und Stimmung vor; Gesangstexte werden gesungen statt beschrieben, und ein leerer Gesangstext führt zu einem Instrumentalstück. Dies ist ein Beta-Node und wird pro GPU-Sekunde abgerechnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Prompt` | Beschreibung des Songs: Stil, Instrumentierung und Stimmung. Führende und nachfolgende Leerzeichen werden vor dem Absenden entfernt. | STRING | Ja | 1 bis 4096 Zeichen |
| `Liedtext` | Zu singende Wörter. Leer lassen für ein Instrumental. | STRING | Nein | 0 bis 4096 Zeichen |
| `Seed` | Zufälliger Seed, der das generierte Ergebnis steuert (Standard: 42). | INT | Ja | 0 bis 9223372036854775807 |
| `maximale Dauer` | Maximale Laufzeit des Tracks in Sekunden (Standard: 120.0). Das Modell kann den Song früher beenden. | FLOAT | Ja | 0.04 bis 360.0 (Schritt 0.04) |
| `Audioqualität` | Ausgabe-Bitrate. `"V0"` ist variabel und die höchste Qualität der drei (Standard: `"V0"`). | COMBO | Ja | `"V0"`<br>`"128k"`<br>`"320k"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `AUDIO` | Der generierte Song. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxMusic3TextToAudioNode/de.md)

---
**Source fingerprint (SHA-256):** `defc8d97071f2eaef4b00c6df721f4d10756e4867fefa22c1db7b8c3aafb6b7b`
