# LTXV Fotogrammi chiave generati in guide

Il nodo LTXV Generated Keyframes to Guides fissa i keyframe generati da una fase precedente come guide immagine congelate su una canvas successiva. Decodifica i keyframe come frame autonomi, li ridimensiona se necessario e li scrive con una maschera di rumore pari a 0 in modo che non vengano nuovamente denoizzati. Dopo un upscale temporale, gli indici registrati vengono scalati dalla canvas su cui sono stati generati a questa; usa `override_frame_indices` per impostare le posizioni esplicitamente.

## Input

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Conditioning positivo a cui aggiungere le guide dei keyframe. | CONDITIONING | Sì | |
| `negative` | Conditioning negativo a cui aggiungere le guide dei keyframe. | CONDITIONING | Sì | |
| `vae` | Il VAE usato per decodificare i keyframe se è necessario ridimensionarli. | VAE | Sì | |
| `latent` | Il latent video di destinazione a cui aggiungere le guide, ad es. quello con upscale temporale. | LATENT | Sì | |
| `keyframes` | L'output keyframes di LTXV Separate Generated Keyframes, che contiene l'indice del frame in pixel in cui è stato generato ciascun keyframe. | LATENT | Sì | |
| `strength` | Forza della guida. 1.0 è un fissaggio rigido; valori inferiori lo allentano. (predefinito: 1.0) | FLOAT | Sì | 0.0 - 10.0 (passo 0.01) |
| `override_frame_indices` | Opzionale — fissa a questi frame in pixel invece che alle posizioni registrate (o scalate automaticamente). Fornisci un indice per keyframe. Lascia vuoto per riutilizzare le posizioni registrate, oppure per scalarle quando la canvas di destinazione ha una lunghezza diversa (ad es. dopo temporal x2). (predefinito: "") | STRING | No | |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `positive` | Conditioning positivo con i keyframe fissati come guide immagine. | CONDITIONING |
| `negative` | Conditioning negativo con i keyframe fissati come guide immagine. | CONDITIONING |
| `latent` | Latent video di destinazione con i keyframe aggiunti come guide congelate. | LATENT |

## Note

- L'input `keyframes` deve essere collegato all'output keyframes di LTXV Separate Generated Keyframes. Il nodo genera un errore se il latent non contiene le posizioni dei keyframe generati.
- Gli input conditioning `positive` e `negative` devono provenire dagli output positive e negative di LTXV Separate Generated Keyframes. Il nodo genera un errore se il conditioning positivo contiene ancora keyframe generati.
- L'input `latent` deve essere un latent video semplice (tensore 5D). Le guide devono essere aggiunte prima di unire i latent video e audio con Concat AV Latent.
- È supportata solo una dimensione del batch pari a 1. Ogni guida è codificata da una singola immagine, quindi non può variare tra gli elementi del batch.
- Il numero di keyframe nel latent `keyframes` deve corrispondere al numero di posizioni registrate; in caso contrario viene generato un errore.
- Se `override_frame_indices` viene lasciato vuoto, vengono utilizzate le posizioni registrate. Se la canvas di destinazione ha un numero di frame diverso dalla canvas su cui sono stati generati i keyframe, gli indici registrati vengono scalati automaticamente.
- Se viene fornito `override_frame_indices`, deve contenere un indice intero per keyframe, separato da virgole o spazi. Gli indici devono essere univoci e compresi tra 1 e (numero di frame in pixel nel latent di destinazione - 1). In caso contrario viene generato un errore.
- Se un qualsiasi indice finale di keyframe è maggiore o uguale al numero di frame in pixel nel latent di destinazione, il nodo genera un errore. Ciò può verificarsi quando la destinazione è stata ridimensionata temporalmente dopo la generazione dei keyframe.
- Il parametro `strength` ha un minimo di 0.0 e un massimo di 10.0.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/it.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`
