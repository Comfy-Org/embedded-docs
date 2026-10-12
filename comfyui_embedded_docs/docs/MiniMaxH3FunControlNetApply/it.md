# MiniMaxH3FunControlNetApply

Questo nodo applica un MiniMax H3 Fun ControlNet a un modello text-to-video come patch del modello. Può usare un video di controllo opzionale e una maschera opzionale per guidare la generazione, e restituisce una copia patchata del modello per il campionamento successivo. Quando la forza è impostata su 0, oppure quando non viene fornito né un video di controllo né una maschera, il modello di input viene restituito invariato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello di diffusione a cui viene applicata la patch MiniMax H3 Fun ControlNet. | MODEL | Sì | N/A |
| `model_patch` | La patch MiniMax H3 Fun ControlNet i cui segnali di controllo vengono iniettati nel modello; deve essere compatibile con il `model` specificato. | MODEL_PATCH | Sì | N/A |
| `vae` | VAE utilizzato per codificare i fotogrammi del video di controllo e del video sorgente nello spazio latente previsto dal modello. | VAE | Sì | N/A |
| `strength` | Forza complessiva dell'effetto ControlNet. Quando impostata su 0, il nodo non fa nulla e restituisce il modello di input invariato. (predefinito: 1.0) | FLOAT | Sì | min 0.0, max 10.0, step 0.01 |
| `start_percent` | Inizio dell'intervallo di campionamento, espresso come percentuale della schedulazione di campionamento, durante il quale ControlNet è attivo. Viene convertito internamente nel valore sigma equivalente. Questa è un'impostazione avanzata. (predefinito: 0.0) | FLOAT | Sì | min 0.0, max 1.0, step 0.001 |
| `end_percent` | Fine dell'intervallo di campionamento, espresso come percentuale della schedulazione di campionamento, durante il quale ControlNet è attivo. Viene convertito internamente nel valore sigma equivalente. Questa è un'impostazione avanzata. (predefinito: 1.0) | FLOAT | Sì | min 0.0, max 1.0, step 0.001 |
| `control_video` | Fotogrammi video opzionali usati come suggerimento visivo per ControlNet. I fotogrammi vengono ridimensionati per corrispondere al video generato e codificati con il `vae`. | IMAGE | No | N/A |
| `mask` | 1 contrassegna le regioni da rigenerare. I valori della maschera superiori a 0.5 vengono trattati come regioni contrassegnate. | MASK | No | N/A |
| `source_video` | Video dietro la maschera; letto solo quando viene fornita una maschera. | IMAGE | No | N/A |

Nota: Perché la patch abbia effetto, `strength` deve essere maggiore di 0 e almeno uno tra `control_video` e `mask` deve essere fornito. `source_video` viene ignorato a meno che non venga fornito `mask`; se `mask` viene fornito senza `source_video`, il contenuto dietro le regioni mascherate viene trattato come nero. Quando vengono forniti sia `control_video` sia `mask`, il suggerimento di controllo combina le caratteristiche del video di controllo con il contenuto sorgente mascherato.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `model` | Una copia patchata del modello di input con il MiniMax H3 Fun ControlNet applicato. Se `strength` è 0, o non viene fornito alcun video di controllo o maschera, il modello originale viene restituito invariato. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3FunControlNetApply/it.md)

---
**Source fingerprint (SHA-256):** `e907fb8e5ae60663d1d10b315985695ee5d49397fef6bd76b0e723637457a74a`
