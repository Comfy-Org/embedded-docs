# Unisci Canali Audio

Il nodo Join Audio Channels combina due ingressi audio mono separati in un'unica uscita audio stereo. Prende un canale sinistro e un canale destro, assicura che abbiano frequenze di campionamento e lunghezze compatibili, e li unisce in una forma d'onda audio a due canali.

## Input
| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio_left` | I dati audio mono da usare come canale sinistro nell'audio stereo risultante. | AUDIO | Sì |  |
| `audio_right` | I dati audio mono da usare come canale destro nell'audio stereo risultante. | AUDIO | Sì |  |

**Nota:** Entrambi i flussi audio in ingresso devono essere mono (a canale singolo). Se hanno frequenze di campionamento diverse, il canale con frequenza inferiore verrà ricampionato automaticamente per corrispondere a quella superiore. Se i flussi audio hanno lunghezze diverse, verranno tagliati alla lunghezza del più breve.

## Output
| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `audio` | L'audio stereo risultante, contenente i canali sinistro e destro uniti. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinAudioChannels/it.md)

---
**Source fingerprint (SHA-256):** `8a68e59e0d037882e9dd87d93b38673a0de3072bab2c574c7a9750de93b50a68`
