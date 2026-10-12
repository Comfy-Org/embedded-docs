# FluxDisableGuidance

Dieser Node deaktiviert das Guidance-Embed bei Flux- und Flux-ähnlichen Modellen vollständig. Er nimmt Conditioning-Daten als Eingabe entgegen und setzt deren Guidance-Wert auf None, wodurch das guidance-basierte Conditioning für den Generierungsprozess effektiv deaktiviert wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `conditioning` | Die Conditioning-Daten, die verarbeitet und aus denen die Guidance entfernt werden soll | CONDITIONING | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `conditioning` | Die modifizierten Conditioning-Daten mit deaktivierter Guidance | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/de.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
