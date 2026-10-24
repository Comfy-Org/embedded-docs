# Referenzmethode für Bearbeitungsmodelle

Der FluxKontextMultiReferenceLatentMethod-Node aktualisiert Konditionierungsdaten, indem eine ausgewählte Referenz-Latents-Methode darin gespeichert wird. Die gespeicherte Methode wird dann verwendet, wenn Referenz-Latents in späteren Generierungsschritten verarbeitet werden. Dieser Node ist als experimentell gekennzeichnet und gehört zum Flux-Conditioning-System.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `conditioning` | Die Konditionierungsdaten, die mit der Referenz-Latents-Methode modifiziert werden sollen | CONDITIONING | Ja | - |
| `reference_latents_method` | Die Methode, die für die Verarbeitung von Referenz-Latents verwendet wird. Wenn ein Wert ausgewählt wird, der "uxo" oder "uso" enthält, wird er vor dem Speichern in "uxo" umgewandelt. Dieser Parameter ist als erweitert gekennzeichnet. | COMBO | Ja | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"`<br>`"index_timestep_zero_isolated"`<br>`"index_timestep_zero_text_start"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `conditioning` | Die modifizierten Konditionierungsdaten mit angewendeter Referenz-Latents-Methode | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/de.md)

---
**Source fingerprint (SHA-256):** `de2e3d34f9e47a90ff37300489bffef8082eb92deefbc2ce338b17b0d853ac77`
