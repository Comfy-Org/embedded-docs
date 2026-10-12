# LoadBackgroundRemovalModel

Lädt ein Hintergrundentfernungsmodell aus einer Datei. Dieser Node bereitet das Modell so vor, dass es von anderen Nodes verwendet werden kann, um Hintergründe aus Bildern zu entfernen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | Das Modell, das zum Entfernen von Hintergründen aus Bildern verwendet wird. Wählen Sie aus der Liste der verfügbaren Modelldateien zur Hintergrundentfernung aus. | COMBO | Ja | Liste der verfügbaren Modelldateien zur Hintergrundentfernung (alphabetisch sortiert) |

Hinweis: Wenn die ausgewählte Datei kein gültiges Hintergrundentfernungsmodell enthält, löst der Node einen RuntimeError aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `bg_model` | Das geladene Hintergrundentfernungsmodell, bereit zur Verwendung durch andere Nodes zur Verarbeitung von Bildern. | BACKGROUND_REMOVAL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/de.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
