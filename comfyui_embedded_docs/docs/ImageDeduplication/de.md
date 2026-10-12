# Doppelte Bilder entfernen

Dieser Node entfernt doppelte oder sehr ähnliche Bilder aus einem Batch. Er funktioniert, indem er für jedes Bild einen perzeptuellen Hash erstellt – einen einfachen numerischen Fingerabdruck, der auf dessen visuellem Inhalt basiert – und diese dann vergleicht. Bilder, deren Hashes ähnlicher sind als ein festgelegter Schwellenwert, gelten als Duplikate und werden herausgefiltert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Der Batch von Bildern, der für die Deduplizierung verarbeitet werden soll. | IMAGE | Ja | - |
| `similarity_threshold` | Ähnlichkeitsschwellenwert (0-1). Höher bedeutet ähnlicher. Bilder oberhalb dieses Schwellenwerts gelten als Duplikate. (Standard: 0.95) | FLOAT | Nein | 0.0 - 1.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Die gefilterte Liste der Bilder mit entfernten Duplikaten. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageDeduplication/de.md)

---
**Source fingerprint (SHA-256):** `d0c40694853c3dd0952d58b920bf735a4626cb2921928bb982ba479dc58fbe53`
