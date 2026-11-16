# Bria Bildhintergrund entfernen

Dieser Node entfernt den Hintergrund aus einem Bild mithilfe des Dienstes Bria RMBG 2.0 oder RMBG 3.0. Er sendet das Bild zur Verarbeitung an eine externe API und gibt das Ergebnis mit entferntem Hintergrund zurück.

## Eingaben

Der Selektor `moderation` blendet zusätzliche Moderationsoptionen ein, wenn er auf `"true"` gesetzt ist.

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, aus dem der Hintergrund entfernt wird. | IMAGE | Ja | - |
| `moderation` | Moderationseinstellungen. Wenn sie auf `"true"` gesetzt sind, werden zusätzliche Moderationsoptionen verfügbar. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |
| `seed` | `seed` steuert, ob der Node erneut ausgeführt werden soll; dasselbe Bild liefert unabhängig vom Seed immer dasselbe Ergebnis. Standard: `0`. | INT | Ja | 0 bis 2147483647 |
| `model` | Modell zur Hintergrundentfernung. `"RMBG2"` ist der Standard; `"RMBG3"` verwendet das neuere Modell Bria RMBG 3.0. | COMBO | Nein | `"RMBG2"`<br>`"RMBG3"` |

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
**Source fingerprint (SHA-256):** `82f7ec2ac2d1579a3da009b464bce7c56fa2d7b1f599744d6158177ecd462cb2`
