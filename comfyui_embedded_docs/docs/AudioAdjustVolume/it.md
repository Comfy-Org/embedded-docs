# AudioAdjustVolume

Il nodo AudioAdjustVolume modifica il volume dell'audio applicando regolazioni di volume in decibel (dB). Riceve un input audio e applica un fattore di guadagno in base al livello di volume specificato, dove i valori positivi aumentano il volume e quelli negativi lo diminuiscono. Il nodo restituisce l'audio modificato con la stessa frequenza di campionamento dell'originale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio` | L'input audio da elaborare | AUDIO | Sì | - |
| `volume` | Regolazione del volume in decibel (dB). 0 = nessuna modifica, +6 = doppio, -6 = metà, ecc. (predefinito: 1) | INT | Sì | -100 a 100 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `audio` | L'audio elaborato con il livello di volume regolato | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/it.md)

---
**Source fingerprint (SHA-256):** `8c19625104901a0c57021b1a775fdf287c8bd0fb1fd535809e1983b1949ca752`
