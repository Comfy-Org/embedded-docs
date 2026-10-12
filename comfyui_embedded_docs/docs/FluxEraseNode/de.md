# FluxEraseNode

Entfernt das maskierte Objekt aus einem Bild und rekonstruiert den Hintergrund. Malen Sie die Maske über den Bereich, den Sie entfernen möchten, und der Node füllt den Bereich mit plausiblen Hintergrundinhalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `image` | Das zu verarbeitende Eingabebild | IMAGE | Ja | - |
| `mask` | Weiße Bereiche werden entfernt; schwarze Bereiche bleiben erhalten | MASK | Ja | - |
| `dilate_pixels` | Erweitert die Maskengrenzen, um eine saubere Abdeckung der Objektkanten sicherzustellen (Standard: 10) | INT | Ja | 0 to 25 |
| `seed` | Der Zufallsseed, der zum Erzeugen des Rauschens verwendet wird (Standard: 0) | INT | Nein | 0 to 2147483647 |

**Hinweis:** Das Eingabebild muss in beiden Dimensionen mindestens 256x256 Pixel groß sein. Die Maske wird automatisch an die Bildabmessungen angepasst, und der Alphakanal des Bildes wird vor der Verarbeitung entfernt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `IMAGE` | Das resultierende Bild, bei dem das maskierte Objekt entfernt und der Hintergrund rekonstruiert wurde | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxEraseNode/de.md)

---
**Source fingerprint (SHA-256):** `124be59b9829aa9f865d7ec76cd68f7978e2010cd3a84f25742a1c17f2d70b76`
