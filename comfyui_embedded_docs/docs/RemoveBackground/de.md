# Hintergrund entfernen

## Übersicht

Der Node „Remove Background“ erzeugt eine Vordergrundmaske, die das Hauptmotiv vom Hintergrund eines Eingabebildes trennt. Er verwendet ein Modell zur Hintergrundentfernung, um das Bild zu analysieren und eine Maske zu erzeugen, die die Vordergrundelemente hervorhebt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Wertebereich |
|-----------|--------------|----------|--------------|--------------|
| `bg_removal_model` | Modell zur Hintergrundentfernung, das zur Erzeugung der Maske verwendet wird | BACKGROUND_REMOVAL_MODEL | Ja | N/A |
| `image` | Eingabebild, aus dem der Hintergrund entfernt werden soll | IMAGE | Ja | N/A |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `mask` | Erzeugte Vordergrundmaske | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/de.md)

---
**Source fingerprint (SHA-256):** `75b415acedaeaa1a694aeba2e4b0367524c6878e3e4a1f48b2a62898c68109f9`
