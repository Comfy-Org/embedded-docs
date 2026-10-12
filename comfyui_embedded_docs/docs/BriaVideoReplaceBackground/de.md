# Bria Videohintergrund ersetzen

Dieser Node ersetzt den Hintergrund eines Videos durch ein bereitgestelltes Bild oder Video mithilfe der Bria-API. Die Ausgabe behält die Auflösung und Bildrate des Vordergrundvideos bei; ein Hintergrund mit einem abweichenden Seitenverhältnis wird gestreckt, um zu passen. Daher liefern übereinstimmende Seitenverhältnisse unverzerrte Ergebnisse.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Vordergrundvideo, dessen Hintergrund ersetzt wird. | VIDEO | Ja | - |
| `background_image` | Hintergrundbild, das hinter dem Vordergrund komponiert werden soll. Geben Sie entweder ein Hintergrundbild oder ein Hintergrundvideo an, nicht beides. | IMAGE | Nein | - |
| `background_video` | Hintergrundvideo, das hinter dem Vordergrund komponiert werden soll. Geben Sie entweder ein Hintergrundbild oder ein Hintergrundvideo an, nicht beides. | VIDEO | Nein | - |
| `seed` | Der Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Ja | 0 bis 2147483647 |

**Hinweis:** Sie müssen genau eines von `background_image` oder `background_video` angeben – nicht beides und nicht keines. Das Vordergrundvideo und das Hintergrundvideo (falls verwendet) dürfen jeweils höchstens 60 Sekunden lang sein. Wenn `background_image` verwendet wird, wird dessen Alphakanal vor der Verarbeitung entfernt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `video` | Das resultierende Video mit ersetztem Hintergrund, kodiert als MP4 (H.264). | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/de.md)

---
**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`
