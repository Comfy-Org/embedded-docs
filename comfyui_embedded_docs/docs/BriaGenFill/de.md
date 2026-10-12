# Bria Generatives Füllen

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das zu bearbeitende Eingabebild. | IMAGE | Ja | - |
| `mask` | Weiße Bereiche werden mit generiertem Inhalt gefüllt, schwarze Bereiche bleiben erhalten. Die Maske wird vor dem Senden mit einem Schwellenwert von 50 % binarisiert: Nur Bereiche, die mit mehr als 50 % Deckkraft markiert sind, gelten als weiß. Muss dasselbe Seitenverhältnis wie das Bild haben. | MASK | Ja | - |
| `prompt` | Beschreibung dessen, was innerhalb des maskierten Bereichs generiert werden soll. Muss mindestens 1 Zeichen enthalten. (Standard: "") | STRING | Ja | - |
| `negative_prompt` | Ein Prompt, der Inhalte beschreibt, die im generierten Ergebnis vermieden werden sollen. Wenn er leer gelassen wird, wird er nicht an die API gesendet. (Standard: "") | STRING | Ja | - |
| `refine_prompt` | Den Prompt automatisch für bessere Ergebnisse anpassen; deaktivieren, um den Prompt genau wie geschrieben zu verwenden. (Standard: true) | BOOLEAN | Ja | true<br>false |
| `seed` | Seed für den Generierungsprozess. (Standard: 42) | INT | Ja | 1 bis 2147483647 |
| `moderation` | Moderationseinstellungen. Wenn auf "true" gesetzt, werden die untenstehenden Moderationsoptionen angewendet. (Standard: "false") | DYNAMIC_COMBO | Ja | "false"<br>"true" |

### Moderations-Eingaben (wenn `moderation` = "true")

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Wendet Inhaltsmoderation auf den Prompt an. (Standard: false) | BOOLEAN | Nein | true<br>false |
| `visual_input_moderation` | Wendet Inhaltsmoderation auf das Eingabebild an. (Standard: false) | BOOLEAN | Nein | true<br>false |
| `visual_output_moderation` | Wendet Inhaltsmoderation auf das Ausgabebild an. (Standard: false) | BOOLEAN | Nein | true<br>false |

**Hinweis:** Der `prompt` darf nicht leer sein. Die `mask` muss dasselbe Seitenverhältnis wie das `image` haben. Die Maske wird bei 50 % Deckkraft binarisiert, sodass Bereiche, die mit weniger als der Hälfte der Deckkraft markiert sind, ignoriert werden; wenn die Maske nach der Binarisierung keine weißen Bereiche enthält, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das resultierende Bild, bei dem der maskierte Bereich mit dem generierten Inhalt gefüllt ist. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/de.md)

---
**Source fingerprint (SHA-256):** `b23e29d4457f859181d68eaeb4b0238de28f4b18932d68438fa2954739cdc66a`
