# RecraftStyleV3InfiniteStyleLibrary

Questo nodo consente di selezionare uno stile dalla Infinite Style Library di Recraft utilizzando un UUID preesistente. Recupera le informazioni sullo stile in base all'identificatore di stile fornito e le restituisce per l'utilizzo in altri nodi Recraft.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `style_id` | UUID dello stile dalla Infinite Style Library. | STRING | Sì | Qualsiasi UUID valido |

**Nota:** L'input `style_id` non può essere vuoto. Se viene fornita una stringa vuota, il nodo genererà un'eccezione.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `recraft_style` | L'oggetto stile selezionato dalla Infinite Style Library di Recraft | STYLEV3 |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/it.md)

---
**Source fingerprint (SHA-256):** `4554acaaba9e83373d6fb44ea5465175182efcf7c9220c2328c4749c2febd40f`
