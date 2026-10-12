# ModelSamplingAuraFlow

Il nodo ModelSamplingAuraFlow applica una configurazione di campionamento specializzata ai modelli di diffusione, progettata specificamente per le architetture dei modelli AuraFlow. Modifica il comportamento di campionamento del modello applicando un valore di shift che regola la distribuzione di campionamento. Questo nodo eredita dal framework di campionamento dei modelli SD3 e offre un controllo preciso sul processo di campionamento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione a cui applicare la configurazione di campionamento AuraFlow | MODEL | Sì | - |
| `shift` | Il valore di shift da applicare alla distribuzione di campionamento (predefinito: 1.73, passo: 0.01) | FLOAT | Sì | 0.0 - 100.0 |
| `sampling` | La modalità di campionamento usata durante il patching del modello (predefinito: "flow"). Contrassegnata come opzione avanzata. | COMBO | No | "flow"<br>"img_to_img_velocity" |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello modificato con la configurazione di campionamento AuraFlow applicata | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/it.md)

---
**Source fingerprint (SHA-256):** `5c1381d2dec9ac84a7ee6cd134de444ab50f657eafd960263c63a055d0a139d6`
