# ControlnetApplyAdvanced

Dieser Node wendet erweiterte Control-Net-Transformationen auf Conditioning-Daten basierend auf einem Bild und einem Control-Net-Modell an. Er ermöglicht fein abgestimmte Anpassungen des Einflusses des Control-Nets auf den generierten Inhalt, wodurch präzisere und vielfältigere Modifikationen der Conditioning-Daten möglich sind.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die positiven Conditioning-Daten, auf die die Control-Net-Transformationen angewendet werden. Sie stellen die gewünschten Attribute oder Merkmale dar, die im generierten Inhalt verstärkt oder beibehalten werden sollen. | `CONDITIONING` |
| `negative` | Die negativen Conditioning-Daten, die Attribute oder Merkmale darstellen, die im generierten Inhalt abgeschwächt oder entfernt werden sollen. Die Control-Net-Transformationen werden ebenfalls auf diese Daten angewendet, was eine ausgewogene Anpassung der Eigenschaften des Inhalts ermöglicht. | `CONDITIONING` |
| `control_net` | Das Control-Net-Modell ist entscheidend für die Definition der spezifischen Anpassungen und Verbesserungen der Conditioning-Daten. Es interpretiert das Referenzbild und die Stärkeparameter, um Transformationen anzuwenden, und beeinflusst die endgültige Ausgabe erheblich, indem es Attribute sowohl in den positiven als auch in den negativen Conditioning-Daten verändert. | `CONTROL_NET` |
| `image` | Das Bild dient als Referenz für die Control-Net-Transformationen. Es beeinflusst die vom Control-Net vorgenommenen Anpassungen der Conditioning-Daten und steuert die Verstärkung oder Unterdrückung bestimmter Merkmale. | `IMAGE` |
| `strength` | Ein skalarer Wert, der die Intensität des Einflusses des Control-Nets auf die Conditioning-Daten bestimmt. Höhere Werte führen zu ausgeprägteren Anpassungen. | `FLOAT` |
| `start_percent` | Der Startprozentsatz der Wirkung des Control-Nets, der eine schrittweise Anwendung der Transformationen über einen festgelegten Bereich ermöglicht. | `FLOAT` |
| `end_percent` | Der Endprozentsatz der Wirkung des Control-Nets, der den Bereich definiert, über den die Transformationen angewendet werden. Dies ermöglicht eine differenziertere Steuerung des Anpassungsprozesses. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die modifizierten positiven Conditioning-Daten nach Anwendung der Control-Net-Transformationen, die die auf Basis der Eingabeparameter vorgenommenen Verbesserungen widerspiegeln. | `CONDITIONING` |
| `negative` | Die modifizierten negativen Conditioning-Daten nach Anwendung der Control-Net-Transformationen, die die Unterdrückung oder Entfernung bestimmter Merkmale auf Basis der Eingabeparameter widerspiegeln. | `CONDITIONING` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplyAdvanced/de.md)
