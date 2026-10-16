# QuiverTextToSVGNodeV2

Erzeugen Sie mit Quiver AI eine skalierbare Vektorgrafik (SVG) aus einem Text-Prompt. Optionale Referenzbilder und Stilanweisungen können die Generierung steuern.

Die Auswahl eines `model` blendet die unten aufgeführten modellspezifischen Parameter ein.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `Modell` | Modell für die SVG-Generierung. | DYNAMIC_COMBO | Ja | `"arrow-2"`<br>`"arrow-2-telos"` |
| `prompt` | Textbeschreibung der gewünschten SVG-Ausgabe. Muss mindestens ein Zeichen enthalten (Standard: leer). | STRING | Ja | Beliebiger Text |
| `instructions` | Zusätzliche Stil- oder Formatierungshinweise. Optionaler erweiterter Parameter (Standard: leer). | STRING | Nein | Beliebiger Text |
| `reference_images` | Erweiterbarer Slot: Verbinden Sie ein oder mehrere optionale Referenzbilder (`ref_1`, `ref_2`, ...), die die Generierung steuern. Die maximale Anzahl der Bilder beträgt 14. | IMAGE | Nein | Bis zu 14 |
| `width` | Breite der SVG-Ausgabezeichenfläche (viewBox) in Benutzereinheiten. Legen Sie sowohl `width` als auch `height` fest, um die Ausgabegröße und das Seitenverhältnis zu steuern; lassen Sie einen der beiden Werte bei 0, damit das Modell wählen kann, was üblicherweise eine quadratische Zeichenfläche ergibt. Erweiterter Parameter (Standard: 0). | INT | Ja | 0 bis 8192 |
| `height` | Höhe der SVG-Ausgabezeichenfläche (viewBox) in Benutzereinheiten. Legen Sie sowohl `width` als auch `height` fest, um die Ausgabegröße und das Seitenverhältnis zu steuern; lassen Sie einen der beiden Werte bei 0, damit das Modell wählen kann, was üblicherweise eine quadratische Zeichenfläche ergibt. Erweiterter Parameter (Standard: 0). | INT | Ja | 0 bis 8192 |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed-Wert nicht deterministisch. Dieser Parameter bietet die Funktionalität „Steuerung nach Generierung“ (Standard: 42). | INT | Ja | 0 bis 2147483647 |

### Modellspezifische Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `reasoning_effort` | Wie viel Denkaufwand das Modell vor dem Zeichnen betreibt. Höhere Stufen verbessern die Detailgenauigkeit und verbrauchen mehr Tokens. Wird nur von den Modellen `"arrow-2"` und `"arrow-2-telos"` verwendet (Standard: `"high"`). | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | Steuerung der Zufälligkeit. Höhere Werte erhöhen die Zufälligkeit. Wird vom Modell `"arrow-2-telos"` nicht verwendet. Erweiterter Parameter (Standard: 1.0). | FLOAT | Ja | 0.0 bis 2.0 (Schrittweite 0.1) |
| `top_p` | Nucleus-Sampling-Parameter. Wird vom Modell `"arrow-2-telos"` nicht verwendet. Erweiterter Parameter (Standard: 1.0). | FLOAT | Ja | 0.05 bis 1.0 (Schrittweite 0.05) |
| `presence_penalty` | Token-Präsenzstrafe. Wird vom Modell `"arrow-2-telos"` nicht verwendet. Erweiterter Parameter (Standard: 0.0). | FLOAT | Ja | -2.0 bis 2.0 (Schrittweite 0.1) |

**Hinweis:** Die maximale Anzahl von `reference_images` beträgt 14. Lassen Sie `width` oder `height` bei 0, damit das Modell die Zeichenflächengröße auswählt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `SVG` | Die generierte SVG-Ausgabe. | SVG |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `a76184592a0c3a24d2758056e0823d8aa8e2684c27659caa2ee1772131cf8d8c`
