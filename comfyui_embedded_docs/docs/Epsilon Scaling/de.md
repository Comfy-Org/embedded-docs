# Epsilon-Skalierung

Dieser Node implementiert die Epsilon-Skalierungsmethode aus dem Forschungspapier „Elucidating the Exposure Bias in Diffusion Models“ (arxiv.org/2308.15321v6). Sie funktioniert, indem das vorhergesagte Rauschen während des Sampling-Prozesses skaliert wird, um Exposure-Bias zu reduzieren, was zu einer verbesserten Qualität der generierten Bilder führen kann. Diese Implementierung verwendet den im Forschungspapier empfohlenen „uniform schedule“ aufgrund seiner Praktikabilität und Wirksamkeit.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das der Epsilon-Skalierungs-Patch angewendet wird. | MODEL | Ja | - |
| `scaling_factor` | Der Faktor, um den das vorhergesagte Rauschen skaliert wird. Ein Wert größer als 1.0 reduziert das Rauschen, während ein Wert kleiner als 1.0 es erhöht (Standard: 1.005). Dies ist ein erweiterter Parameter. | FLOAT | Nein | 0.5 - 1.5 (Schrittweite: 0.001) |

Hinweis: Wenn `scaling_factor` auf 0 gesetzt wird, ersetzt der Node ihn automatisch durch einen sehr kleinen Wert (1e-9), um eine Division durch null zu verhindern. Der minimale Wert der Benutzeroberfläche von 0.5 verhindert normalerweise, dass dies geschieht.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Eine gepatchte Version des Eingabemodells, auf dessen Sampling-Prozess die Epsilon-Skalierungsfunktion angewendet wurde. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/de.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
