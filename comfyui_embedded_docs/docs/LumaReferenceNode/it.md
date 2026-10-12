# LumaReferenceNode

Questo nodo contiene un'immagine e un valore di peso da usare con il nodo Luma Generate Image. Crea una catena di riferimento che può essere passata ad altri nodi Luma per influenzare la generazione delle immagini. Il nodo può iniziare una nuova catena di riferimento oppure aggiungersi a una esistente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | Immagine da usare come riferimento. | IMAGE | Sì | - |
| `weight` | Peso del riferimento immagine (predefinito: 1.0). | FLOAT | Sì | 0.0 - 1.0 |
| `luma_ref` | Catena di riferimento Luma esistente opzionale a cui aggiungere il riferimento. | LUMA_REF | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `luma_ref` | La catena di riferimento Luma contenente l'immagine e il peso. | LUMA_REF |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/it.md)

---
**Source fingerprint (SHA-256):** `f7e7789f2f19cac41cb9e55d21f10fef3012b10dcdbd59eb79f97fe5c2a944b7`
