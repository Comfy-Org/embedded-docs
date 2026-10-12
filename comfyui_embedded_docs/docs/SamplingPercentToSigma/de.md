# SamplingPercentToSigma

Wandelt einen Sampling-Prozentsatz mithilfe der Sampling-Einstellungen des ausgewählten Modells in den passenden Sigma-Wert um. Er ordnet einen Prozentsatz zwischen 0.0 und 1.0 dem Rauschplan des Modells zu und kann optional den tatsächlichen maximalen oder minimalen Sigma-Wert des Modells an den beiden Endpunkten zurückgeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, das die für die Konvertierung verwendeten Sampling-Parameter enthält | MODEL | Ja | - |
| `sampling_percent` | Der Sampling-Prozentsatz, der in einen Sigma-Wert umgewandelt werden soll (Standard: 0.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.0001) |
| `return_actual_sigma` | Gibt den tatsächlichen Sigma-Wert anstelle des für Intervallprüfungen verwendeten Werts zurück. Dies wirkt sich nur auf Ergebnisse bei 0.0 und 1.0 aus. (Standard: False) | BOOLEAN | Ja | - |

Wenn `return_actual_sigma` aktiviert ist, gibt ein `sampling_percent` von 0.0 den maximalen Sigma-Wert des Modells (sigma_max) zurück, und ein `sampling_percent` von 1.0 gibt den minimalen Sigma-Wert (sigma_min) zurück. Bei allen anderen Prozentsätzen ist das Ergebnis dasselbe, unabhängig davon, ob diese Option aktiviert ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigma_value` | Der Sigma-Wert, der dem eingegebenen Sampling-Prozentsatz entspricht | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/de.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`
