# SenseNova Interleave Decode

Trasforma la cronologia interleave lasciata da SenseNova Conditioning in testo, immagini e ragionamento utilizzabili. Eseguilo alla fine del ciclo, con End Loop accumulate disabilitato, per raccogliere tutto ciò che il modello ha prodotto in un'unica passata.

## Ingressi

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip` | Modello CLIP SenseNova utilizzato per decodificare i token generati. | CLIP | Sì | - |
| `conditioning` | Conditioning interleave da SenseNova Conditioning. | CONDITIONING | Sì | - |
| `samples` | Ultimo latente pixel di KSampler, necessario quando il ciclo è terminato su una richiesta di immagine. | LATENT | No | - |

**Vincoli e comportamento:**

* Il conditioning deve provenire da SenseNova Conditioning con task `interleave` o `self-correction`; qualsiasi altro valore genera un errore.
* Quando il modello è in attesa di un'immagine, collegare l'output LATENT del sampler a `samples`.
* Le immagini di riferimento collegate all'inizio dell'esecuzione sono escluse dall'output e i nodi che utilizzano le immagini vengono saltati quando non è stata generata alcuna immagine.

## Uscite

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `text` | Testo decodificato dalla cronologia interleave, con i marcatori delle immagini sostituiti da righe vuote. | STRING |
| `images` | Le immagini generate dal modello durante l'esecuzione. | IMAGE |
| `thinking` | Il testo di ragionamento del modello, quando ne ha prodotto uno. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaInterleaveDecode/it.md)

---
**Source fingerprint (SHA-256):** `62c7ded50c1348e2242319209729a17d543d80e4d01ddf173cf8b77e4fd0be50`
