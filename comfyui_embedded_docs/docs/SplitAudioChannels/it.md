# Dividi Canali Audio

Il nodo SplitAudioChannels separa l'audio stereo nei singoli canali sinistro e destro. Riceve in input un audio stereo con due canali e restituisce due flussi audio separati, uno per il canale sinistro e uno per il canale destro.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio` | L'input audio stereo da separare in canali | AUDIO | Sì | - |

**Nota:** L'audio di input deve avere esattamente due canali (stereo). Il nodo genererà un errore se l'audio di input ha un solo canale.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `left` | L'audio del canale sinistro separato | AUDIO |
| `right` | L'audio del canale destro separato | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/it.md)

---
**Source fingerprint (SHA-256):** `c6e6ecb219e0cb47b003ec9c28fdc060ef83bf1c8bd77d9fb29a088d55a9ab3f`
