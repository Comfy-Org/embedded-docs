# VEED Lipsync 2.0

Risincronizza la bocca di un parlante in un video con una nuova traccia vocale tramite VEED Lipsync. Usalo per doppiare una clip o sostituirne il dialogo mantenendo il video originale. L'output mantiene la risoluzione del video a 25 fps e ha la stessa durata dell'audio, con un solo parlante per video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da utilizzare. Selezionando un modello vengono mostrati i parametri specifici: `video`, `audio` e `seed`. | DYNAMIC_COMBO | Sì | `"lipsync-2.0"` |
| `video` | Filmato di un solo parlante rivolto verso la telecamera. Se è più corto dell'audio, viene riprodotto in avanti e all'indietro fino alla fine dell'audio. | VIDEO | Sì | - |
| `audio` | Nuovo parlato, fino a 600 secondi. Determina la durata del video. | AUDIO | Sì | Fino a 600 secondi |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 42) | INT | Sì | 0 - 2147483647 |

Il nodo si interrompe con un errore quando la traccia vocale dura più di 600 secondi o quando il processo VEED fallisce.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `VIDEO` | Il video risincronizzato: il filmato originale con la bocca sincronizzata al nuovo parlato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedLipsyncNode/it.md)

---
**Source fingerprint (SHA-256):** `1a1e854b6923b5bad0fd6f3a79e76c70231dee31a12e9cf0b22be6bdcc741168`
