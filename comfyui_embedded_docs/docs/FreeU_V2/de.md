# FreeU_V2

FreeU_V2 verbessert die Qualität der Bilderzeugung, indem es frequenzbasierte Modifikationen auf die U-Net-Architektur eines Diffusionsmodells anwendet. Es verwendet konfigurierbare Skalierungsfaktoren, um Feature-Kanäle in verschiedenen Blöcken anzupassen, und verbessert so die Ausgabe, ohne zusätzliches Training zu erfordern. Der Node funktioniert, indem er die Ausgabeblöcke des Modells patcht und Hochfrequenzkomponenten der verborgenen Zustände filtert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, auf das die FreeU-Verbesserung angewendet werden soll | MODEL | Ja | - |
| `b1` | Skalierungsfaktor für Backbone-Features des ersten Blocks (Standard: 1.3) | FLOAT | Ja | 0.0 - 10.0 |
| `b2` | Skalierungsfaktor für Backbone-Features des zweiten Blocks (Standard: 1.4) | FLOAT | Ja | 0.0 - 10.0 |
| `s1` | Skalierungsfaktor für Skip-Features des ersten Blocks (Standard: 0.9) | FLOAT | Ja | 0.0 - 10.0 |
| `s2` | Skalierungsfaktor für Skip-Features des zweiten Blocks (Standard: 0.2) | FLOAT | Ja | 0.0 - 10.0 |

Hinweis: `b1`, `b2`, `s1` und `s2` sind erweiterte Parameter, die in der Benutzeroberfläche des Nodes standardmäßig ausgeblendet sind. Sie können in Schritten von 0.01 innerhalb des Bereichs 0.0 - 10.0 festgelegt werden. `b1` und `s1` steuern den U-Net-Block mit den meisten Kanälen (das Vierfache der Basiskanalanzahl des Modells), während `b2` und `s2` den Block mit halb so vielen Kanälen steuern (das Doppelte der Basiskanalanzahl).

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das verbesserte Diffusionsmodell mit angewendeten FreeU-Modifikationen | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/de.md)

---
**Source fingerprint (SHA-256):** `4cef2af9b04164a8ead25bea9c9bb3311be9224f2539a5cc6edbe97ad8465d65`
