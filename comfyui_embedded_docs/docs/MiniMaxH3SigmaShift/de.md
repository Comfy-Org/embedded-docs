# MiniMaxH3SigmaShift

Setzt die Video- und Audio-Flow-Shift-Werte für ein MiniMax H3-Modell. Der Video-Shift steuert den Sigma-Zeitplan des Samplers, und beide Shift-Werte werden an den internen Transformer des Modells übergeben, der sie verwendet, um den Audio-Zeitplan aus dem gemeinsamen Basisraster abzuleiten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Modell, auf das der Sigma-Shift-Patch angewendet werden soll. Der Node klont das Modell, sodass das Original unverändert bleibt. | MODEL | Ja | - |
| `shift_video` | Der Video-Flow-Shift-Wert. Er steuert den Sigma-Zeitplan des Samplers. Standard: 12.0. | FLOAT | Ja | 0.01 to 100.0 |
| `shift_audio` | Der Audio-Flow-Shift-Wert. Er wird vom Modell verwendet, um den Audio-Zeitplan abzuleiten. Standard: 3.0. | FLOAT | Ja | 0.01 to 100.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `MODEL` | Das geklonte Modell mit den angewendeten Video- und Audio-Sigma-Shift-Einstellungen. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3SigmaShift/de.md)

---
**Source fingerprint (SHA-256):** `0f731585cc1a9c87a3e54341757c4cf4e490d1d4718ecf458bd2b9f4378af63f`
