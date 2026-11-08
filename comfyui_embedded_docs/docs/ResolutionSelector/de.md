# Auflösungsauswahl

Der Node „Resolution Selector“ berechnet die Pixelbreite und -höhe basierend auf einem ausgewählten Seitenverhältnis und einer Ziel-Gesamtauflösung in Megapixeln. Er ist nützlich, um konsistente Abmessungen für andere Nodes zu erzeugen, wie z. B. für den Node „Empty Latent Image“.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Das Seitenverhältnis für die Ausgabeabmessungen (Standard: `"1:1 (Square)"`). | COMBO | Ja | `"1:1 (Square)"`<br>`"2:3 (Portrait Photo)"`<br>`"3:2 (Photo)"`<br>`"3:4 (Portrait Standard)"`<br>`"4:3 (Standard)"`<br>`"9:16 (Portrait Widescreen)"`<br>`"16:9 (Widescreen)"`<br>`"21:9 (Ultrawide)"` |
| `megapixels` | Ziel-Gesamtauflösung in Megapixeln. 1,0 MP ≈ 1024x1024 für quadratisch (Standard: 1,0). | FLOAT | Ja | 0.1 - 16.0 (Schritt: 0.01) |
| `preview` | Live-Vorschau der berechneten Ausgabeauflösung. Dieses schreibgeschützte Widget wird automatisch aktualisiert und akzeptiert keine Benutzereingaben. | RESOLUTION_PREVIEW | Nein | N/A |
| `multiple` | Nächstes Vielfaches des Ergebnisses, auf das die ausgewählte Auflösung eingestellt wird (Standard: 8). | INT | Nein | 8 - 128 (Schritt: 4) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `width` | Berechnete Breite in Pixeln, multipliziert mit dem ausgewählten Vielfachen. | INT |
| `height` | Berechnete Höhe in Pixeln, multipliziert mit dem ausgewählten Vielfachen. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/de.md)

---
**Source fingerprint (SHA-256):** `d97624227fa02cd2e2f9bdecb3443f9877402092dcee8c45b721a83739454e18`
