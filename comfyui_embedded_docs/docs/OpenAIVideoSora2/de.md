# OpenAIVideoSora2

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das OpenAI-Sora-Modell, das für die Videogenerierung verwendet werden soll (Standard: "sora-2") | COMBO | Ja | "sora-2"<br>"sora-2-pro" |
| `prompt` | Leittext; kann leer sein, wenn ein Eingabebild vorhanden ist (Standard: leerer String) | STRING | Ja | - |
| `size` | Die Auflösung des generierten Videos (Standard: "1280x720") | COMBO | Ja | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duration` | Die Dauer des generierten Videos in Sekunden (Standard: 8) | COMBO | Ja | 4<br>8<br>12 |
| `image` | Optionales Referenzbild als Eingabe für die Videogenerierung; es wird nur ein einzelnes Bild unterstützt | IMAGE | Nein | - |
| `seed` | Seed, der bestimmt, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0) | INT | Nein | 0 bis 2147483647 |

**Einschränkungen und Limitierungen:**

- Das Modell "sora-2" unterstützt nur die Größen "720x1280" und "1280x720"; die Auswahl von "1024x1792" oder "1792x1024" mit "sora-2" löst einen Fehler aus. Die größeren Größen sind nur mit "sora-2-pro" verfügbar.
- Wenn ein Bild verbunden ist, muss es genau ein Bild enthalten; das Verbinden von mehr als einem Bild löst einen Fehler aus.
- Die Ergebnisse sind unabhängig vom Seed-Wert nicht deterministisch.
- Die angezeigte Preisschätzung hängt von den ausgewählten Werten für `model`, `size` und `duration` ab.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Das von OpenAI Sora generierte Video | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/de.md)

---
**Source fingerprint (SHA-256):** `d19eb6b65d7f712278828e4b1f7105068cc5e7cb72813b7549ab24520e7719fc`
