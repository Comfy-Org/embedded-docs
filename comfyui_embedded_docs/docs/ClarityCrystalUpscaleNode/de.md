# ClarityCrystalUpscaleNode

Skalieren Sie ein Bild mit dem Crystal Upscaler von Clarity AI hoch – einem hochpräzisen Upscaler, der originalgetreu bleibt und gleichzeitig Gesichter, Haut und feine Texturen wiederherstellt. Das Bild wird an die API von Clarity AI gesendet und das hochskalierte Ergebnis wird als Bild zurückgegeben.

Die Auswahl eines `model` zeigt die für dieses Modell spezifischen Parameter an.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Zu verwendendes Modell. Die Auswahl eines Modells zeigt die für dieses Modell spezifischen Parameter an: `image`, `scale_factor` und `creativity`. | DYNAMIC_COMBO | Ja | `"crystal-upscaler"` |
| `image` | Das hochzuskalierende Bild. Muss genau ein Bild enthalten; Bildstapel werden nicht unterstützt. | IMAGE | Ja | N/A |
| `scale_factor` | Faktor, mit dem die Bildbreite und -höhe multipliziert werden. Die Ausgabe ist auf 100 Megapixel begrenzt (Standard: 2.0). | FLOAT | Ja | 1.0 bis 200.0 (Schritt 0.1) |
| `creativity` | Höhere Werte lassen das Modell mehr Details rekonstruieren, anstatt das Original streng zu bewahren. Hat keine Auswirkung auf Bilder, deren kürzere Seite 256 Pixel oder weniger beträgt (Standard: 0). | INT | Ja | 0 bis 10 |

**Hinweis:** Das Eingabebild muss mindestens 2x2 Pixel groß sein. Die Ausgabe ist auf 100 Megapixel und 65535 Pixel pro Seite begrenzt; ein größeres Ergebnis löst einen Fehler aus. Verwenden Sie daher ein kleineres Bild oder einen niedrigeren `scale_factor`.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `IMAGE` | Das hochskalierte Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalUpscaleNode/de.md)

---
**Source fingerprint (SHA-256):** `38c90cf7054a93477ee63c356c3fdf8ba38c7edaf1a337da7ac366cd9d746d9e`
