# Bilder bündeln

Der Node „Batch Images“ kombiniert mehrere einzelne Bilder zu einem einzigen Batch. Er nimmt eine variable Anzahl von Bildeingaben entgegen und gibt sie als einen gebatchten Bildtensor aus, sodass sie in nachfolgenden Nodes gemeinsam verarbeitet werden können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Eine dynamische Liste von Bildeingaben. Sie können zwischen 2 und 50 Bilder hinzufügen, die zu einem Batch kombiniert werden. Die Benutzeroberfläche des Nodes ermöglicht es Ihnen, bei Bedarf weitere Bildeingabe-Slots hinzuzufügen. | IMAGE | Ja | 2 bis 50 Eingaben |

**Hinweis:** Sie müssen mindestens zwei Bilder verbinden, damit der Node funktioniert. Der erste Eingabe-Slot ist immer erforderlich, und Sie können weitere über die Schaltfläche „+“ hinzufügen, die in der Benutzeroberfläche des Nodes angezeigt wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Ein einzelner gebatchter Bildtensor, der alle Eingabebilder zusammengestapelt enthält. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesNode/de.md)

---
**Source fingerprint (SHA-256):** `f756fb15760cd2518da9c3f88281d3ab3361b4c2b4820fe2be152e4db1cf102c`
