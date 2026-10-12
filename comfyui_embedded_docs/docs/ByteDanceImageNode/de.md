# ByteDanceImageNode

Der ByteDance Image-Node erzeugt Bilder mithilfe von ByteDance-Modellen über eine API auf Basis von Text-Prompts. Er ermöglicht Ihnen, ein Modell auszuwählen, Bildabmessungen festzulegen und verschiedene Generierungsparameter wie Seed und Guidance Scale zu steuern. Der Node verbindet sich mit dem Bilderzeugungsdienst von ByteDance und gibt das erstellte Bild zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Das ByteDance-Modell, das für die Bilderzeugung verwendet werden soll. Derzeit ist nur eine Modelloption verfügbar. | STRING | Ja | `"seedream-3-0-t2i-250415"` |
| `prompt` | Der Text-Prompt, der zur Generierung des Bildes verwendet wird. Muss nach dem Entfernen von Leerzeichen mindestens 1 Zeichen lang sein. | STRING | Ja | - |
| `size_preset` | Wählen Sie eine empfohlene Größe. Wählen Sie Custom, um die untenstehende Breite und Höhe zu verwenden. Verfügbare Voreinstellungen werden durch die Liste `RECOMMENDED_PRESETS` definiert. | STRING | Ja | Siehe Beschreibung |
| `width` | Benutzerdefinierte Breite für das Bild. Dieser Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 1024. | INT | Ja | 512 bis 2048 (Schritt 64) |
| `height` | Benutzerdefinierte Höhe für das Bild. Dieser Wert wird nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Standard: 1024. | INT | Ja | 512 bis 2048 (Schritt 64) |
| `seed` | Seed für die Generierung. Standard: 0. | INT | Nein | 0 bis 2147483647 (Schritt 1) |
| `guidance_scale` | Ein höherer Wert bewirkt, dass das Bild dem Prompt genauer folgt. Standard: 2.5. | FLOAT | Nein | 1.0 bis 10.0 (Schritt 0.01) |
| `watermark` | Ob dem Bild ein Wasserzeichen „AI generated“ hinzugefügt werden soll. Standard: False. Dies ist ein erweiterter Parameter. | BOOLEAN | Nein | True / False |

**Hinweis zu Größenparametern:** Die Parameter `width` und `height` werden nur verwendet, wenn `size_preset` auf `Custom` gesetzt ist. Wenn eine voreingestellte Größe ausgewählt ist, überschreiben die Abmessungen der Voreinstellung die benutzerdefinierten Werte für Breite und Höhe. Sowohl Breite als auch Höhe müssen bei benutzerdefinierten Abmessungen zwischen 512 und 2048 Pixeln liegen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `IMAGE` | Das generierte Bild, das von der ByteDance-API als Tensor zurückgegeben wird. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/de.md)

---
**Source fingerprint (SHA-256):** `0b40c75ca43ef3cccbc644e64822f701a0d772decacd813c58d7d5ac60c230a1`
