# Recraft Bild vektorisieren

Erzeugt SVG-Vektorgrafiken aus einem Eingabebild. Dieser Node konvertiert Rasterbilder in ein skalierbares Vektorformat, indem jedes Bild an die Recraft-API gesendet und die Ergebnisse in einer einzigen SVG-Ausgabe zusammengeführt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das in das SVG-Format konvertiert werden soll. Unterstützt die Stapelverarbeitung mehrerer Bilder. | IMAGE | Ja | - |
| `version` | Die Version des Vektorisierers: `v1` ist die Standardversion, und `v1_pro` (Vectorizer Pro) liefert sauberere SVGs mit glatten Kurven, geraden Linien und scharfen Ecken, am besten geeignet für Schriftzüge und komplexe Formen (Standard: "v1"). | COMBO | Nein | "v1"<br>"v1_pro" |
| `shape_stacking` | Wie Formen im SVG gestapelt werden: `hierarchical` legt Formen übereinander; `cut_out` erzeugt Formen, die sich nie überlappen, für Plotter, Vinylschneider und Siebdruck (Standard: "hierarchical"). | COMBO | Nein | "hierarchical"<br>"cut_out" |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `SVG` | Die erzeugte Vektorgrafik-Ausgabe, die alle verarbeiteten Bilder in einem einzigen SVG-Dokument zusammenführt. | SVG |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/de.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`
