# BriaEraser

Bria Eraser entfernt Objekte oder Bereiche aus einem Bild mithilfe der Bria API. Sie stellen ein Bild und eine Maske bereit, die die zu entfernenden Regionen umreißt; der Node lädt beide zu Bria hoch, führt den Erase-Job aus, wartet auf dessen Abschluss und gibt das bearbeitete Bild mit den entfernten maskierten Bereichen zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das die zu entfernenden Objekte oder Bereiche enthält. | IMAGE | Ja | - |
| `mask` | Weiße Bereiche werden entfernt, schwarze Bereiche bleiben erhalten. Die Maske wird vor dem Senden binarisiert, mit einem Schwellenwert von 50 %: Nur Bereiche, die mit mehr als 50 % Deckkraft gemalt wurden, gelten als weiß. Muss dasselbe Seitenverhältnis wie das Bild haben. | MASK | Ja | - |
| `mask_type` | Der Quelltyp der Maske. "manual" ist für handgezeichnete oder Pinsel-Masken; "automatic" ist für Masken, die von Segmentierungsmodellen wie SAM erzeugt wurden. | COMBO | Ja | "manual"<br>"automatic" |
| `moderation` | Moderationseinstellungen. Auf "true" setzen, um visuelle Inhaltsmoderation für das/die Eingabe- und/oder Ausgabebild(er) zu aktivieren. | DYNAMIC_COMBO | Ja | "false"<br>"true" |

Wenn `moderation` auf "true" gesetzt ist, werden zwei zusätzliche boolesche Einstellungen verfügbar:

- `visual_input_moderation` — Wendet visuelle Inhaltsmoderation auf das Eingabebild an (Standard: false)
- `visual_output_moderation` — Wendet visuelle Inhaltsmoderation auf das Ausgabebild an (Standard: false)

Hinweis: Die Maske muss dem Seitenverhältnis des Bildes entsprechen, andernfalls schlägt die Anfrage fehl. Die Maske wird vor dem Senden an die API in eine binäre (schwarz-weiße) Maske umgewandelt: Bereiche, die mit weniger als halber Deckkraft gemalt wurden, werden ignoriert, und teilweise bemalte Bereiche werden als weiß behandelt und entfernt. Die Maske muss mindestens einen weißen Bereich enthalten; eine leere Maske führt dazu, dass die Anfrage fehlschlägt, da nichts zu entfernen ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das bearbeitete Bild, bei dem die maskierten Objekte oder Bereiche entfernt wurden. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/de.md)

---
**Source fingerprint (SHA-256):** `5528b7a3cb4d0a7b1b28acbc642a8bd21e2eacf5aa225403d6344c29f0cdba80`
