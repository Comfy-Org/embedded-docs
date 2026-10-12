# GeminiInputFiles

Lädt Eingabedateien und formatiert sie für die Verwendung mit der Gemini API. Dieser Node ermöglicht es Benutzern, Text- (.txt) und PDF-Dateien (.pdf) als Eingabekontext für das Gemini-Modell einzubinden. Dateien werden in das von der API benötigte Format konvertiert und können verkettet werden, um mehrere Dateien in einer einzigen Anfrage einzubinden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `file` | Eingabedateien, die als Kontext für das Modell eingebunden werden sollen. Akzeptiert derzeit nur Text- (.txt) und PDF-Dateien (.pdf). Die Dateien müssen kleiner als die maximale Größenbeschränkung für Eingabedateien (20 MB) sein. | COMBO | Ja | Mehrere Optionen verfügbar (nur .txt- und .pdf-Dateien unter 20 MB) |
| `GEMINI_INPUT_FILES` | Optionale zusätzliche Datei(en), die zusammen mit der von diesem Node geladenen Datei gebündelt werden. Ermöglicht die Verkettung von Eingabedateien, sodass eine einzelne Nachricht mehrere Eingabedateien enthalten kann. | GEMINI_INPUT_FILES | Nein | N/A |

**Hinweis:** Der Parameter `file` zeigt nur Text- (.txt) und PDF-Dateien (.pdf) an, die kleiner als 20 MB sind. Dateien werden automatisch gefiltert und nach Namen sortiert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `GEMINI_INPUT_FILES` | Formatierte Dateidaten, bereit zur Verwendung mit Gemini-LLM-Nodes, die den geladenen Dateiinhalt im passenden API-Format enthalten. | GEMINI_INPUT_FILES |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiInputFiles/de.md)

---
**Source fingerprint (SHA-256):** `1c80a87746c7ac73379f5c1e2d5c4d22f0fc44d3241fafb0297e087e436df7d6`
