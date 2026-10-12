# Masken kombinieren

Dieser Node ist auf die Kombination zweier Maskeneingaben durch verschiedene Operationen wie Addition, Subtraktion und logische Operationen spezialisiert, um eine neue, modifizierte Maske zu erzeugen. Er übernimmt abstrakt die Manipulation von Maskendaten, um komplexe Maskierungseffekte zu erzielen, und dient als entscheidende Komponente in maskenbasierten Bildbearbeitungs- und Verarbeitungsworkflows.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `destination` | Die primäre Maske, die basierend auf der Operation mit der Quellmaske geändert wird. Sie spielt eine zentrale Rolle bei der zusammengesetzten Operation und dient als Basis für Änderungen. | MASK |
| `source` | Die sekundäre Maske, die zusammen mit der Zielmaske verwendet wird, um die angegebene Operation auszuführen und die endgültige Ausgabemaske zu beeinflussen. | MASK |
| `x` | Der horizontale Offset, an dem die Quellmaske auf die Zielmaske angewendet wird, wodurch die Positionierung des zusammengesetzten Ergebnisses beeinflusst wird. | INT |
| `y` | Der vertikale Offset, an dem die Quellmaske auf die Zielmaske angewendet wird, wodurch die Positionierung des zusammengesetzten Ergebnisses beeinflusst wird. | INT |
| `operation` | Gibt den Typ der Operation an, die zwischen Ziel- und Quellmaske angewendet werden soll, z. B. 'add', 'subtract' oder logische Operationen, und bestimmt damit die Art des zusammengesetzten Effekts. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Die resultierende Maske nach Anwendung der angegebenen Operation zwischen Ziel- und Quellmaske, die das zusammengesetzte Ergebnis darstellt. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskComposite/de.md)
