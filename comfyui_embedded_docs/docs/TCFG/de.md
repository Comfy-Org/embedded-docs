# CFG mit tangentialer Dämpfung

TCFG (Tangential Damping CFG) verfeinert die unbedingten (negativen) Vorhersagen, um sie während des Sampling-Prozesses besser an den bedingten (positiven) Vorhersagen auszurichten. Diese Technik verbessert die Ausgabequalität, indem sie eine tangentiale Dämpfung auf die unbedingte Führung anwendet, basierend auf dem Forschungspapier 2503.18137. Der Node ändert das Sampling-Verhalten des Modells, indem er anpasst, wie unbedingte Vorhersagen während der Classifier-Free-Guidance verarbeitet werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das Tangential Damping CFG angewendet wird | MODEL | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `patched_model` | Das geänderte Modell mit angewendetem Tangential Damping CFG | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TCFG/de.md)

---
**Source fingerprint (SHA-256):** `6e0e1df09bdc29f14a4828ec54fd29f89926b9d8121bc8ba9f95ce066b899e95`
