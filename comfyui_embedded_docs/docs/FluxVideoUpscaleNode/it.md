# FluxVideoUpscaleNode

Flux Video Upscale esegue l'upscaling di una clip video da 1,5 a 3 volte usando la super-risoluzione FLUX. In modalità creative ripristina e inventa dettagli fini; in modalità precise rende più nitida la sorgente senza modificarla.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Clip sorgente da 1 a 20 secondi con proporzioni comprese tra 1:4 e 4:1. L'output viene renderizzato a 24 fps e limitato a circa 14,4 megapixel per fotogramma. | VIDEO | Sì | Durata da 1 a 20 secondi; proporzioni tra 1:4 e 4:1; minimo 64x64 pixel |
| `upscale_factor` | Dimensione dell'output rispetto alla sorgente. Le sorgenti molto grandi vengono ingrandite di un fattore inferiore a quello richiesto a causa del limite per fotogramma. (predefinito: 2.0) | FLOAT | Sì | da 1.5 a 3.0 (passo 0.1) |
| `mode` | 'creative' ripristina e inventa dettagli fini, ideale per filmati generati, texture e paesaggi. 'precise' rende più nitida la sorgente senza modificarla, per volti, prodotti e filmati reali. (predefinito: "creative") | COMBO | Sì | "creative"<br>"precise" |
| `prompt` | Descrizione opzionale della clip che guida il dettaglio migliorato. Lasciare vuoto per un upscaling neutro. (predefinito: vuoto) | STRING | Sì | Testo multilinea |
| `auto_downscale` | Ridimensiona automaticamente verso il basso le sorgenti con area superiore a 3840x2160 pixel per rientrare nel limite di input. Le proporzioni vengono preservate; i video più piccoli non vengono modificati. (predefinito: true) | BOOLEAN | Sì | true<br>false |
| `safety_tolerance` | Tolleranza di moderazione, 0 è il valore più restrittivo. (predefinito: 2, parametro avanzato) | INT | Sì | da 0 a 4 |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; FLUX sceglie il proprio seed, quindi i risultati effettivi sono non deterministici indipendentemente da questo valore. (predefinito: 42) | INT | Sì | da 0 a 4294967295 |

Nota: il video sorgente deve durare tra 1 e 20 secondi, avere una dimensione di almeno 64x64 pixel e proporzioni comprese tra 1:4 e 4:1. Se `auto_downscale` è disabilitato e l'area del video supera 3840x2160 pixel, il nodo genera un errore. Il video di output viene renderizzato a 24 fps e limitato a circa 14,4 megapixel per fotogramma, quindi sorgenti molto grandi possono essere ingrandite di un fattore inferiore a quello richiesto.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | La clip video con upscaling. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/it.md)

---
**Source fingerprint (SHA-256):** `22dcf7c176705ce21a9032b1c9f4fe82ee6aa153f5057b90dac653b37281a677`
