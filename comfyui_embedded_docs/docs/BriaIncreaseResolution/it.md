# BriaIncreaseResolution

Bria Increase Resolution esegue l'upscaling di un'immagine di input di 2x o 4x usando il servizio di upscaling immagini di Bria, preservando il contenuto originale. Il nodo carica l'immagine, la invia per l'elaborazione al servizio Bria, attende il risultato e restituisce l'immagine sottoposta a upscaling.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da sottoporre a upscaling. | IMAGE | Sì | Immagine singola |
| `desired_increase` | Moltiplicatore di risoluzione. L'output deve rientrare entro 8192 pixel su ciascun lato. | COMBO | Sì | "2"<br>"4" |
| `auto_downscale` | Abbassa automaticamente il moltiplicatore e, se ciò non basta ancora, esegue il downscaling dell'immagine di input quando l'output supererebbe il limite. (predefinito: False) | BOOLEAN | Sì | True<br>False |
| `moderation` | Impostazioni di moderazione. Se impostato su "true", abilita le sotto-opzioni `visual_input_moderation` e `visual_output_moderation`, entrambe predefinite a False. | DYNAMIC_COMBO | Sì | "false"<br>"true" |

Note:
- Quando `moderation` è impostato su "true", le sotto-opzioni `visual_input_moderation` e `visual_output_moderation` diventano disponibili, entrambe predefinite a False. Esse controllano la moderazione dell'immagine di input e del contenuto dell'immagine di output.
- Il nodo impone un lato massimo di output di 8192 pixel. Se il moltiplicatore selezionato supera questo limite e `auto_downscale` è disabilitato, viene generato un errore. Abilitando `auto_downscale`, il nodo può usare automaticamente un moltiplicatore inferiore o eseguire il downscaling dell'immagine di input.
- Bria dapprima ingrandisce il lato corto dell'immagine di input portandolo ad almeno 224 pixel prima di eseguire l'upscaling. Immagini troppo allungate possono attivare un errore che richiede di ritagliarle in una forma più quadrata.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine sottoposta a upscaling restituita dal servizio Bria. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/it.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
