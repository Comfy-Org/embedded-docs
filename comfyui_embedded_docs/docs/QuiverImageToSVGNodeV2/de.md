# QuiverImageToSVGNodeV2

Vektorisieren Sie ein Rasterbild mit Quiver AI in eine skalierbare Vektorgrafik (SVG). Das Bild wird an die API von Quiver AI gesendet, die das vektorisierte Ergebnis zurückgibt.

**Hinweis:** Quiver stellt die Modelle der Arrow 1-Serie am 16. Oktober 2026 ein; danach funktionieren die Optionen `arrow-1.1`, `arrow-1.1-max` und `arrow-preview` nicht mehr. Verwenden Sie stattdessen `arrow-2` oder `arrow-2-telos`.

Wenn Sie ein `model` auswählen, werden die unten aufgeführten modellspezifischen Parameter angezeigt.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell, das für die SVG-Vektorisierung verwendet werden soll. | DYNAMIC_COMBO | Ja | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `image` | Eingabebild, das vektorisiert werden soll. | IMAGE | Ja | N/A |
| `auto_crop` | Schneidet automatisch auf das dominante Motiv zu. Erweiterter Parameter (Standard: False). | BOOLEAN | Ja | `True`<br>`False` |
| `target_size` | Quadratische Größenänderung, die vor dem Vektorisieren auf das Eingabebild angewendet wird, in Pixeln. 0 behält die Quellgröße bei, was sauberer vektorisiert als ein erzwungenes Resize; jeder andere Wert unter 128 wird auf 128 begrenzt. Dies legt nicht den Ausgabe-Canvas fest; verwenden Sie dafür `width` und `height`. Erweiterter Parameter (Standard: 0). | INT | Ja | 0 bis 4096 |
| `width` | Breite des Ausgabe-SVG-Canvas (viewBox), in Benutzereinheiten. Setzen Sie sowohl `width` als auch `height`, um Ausgabegröße und Seitenverhältnis zu steuern; lassen Sie einen der Werte auf 0, damit das Modell wählen kann, was normalerweise einen quadratischen Canvas ergibt. Erweiterter Parameter (Standard: 0). | INT | Ja | 0 bis 8192 |
| `height` | Höhe des Ausgabe-SVG-Canvas (viewBox), in Benutzereinheiten. Setzen Sie sowohl `width` als auch `height`, um Ausgabegröße und Seitenverhältnis zu steuern; lassen Sie einen der Werte auf 0, damit das Modell wählen kann, was normalerweise einen quadratischen Canvas ergibt. Erweiterter Parameter (Standard: 0). | INT | Ja | 0 bis 8192 |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed-Wert nicht deterministisch. Dieser Parameter bietet eine Funktion zur Steuerung nach der Generierung (Standard: 42). | INT | Ja | 0 bis 2147483647 |

### Modellspezifische Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Wie viel Reasoning das Modell vor dem Zeichnen aufwendet. Höhere Stufen verbessern das Detail und verbrauchen mehr Tokens. Wird nur von den Modellen `"arrow-2"` und `"arrow-2-telos"` verwendet (Standard: `"high"`). | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | Steuerung der Zufälligkeit. Höhere Werte erhöhen die Zufälligkeit. Wird vom Modell `"arrow-2-telos"` nicht verwendet. Erweiterter Parameter (Standard: 1.0). | FLOAT | Ja | 0.0 bis 2.0 (Schritt 0.1) |
| `top_p` | Nucleus-Sampling-Parameter. Wird vom Modell `"arrow-2-telos"` nicht verwendet. Erweiterter Parameter (Standard: 1.0). | FLOAT | Ja | 0.05 bis 1.0 (Schritt 0.05) |
| `presence_penalty` | Token-Präsenzstrafe. Wird vom Modell `"arrow-2-telos"` nicht verwendet. Erweiterter Parameter (Standard: 0.0). | FLOAT | Ja | -2.0 bis 2.0 (Schritt 0.1) |

**Hinweis:** `target_size` wird vor dem Vektorisieren angewendet und ändert nicht den Ausgabe-Canvas. Lassen Sie `width` oder `height` auf 0, damit das Modell die Canvas-Größe wählen kann.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `SVG` | Die vektorisierte SVG-Ausgabe. | SVG |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `186769b09bef2d2dbbfc26102f375ff80f8b324a24cd593da20afcea9cc2095b`
