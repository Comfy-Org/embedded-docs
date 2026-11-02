# Flux Video Upscale

Flux Video Upscale ingrandisce un video con la super-risoluzione FLUX, portandolo a una dimensione fissa del fotogramma di 1080p, 2K o 4K oppure ingrandendolo da 1,5 a 3 volte. La modalità creative ripristina e inventa dettagli fini, adatta ai filmati generati; la modalità precise aumenta la nitidezza della sorgente senza modificarla, adatta a volti, prodotti e filmati reali. La clip viene caricata, il job BFL viene monitorato tramite polling e il video finito viene restituito a 24 fps.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Clip sorgente da 1 a 20 secondi e al massimo 50 MB, almeno 64x64 pixel, con un rapporto d'aspetto tra 1:4 e 4:1. L'output viene renderizzato a 24 fps e limitato a circa 14,4 megapixel per fotogramma. | VIDEO | Sì | durata da 1 a 20 secondi; rapporto d'aspetto tra 1:4 e 4:1; minimo 64x64 pixel |
| `target_resolution` | Dimensione dell'output. `"1080p"`, `"2K"` e `"4K"` adattano il risultato entro 1920x1080, 2560x1440 o 3840x2160 pixel, con orientamento ruotato per clip verticali; `"by factor"` usa invece `upscale_factor`. | DYNAMIC_COMBO | Sì | `"2K"`<br>`"4K"`<br>`"1080p"`<br>`"by factor"` |
| `mode` | `"creative"` ripristina e inventa dettagli fini, ideale per filmati generati, texture e paesaggi. `"precise"` aumenta la nitidezza della sorgente senza modificarla, per volti, prodotti e filmati reali. (predefinito: `"creative"`) | COMBO | Sì | `"creative"`<br>`"precise"` |
| `prompt` | Descrizione facoltativa della clip che guida il dettaglio migliorato. Lasciare vuoto per un ingrandimento neutro. (predefinito: vuoto) | STRING | Sì | Testo multiriga |
| `auto_downscale` | Ridimensiona verso il basso le sorgenti troppo grandi invece di rifiutarle: oltre 2560x1440 pixel di area, oppure oltre due terzi della risoluzione di destinazione. Il rapporto d'aspetto viene preservato. (predefinito: true) | BOOLEAN | Sì | true<br>false |
| `safety_tolerance` | Tolleranza di moderazione; 0 è il valore più severo. (predefinito: 2, parametro avanzato) | INT | Sì | da 0 a 4 |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; FLUX sceglie il proprio seed, quindi i risultati effettivi sono non deterministici indipendentemente da questo valore. (predefinito: 42) | INT | Sì | da 0 a 4294967295 |

### Input di by factor

Questi input compaiono quando `target_resolution` è impostato su `"by factor"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `upscale_factor` | Dimensione dell'output rispetto alla sorgente. Le sorgenti molto grandi vengono ingrandite meno del fattore richiesto a causa del limite per fotogramma. (predefinito: 2.0) | FLOAT | Sì | da 1.5 a 3.0 (passo 0.1) |

Una dimensione di destinazione viene applicata come un fattore di ingrandimento limitato a 1,5-3,0, quindi una sorgente troppo piccola per riempire il riquadro a 3x risulta più piccola della risoluzione richiesta, e una sorgente che richiederebbe meno di 1,5x per adattarsi al riquadro viene prima ridotta. Con `auto_downscale` disattivato, il nodo si interrompe con un errore invece di ridimensionare verso il basso. L'output è a 24 fps ed è limitato a circa 14,4 megapixel per fotogramma, quindi le sorgenti molto grandi possono essere ingrandite meno del fattore richiesto.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | La clip video ingrandita. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `bef6ef4614d75bc9e6bab977f5f19c45fe30d300907913462a058e6e7e7e4ac7`
