# WanAnimate2ToVideo

WanAnimate2ToVideo anima un personaggio a partire da un'immagine di riferimento trasferendo le espressioni facciali, il movimento del corpo e i gesti delle mani da un video di posa separato. Costruisce i dati di condizionamento e un latente iniziale che un campionatore per la generazione video utilizza per creare l'animazione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Il condizionamento positivo per la generazione video. | CONDITIONING | Sì | N/A |
| `negative` | Il condizionamento negativo per la generazione video. | CONDITIONING | Sì | N/A |
| `vae` | Il VAE utilizzato per codificare l'immagine di riferimento e i fotogrammi video nello spazio latente. | VAE | Sì | N/A |
| `width` | Larghezza del video in output in pixel. (predefinito: 832) | INT | Sì | da 16 a MAX_RESOLUTION (passo 16) |
| `height` | Altezza del video in output in pixel. (predefinito: 480) | INT | Sì | da 16 a MAX_RESOLUTION (passo 16) |
| `length` | Numero di fotogrammi da generare. (predefinito: 81) | INT | Sì | da 1 a MAX_RESOLUTION (passo 4) |
| `batch_size` | Numero di video da generare simultaneamente. (predefinito: 1) | INT | Sì | da 1 a 4096 |
| `reference_image` | Il personaggio da animare. Se omesso, viene utilizzata un'immagine nera. | IMAGE | No | N/A |
| `pose_video` | Il video il cui movimento viene trasferito al personaggio di riferimento. Se ha meno fotogrammi di `length`, l'ultimo fotogramma viene ripetuto per riempire i fotogrammi mancanti. | IMAGE | No | N/A |
| `clip_vision_output` | Visione CLIP dell'immagine di riferimento. | CLIP_VISION_OUTPUT | No | N/A |
| `positive_pose` | Prompt per il ramo del video di posa, che descrive il movimento anziché il personaggio. Il valore predefinito è `positive`. Usato sia per il passaggio cond sia per quello uncond. | CONDITIONING | No | N/A |
| `clip_vision_output_pose` | Visione CLIP del primo fotogramma del video di posa. Il valore predefinito è `clip_vision_output`. | CLIP_VISION_OUTPUT | No | N/A |
| `continue_motion` | Sequenza di movimento precedente da cui continuare per la coerenza temporale. Solo l'ultimo fotogramma di questa sequenza viene usato come fotogramma di movimento iniziale. | IMAGE | No | N/A |
| `video_frame_offset` | Fotogrammi da avanzare nel video di posa. Collegare all'output `video_frame_offset` del nodo precedente durante l'estensione. (predefinito: 0) | INT | Sì | da 0 a MAX_RESOLUTION |
| `pose_strength` | Ridimensiona l'influenza del video di posa sul movimento. 1.0 è il comportamento addestrato; valori inferiori indeboliscono l'aderenza, valori superiori la amplificano. 0.0 la attenua ma non la rimuove completamente. (predefinito: 1.0) | FLOAT | Sì | da 0.00 a 10.00 (passo 0.01) |
| `pose_start_percent` | Percentuale di campionamento in cui inizia l'influenza della posa. Al di fuori dell'intervallo il ramo della posa viene saltato completamente, il che velocizza anche quei passaggi. (predefinito: 0.0) | FLOAT | Sì | da 0.00 a 1.00 (passo 0.01) |
| `pose_end_percent` | Percentuale di campionamento in cui termina l'influenza della posa. Il movimento è per lo più stabilito presto, quindi ad es. 0.7 può allentare i dettagli fini mantenendo la coreografia. (predefinito: 1.0) | FLOAT | Sì | da 0.00 a 1.00 (passo 0.01) |
| `reference_image_strength` | Ridimensiona quanto fortemente i fotogrammi generati prestano attenzione al fotogramma latente dell'immagine di riferimento. Valori inferiori a 1.0 allentano l'aderenza a identità/aspetto (ad es. per consentire al prompt di ridefinire lo stile), valori superiori la stringono contro la deriva. (predefinito: 1.0) | FLOAT | Sì | da 0.00 a 10.00 (passo 0.01) |

**Note di validazione:**

- `pose_start_percent` non deve essere maggiore di `pose_end_percent`; in caso contrario il nodo genera un ValueError.
- Se viene fornito `pose_video`, il suo numero di fotogrammi deve essere maggiore di `video_frame_offset`; in caso contrario il nodo genera un ValueError.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `positive` | Condizionamento positivo per il campionamento, con l'immagine di riferimento, la maschera e i dati di posa opzionali allegati. | CONDITIONING |
| `negative` | Condizionamento negativo per il campionamento, con la stessa immagine di riferimento, maschera e dati di posa opzionali allegati. | CONDITIONING |
| `latent` | Latente iniziale riempito di zeri per il campionatore video; i primi `trim_latent` fotogrammi dovrebbero essere rimossi prima della decodifica. | LATENT |
| `trim_latent` | Numero di fotogrammi latenti che dovrebbero essere rimossi prima della decodifica. | INT |
| `trim_image` | Numero di fotogrammi immagine sovrapposti quando si estende un video. | INT |
| `video_frame_offset` | Fotogrammi da avanzare nel video di posa; equivale all'offset di input regolato più il numero di fotogrammi generati. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2ToVideo/it.md)

---
**Source fingerprint (SHA-256):** `7e1f497983ab63a68e5ef5439b3ef4e9295f79f78530c9dc5de16a8238475f05`
