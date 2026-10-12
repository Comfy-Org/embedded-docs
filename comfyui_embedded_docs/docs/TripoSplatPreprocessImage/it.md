# TripoSplatPreprocessImage

Questo nodo ritaglia ciascuna immagine di input in un quadrato centrato su sfondo nero e aggiunge padding per raggiungere la dimensione di output specificata. È progettato per preparare le immagini al modello 3D TripoSplat garantendo un'inquadratura quadrata coerente e un'erosione opzionale del matte alpha per prevenire artefatti ai bordi.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine o le immagini di input da preprocessare. | IMAGE | Sì | - |
| `mask` | Maschera alpha per l'immagine, usata per determinare la regione di ritaglio. | MASK | Sì | - |
| `erode_radius` | Erode il matte alpha di questo raggio in pixel prima del ritaglio (evita il bleed dei bordi). Predefinito: 1. Imposta a 0 per disabilitare l'erosione. | INT | Sì | da 0 a 16 |
| `size` | Dimensione immagine quadrata. Il modello è addestrato a 1024; altre dimensioni funzionano ma sono fuori distribuzione. Predefinito: 1024. | INT | Sì | da 256 a 4096 (passo di 16) |

**Nota:** L'input `mask` è obbligatorio e deve essere fornito. Se la maschera ha una dimensione batch diversa da quella dell'immagine, viene ripetuta automaticamente per corrispondere. Se le dimensioni della maschera differiscono da quelle dell'immagine, la maschera viene ridimensionata per corrispondere all'immagine usando l'interpolazione bilineare. La dimensione di output viene automaticamente arrotondata per difetto al multiplo di 16 più vicino (minimo 16) per garantire la compatibilità con i requisiti di stride della patch DINOv3 e del VAE Flux2. Il nodo genera un errore se la maschera non contiene pixel in primo piano (maschera vuota). Quando `erode_radius` è 0, non viene applicata alcuna erosione. Il ritaglio quadrato è centrato sul bounding box alpha della maschera e dimensionato a 1,2 volte la dimensione maggiore del bounding box; qualsiasi area esterna ai limiti dell'immagine viene riempita di nero.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine o le immagini preprocessate, ritagliate in un quadrato centrato su sfondo nero con padding, alla risoluzione `size` richiesta. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/it.md)

---
**Source fingerprint (SHA-256):** `ec66941846398ee6637576b11ae9d2f9576f6b05ed2ef730cdbf99a68fe9b838`
