# LoRA trainieren

Der TrainLoraNode erstellt und trainiert ein LoRA-Modell (Low-Rank Adaptation) auf einem Diffusionsmodell unter Verwendung der bereitgestellten Latents und Conditioning-Daten. Er ermöglicht das Fine-Tuning eines Modells mit benutzerdefinierten Trainingsparametern, Optimierern und Verlustfunktionen. Der Node gibt die trainierten LoRA-Gewichte, eine Loss-Verlauf-Map und die insgesamt abgeschlossenen Trainingsschritte aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das Modell, auf dem die LoRA trainiert werden soll. | MODEL | Ja | - |
| `latents` | Die Latents, die für das Training verwendet werden; dienen als Datensatz/Eingabe des Modells. | LATENT | Ja | - |
| `positive` | Das positive Conditioning, das für das Training verwendet wird. | CONDITIONING | Ja | - |
| `batch_size` | Die Batch-Größe, die für das Training verwendet wird (Standard: 1). | INT | Ja | 1-10000 |
| `grad_accumulation_steps` | Die Anzahl der Gradientenakkumulationsschritte, die für das Training verwendet wird (Standard: 1). | INT | Ja | 1-1024 |
| `steps` | Die Anzahl der Schritte, für die die LoRA trainiert wird (Standard: 16). | INT | Ja | 1-100000 |
| `learning_rate` | Die Lernrate, die für das Training verwendet wird (Standard: 0.0005). | FLOAT | Ja | 0.0000001-1.0 |
| `rank` | Der Rang der LoRA-Schichten (Standard: 8). | INT | Ja | 1-128 |
| `optimizer` | Der Optimierer, der für das Training verwendet wird (Standard: "AdamW"). | COMBO | Ja | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" |
| `loss_function` | Die Verlustfunktion, die für das Training verwendet wird (Standard: "MSE"). | COMBO | Ja | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" |
| `seed` | Der Seed, der für das Training verwendet wird (verwendet im Generator für die Initialisierung der LoRA-Gewichte und die Rauschabtastung) (Standard: 0). | INT | Ja | 0-18446744073709551615 |
| `training_dtype` | Der dtype, der für das Training verwendet wird. 'none' behält den nativen Compute-dtype des Modells bei, anstatt ihn zu überschreiben. Bei fp16-Modellen wird GradScaler automatisch aktiviert (Standard: "bf16"). | COMBO | Ja | "bf16"<br>"fp32"<br>"none" |
| `lora_dtype` | Der dtype, der für LoRA verwendet wird (Standard: "bf16"). | COMBO | Ja | "bf16"<br>"fp32" |
| `quantized_backward` | Bei Verwendung von training_dtype 'none' und Training auf einem quantisierten Modell wird bei Aktivierung die Rückwärtspropagation mit quantisierter Matmul durchgeführt (Standard: False). | BOOLEAN | Ja | - |
| `algorithm` | Der Algorithmus, der für das Training verwendet wird. | COMBO | Ja | Mehrere Optionen verfügbar |
| `gradient_checkpointing` | Gradient-Checkpointing für das Training verwenden (Standard: True). | BOOLEAN | Ja | - |
| `checkpoint_depth` | Tiefenstufe für Gradient-Checkpointing (Standard: 1). | INT | Ja | 1-5 |
| `offloading` | Modellgewichte während des Trainings auf CPU auslagern, um GPU-Speicher zu sparen (Standard: False). | BOOLEAN | Ja | - |
| `existing_lora` | Die vorhandene LoRA, an die angehängt werden soll. Auf None setzen für neue LoRA (Standard: "[None]"). | COMBO | Ja | Mehrere Optionen verfügbar |
| `bucket_mode` | Auflösungs-Bucket-Modus aktivieren. Wenn aktiviert, werden vorab gebuckelte Latents vom ResolutionBucket-Node erwartet (Standard: False). | BOOLEAN | Ja | - |
| `bypass_mode` | Bypass-Modus für das Training aktivieren. Wenn aktiviert, werden Adapter über Forward-Hooks angewendet, anstatt die Gewichte zu verändern. Nützlich für quantisierte Modelle, bei denen Gewichte nicht direkt geändert werden können (Standard: False). | BOOLEAN | Ja | - |

**Hinweis:** Die Anzahl der positiven Conditioning-Eingaben muss mit der Anzahl der Latent-Bilder übereinstimmen. Wenn nur ein positives Conditioning mit mehreren Bildern bereitgestellt wird, wird es automatisch für alle Bilder wiederholt.

**Hinweis zu `training_dtype`:** Wenn auf "none" gesetzt, bleibt der native Compute-dtype des Modells erhalten. Bei fp16-Modellen wird GradScaler automatisch aktiviert, um Unterlauf während der Gradientenberechnung zu verhindern. Wenn zusätzlich `fp16_accumulation` aktiviert ist (über `--fast` Flags), kann diese Kombination numerisch instabil sein und NaN-Werte verursachen.

**Hinweis zu `quantized_backward`:** Dieser Parameter ist nur relevant, wenn `training_dtype` auf "none" gesetzt ist und das Modell ein quantisiertes Modell ist. Er aktiviert quantisierte Matrixmultiplikation während des Rückwärtsdurchlaufs.

**Hinweis zu `bypass_mode`:** Wenn aktiviert, werden Adapter über Forward-Hooks angewendet, anstatt die Modellgewichte direkt zu verändern. Dies ist besonders nützlich für quantisierte Modelle, bei denen Gewichte nicht direkt verändert werden können.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `lora` | Die trainierten LoRA-Gewichte, die gespeichert oder auf andere Modelle angewendet werden können. | LORA_MODEL |
| `loss_map` | Ein Wörterbuch, das die Trainingsloss-Werte über die Zeit enthält. | LOSS_MAP |
| `steps` | Die Gesamtzahl der abgeschlossenen Trainingsschritte (einschließlich etwaiger vorheriger Schritte aus vorhandener LoRA). | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/de.md)

---
**Source fingerprint (SHA-256):** `39e88045270d36855442024b62d6a225a58b34842f45ac04fbc6c1ade6768a76`
