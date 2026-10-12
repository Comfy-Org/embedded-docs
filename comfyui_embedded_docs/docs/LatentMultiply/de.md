# LatentMultiply

Der Node `LatentMultiply` dient dazu, die latente Repräsentation von Samples mit einem angegebenen Multiplikator zu skalieren. Dieser Vorgang ermöglicht die Anpassung der Intensität oder Ausprägung von Merkmalen im latenten Raum, wodurch generierte Inhalte fein abgestimmt oder Variationen innerhalb einer gegebenen latenten Richtung erkundet werden können.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Der Parameter `samples` repräsentiert die latenten Repräsentationen, die skaliert werden sollen. Er ist entscheidend für die Definition der Eingabedaten, auf die die Multiplikationsoperation angewendet wird. | `LATENT` |
| `multiplier` | Der Parameter `multiplier` gibt den Skalierungsfaktor an, der auf die latenten Samples angewendet werden soll. Er spielt eine Schlüsselrolle bei der Anpassung der Größe der latenten Merkmale und ermöglicht eine differenzierte Kontrolle über die generierte Ausgabe. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe ist eine modifizierte Version der latenten Eingabe-Samples, skaliert mit dem angegebenen Multiplikator. Dadurch können Variationen innerhalb des latenten Raums durch Anpassung der Intensität seiner Merkmale erkundet werden. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentMultiply/de.md)
