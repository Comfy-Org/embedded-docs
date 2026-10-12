# BatchLatentsNode

Il nodo Batch Latents combina più input latenti in un unico batch. Accetta un numero variabile di campioni latenti e li unisce lungo la dimensione batch, in modo che possano essere elaborati insieme dai nodi successivi. Il nodo unisce inoltre i metadati dell'indice di batch di tutti gli input nell'output combinato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `latents` | Un insieme di campioni latenti da combinare in un unico batch. È necessario fornire almeno un latente ed è possibile aggiungerne fino a 50. Il nodo crea automaticamente gli slot di input (`latent_1`, `latent_2`, e così via) man mano che si collegano più latenti. | LATENT | Sì | da 1 a 50 input |

**Nota:** È necessario fornire almeno un input latente affinché il nodo funzioni. Il nodo crea automaticamente slot di input man mano che si collegano più latenti, fino a un massimo di 50. Ogni input latente viene rimodellato per corrispondere alla forma del campione del primo latente prima di essere combinato, e a qualsiasi latente privo di metadati dell'indice di batch viene assegnato un indice di batch sequenziale. Gli input latenti vengono uniti lungo la dimensione batch per produrre il risultato combinato.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Un singolo output latente contenente tutti gli input latenti combinati in un unico batch, insieme ai relativi metadati dell'indice di batch uniti. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/it.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`
