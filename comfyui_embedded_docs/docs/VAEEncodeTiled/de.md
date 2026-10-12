# VAEEncodeTiled

VAEEncodeTiled verarbeitet Bilder, indem es sie in kleinere Kacheln aufteilt und sie mit einem Variational Autoencoder kodiert. Dieser Kachelungsansatz ermöglicht die Verarbeitung großer Bilder, die andernfalls die Speichergrenzen überschreiten könnten. Der Node unterstützt sowohl Bild- als auch Video-VAEs, mit separaten Kachelungssteuerungen für räumliche und zeitliche Dimensionen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `pixels` | Die zu kodierenden Eingabebilddaten. | IMAGE | Ja | - |
| `vae` | Das Variational-Autoencoder-Modell, das zur Kodierung verwendet wird. | VAE | Ja | - |
| `tile_size` | Die Größe jeder Kachel für die räumliche Verarbeitung (Standard: 512). Erweiterte Einstellung. | INT | Ja | 64-4096 (step: 64) |
| `overlap` | Die Überlappung zwischen benachbarten Kacheln (Standard: 64). Erweiterte Einstellung. | INT | Ja | 0-4096 (step: 32) |
| `temporal_size` | Nur für Video-VAEs verwendet: Anzahl der gleichzeitig zu kodierenden Frames (Standard: 64). Erweiterte Einstellung. | INT | Ja | 8-4096 (step: 4) |
| `temporal_overlap` | Nur für Video-VAEs verwendet: Anzahl der zu überlappenden Frames (Standard: 8). Erweiterte Einstellung. | INT | Ja | 4-4096 (step: 4) |

**Hinweis:** Die Parameter `temporal_size` und `temporal_overlap` sind nur bei Verwendung von Video-VAEs relevant und haben keine Auswirkung auf Standard-Bild-VAEs.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `LATENT` | Die kodierte latente Repräsentation des Eingabebildes. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/de.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`
