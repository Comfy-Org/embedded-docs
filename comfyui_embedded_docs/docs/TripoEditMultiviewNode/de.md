# Tripo: Multiview bearbeiten

Bearbeitet die Ansichten eines Ergebnisses von Tripo: Image to Multiview mithilfe einer separaten Textanweisung für jede Ansicht. Ansichten ohne Anweisung bleiben unverändert. Die bearbeiteten Bilder sind dafür gedacht, mit Tripo: Multiview to Model verbunden zu werden, um ein 3D-Modell zu erstellen; ein bearbeitetes Multiview-Set kann nicht erneut bearbeitet werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `multiview_task_id` | Task-ID des Ergebnisses von Tripo: Image to Multiview, dessen Ansichten bearbeitet werden. Muss vom Node Tripo: Image to Multiview stammen. | MULTIVIEW_TASK_ID | Ja | Task-ID |
| `front_prompt` | Textanweisung, die die auf die Vorderansicht anzuwendende Bearbeitung beschreibt. Wenn leer, bleibt die Vorderansicht unverändert. Standardwert: leerer String. | STRING | Nein | Mehrzeiliger Text |
| `left_prompt` | Textanweisung, die die auf die linke Ansicht anzuwendende Bearbeitung beschreibt. Wenn leer, bleibt die linke Ansicht unverändert. Standardwert: leerer String. | STRING | Nein | Mehrzeiliger Text |
| `back_prompt` | Textanweisung, die die auf die Rückansicht anzuwendende Bearbeitung beschreibt. Wenn leer, bleibt die Rückansicht unverändert. Standardwert: leerer String. | STRING | Nein | Mehrzeiliger Text |
| `right_prompt` | Textanweisung, die die auf die rechte Ansicht anzuwendende Bearbeitung beschreibt. Wenn leer, bleibt die rechte Ansicht unverändert. Standardwert: leerer String. | STRING | Nein | Mehrzeiliger Text |

Hinweis: Mindestens einer der vier Prompts (`front_prompt`, `left_prompt`, `back_prompt`, `right_prompt`) muss einen nicht leeren Text enthalten; Text, der nur aus Leerzeichen besteht, wird als leer behandelt, und wenn alle Prompts leer sind, löst der Node einen Fehler aus.

Hinweis: Die Kosten betragen ungefähr 0,05 USD pro Ansicht mit einer Bearbeitungsanweisung.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `front` | Bearbeitetes Bild der Vorderansicht. | IMAGE |
| `left` | Bearbeitetes Bild der linken Ansicht. | IMAGE |
| `back` | Bearbeitetes Bild der Rückansicht. | IMAGE |
| `right` | Bearbeitetes Bild der rechten Ansicht. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/de.md)

---
**Source fingerprint (SHA-256):** `db8b0a3ffe4332fcbcaac4da0d7b07217d01d2f05526750540f6036293e013ab`
