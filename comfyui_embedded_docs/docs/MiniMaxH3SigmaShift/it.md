# ModelSamplingMiniMaxH3

Imposta i valori di spostamento del flusso video e audio per un modello MiniMax H3. Lo spostamento video controlla il programma sigma del sampler, ed entrambi i valori di spostamento vengono passati al transformer interno del modello, che li usa per derivare il programma audio dalla griglia di base condivisa.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello a cui applicare la patch di spostamento sigma. Il nodo clona il modello, quindi l'originale rimane invariato. | MODEL | Sì | - |
| `shift_video` | Il valore di spostamento del flusso video. Determina il programma sigma del sampler. Predefinito: 12.0. | FLOAT | Sì | 0.01 a 100.0 |
| `shift_audio` | Il valore di spostamento del flusso audio. È usato dal modello per derivare il programma audio. Predefinito: 3.0. | FLOAT | Sì | 0.01 a 100.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `MODEL` | Il modello clonato con le impostazioni di spostamento sigma video e audio applicate. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3SigmaShift/it.md)

---
**Source fingerprint (SHA-256):** `0f731585cc1a9c87a3e54341757c4cf4e490d1d4718ecf458bd2b9f4378af63f`
