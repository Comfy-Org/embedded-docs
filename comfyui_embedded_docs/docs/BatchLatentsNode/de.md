# BatchLatentsNode

Der Node Batch Latents kombiniert mehrere Latent-Eingaben zu einem einzigen Batch. Er nimmt eine variable Anzahl von Latent-Stichproben entgegen und führt sie entlang der Batch-Dimension zusammen, damit sie von nachfolgenden Nodes gemeinsam verarbeitet werden können. Der Node führt außerdem die Batch-Index-Metadaten aller Eingaben in der kombinierten Ausgabe zusammen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `latents` | Ein Satz von Latent-Stichproben, die zu einem einzigen Batch kombiniert werden sollen. Sie müssen mindestens ein Latent angeben, und Sie können bis zu 50 hinzufügen. Der Node erstellt automatisch Eingabe-Slots (`latent_1`, `latent_2` usw.), wenn Sie weitere Latents verbinden. | LATENT | Ja | 1 bis 50 Eingaben |

**Hinweis:** Sie müssen mindestens eine Latent-Eingabe angeben, damit der Node funktioniert. Der Node erstellt automatisch Eingabe-Slots, wenn Sie weitere Latents verbinden, bis zu einem Maximum von 50. Jedes Eingabe-Latent wird umgeformt, um der Sample-Form des ersten Latents zu entsprechen, bevor es kombiniert wird, und jedem Latent ohne Batch-Index-Metadaten wird ein fortlaufender Batch-Index zugewiesen. Die Eingabe-Latents werden entlang der Batch-Dimension zusammengefügt, um das kombinierte Ergebnis zu erzeugen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Eine einzelne Latent-Ausgabe, die alle Eingabe-Latents zu einem Batch zusammengefasst enthält, zusammen mit ihren zusammengeführten Batch-Index-Metadaten. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/de.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`
