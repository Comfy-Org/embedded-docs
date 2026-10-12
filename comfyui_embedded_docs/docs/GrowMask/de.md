# GrowMask

Der Node `GrowMask` dient dazu, die Größe einer gegebenen Maske zu ändern, indem er sie entweder erweitert oder verkleinert und optional einen Verjüngungseffekt auf die Ecken anwendet. Diese Funktionalität ist entscheidend für die dynamische Anpassung von Maskengrenzen in Bildverarbeitungsaufgaben und ermöglicht eine flexiblere und präzisere Steuerung des interessierenden Bereichs.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Die Eingabemaske, die geändert werden soll. Dieser Parameter ist zentral für die Funktionsweise des Nodes und dient als Basis, auf der die Maske entweder erweitert oder verkleinert wird. | MASK |
| `expand` | Bestimmt das Ausmaß und die Richtung der Maskenänderung. Positive Werte bewirken eine Erweiterung der Maske, während negative Werte zu einer Verkleinerung führen. Dieser Parameter beeinflusst direkt die endgültige Größe der Maske. | INT |
| `tapered_corners` | Ein boolesches Flag, das, wenn auf True gesetzt, einen Verjüngungseffekt auf die Ecken der Maske während der Änderung anwendet. Diese Option ermöglicht sanftere Übergänge und visuell ansprechendere Ergebnisse. | BOOLEAN |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Die geänderte Maske nach Anwendung der angegebenen Erweiterung/Verkleinerung und des optionalen Effekts verjüngter Ecken. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrowMask/de.md)
