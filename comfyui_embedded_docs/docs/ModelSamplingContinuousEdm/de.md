# ModelSamplingContinuousEdm

Dieser Node wurde entwickelt, um die Sampling-Fähigkeiten eines Modells zu verbessern, indem kontinuierliche EDM (Energy-based Diffusion Models)-Sampling-Techniken integriert werden. Er ermöglicht die dynamische Anpassung der Rauschpegel innerhalb des Sampling-Prozesses des Modells und bietet eine feinere Kontrolle über die Generierungsqualität und -vielfalt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Python dtype |
| --- | --- | --- | --- |
| `model` | Das Modell, das um kontinuierliche EDM-Sampling-Fähigkeiten erweitert werden soll. Es dient als Grundlage für die Anwendung der fortschrittlichen Sampling-Techniken. | `MODEL` | `torch.nn.Module` |
| `sampling` | Gibt die Art des anzuwendenden Samplings an, entweder 'eps' für Epsilon-Sampling oder 'v_prediction' für Geschwindigkeitsvorhersage, was das Verhalten des Modells während des Sampling-Prozesses beeinflusst. | COMBO[STRING] | `str` |
| `sigma_max` | Der maximale Sigma-Wert für den Rauschpegel, der eine Obergrenzenkontrolle beim Rauscheinfügen während des Samplings ermöglicht. | `FLOAT` | `float` |
| `sigma_min` | Der minimale Sigma-Wert für den Rauschpegel, der die Untergrenze für das Rauscheinfügen festlegt und somit die Sampling-Präzision des Modells beeinflusst. | `FLOAT` | `float` |

## Ausgaben

| Parameter | Beschreibung | Datentyp | Python dtype |
| --- | --- | --- | --- |
| `model` | Das erweiterte Modell mit integrierten kontinuierlichen EDM-Sampling-Fähigkeiten, bereit zur weiteren Verwendung in Generierungsaufgaben. | MODEL | `torch.nn.Module` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEdm/de.md)
