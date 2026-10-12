# LatentBlend

Der LatentBlend-Node kombiniert zwei latente Samples, indem er sie mithilfe eines angegebenen Blend-Faktors miteinander vermischt. Er nimmt zwei latente Eingaben entgegen und erzeugt eine neue Ausgabe, bei der das erste Sample mit dem Blend-Faktor und das zweite Sample mit dem Kehrwert gewichtet wird. Wenn die Eingabe-Samples unterschiedliche Formen haben, wird das zweite Sample automatisch angepasst, um den Abmessungen des ersten Samples zu entsprechen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `samples1` | Das erste latente Sample, das vermischt werden soll | LATENT | Ja | - |
| `samples2` | Das zweite latente Sample, das vermischt werden soll | LATENT | Ja | - |
| `blend_factor` | Steuert das Mischungsverhältnis zwischen den beiden Samples (Standard: 0.5) | FLOAT | Ja | 0 bis 1 |

**Hinweis:** Wenn `samples1` und `samples2` unterschiedliche Formen haben, wird `samples2` automatisch an die Abmessungen von `samples1` angepasst, wobei bikubische Interpolation mit zentriertem Zuschneiden verwendet wird.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Das vermischte latente Sample, das beide Eingabe-Samples kombiniert | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/de.md)

---
**Source fingerprint (SHA-256):** `a19808c5b606a8c05f2685fcd78d9f08c1ba51613a4029b36cf0ce5305618c2f`
