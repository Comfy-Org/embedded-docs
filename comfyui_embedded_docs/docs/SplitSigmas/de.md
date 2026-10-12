# SplitSigmas

Der SplitSigmas-Node dient dazu, eine Sequenz von Sigma-Werten anhand eines angegebenen Schritts in zwei Teile zu unterteilen. Diese Funktionalität ist entscheidend für Vorgänge, die eine unterschiedliche Behandlung oder Verarbeitung des Anfangs- und des nachfolgenden Teils der Sigma-Sequenz erfordern, und ermöglicht eine flexiblere und gezieltere Manipulation dieser Werte.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Der Parameter `sigmas` stellt die Sequenz der zu teilenden Sigma-Werte dar. Er ist entscheidend für die Bestimmung des Teilungspunkts und der resultierenden beiden Sigma-Wert-Sequenzen und beeinflusst die Ausführung und die Ergebnisse des Nodes. | `SIGMAS` |
| `step` | Der Parameter `step` gibt den Index an, an dem die Sigma-Sequenz geteilt werden soll. Er spielt eine entscheidende Rolle bei der Definition der Grenze zwischen den beiden resultierenden Sigma-Sequenzen und beeinflusst die Funktionalität des Nodes sowie die Eigenschaften der Ausgabe. | `INT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Der Node gibt zwei Sequenzen von Sigma-Werten aus, die jeweils einen Teil der ursprünglichen, am angegebenen Schritt geteilten Sequenz darstellen. Diese Ausgaben sind entscheidend für nachfolgende Vorgänge, die eine unterschiedliche Behandlung von Sigma-Werten erfordern. | `SIGMAS` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmas/de.md)
