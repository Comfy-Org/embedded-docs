# SelectModelDevice

Der Node Select Model Device ermöglicht es Ihnen, manuell auszuwählen, auf welchem Gerät (CPU oder eine bestimmte GPU) ein Diffusionsmodell ausgeführt wird. Er kann ein Modell auf ein anderes Gerät verschieben und behandelt Konflikte mit anderen Multi-GPU-Nodes automatisch. Die Auswahl von `"default"` stellt das ursprüngliche Gerät wieder her, das vom Modell-Loader gewählt wurde.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, das auf einem bestimmten Gerät platziert werden soll. | MODEL | Ja |  |
| `device` | Das Zielgerät für das Modell. Die Optionen werden dynamisch basierend auf den verfügbaren Geräten des aktuellen Rechners generiert. (Standard: `"default"`) | COMBO | Ja | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>... (ein `"gpu:N"`-Eintrag pro erkannter GPU) |

**Parameterdetails:**
- `"default"`: Stellt die vom Modell-Loader zugewiesenen Lade- und Offload-Geräte wieder her, auch nach einem vorherigen Aufruf von Select Model Device.
- `"cpu"`: Fixiert sowohl das Lade- als auch das Offload-Gerät auf CPU.
- `"gpu:N"`: Fixiert das Ladegerät auf die N-te verfügbare GPU (zum Beispiel `"gpu:0"` für die erste GPU). Das Offload-Gerät wird auf die ursprüngliche Auswahl des Loaders zurückgesetzt.

**Wichtige Hinweise:**
- Wenn das angeforderte Gerät auf dem aktuellen Rechner nicht existiert (zum Beispiel, wenn ein auf einem Rechner mit 2 GPUs erstellter Workflow auf einem Rechner mit 1 GPU geöffnet wird), reicht der Node das Modell unverändert durch und protokolliert eine Meldung, anstatt fehlzuschlagen. Unbekannte `gpu:N`-Werte sind während der Eingabevalidierung zulässig, damit portable Workflows nicht frühzeitig einen Fehler auslösen.
- Wenn das Modell bereits auf dem angeforderten Gerät liegt, verwendet der Node einen schnellen Pfad und lädt das Modell nicht neu.
- Wenn das angeforderte Gerät von dem Gerät abweicht, auf dem sich das Eingabemodell bereits befindet, wird ein neues Modell über die Reload-Factory des Loaders erzeugt, damit der neue Patcher unabhängige Gewichte auf dem neuen Gerät besitzt.
- Wenn der Modell-Loader Multi-GPU nicht unterstützt (keine Reload-Factory), reicht der Node das Modell unverändert durch und protokolliert eine Warnung.
- Wenn ein MultiGPU CFG Split-Klon bereits das ausgewählte Gerät belegt, wird dieser Klon entfernt, damit nicht zwei Modelle an dasselbe Gerät gebunden sind.
- Wenn ein Nicht-Standard-Gerät ausgewählt wird (CPU oder GPU), passt der Node außerdem den Compute-Dtype des Modells an einen von diesem Gerät unterstützten Typ an.
- Es wird nicht empfohlen, diesen Node nach einem Node zu platzieren, der das Modell bereits verwendet hat (zum Beispiel ein KSampler), da alle vom vorherigen Node geänderten Zustände wirksam werden, wenn das Gerät dem ursprünglichen entspricht.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das Diffusionsmodell, jetzt auf dem ausgewählten Gerät platziert. Wenn das Gerät ungültig oder nicht verfügbar war, wird das Modell unverändert durchgereicht. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/de.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
