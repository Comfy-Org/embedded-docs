# Maskenvorschau

Der MaskPreview-Node zeigt eine visuelle Vorschau der Maskendaten direkt in der ComfyUI-Oberfläche an, ohne sie im Ausgabeverzeichnis zu speichern. So können Sie die Maske an jedem Punkt Ihres Workflows prüfen; gleichzeitig wird die Maske unverändert durch den Node geleitet, sodass sie weiterhin nachgelagert verwendet werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mask` | Die Maskendaten, die in der Vorschau angezeigt werden sollen | MASK | Ja | - |
| `filename_prefix` | Dateinamenpräfix für die Vorschau (Standard: "ComfyUI") | STRING | Nein | - |
| `prompt` | Prompt-Informationen für Metadaten (automatisch bereitgestellt) | PROMPT | Nein | - |
| `extra_pnginfo` | Zusätzliche PNG-Informationen für Metadaten (automatisch bereitgestellt) | EXTRA_PNGINFO | Nein | - |

Nur `mask` ist eine sichtbare Eingabe, die verbunden werden muss. Die Parameter `filename_prefix`, `prompt` und `extra_pnginfo` werden vom System bereitgestellt: `filename_prefix` fällt auf seinen Standardwert zurück, während `prompt` und `extra_pnginfo` ausgeblendet sind und automatisch von der ComfyUI-Laufzeit bereitgestellt werden.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mask` | Dieselben Maskendaten, die in der Vorschau angezeigt wurden, unverändert zurückgegeben, sodass sie an anderer Stelle im Workflow verwendet werden können | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/de.md)

---
**Source fingerprint (SHA-256):** `fb7abe8cb6b5ac8a6a38e88ef90a146d16caf41d24c5de95309a94bc3c371d75`
