# Anteprima Audio

Il nodo Preview Audio consente di ascoltare l'audio direttamente all'interno di ComfyUI senza salvarlo nella directory di output. Riceve un input audio, verifica che i dati audio siano effettivamente presenti e poi lo riproduce tramite un lettore di anteprima nell'interfaccia, passando contemporaneamente lo stesso audio come output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio` | I dati audio da visualizzare in anteprima. Se questo input è None, il nodo genera un ValueError, cosa che può verificarsi quando il video di origine non ha una traccia audio. | AUDIO | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `audio` | I dati audio passati invariati dall'input, così il nodo può essere inserito nel mezzo di un workflow. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/it.md)

---
**Source fingerprint (SHA-256):** `02dbc5cb7d6924aae63c59e926a8ea265eb0889dbc2e6b47ff60f666a55d1adf`
