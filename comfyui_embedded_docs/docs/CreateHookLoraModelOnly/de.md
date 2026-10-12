# Hook-LoRA erstellen (MO)

Dieser Node erstellt einen LoRA-Hook (Low-Rank-Adaption), der nur auf die Modellkomponente angewendet wird und die CLIP-Komponente vollständig unverändert lässt. Er lädt eine LoRA-Datei und wendet sie mit einer angegebenen Stärke auf das Modell an, während die CLIP-Stärke auf null gesetzt wird. Der Node kann mit vorherigen Hooks verkettet werden, um komplexe Modifikationspipelines aufzubauen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `lora_name` | Der Name der LoRA-Datei, die aus dem Ordner loras geladen werden soll | STRING | Ja | Mehrere Optionen verfügbar |
| `strength_model` | Der Stärkemultiplikator für die Anwendung der LoRA auf die Modellkomponente (Standard: 1.0) | FLOAT | Ja | -20.0 bis 20.0 |
| `prev_hooks` | Optionale vorherige Hooks, die mit diesem Hook verkettet werden sollen | HOOKS | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `hooks` | Der erstellte LoRA-Hook, der auf die Modellverarbeitung angewendet werden kann | HOOKS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/de.md)

---
**Source fingerprint (SHA-256):** `10adbdfc2e37fcf317e93130f87d9a7038d00b091cb6d1b45f4658c81632ef80`
