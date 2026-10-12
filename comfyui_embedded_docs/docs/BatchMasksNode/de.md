# Masken bündeln

Der Node „Batch Masks“ kombiniert mehrere einzelne Maskeneingaben zu einem einzigen Batch. Er nimmt eine variable Anzahl von Maskeneingaben entgegen und gibt sie als einen einzelnen gebatchten Maskentensor aus, wodurch die Batch-Verarbeitung von Masken in nachfolgenden Nodes ermöglicht wird. Wenn die Eingabemasken unterschiedliche Größen haben, werden sie automatisch an die Abmessungen der ersten Maske angepasst.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `mask` | Die Maskeneingaben, die zu einem Batch kombiniert werden sollen. Mindestens eine Maske ist erforderlich. Sie können insgesamt bis zu 50 Masken hinzufügen, indem Sie auf die Schaltfläche „+“ am Node klicken. Wenn Masken unterschiedliche Größen haben, werden sie automatisch an die Abmessungen der ersten Maske angepasst. | MASK | Ja | 1 bis 50 Masken |

**Hinweis:** Dieser Node verwendet eine Auto-Grow-Eingabevorlage. Sie müssen mindestens eine Maske verbinden. Sie können bis zu 49 weitere Maskeneingaben für insgesamt 50 Masken hinzufügen. Alle verbundenen Masken werden zu einem einzigen Batch kombiniert. Wenn Masken unterschiedliche Höhen oder Breiten haben, werden sie automatisch mithilfe bilinearer Interpolation an die Abmessungen der ersten Maske angepasst.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Eine einzelne gebatchte Maske, die alle Eingabemasken zusammengestapelt enthält. Wenn keine Masken bereitgestellt werden, wird None zurückgegeben. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/de.md)

---
**Source fingerprint (SHA-256):** `7e9bc4be72c7fa8fceab2cf167c72b7e1ff858c0281d977f2ad3ab433d9d58d6`
