# GITSScheduler

Der Node GITSScheduler erzeugt Sigmas für den Rausch-Zeitplan der Sampling-Methode GITS (Generative Iterative Time Steps). Er berechnet Sigma-Werte basierend auf einem Koeffizientenparameter und der Anzahl der Schritte, wobei ein Denoising-Faktor die insgesamt verwendeten Schritte reduzieren kann. Der Node verwendet vordefinierte Rauschpegel und Interpolation, um den endgültigen Sigma-Zeitplan zu erstellen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `coeff` | Erweiterter Parameter. Der Koeffizientenwert, der die Kurve des Rausch-Zeitplans steuert (Standard: 1.20). Der Wert wird auf zwei Dezimalstellen gerundet und wählt aus, welche vordefinierte Rauschpegel-Tabelle verwendet wird. | FLOAT | Ja | 0.80 - 1.50 (step 0.05) |
| `steps` | Die Gesamtzahl der Sampling-Schritte, für die Sigmas erzeugt werden sollen (Standard: 10). | INT | Ja | 2 - 1000 |
| `denoise` | Denoising-Faktor, der die Anzahl der verwendeten Schritte reduziert (Standard: 1.0). | FLOAT | Ja | 0.0 - 1.0 (step 0.01) |

**Hinweis:** Wenn `denoise` 0.0 oder kleiner ist, gibt der Node einen leeren Tensor zurück. Wenn `denoise` kleiner als 1.0 ist, wird die tatsächlich verwendete Anzahl von Schritten als `round(steps * denoise)` berechnet, und nur der letzte entsprechende Teil des Rausch-Zeitplans wird beibehalten. Für Schritte zwischen 2 und 20 wählt der Node einen passenden vordefinierten Rausch-Zeitplan aus. Für Schritte größer als 20 verwendet der Node logarithmisch-lineare Interpolation, um die vordefinierten Rauschpegel auf die gewünschte Anzahl von Schritten zu erweitern.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `sigmas` | Die erzeugten Sigma-Werte für den Rausch-Zeitplan. Für N Sampling-Schritte werden N+1 Sigma-Werte zurückgegeben, und das letzte Sigma wird auf 0 gesetzt. | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/de.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
