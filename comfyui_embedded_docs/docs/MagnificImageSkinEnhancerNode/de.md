# Magnific Image Hautverbesserung

Der Node „Magnific Image Skin Enhancer“ wendet spezialisierte KI-Verarbeitung auf Porträtbilder an, um das Hautbild zu verbessern. Er bietet drei verschiedene Modi für unterschiedliche Verbesserungsziele: creative für künstlerische Effekte, faithful zur Bewahrung des ursprünglichen Aussehens und flexible für gezielte Verbesserungen wie Beleuchtung oder Realismus. Der Node lädt das Bild zur Verarbeitung auf eine externe API hoch und gibt das verbesserte Ergebnis zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das zu verbessernde Porträtbild. | IMAGE | Ja | - |
| `sharpen` | Intensität der Schärfung (Standard: 0). | INT | Nein | 0 bis 100 |
| `smart_grain` | Intensität der intelligenten Körnung (Standard: 2). | INT | Nein | 0 bis 100 |
| `mode` | Der zu verwendende Verarbeitungsmodus. `"creative"` dient der künstlerischen Verbesserung, `"faithful"` der Bewahrung des ursprünglichen Aussehens und `"flexible"` der gezielten Optimierung. | COMBO | Ja | `"creative"`<br>`"faithful"`<br>`"flexible"` |
| `skin_detail` | Grad der Hautdetailverbesserung. Diese Eingabe ist nur verfügbar, wenn `mode` auf `"faithful"` gesetzt ist (Standard: 80). | INT | Nein | 0 bis 100 |
| `optimized_for` | Ziel der Verbesserungsoptimierung. Diese Eingabe ist nur verfügbar, wenn `mode` auf `"flexible"` gesetzt ist. | COMBO | Nein | `"enhance_skin"`<br>`"improve_lighting"`<br>`"enhance_everything"`<br>`"transform_to_real"`<br>`"no_make_up"` |

**Einschränkungen:**

* Der Node akzeptiert genau ein Eingabebild.
* Das Eingabebild muss eine Mindesthöhe und -breite von 160 Pixeln haben.
* Das Seitenverhältnis des Eingabebilds muss zwischen 1:3 und 3:1 liegen (nicht strikte Validierung).
* Der Parameter `skin_detail` ist nur aktiv, wenn `mode` auf `"faithful"` gesetzt ist.
* Der Parameter `optimized_for` ist nur aktiv, wenn `mode` auf `"flexible"` gesetzt ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das verbesserte Porträtbild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageSkinEnhancerNode/de.md)

---
**Source fingerprint (SHA-256):** `2430cc0fb1d2042a8eda78f7f5a5794fa6b4e555d3957616ae6891374b556a76`
