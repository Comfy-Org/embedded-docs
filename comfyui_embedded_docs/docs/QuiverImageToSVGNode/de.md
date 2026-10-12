# Quiver Bild zu SVG

Dieser Node wandelt ein Rasterbild mithilfe der Vektorisierungsmodelle von Quiver AI in eine skalierbare Vektorgrafik (SVG) um. Er sendet das Bild an eine externe API, die es verarbeitet und das vektorisierte Ergebnis zurückgibt.

**Hinweis:** Dieser Node ist im Quellcode als veraltet markiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Eingabebild zur Vektorisierung. | IMAGE | Ja | N/A |
| `auto_crop` | Automatisches Zuschneiden auf das dominante Motiv (Standard: False). | BOOLEAN | Ja | True<br>False |
| `model` | Modell für die SVG-Vektorisierung. Die Auswahl eines Modells zeigt zusätzliche Parameter an, die für dieses Modell spezifisch sind: `target_size` (quadratische Zielgröße in Pixeln; 0 behält die Größe des Quellbilds bei, andernfalls 128 bis 4096), `temperature`, `top_p` und `presence_penalty`. | DYNAMIC_COMBO | Ja | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed-Wert nicht deterministisch. Dieser Parameter verfügt über eine „Steuerung nach Generierung“-Funktionalität (Standard: 0). | INT | Ja | 0 bis 2147483647 |
| `reasoning_effort` | Wie viel Reasoning das Modell vor dem Zeichnen aufwendet. Höhere Stufen verbessern die Detailgenauigkeit und verbrauchen mehr Tokens. Wird nur von den Arrow-2-Modellen verwendet (Standard: "high"). | COMBO | Nein | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `SVG` | Die vektorisierte SVG-Ausgabe. | SVG |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/de.md)

---
**Source fingerprint (SHA-256):** `3f5b97794fa4c2e87d954d98f966d4ef0fddd1c3b1054fba552e282d6ac21c83`
