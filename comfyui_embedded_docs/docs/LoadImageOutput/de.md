# Bild laden (aus Ausgaben)

Der LoadImageOutput-Node lädt Bilder aus dem Ausgabeordner. Wenn Sie auf die Aktualisierungsschaltfläche klicken, wird die Liste der verfügbaren Bilder aktualisiert und automatisch das erste ausgewählt, was die Iteration durch Ihre generierten Bilder erleichtert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Lädt ein Bild aus dem Ausgabeordner. Enthält eine Upload-Option und eine Aktualisierungsschaltfläche zum Aktualisieren der Bildliste. Wenn die Aktualisierungsschaltfläche angeklickt wird, aktualisiert der Node die Bildliste und wählt automatisch das erste Bild aus, was eine einfache Iteration ermöglicht. | COMBO | Ja | Mehrere Optionen verfügbar |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das geladene Bild aus dem Ausgabeordner | IMAGE |
| `mask` | Die dem geladenen Bild zugeordnete Maske | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/de.md)

---
**Source fingerprint (SHA-256):** `d1de0140765c9d5dd393715faa84dc5c3f0e49117391b8823a51b176bcb568d8`
