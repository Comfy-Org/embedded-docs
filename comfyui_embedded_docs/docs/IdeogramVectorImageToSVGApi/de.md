# Ideogram Vector Image to SVG

Dieser Node konvertiert ein Bild mit Ideogram Vector in ein bearbeitbares SVG. Das Ergebnis ist Vektormarkup statt eines Rasterbildes, sodass die nachgezeichneten Formen in einem Vektoreditor bearbeitbar bleiben. Transparente Bereiche eines Bildes mit Alpha bleiben transparent.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell. Standard: `"ideogram-vector-1"`. | DYNAMIC_COMBO | Ja | `"ideogram-vector-1"` |
| `image` | Das zu konvertierende Bild. Eine Batch-Eingabe wird Bild für Bild konvertiert und die resultierenden SVGs werden zusammen zurückgegeben. | IMAGE | Ja | - |
| `mode` | `"simple"` zeichnet weniger, größere Formen nach; `"default"` behält feinere Details bei. Standard: `"default"`. | COMBO | Ja | `"simple"`<br>`"default"` |

**Einschränkungen:**

* Bilder, deren längste Seite mehr als 2048 Pixel beträgt, werden vor dem Hochladen herunterskaliert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `SVG` | Das konvertierte Bild als bearbeitbares Vektormarkup. | SVG |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorImageToSVGApi/de.md)

---
**Source fingerprint (SHA-256):** `6553291e9d887b31485b9cbf8f6ced4186470eb47e8621ebb0f4e5df6542123e`
