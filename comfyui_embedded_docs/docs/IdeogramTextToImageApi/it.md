# Ideogram 4.5 da testo a immagine

Genera immagini da un prompt testuale con Ideogram 4.5. Il prompt accetta anche una didascalia JSON strutturata di Ideogram, ad esempio il `final_prompt` restituito da un'esecuzione precedente, che offre un controllo esatto su stringhe di testo, colori e layout. Il nodo restituisce l'immagine o le immagini generate insieme alla didascalia da cui è stata effettivamente generata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da usare. (predefinito: `"ideogram-4.5"`) | DYNAMIC_COMBO | Sì | `"ideogram-4.5"` |
| `prompt` | Prompt testuale, oppure una didascalia JSON strutturata di Ideogram come un `final_prompt` precedente. (predefinito: stringa vuota) | STRING | Sì | da 1 a 10000 caratteri |
| `size` | Dimensione di output. `"auto"` lascia che il modello scelga una tela adatta al prompt. Un preset `(2K)` o `(1K)` fissa sia la dimensione in pixel sia le proporzioni. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1296x3168 (9:22)"`<br>`"(2K) 3168x1296 (22:9)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(1K) 720x1280 (9:16)"`<br>`"(1K) 1280x720 (16:9)"`<br>`"(1K) 720x1440 (1:2)"`<br>`"(1K) 1440x720 (2:1)"` |
| `quality` | Livello di qualità. I livelli più alti costano di più e richiedono più tempo. (predefinito: `"medium"`) | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"` |
| `magic_prompt` | Riscrive il prompt in una didascalia strutturata dettagliata prima di generare; `"off"` mantiene la tua formulazione il più letterale possibile. La didascalia viene restituita come `final_prompt`. (predefinito: `"auto"`) Questa è un'impostazione avanzata. | COMBO | Sì | `"auto"`<br>`"on"`<br>`"off"` |
| `seed` | Seme per la generazione. Il text-to-image non è riproducibile dal solo seme perché il prompt viene riscritto a ogni esecuzione; per riprodurre un'immagine, riutilizza il suo `final_prompt` con `magic_prompt` impostato su `"off"` e lo stesso seme. (predefinito: 42) | INT | Sì | da 0 a 2147483647 |

### Vincoli dei parametri

- **Prompt obbligatorio:** il prompt deve contenere almeno un carattere non di spaziatura e al massimo 10000 caratteri. Imposta `magic_prompt` su `"off"` quando fornisci la tua didascalia JSON o una formulazione esatta.
- **Dimensione:** `"auto"` lascia che il modello scelga. I preset `(2K)` sono circa 3-4 megapixel e i preset `(1K)` circa 1 megapixel, quindi l'etichetta del livello descrive il budget di pixel anziché un lato lungo fisso; le proporzioni del preset vengono rispettate. All'API viene inviata solo la parte del preset relativa alla dimensione in pixel.
- **Riproducibilità:** con `magic_prompt` impostato su `"auto"` o `"on"` il prompt viene riscritto a ogni esecuzione, quindi lo stesso seed può comunque produrre un'immagine diversa. Per riprodurre un'immagine, reinserisci il suo `final_prompt` con `magic_prompt` impostato su `"off"` e lo stesso seed.
- **Sicurezza dei contenuti:** se il filtro di sicurezza dei contenuti di Ideogram blocca la generazione, il nodo solleva un errore invece di restituire un'immagine.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine o le immagini generate come batch. | IMAGE |
| `final_prompt` | La didascalia strutturata da cui è stata generata l'immagine. Reinseriscila con `magic_prompt` impostato su `"off"` e lo stesso seed per riprodurre l'immagine. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramTextToImageApi/it.md)

---
**Source fingerprint (SHA-256):** `a21f1faed9ca7a7bc63dae74003cc7599f11013075f718af9e5860d2cd666828`
