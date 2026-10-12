# HeyGenTalkingPhotoNode

Anima un'immagine fissa di una persona trasformandola in un video parlante con sincronizzazione labiale tramite la tecnologia Avatar IV di HeyGen. Puoi guidare l'animazione con uno script testuale che HeyGen converte in parlato, oppure fornire il tuo audio affinché l'avatar sincronizzi il labiale.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | Immagine di una persona da animare. Ridimensionata automaticamente se più grande di 2K. | IMAGE | Sì | - |
| `speech` | Guida l'avatar con uno script testuale (sintesi vocale di HeyGen) oppure con il tuo audio. | DYNAMIC_COMBO | Sì | `"script"`<br>`"audio"` |
| `resolution` | Risoluzione video in output (predefinito: `"1080p"`). | COMBO | No | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Rapporto d'aspetto in output. `"auto"` segue l'immagine di input (predefinito: `"auto"`). | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `expressiveness` | Quanto sono espressivi il volto animato e i gesti (predefinito: `"low"`). | COMBO | No | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Non viene inviato a HeyGen; modificalo per forzare una nuova esecuzione (predefinito: 42). | INT | No | 0 to 2147483647 |

### Input dello script

Mostrati quando `speech` è `"script"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `text` | Testo che l'avatar deve pronunciare (fino a 5000 caratteri). Il parlato generato deve durare almeno 1 secondo. (predefinito: vuoto) | STRING | Sì | Da 1 a 5000 caratteri |
| `voice` | Voce per lo script (le voci più popolari di HeyGen). | COMBO | Sì | Diverse opzioni disponibili |
| `custom_voice_id` | ID voce HeyGen opzionale. Se impostato, sostituisce la voce selezionata sopra. È possibile usare qualsiasi voce della libreria HeyGen (oltre 2000). (predefinito: vuoto) | STRING | No | - |
| `voice_speed` | Moltiplicatore della velocità del parlato (predefinito: 1.0). | FLOAT | No | Da 0.5 a 1.5 (incremento 0.05) |

### Input audio

Mostrati quando `speech` è `"audio"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `audio` | Audio che l'avatar deve sincronizzare labialmente, fino a 10 minuti. | AUDIO | Sì | Fino a 10 minuti |

Nota: quando `speech` è `"script"`, è necessario specificare `text` e fornire una voce tramite il selettore `voice` (scegliendo una voce diversa da quella predefinita dell'avatar) oppure un `custom_voice_id`. Quando `speech` è `"audio"`, al suo posto è obbligatorio `audio`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Video generato della foto parlante animata con parlato sincronizzato labialmente. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTalkingPhotoNode/it.md)

---
**Source fingerprint (SHA-256):** `2181066a8c6191cfcaa15ece4f89a16c37e76aa22763d6df4007baa20336f05a`
