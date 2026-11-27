# Recraft Bild vektorisieren

Erzeugt SVG-Vektorgrafiken aus einem Eingabebild. Dieser Node wandelt Rasterbilder in ein skalierbares Vektorformat um, indem jedes Bild an die Recraft-API gesendet und die Ergebnisse in einer einzigen SVG-Ausgabe zurückgegeben werden. Diese Ausgabe enthält für jedes verarbeitete Bild ein separates SVG-Dokument; die Dokumente werden nicht zu einem zusammengeführt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das in das SVG-Format konvertiert werden soll. Unterstützt die Stapelverarbeitung mehrerer Bilder. | IMAGE | Ja | - |
| `Version` | Die Version des Vektorisierers: `v1` ist die Standardversion, und `v1_pro` (Vectorizer Pro) liefert sauberere SVGs mit glatten Kurven, geraden Linien und scharfen Ecken, ideal für Beschriftungen und komplexe Formen (Standard: "v1"). | COMBO | Nein | "v1"<br>"v1_pro" |
| `shape_stacking` | Wie Formen im SVG gestapelt werden: `hierarchical` schichtet Formen übereinander; `cut_out` erzeugt Formen, die sich niemals überlappen, für Plotter, Vinylschneider und Siebdruck (Standard: "hierarchical"). | COMBO | Nein | "hierarchical"<br>"cut_out" |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `SVG` | Die erzeugten Vektorgrafiken. Die einzelne SVG-Ausgabe enthält für jedes verarbeitete Bild ein separates SVG-Dokument. | SVG |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/de.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`
