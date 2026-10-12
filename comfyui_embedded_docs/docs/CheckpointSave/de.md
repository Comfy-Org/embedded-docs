# Checkpoint speichern

Der Node `Save Checkpoint` ist dafür ausgelegt, ein vollständiges Stable-Diffusion-Modell (einschließlich UNet-, CLIP- und VAE-Komponenten) als Checkpoint-Datei im Format **.safetensors** zu speichern.

Der Node `Save Checkpoint` wird hauptsächlich in Workflows zum Zusammenführen von Modellen verwendet. Nachdem Sie mit Nodes wie `ModelMergeSimple`, `ModelMergeBlocks` usw. ein neues zusammengeführtes Modell erstellt haben, können Sie diesen Node verwenden, um das Ergebnis als wiederverwendbare Checkpoint-Datei zu speichern.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Der Parameter `model` repräsentiert das primäre Modell, dessen Zustand gespeichert werden soll. Er ist wesentlich, um den aktuellen Zustand des Modells für zukünftige Wiederherstellung oder Analyse zu erfassen. | MODEL |
| `clip` | Der Parameter `clip` ist für das dem primären Modell zugeordnete CLIP-Modell vorgesehen, sodass sein Zustand zusammen mit dem Hauptmodell gespeichert werden kann. | CLIP |
| `vae` | Der Parameter `vae` ist für das Variational-Autoencoder-(VAE)-Modell gedacht, sodass sein Zustand zusammen mit dem Hauptmodell und CLIP für zukünftige Nutzung oder Analyse gespeichert werden kann. | VAE |
| `filename_prefix` | Dieser Parameter legt das Präfix für den Dateinamen fest, unter dem der Checkpoint gespeichert wird. | STRING |

Zusätzlich verfügt der Node über zwei versteckte Eingaben für Metadaten:

**prompt (PROMPT)**: Workflow-Prompt-Informationen  
**extra_pnginfo (EXTRA_PNGINFO)**: Zusätzliche PNG-Informationen

## Ausgaben

Dieser Node gibt eine Checkpoint-Datei aus. Der entsprechende Ausgabedateipfad ist das Verzeichnis `output/checkpoints/`.

## Architekturkompatibilität

- Derzeit vollständig unterstützt: SDXL, SD3, SVD und andere gängige Architekturen, siehe [Quellcode](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- Grundlegende Unterstützung: Andere Architekturen können gespeichert werden, jedoch ohne standardisierte Metadateninformationen

## Zugehörige Links

Zugehöriger Quellcode: [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointSave/de.md)
