# Bria Foto restaurieren

Dieser Node repariert alte oder beschädigte Fotografien über die Bria API. Er entfernt Korn, Kratzer und Unschärfe, neutralisiert altersbedingte Farbstiche, kann Kartonpassepartouts und Studioränder wegschneiden und Gesichter neu zeichnen. Das Ergebnis wird mit etwa 1 Megapixel neu gerendert, daher ist es nicht pixelgenau am Eingang ausgerichtet.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `image` | Das zu reparierende Foto. Der Alphakanal wird vor dem Hochladen verworfen. | IMAGE | Ja | - |
| `moderation` | Moderationseinstellungen für die Anfrage. Die Auswahl von `"true"` blendet zwei zusätzliche boolesche Schalter ein; die Auswahl von `"false"` sendet keine Moderations-Flags. Standard: `"false"`. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |

### Moderationseingaben

Diese Eingaben erscheinen nur, wenn `moderation` auf `"true"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `visual_input_moderation` | Aktiviert die Moderation visueller Inhalte für das Eingabebild. Standard: false. | BOOLEAN | Nein | true<br>false |
| `visual_output_moderation` | Aktiviert die Moderation visueller Inhalte für das Ausgabebild. Standard: false. | BOOLEAN | Nein | true<br>false |

**Hinweis:** Der Node rendert das gesamte Bild mit etwa 1 Megapixel neu, daher ist das Ergebnis nicht pixelgenau am Eingang ausgerichtet. Verwenden Sie den Bria Increase Resolution-Node, um das Bild zu vergrößern, anstatt diesen Node zu verwenden.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `IMAGE` | Das von Bria zurückgegebene reparierte Foto. | IMAGE |
| `structured_prompt` | Strukturierte Beschreibung des bearbeiteten Bildes für eine nachfolgende Bearbeitung mit Bria FIBO Image Edit. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRestorePhoto/de.md)

---
**Source fingerprint (SHA-256):** `387ec3e049464f185e27f79d160ade2a4170ab238853064c008892d84523fa68`
