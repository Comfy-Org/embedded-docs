# SamplerSASolver

Der SamplerSASolver-Node erstellt und konfiguriert einen benutzerdefinierten Sampler für Diffusionsmodelle. Er verwendet den Sampling-Algorithmus "sa_solver" mit einem konfigurierbaren Prädiktor-Korrektor-Schema und Einstellungen für stochastische Differentialgleichungen (SDE) und gibt ein Sampler-Objekt zurück, das in einen Sampling-Node eingebunden werden kann. Die Werte `sde_start_percent` und `sde_end_percent` werden mithilfe des Sampling-Zeitplans des verbundenen Modells in Sigma-Werte umgewandelt, um das Intervall zu definieren, in dem die stochastische Komponente angewendet wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, dessen Sampling-Zeitplan zum Aufbau des Samplers verwendet wird | MODEL | Ja | - |
| `eta` | Steuert den Skalierungsfaktor der Schrittweite des SDE-Lösers (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |
| `sde_start_percent` | Startprozentsatz des Sampling-Prozesses, an dem die stochastische (SDE) Komponente beginnt; wird mithilfe des Modell-Zeitplans in einen Sigma-Wert umgewandelt (Standard: 0.2) | FLOAT | Nein | 0.0 - 1.0 |
| `sde_end_percent` | Endprozentsatz des Sampling-Prozesses, an dem die stochastische (SDE) Komponente stoppt; wird mithilfe des Modell-Zeitplans in einen Sigma-Wert umgewandelt (Standard: 0.8) | FLOAT | Nein | 0.0 - 1.0 |
| `s_noise` | Steuert die Menge an Rauschen, die während des Samplings hinzugefügt wird (Standard: 1.0) | FLOAT | Nein | 0.0 - 100.0 |
| `predictor_order` | Die Ordnung der Prädiktor-Komponente im Löser (Standard: 3) | INT | Nein | 1 - 6 |
| `corrector_order` | Die Ordnung der Korrektor-Komponente im Löser (Standard: 4) | INT | Nein | 0 - 6 |
| `use_pece` | Aktiviert die PECE-Methode (Predict-Evaluate-Correct-Evaluate) (Standard: deaktiviert) | BOOLEAN | Nein | - |
| `simple_order_2` | Aktiviert vereinfachte Berechnungen zweiter Ordnung (Standard: deaktiviert) | BOOLEAN | Nein | - |

Alle optionalen Eingaben sind in der Benutzeroberfläche als erweitert gekennzeichnet.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Ein konfiguriertes Sampler-Objekt (unter Verwendung des `sa_solver`-Algorithmus), das von Sampling-Nodes verwendet werden kann | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/de.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
