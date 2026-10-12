# ModelMergeAdd

Der Node ModelMergeAdd ist dafür ausgelegt, zwei Modelle zusammenzuführen, indem Schlüssel-Patches von einem Modell zu einem anderen hinzugefügt werden. Dieser Prozess umfasst das Klonen des ersten Modells und anschließend das Anwenden von Patches aus dem zweiten Modell, wodurch Merkmale oder Verhaltensweisen beider Modelle kombiniert werden können.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model1` | Das erste Modell, das geklont wird und zu dem Patches aus dem zweiten Modell hinzugefügt werden. Es dient als Basismodell für den Zusammenführungsprozess. | `MODEL` |
| `model2` | Das zweite Modell, aus dem Schlüssel-Patches extrahiert und zum ersten Modell hinzugefügt werden. Es trägt zusätzliche Merkmale oder Verhaltensweisen zum zusammengeführten Modell bei. | `MODEL` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das Ergebnis der Zusammenführung zweier Modelle durch Hinzufügen von Schlüssel-Patches aus dem zweiten Modell zum ersten. Dieses zusammengeführte Modell kombiniert Merkmale oder Verhaltensweisen beider Modelle. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAdd/de.md)
