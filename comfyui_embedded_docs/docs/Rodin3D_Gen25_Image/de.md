# Rodin 3D Gen-2.5 – Bild zu 3D

## Übersicht

Dieser Node generiert aus ein bis fünf Referenzbildern ein 3D-Modell mithilfe der Rodin Gen-2.5 API. Sie können zwischen den Qualitätsmodi Fast, Regular oder Extreme-High wählen, um Generierungsgeschwindigkeit und Kosten abzuwägen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Ein bis fünf Eingabebilder. Wenn mehrere Bilder bereitgestellt werden, wird das erste Bild für Materialien verwendet. | IMAGE | Ja | 1 bis 5 Bilder |
| `mode` | Der Generierungsqualitätsmodus. Höhere Qualitätsmodi liefern bessere Ergebnisse, kosten jedoch mehr. | COMBO | Ja | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | Der Materialtyp für das generierte 3D-Modell. | COMBO | Ja | `"PBR"`<br>`"Matte"` |
| `geometry_file_format` | Das Ausgabedateiformat für die Geometrie des 3D-Modells. | COMBO | Ja | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `texture_mode` | Der Texturgenerierungsmodus. „Original“ behält die Eingabetexturen bei, „Clean“ entfernt sie, und „Style“ wendet eine stilisierte Textur an. | COMBO | Ja | `"Original"`<br>`"Clean"`<br>`"Style"` |
| `seed` | Ein zufälliger Seed für reproduzierbare Ergebnisse. Verwenden Sie denselben Seed, um dieselbe Ausgabe zu erhalten. | INT | Ja | 0 bis 2147483647 |
| `TAPose` | Ob T-Pose auf das generierte Modell angewendet werden soll. | BOOLEAN | Ja | True / False |
| `hd_texture` | Ob eine hochauflösende Texturmap generiert werden soll. | BOOLEAN | Ja | True / False |
| `texture_delight` | Ob vor der Texturgenerierung die Beleuchtung aus den Eingabebildern entfernt werden soll. | BOOLEAN | Ja | True / False |
| `use_original_alpha` | Ob der ursprüngliche Alphakanal aus den Eingabebildern verwendet werden soll. | BOOLEAN | Ja | True / False |
| `addon_highpack` | Ob zusätzlich zum Standardmodell eine hochpolygonale Version des Modells generiert werden soll. | BOOLEAN | Ja | True / False |
| `bbox_width` | Die Breite des Begrenzungsrahmens für das generierte Modell in Zentimetern. | INT | Ja | 1 bis 1000 |
| `bbox_height` | Die Höhe des Begrenzungsrahmens für das generierte Modell in Zentimetern. | INT | Ja | 1 bis 1000 |
| `bbox_length` | Die Länge des Begrenzungsrahmens für das generierte Modell in Zentimetern. | INT | Ja | 1 bis 1000 |
| `height_cm` | Die Höhe des generierten Modells in Zentimetern. | INT | Ja | 1 bis 300 |

**Hinweis zur Bildanzahl:** Der Node akzeptiert zwischen 1 und 5 Bildern. Wenn Sie einen Batch von Bildern bereitstellen (z. B. einen Batch mit 4 Bildern), wird jedes Bild im Batch als separates Eingabebild behandelt. Die Angabe von mehr als 5 Bildern führt zu einem Fehler.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Die generierte 3D-Modell-Datei im ausgewählten Geometrieformat. | FILE3D |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Image/de.md)

---
**Source fingerprint (SHA-256):** `6437f8d34624fccfb92505bcdc627db2df2f4159c929a4f7b00352906c609a25`
