# ReferenceLatent

Dieser Node legt das leitende Latent für ein Editiermodell fest. Er nimmt Conditioning-Daten und eine optionale Latent-Eingabe entgegen und modifiziert dann die Conditioning-Daten, um Referenz-Latent-Informationen aufzunehmen. Wenn das Modell dies unterstützt, können Sie mehrere Nodes vom Typ Set Reference Latent verketten, um mehrere Referenzbilder festzulegen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `conditioning` | Die Conditioning-Daten, die mit Referenz-Latent-Informationen modifiziert werden sollen | CONDITIONING | Ja | - |
| `latent` | Optionale Latent-Daten, die als Referenz für das Editiermodell verwendet werden sollen. Wenn nicht angegeben, werden die Conditioning-Daten unverändert zurückgegeben | LATENT | Nein | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die modifizierten Conditioning-Daten, die Referenz-Latent-Informationen enthalten | CONDITIONING |

## Hinweise

- Das Referenz-Latent wird als Liste von Sample-Tensoren gespeichert. Wenn mehrere Nodes vom Typ Set Reference Latent nacheinander verbunden werden, werden daher zusätzliche Referenzen angehängt, anstatt die vorherige zu ersetzen.
- Wenn kein `latent` verbunden ist, gibt der Node die eingehende `conditioning` unverändert weiter.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/de.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
