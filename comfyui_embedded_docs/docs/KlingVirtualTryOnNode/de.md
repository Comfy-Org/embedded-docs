# KlingVirtualTryOnNode

Kling Virtual Try On Node. Geben Sie ein Bild einer Person und ein Bild eines Kleidungsstücks ein, um das Kleidungsstück an der Person anzuprobieren. Sie können mehrere Bilder von Kleidungsstücken zu einem Bild mit weißem Hintergrund zusammenführen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `human_image` | Das Bild der Person, an der die Kleidung anprobiert werden soll | IMAGE | Ja | - |
| `cloth_image` | Das Bild des Kleidungsstücks, das an der Person anprobiert werden soll | IMAGE | Ja | - |
| `model_name` | Das für die virtuelle Anprobe zu verwendende Modell (Standard: "kolors-virtual-try-on-v1") | STRING | Ja | `"kolors-virtual-try-on-v1"` |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output` | Das resultierende Bild, das die Person mit dem anprobierten Kleidungsstück zeigt | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/de.md)

---
**Source fingerprint (SHA-256):** `bf256d8732f4c6acf65838812fc322e48ef886257bbb48c02b0cc6ab5d78dce5`
