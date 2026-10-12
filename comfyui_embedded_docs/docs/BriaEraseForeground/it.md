# Bria Cancella primo piano

Questo nodo rimuove il primo piano di un'immagine con Bria e genera un nuovo sfondo al suo posto. Tutto ciò che Bria identifica come primo piano viene rimosso, non solo le persone, e i pixel non modificati vengono preservati. Il risultato viene renderizzato nuovamente a una dimensione standard vicina a 1 megapixel.

Questo è un nodo API a pagamento che viene eseguito sul servizio di Bria, quindi le tue credenziali API Comfy vengono utilizzate per ogni esecuzione.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine il cui primo piano viene rimosso e sostituito con uno sfondo generato. Vengono inviati solo i canali di colore; qualsiasi canale alfa viene scartato prima del caricamento. | IMAGE | Sì | - |
| `moderation` | Impostazioni di moderazione. Seleziona `"false"` per inviare l'immagine senza flag di moderazione, oppure `"true"` per mostrare gli interruttori di moderazione dei contenuti riportati di seguito. Predefinito: `"false"`. | DYNAMIC_COMBO | Sì | `"false"`<br>`"true"` |

### Input per `"false"`

Nessun input aggiuntivo. La richiesta viene inviata senza flag di moderazione dei contenuti.

### Input per `"true"`

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Abilita la moderazione dei contenuti sull'immagine di input. Predefinito: false. | BOOLEAN | Sì | true<br>false |
| `visual_output_moderation` | Abilita la moderazione dei contenuti sull'immagine di output generata. Predefinito: false. | BOOLEAN | Sì | true<br>false |

### Note

- L'output viene renderizzato nuovamente a una dimensione standard vicina a 1 megapixel, quindi l'immagine restituita può differire nelle dimensioni da quella di input.
- Questo nodo è un nodo API a pagamento; ogni esecuzione costa circa 0,0572 USD.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `IMAGE` | L'immagine di input con il primo piano cancellato e un nuovo sfondo generato al suo posto. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseForeground/it.md)

---
**Source fingerprint (SHA-256):** `4d8c3c5eed97c648b1191ec41931c97caa17e98a8edd1c054ed63e80cc671b05`
