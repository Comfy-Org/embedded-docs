# JSON-Prompt erstellen (Ideogram)

Dieser Node erstellt einen strukturierten JSON-Prompt, der speziell für das Ideogram 4-Bildgenerierungsmodell formatiert ist. Er organisiert Ihre Textanweisungen, Stilpräferenzen, Kamera- oder Kunstdetails, Beleuchtung, Medium und optionale Farbpalette in die erforderliche JSON-Struktur, die das Modell erwartet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `element` | Prompt-Elemente vom Node Create Bounding Boxes. | ARRAY | Ja | - |
| `high_level_description` | Optionale Beschreibung des Bildes in ein bis zwei Sätzen. Sehr zu empfehlen. (Standard: leer) | STRING | Nein | - |
| `background` | Obligatorische Beschreibung des Bildhintergrunds oder der Umgebung. Die Angabe eines Werts wird dringend empfohlen – der Node läuft mit einer leeren Zeichenkette, aber die Ergebnisse können unvorhersehbar sein. (Standard: leer) | STRING | Nein | - |
| `style` | Die visuelle Stilkategorie für das generierte Bild. Wählen Sie eine der Optionen. (Standard: `"none"`) | COMBO | Ja | `"none"`<br>`"photo"`<br>`"art_style"` |
| `photo` | Kamera- oder Objektivdetails für fotografische Ausgaben (z. B. 35mm, f/1.4, Bokeh). Nur verfügbar, wenn `style` auf `"photo"` gesetzt ist. (Standard: leer) | STRING | Nein | - |
| `art_style` | Kunststilbeschreibung (z. B. flache Vektorillustration, kräftige Konturen). Nur verfügbar, wenn `style` auf `"art_style"` gesetzt ist. (Standard: leer) | STRING | Nein | - |
| `aesthetics` | Obligatorische ästhetische Schlüsselwörter (z. B. stimmungsvoll, filmisch, entsättigt). Die Angabe eines Werts wird dringend empfohlen. (Standard: leer) | STRING | Nein | - |
| `lighting` | Obligatorische Lichtbeschreibung (z. B. goldene Stunde, Kantenlicht, dramatische Schatten). Die Angabe eines Werts wird dringend empfohlen. (Standard: leer) | STRING | Nein | - |
| `medium` | Obligatorischer Medientyp (z. B. photograph, illustration, 3d_render, painting, graphic_design). Wenn `style` = `"photo"`, auf `"photograph"` setzen. Die Angabe eines Werts wird dringend empfohlen. (Standard: leer) | STRING | Nein | - |
| `color_palette` | Hex-Farbcodes, die die dominanten Farben des Bildes steuern. Bis zu 16 Einträge. | COLORS | Nein | - |

**Hinweis:** Wenn `style` auf `"photo"` gesetzt ist, wird die Eingabe `photo` verfügbar und Sie sollten normalerweise `medium` auf `"photograph"` setzen. Wenn `style` auf `"art_style"` gesetzt ist, wird die Eingabe `art_style` verfügbar. Die Parameter `background`, `aesthetics`, `lighting` und `medium` haben standardmäßig leere Zeichenketten, gelten aber als obligatorisch für eine zuverlässige Bildgenerierung; die Angabe von Werten wird dringend empfohlen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `prompt` | Ein strukturiertes JSON-Wörterbuch, das die High-Level-Beschreibung, die Stilbeschreibung (falls ein anderer Stil als `"none"` ausgewählt wurde) und eine kompositorische Dekonstruktion mit Hintergrund und Elementen enthält. | DICT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildJsonPromptIdeogram/de.md)

---
**Source fingerprint (SHA-256):** `56a045e0c7c19531e6443696c0bdf3946df066d03eea7d2d217b7d92f052592f`
