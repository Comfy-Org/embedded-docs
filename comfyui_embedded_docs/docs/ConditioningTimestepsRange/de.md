# Zeitschrittbereich

Der Knoten ConditioningTimestepsRange erstellt drei verschiedene Zeitschrittbereiche, um zu steuern, wann Conditioning-Effekte während des Generierungsprozesses angewendet werden. Er nimmt Start- und Endprozentwerte entgegen und unterteilt den gesamten Zeitschrittbereich (0.0 bis 1.0) in drei Segmente: den Hauptbereich zwischen den angegebenen Prozentwerten, den Bereich vor dem Startprozentwert und den Bereich nach dem Endprozentwert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `start_percent` | Der Startprozentsatz des Zeitschrittbereichs (Standard: 0.0) | FLOAT | Ja | 0.0 - 1.0 |
| `end_percent` | Der Endprozentsatz des Zeitschrittbereichs (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `TIMESTEPS_RANGE` | Der Haupt-Zeitschrittbereich, definiert durch start_percent und end_percent | TIMESTEPS_RANGE |
| `BEFORE_RANGE` | Der Zeitschrittbereich von 0.0 bis start_percent | TIMESTEPS_RANGE |
| `AFTER_RANGE` | Der Zeitschrittbereich von end_percent bis 1.0 | TIMESTEPS_RANGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/de.md)

---
**Source fingerprint (SHA-256):** `dee21b5ac80fabdeacf3f4a985550fff795702e02911400ae49a97baae834e5e`
