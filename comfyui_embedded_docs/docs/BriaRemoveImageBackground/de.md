# BriaRemoveImageBackground

Dieser Node entfernt den Hintergrund aus einem Bild mithilfe des Dienstes Bria RMBG 2.0. Er sendet das Bild zur Verarbeitung an eine externe API und gibt das Ergebnis mit entferntem Hintergrund zurück.

## Eingaben

Der Selektor `moderation` blendet zusätzliche Moderationsoptionen ein, wenn er auf `"true"` gesetzt ist.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, aus dem der Hintergrund entfernt wird. | IMAGE | Ja | - |
| `moderation` | Moderationseinstellungen. Wenn sie auf `"true"` gesetzt sind, werden zusätzliche Moderationsoptionen verfügbar. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |
| `seed` | `seed` steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. Standard: `0`. | INT | Ja | 0 bis 2147483647 |

### Eingaben für Moderation „true“

Diese Parameter werden nur angezeigt, wenn `moderation` auf `"true"` gesetzt ist. Die Option `"false"` fügt keine zusätzlichen Eingaben hinzu.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Aktiviert die Moderation visueller Inhalte für das Eingabebild. Standard: `False`. | BOOLEAN | Nein | - |
| `visual_output_moderation` | Aktiviert die Moderation visueller Inhalte für das Ausgabebild. Standard: `True`. | BOOLEAN | Nein | - |

**Hinweis:** Die Parameter `visual_input_moderation` und `visual_output_moderation` hängen vom Parameter `moderation` ab. Sie sind nur aktiv, wenn `moderation` auf `"true"` gesetzt ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das verarbeitete Bild mit entferntem Hintergrund. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/de.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
