# Recraft Hintergrund entfernen

Dieser Node entfernt den Hintergrund aus Bildern mithilfe des Recraft-API-Dienstes. Er verarbeitet jedes Bild im Eingabe-Batch einzeln und gibt sowohl die verarbeiteten Bilder mit transparentem Hintergrund als auch entsprechende Alpha-Masken zurück, die die entfernten Hintergrundbereiche anzeigen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `image` | Das oder die Eingabebilder, die für die Hintergrundentfernung verarbeitet werden sollen. Jedes Bild im Batch wird einzeln verarbeitet. | IMAGE | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `image` | Verarbeitete Bilder mit transparentem Hintergrund (RGBA-Format) | IMAGE |
| `mask` | Alpha-Kanal-Masken, die die entfernten Hintergrundbereiche anzeigen, im B,H,W-Format | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/de.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`
