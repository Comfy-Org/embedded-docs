# Referenzmethode für Bearbeitungsmodelle

Der FluxKontextMultiReferenceLatentMethod-Node aktualisiert Konditionierungsdaten, indem eine ausgewählte Referenz-Latents-Methode darin gespeichert wird. Die gespeicherte Methode wird dann verwendet, wenn Referenz-Latents in späteren Generierungsschritten verarbeitet werden. Dieser Node ist als experimentell gekennzeichnet und gehört zum Flux-Conditioning-System.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `conditioning` | Die Konditionierungsdaten, die mit der Referenz-Latents-Methode modifiziert werden sollen | CONDITIONING | Ja | - |
| `reference_latents_method` | Die Methode, die für die Verarbeitung von Referenz-Latents verwendet wird. Wenn ein Wert ausgewählt wird, der "uxo" oder "uso" enthält, wird er vor dem Speichern in "uxo" umgewandelt. Dieser Parameter ist als erweitert gekennzeichnet. | COMBO | Ja | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `conditioning` | Die modifizierten Konditionierungsdaten mit angewendeter Referenz-Latents-Methode | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/de.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
