# SetModelHooksOnCond

Dieser Node hängt benutzerdefinierte Hooks an Konditionierungsdaten an, sodass Sie den Konditionierungsprozess während der Modellausführung abfangen und verändern können. Er nimmt eine Reihe von Hooks entgegen und wendet sie auf die bereitgestellten Konditionierungsdaten an, wodurch eine erweiterte Anpassung des Text-zu-Bild-Generierungsworkflows ermöglicht wird. Die modifizierten Konditionierungsdaten mit angehängten Hooks werden dann für die Verwendung in nachfolgenden Verarbeitungsschritten zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `conditioning` | Die Konditionierungsdaten, an die Hooks angehängt werden | CONDITIONING | Ja | - |
| `hooks` | Die Hook-Definitionen, die auf die Konditionierungsdaten angewendet werden | HOOKS | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `conditioning` | Die modifizierten Konditionierungsdaten mit angehängten Hooks | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/de.md)

---
**Source fingerprint (SHA-256):** `a6e63a3a4d94d1b66a82d449af5ae001e1fc4a04f0f81d9fb5c4f8c13e5bdf8b`
