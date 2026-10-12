# ManualSigmas

Der Node ManualSigmas ermöglicht es Ihnen, manuell eine benutzerdefinierte Sequenz von Rauschpegeln (Sigmas) für den Sampling-Prozess zu definieren. Sie geben eine Liste von Zahlen als String ein, und der Node wandelt sie in einen SIGMAS-Tensor um, der von anderen Sampling-Nodes verwendet werden kann. Dies ist nützlich zum Testen oder zum Erstellen spezifischer Rauschpläne.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `sigmas` | Ein String, der die Sigma-Werte enthält. Der Node extrahiert alle Zahlen aus dieser Zeichenkette, einschließlich Dezimalzahlen und negativer Werte. Zum Beispiel: "1, 0.5, 0.1" oder "1 0.5 0.1". Standard: "1, 0.5". | STRING | Ja | Beliebige durch Kommas oder Leerzeichen getrennte numerische Werte |

Hinweis: Dieser Node ist als experimentell gekennzeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Ein Tensor, der die Sequenz der aus der Eingabezeichenkette extrahierten Sigma-Werte enthält. | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/de.md)

---
**Source fingerprint (SHA-256):** `19d938ef0eac7343a3138393a039f63632b0763e3884636653c06b91b6f44ed6`
