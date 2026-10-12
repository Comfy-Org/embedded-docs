# AudioMerge

Il nodo AudioMerge combina due tracce audio sovrapponendo le loro forme d'onda. Adatta automaticamente le frequenze di campionamento di entrambi gli input audio e regola le loro lunghezze per renderle uguali prima dell'unione. Il nodo fornisce diversi metodi matematici per combinare i segnali audio e garantisce che l'output rimanga entro livelli di volume accettabili.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio1` | Primo input audio da unire | AUDIO | Sì | - |
| `audio2` | Secondo input audio da unire | AUDIO | Sì | - |
| `merge_method` | Il metodo utilizzato per combinare le forme d'onda audio. | COMBO | Sì | `"add"`<br>`"mean"`<br>`"subtract"`<br>`"multiply"` |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `AUDIO` | L'output audio unito contenente la forma d'onda combinata e la frequenza di campionamento | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/it.md)

---
**Source fingerprint (SHA-256):** `3bb8c223e9a5155b5e60f901e8653c6654336a10a56d25ba7a3c5e8f5382ad27`
