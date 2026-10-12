# WanSCAILToVideo

Il nodo WanSCAILToVideo prepara il condizionamento e uno spazio latente vuoto per la generazione video con i modelli video SCAIL e SCAIL-2. Elabora input opzionali come immagini di riferimento, video di posa, output CLIP vision, maschere di identità colorate e blocchi di frame precedenti, incorporandoli nel condizionamento positivo e negativo. Il nodo restituisce il condizionamento modificato e un tensore latente vuoto delle dimensioni video specificate, pronto per il campionamento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `positive` | L'input di condizionamento positivo. | CONDITIONING | Sì | - |
| `negative` | L'input di condizionamento negativo. | CONDITIONING | Sì | - |
| `vae` | Il modello VAE utilizzato per codificare immagini e frame video. | VAE | Sì | - |
| `width` | La larghezza del video di output in pixel (predefinito: 512). I valori aumentano a passi di 32. | INT | Sì | da 32 a MAX_RESOLUTION |
| `height` | L'altezza del video di output in pixel (predefinito: 896). I valori aumentano a passi di 32. | INT | Sì | da 32 a MAX_RESOLUTION |
| `length` | Il numero di frame nel video (predefinito: 81). I valori aumentano a passi di 4. | INT | Sì | da 1 a MAX_RESOLUTION |
| `batch_size` | Il numero di video da generare in un batch (predefinito: 1). | INT | Sì | da 1 a 4096 |
| `pose_video` | Video utilizzato per il condizionamento della posa. Verrà ridimensionato a metà della risoluzione del video principale. | IMAGE | No | - |
| `pose_video_mask` | Solo SCAIL-2. Video maschera SAM3 colorato per identità alla stessa risoluzione di `pose_video`. | IMAGE | No | - |
| `replacement_mode` | Solo SCAIL-2. False = Modalità animazione (`pose_video_mask` deve avere sfondo nero). True = Modalità sostituzione (`pose_video_mask` deve avere sfondo bianco). (predefinito: False) | BOOLEAN | No | - |
| `pose_strength` | Intensità del latente di posa. (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 10.0 |
| `pose_start` | Passo iniziale del condizionamento della posa. (predefinito: 0.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `pose_end` | Passo finale del condizionamento della posa. (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `reference_image` | Immagine di riferimento. La prima immagine è il riferimento principale (combina tutte le identità su di essa). SCAIL-2: le immagini extra del batch vengono usate come viste aggiuntive (vista posteriore, primo piano, sfondo occluso), ciascuna necessita di una `reference_image_mask` corrispondente nel colore di quell'identità. | IMAGE | No | - |
| `reference_image_mask` | Solo SCAIL-2. Maschera di riferimento colorata, con batch corrispondente a `reference_image` (la prima = maschera di riferimento principale, le restanti = maschere delle identità per le immagini di riferimento aggiuntive). | IMAGE | No | - |
| `clip_vision_output` | Caratteristiche CLIP vision per il condizionamento. Il modello è addestrato con ridimensionamento stretch alle proporzioni. | CLIP_VISION_OUTPUT | No | - |
| `video_frame_offset` | Frame di output cumulativo da cui inizia questo blocco. Collegare dall'output `video_frame_offset` del blocco precedente. (predefinito: 0) | INT | Sì | da 0 a MAX_RESOLUTION |
| `previous_frame_count` | Frame di coda di `previous_frames` da ancorare. SCAIL-2 è addestrato a 5 (blocchi da 81 frame, passo di 76 frame). (predefinito: 5). I valori aumentano a passi di 4. | INT | Sì | da 1 a MAX_RESOLUTION |
| `previous_frames` | Solo SCAIL-2. Output decodificato completo del blocco precedente. Solo gli ultimi `previous_frame_count` vengono usati come ancora di estensione. | IMAGE | No | - |

**Nota:** Gli input `pose_video` e `pose_video_mask` vengono troncati insieme al più corto dei due, e vengono elaborati solo per i primi `length` frame. Se uno dei due input è più corto o uguale a `video_frame_offset`, viene ignorato completamente. Il `pose_video` viene ridimensionato a metà della risoluzione del video principale prima della codifica, e il latente di posa codificato viene moltiplicato per `pose_strength` e applicato al condizionamento solo tra i passi temporali `pose_start` e `pose_end`. Se viene fornito `pose_video_mask`, il video maschera colorato viene ridimensionato a metà risoluzione e convertito in una maschera di guida a 28 canali, che viene aggiunta sia al condizionamento positivo sia a quello negativo.

**Nota:** Quando viene fornito `reference_image`, ogni immagine nel batch viene codificata individualmente in un latente e incorporata sia nel condizionamento positivo sia in quello negativo. La prima immagine è il riferimento principale; le immagini aggiuntive vengono usate come viste aggiuntive, ciascuna necessita di una `reference_image_mask` corrispondente. `reference_image_mask` viene usato solo quando è fornito anche `reference_image`; quando entrambi sono forniti, dalle maschere viene anche costruita una maschera di riferimento a 28 canali che collega i frame di riferimento alle identità, e viene aggiunta al condizionamento. In Modalità sostituzione (`replacement_mode=True`), l'immagine di riferimento viene composta su sfondo nero usando la maschera dell'immagine di riferimento come maschera alpha. Quando viene fornito `clip_vision_output`, viene applicato sia al condizionamento positivo sia a quello negativo.

**Nota:** Quando viene fornito `previous_frames`, solo gli ultimi `previous_frame_count` frame vengono usati come ancora di estensione, e `video_frame_offset` viene regolato di conseguenza (ridotto del numero di frame ancorati, con valore minimo 0). I frame ancorati vengono codificati e scritti all'inizio del latente di output, e viene inclusa una maschera di rumore in modo che quei frame rimangano invariati durante la generazione.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `positive` | Il condizionamento positivo modificato, che può contenere latenti di immagini di riferimento incorporati, output CLIP vision, latenti di video di posa, maschere di guida, maschere di riferimento o latenti di frame precedenti. | CONDITIONING |
| `negative` | Il condizionamento negativo modificato, che può contenere latenti di immagini di riferimento incorporati, output CLIP vision, latenti di video di posa, maschere di guida, maschere di riferimento o latenti di frame precedenti. | CONDITIONING |
| `latent` | Un tensore latente vuoto di forma `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. Quando viene fornito `previous_frames`, il latente viene parzialmente riempito con i frame precedenti codificati e viene inclusa una maschera di rumore. | LATENT |
| `video_frame_offset` | Offset regolato + `length`. Collegare nel blocco successivo per la generazione video sequenziale. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/it.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
