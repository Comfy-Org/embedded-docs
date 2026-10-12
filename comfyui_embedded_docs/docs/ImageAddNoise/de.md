# ImageAddNoise

Der ImageAddNoise-Node fügt einem Eingabebild zufälliges Rauschen hinzu. Er verwendet einen angegebenen zufälligen Seed, um konsistente Rauschmuster zu erzeugen, und ermöglicht die Steuerung der Intensität des Rauscheffekts. Das resultierende Bild behält dieselben Abmessungen wie die Eingabe, weist jedoch eine zusätzliche visuelle Textur auf.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Eingabebild, dem Rauschen hinzugefügt wird | IMAGE | Ja | - |
| `seed` | Der zufällige Seed, der zum Erzeugen des Rauschens verwendet wird (Standard: 0). Dieser Parameter unterstützt die Funktionalität „control after generate“. | INT | Ja | 0 bis 18446744073709551615 |
| `strength` | Steuert die Intensität des Rauscheffekts (Standard: 0.5, Schritt: 0.01) | FLOAT | Ja | 0.0 bis 1.0 |

**Hinweis:** Rauschwerte werden zum Bild addiert und das Ergebnis wird auf den Bereich 0.0–1.0 begrenzt. Wenn das Eingabebild einen Alpha-Kanal (4 Kanäle) besitzt, bleibt der ursprüngliche Alpha-Kanal unverändert erhalten – Rauschen wird nur auf die Farbkanäle angewendet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das Ausgabebild mit angewendetem Rauschen | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/de.md)

---
**Source fingerprint (SHA-256):** `e6b9815e7c075c7ee97c924c22a92dfef6d9c65b97b6e65b0f9e1c96628f39f2`
