# Quiver Text zu SVG

Der Node Quiver Text to SVG erzeugt aus einer Textbeschreibung mithilfe der Modelle von Quiver AI eine Scalable Vector Graphic (SVG). Optional können Sie Referenzbilder und Stilanweisungen bereitstellen, um den Generierungsprozess zu steuern.

**Hinweis:** Dieser Node ist im Quellcode als veraltet (deprecated) gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Textbeschreibung der gewünschten SVG-Ausgabe. Dies ist die Hauptanweisung dafür, was generiert werden soll. | STRING | Ja | N/A |
| `instructions` | Zusätzliche Stil- oder Formatierungsvorgaben. Dies ist ein optionaler, erweiterter Parameter. | STRING | Nein | N/A |
| `reference_images` | Bis zu 4 Referenzbilder zur Steuerung der Generierung. Dies ist eine optionale Eingabe. | IMAGE | Nein | 0 bis 4 Bilder |
| `model` | Modell, das für die SVG-Generierung verwendet werden soll. Die Auswahl eines Modells blendet zusätzliche, modellspezifische Parameter ein: `temperature`, `top_p` und `presence_penalty`. | DYNAMIC_COMBO | Ja | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: 0. | INT | Ja | 0 bis 2147483647 |
| `reasoning_effort` | Gibt an, wie viel Reasoning das Modell vor dem Zeichnen aufwendet. Höhere Stufen verbessern die Detailtreue und verbrauchen mehr Tokens. Wird nur von den Arrow-2-Modellen verwendet (Standard: "high"). | COMBO | Nein | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

**Hinweis:** Die Eingabe `reference_images` akzeptiert maximal 4 Bilder.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-----------|-----------|
| `SVG` | Das erzeugte Scalable Vector Graphic (SVG)-Bild. | SVG |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/de.md)

---
**Source fingerprint (SHA-256):** `e03e130a4aedbf003e898300b3a83e343fdfa5b3da35df20d55876d437bf5426`
