# MultiGPU_Options

## Überblick

Dieser Node ermöglicht es Ihnen, die relative Leistung jeder GPU festzulegen, wenn mehrere Grafikkarten mit unterschiedlichen Geschwindigkeiten verwendet werden. Er erstellt eine Gruppe von GPU-Optionen, die verwendet werden kann, um Arbeit auf Geräte zu verteilen, obwohl die tatsächliche geschwindigkeitsbasierte Arbeitslastverteilung in der aktuellen Version noch nicht implementiert ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `device_index` | Die Indexnummer des zu konfigurierenden GPU-Geräts (Standard: 0) | INT | Ja | 0 bis 64 |
| `relative_speed` | Die relative Geschwindigkeit dieser GPU im Vergleich zu anderen, verwendet für die Arbeitslastverteilung (Standard: 1.0, Schritt: 0.01) | FLOAT | Ja | 0.0 bis unbegrenzt |
| `gpu_options` | Eine vorhandene GPU-Optionsgruppe, zu der die Optionen dieses Geräts hinzugefügt werden sollen. Falls nicht angegeben, wird eine neue Gruppe erstellt | GPU_OPTIONS | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `GPU_OPTIONS` | Eine Gruppe von GPU-Optionen mit den konfigurierten Geräteeinstellungen, die an andere Nodes für Multi-GPU-Vorgänge übergeben werden kann | GPU_OPTIONS |

**Hinweis:** Der Parameter `relative_speed` ist definiert, wird aber noch nicht vom internen Scheduler verwendet, um Arbeit auf GPUs zu verteilen. In der aktuellen Implementierung wird die Arbeit gleichmäßig auf alle Geräte verteilt, unabhängig von ihren relativen Geschwindigkeiten.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_Options/de.md)

---
**Source fingerprint (SHA-256):** `8010460560a69c57d4ee0d8c3728a7a5d999e56ef5316b557fba0c660c9f38b0`
