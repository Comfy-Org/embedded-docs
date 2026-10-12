# Bild in Maske umwandeln

Der ImageToMask-Node dient dazu, ein Bild basierend auf einem festgelegten Farbkanal in eine Maske umzuwandeln. Er ermöglicht die Extraktion von Maskenebenen, die den Rot-, Grün-, Blau- oder Alpha-Kanälen eines Bildes entsprechen, und erleichtert Operationen, die kanalspezifische Maskierung oder Verarbeitung erfordern.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Der Parameter `image` stellt das Eingabebild dar, aus dem basierend auf dem angegebenen Farbkanal eine Maske erzeugt wird. Er spielt eine entscheidende Rolle bei der Bestimmung des Inhalts und der Eigenschaften der resultierenden Maske. | `IMAGE` |
| `channel` | Der Parameter `channel` legt fest, welcher Farbkanal (Rot, Grün, Blau oder Alpha) des Eingabebildes zur Erzeugung der Maske verwendet werden soll. Diese Wahl beeinflusst direkt das Aussehen der Maske und welche Bildbereiche hervorgehoben oder maskiert werden. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Die Ausgabe `mask` ist eine binäre oder Graustufendarstellung des angegebenen Farbkanals aus dem Eingabebild, die für weitere Bildverarbeitungs- oder Maskierungsoperationen nützlich ist. | `MASK` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageToMask/de.md)
