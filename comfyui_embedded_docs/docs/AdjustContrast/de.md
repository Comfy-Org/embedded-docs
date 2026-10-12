# Kontrast anpassen

Der Node „Adjust Contrast“ passt den Kontrast eines Eingabebilds an, indem er die Differenz zwischen hellen und dunklen Bereichen um den Mittelpunkt des Farbbereichs skaliert. Ein Faktor von 1.0 lässt das Bild unverändert, Werte unter 1.0 verringern den Kontrast, Werte über 1.0 erhöhen den Kontrast.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Eingabebild, dessen Kontrast angepasst werden soll. | IMAGE | Ja | - |
| `factor` | Kontrastfaktor. 1.0 = keine Änderung, <1.0 = weniger Kontrast, >1.0 = mehr Kontrast. (Standard: 1.0) | FLOAT | Nein | 0.0 - 2.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das resultierende Bild mit angepasstem Kontrast. Pixelwerte werden auf den Bereich 0.0–1.0 begrenzt. Wenn das Eingabebild einen Alphakanal besitzt, bleibt dieser unverändert erhalten. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/de.md)

---
**Source fingerprint (SHA-256):** `489f840cc3d98339a5cf7b55e9179c60878c58b2f992740796c7d49642e05932`
