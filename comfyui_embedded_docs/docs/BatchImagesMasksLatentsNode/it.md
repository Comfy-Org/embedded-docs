# BatchImagesMasksLatentsNode

Il nodo Batch Images/Masks/Latents combina più input dello stesso tipo in un unico batch. Rileva automaticamente se gli input sono immagini, maschere o rappresentazioni latent e utilizza il metodo di batching appropriato. Questo è utile per preparare più elementi da elaborare con nodi che accettano input in batch.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `inputs` | Un elenco dinamico di input da combinare in un batch. È possibile aggiungere da 1 a 50 elementi. Tutti gli elementi devono essere dello stesso tipo (tutte immagini, tutte maschere o tutti latent). | IMAGE, MASK o LATENT | Sì | Da 1 a 50 input |

**Nota:** Il nodo determina automaticamente il tipo di dato (IMAGE, MASK o LATENT) in base al primo elemento della lista `inputs`. Tutti gli elementi successivi devono corrispondere a questo tipo. Il nodo fallirà se si tenta di mescolare tipi di dato diversi.

**Comportamento aggiuntivo in base al tipo di input:**
- **Immagini**: quando si raggruppano immagini in batch, il nodo aggiunge padding alle immagini con un numero inferiore di canali di colore per allinearle al numero massimo di canali tra tutti gli input (il valore di padding è 1.0). Ridimensiona inoltre tutte le immagini per corrispondere alle dimensioni della prima immagine utilizzando l'interpolazione bilineare.
- **Maschere**: quando si raggruppano maschere in batch, il nodo ridimensiona tutte le maschere per corrispondere alle dimensioni della prima maschera utilizzando l'interpolazione bilineare.
- **Latent**: quando si raggruppano latent in batch, il nodo rimodella tutti i tensori latent per corrispondere alle dimensioni dei campioni del primo latent. Combina inoltre i valori `batch_index` di ciascun latent, estendendo l'elenco con indici sequenziali se un latent è privo di `batch_index`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Un singolo output in batch. Il tipo di dato corrisponde al tipo di input (IMAGE in batch, MASK in batch o LATENT in batch). | IMAGE, MASK o LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesMasksLatentsNode/it.md)

---
**Source fingerprint (SHA-256):** `9f82b036c99577ebcda6de647c662def572ae1f01bd78dca1a0ab32f4698e09e`
