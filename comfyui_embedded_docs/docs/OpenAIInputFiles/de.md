# OpenAI ChatGPT-Eingabedateien

Lädt Eingabedateien für die OpenAI API und formatiert sie. Dieser Node bereitet Text- (.txt) und PDF-Dateien (.pdf) darauf vor, als Kontext-Eingaben für den OpenAI Chat Node verwendet zu werden. Die Dateien werden vom OpenAI-Modell gelesen, wenn eine Antwort generiert wird. Mehrere Nodes vom Typ OpenAI Input Files können verkettet werden, um mehrere Dateien in einer einzigen Nachricht einzubinden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `file` | Eingabedateien, die als Kontext für das Modell eingebunden werden sollen. Derzeit werden nur Text- (.txt) und PDF-Dateien (.pdf) akzeptiert. Die Dateien müssen kleiner als 32MB sein. | COMBO | Ja | Mehrere Optionen verfügbar (alle .txt- und .pdf-Dateien im Eingabeverzeichnis unter 32MB) |
| `OPENAI_INPUT_FILES` | Eine optionale zusätzliche Datei bzw. optionale zusätzliche Dateien, die zusammen mit der von diesem Node geladenen Datei gebündelt werden. Ermöglicht die Verkettung von Eingabedateien, sodass eine einzelne Nachricht mehrere Eingabedateien enthalten kann. | OPENAI_INPUT_FILES | Nein | N/A |

**Dateieinschränkungen:**

- Es werden nur .txt- und .pdf-Dateien unterstützt
- Maximale Dateigröße: 32MB
- Dateien werden aus dem ComfyUI-Eingabeverzeichnis geladen

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `OPENAI_INPUT_FILES` | Formatierte Eingabedateien, die als Kontext für OpenAI-API-Aufrufe verwendet werden können. | OPENAI_INPUT_FILES |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/de.md)

---
**Source fingerprint (SHA-256):** `6554e685184ced830ee27aa96efefc8bb9616bd0504685bdb643c715ebc6dd98`
