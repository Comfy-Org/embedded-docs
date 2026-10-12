# Recraft Bild vektorisieren

Erzeugt SVG-Vektorgrafiken aus einem Eingabebild. Dieser Node konvertiert Rasterbilder in ein skalierbares Vektorformat, indem jedes Bild an die Recraft API gesendet und die Ergebnisse zu einer einzelnen SVG-Ausgabe zusammengeführt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `image` | Das Eingabebild, das in das SVG-Format konvertiert werden soll. Unterstützt die Stapelverarbeitung mehrerer Bilder. | IMAGE | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `SVG` | Die generierte Vektorgrafik-Ausgabe, die alle verarbeiteten Bilder zu einem einzelnen SVG-Dokument kombiniert. | SVG |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/de.md)

---
**Source fingerprint (SHA-256):** `bda74d9f11cc79217c61ecb8ba597a671133baa4380386428c4d9e9b68006713`
