# Maske invertieren

Der InvertMask-Node dient dazu, die Werte einer gegebenen Maske zu invertieren, wodurch maskierte und nicht maskierte Bereiche effektiv vertauscht werden. Dieser Vorgang ist grundlegend für Bildverarbeitungsaufgaben, bei denen der Fokus des Interesses zwischen Vordergrund und Hintergrund gewechselt werden muss.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Der Parameter `mask` stellt die Eingabemaske dar, die invertiert werden soll. Er ist entscheidend dafür, die Bereiche zu bestimmen, die beim Inversionsprozess vertauscht werden. | MASK |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Die Ausgabe ist eine invertierte Version der Eingabemaske, wobei zuvor maskierte Bereiche unmaskiert werden und umgekehrt. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InvertMask/de.md)
