# KlingImageGenerationNode

Der Kling Image Generation Node generiert Bilder aus Text-Prompts mit der Option, ein Referenzbild zur Orientierung zu verwenden. Er erstellt ein oder mehrere Bilder basierend auf Ihrer Textbeschreibung und den Referenzeinstellungen und gibt dann die generierten Bilder als Ausgabe zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Positiver Text-Prompt. Erforderlich, muss zwischen 1 und 500 Zeichen lang sein. | STRING | Ja | Maximal 500 Zeichen |
| `negative_prompt` | Negativer Text-Prompt. | STRING | Ja | Maximal 500 Zeichen |
| `image_type` | Auswahl des Bildreferenztyps (erweitert). Erforderlich, wenn ein Referenzbild bereitgestellt wird. | COMBO | Ja | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | Referenzintensität für vom Benutzer hochgeladene Bilder (Standard: 0.5, erweitert) | FLOAT | Ja | 0.0 - 1.0 |
| `human_fidelity` | Ähnlichkeit der Subjektreferenz (Standard: 0.45, erweitert) | FLOAT | Ja | 0.0 - 1.0 |
| `model_name` | Modellauswahl für die Bildgenerierung (Standard: "kling-v3") | COMBO | Ja | `"kling-v3"` |
| `aspect_ratio` | Seitenverhältnis für generierte Bilder (Standard: "16:9") | COMBO | Ja | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Anzahl der generierten Bilder (Standard: 1) | INT | Ja | 1 - 9 |
| `image` | Optionales Referenzbild | IMAGE | Nein | - |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0) | INT | Nein | 0 - 2147483647 |

**Parametereinschränkungen:**

- Der Parameter `image` ist optional. Wenn ein Referenzbild bereitgestellt wird, bestimmt der Parameter `image_type`, ob die Referenz als Subjektreferenz oder Stilreferenz verwendet wird.
- Wenn kein Referenzbild bereitgestellt wird, haben die referenzbezogenen Einstellungen (`image_type`, `image_fidelity`, `human_fidelity`) keine Auswirkung auf das Ergebnis.
- `prompt` und `negative_prompt` haben eine maximale Länge von 500 Zeichen.
- Der Parameter `seed` ist optional und garantiert keine deterministischen Ergebnisse.
- Der Parameter `n` steuert, wie viele Bilder erzeugt werden, und bestimmt auch den Preis der Anfrage.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Generierte(s) Bild(er) basierend auf den Eingabeparametern. Wenn `n` größer als 1 ist, werden mehrere Bilder als Batch zurückgegeben. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/de.md)

---
**Source fingerprint (SHA-256):** `fd344519346f63ac03975b93f03725749ed9697245d6dfa2378884c59a5325cd`
