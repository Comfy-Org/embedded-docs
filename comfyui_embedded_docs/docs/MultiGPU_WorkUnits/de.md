# MultiGPU cfg-Aufteilung

## Übersicht:

Der MultiGPU CFG Split-Knoten ermöglicht die Diffusionsverarbeitung mit mehreren im selben System installierten GPUs. Die Leistungsergebnisse hängen vom Workflow ab, aber in gängigen Workflows wurden Geschwindigkeitssteigerungen von bis zu 1,95x gemessen.

## Wichtige Details:

Das Mischen verschiedener GPU-Typen wird nicht unterstützt; die installierten GPUs müssen identisch sein (d. h. 2x 5090 oder 2x 5080 usw.).

ComfyUI erkennt beim Start automatisch mehrere installierte GPUs.

## Unterstützte GPUs:

Alle homogenen Dual-GPU-Setups mit Ampere+-Architektur (z. B. 2 x 3090 oder 2 x RTX6000 Pro)

## Unterstützte Modelle:

* LTX-2.3  
* WAN 2.2  
* FLUX.2 Klein - Basisversionen  
* Z-Image  
* Stable Diffusion 3.5 Large  
* Hunyuan Video  
* Qwen-Image-Edit-2511  
* Hunyuan-3D-v2.1  
* SDXL

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, das vor dem Sampling für die MultiGPU-CFG-Aufteilung vorbereitet werden soll. | MODEL | Ja | N/A |
| `max_gpus` | Die maximale Anzahl identischer GPUs, die zum Aufteilen der Arbeitslast verwendet werden soll. Setzen Sie diesen Wert auf die Anzahl der in Ihrem System installierten passenden GPUs. | INT | Ja | Minimum: 1<br>Schritt: 1<br>Standard: 2 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL` | Das für die MultiGPU-CFG-Aufteilung vorbereitete Modell, bereit für beschleunigtes Sampling. | MODEL |

## Knoten:

![image1.png](./asset/image1.png)  
Das Feld `max_gpus` sollte auf die maximale Anzahl identischer im System installierter GPUs gesetzt werden.

**Platzierung des Knotens:** Der MultiGPU CFG Split muss zwischen dem Model Load-Knoten und dem Sampling-Knoten platziert werden. Wenn andere Knoten mit dem Modellausgang des Model Loader-Knotens verbunden sind, sollte der MultiGPU CFG der letzte Knoten in der Kette vor dem Sampling-Knoten sein.

![image2.png](./asset/image2.png)

**Workflow-Anforderungen:** Der Knoten funktioniert, indem er den Diffusions-Workflow auf CFG-Ebene aufteilt. Aus diesem Grund muss der CFG-Wert im Workflow größer als CFG=1 sein. Destillierte Workflows, die CFG=1 erfordern, zeigen keinen Leistungsvorteil, wenn der MultiGPU CFG Split-Knoten verwendet wird, um auf mehreren GPUs auszuführen.

## Überprüfen der Multi-GPU-Auslastung

Wenn Sie einen Workflow mit aktiviertem MultiGPU CFG Split ausführen, können Sie den Windows Task-Manager öffnen und die Kategorie „Leistung“ auswählen.  
![image3.png](./asset/image3.webp)  
![image4.png](./asset/image4.webp)  
Während der Sampler im Workflow läuft, sollten Sie Aktivität auf beiden installierten GPUs sehen.

## Beispiel-Workflow für Multi-GPU: (Wan 2.2 FP8)

[Beispiel-Workflow (Wan 2.2 FP8)](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/asset/video_wan2_2_14B_t2v_mGPU.json)

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/de.md)

---
**Source fingerprint (SHA-256):** `7293ee785e29aea9a1a70a10444b99e89fb23c866505628ec57c209a2b8aaee0`
