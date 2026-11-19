# Ideogram 4.5 da testo a immagine

Genera immagini da un prompt testuale con Ideogram 4.6 o 4.5. Il prompt accetta anche una didascalia JSON strutturata di Ideogram, ad esempio il `final_prompt` restituito da un'esecuzione precedente, che offre un controllo esatto su stringhe di testo, colori e layout. Il nodo restituisce l'immagine insieme alla didascalia da cui l'immagine è stata effettivamente generata.

## Input

La selezione di un `model` determina quali input compaiono. Ideogram 4.6 aggiunge `background`, il livello di qualità `very_low`, dimensioni `(4K)` e larghezza e altezza personalizzate; 4.5 mantiene i preset `(1K)` e `(2K)`.

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da usare. `"ideogram-4.6"` genera fino a 4K con uno sfondo trasparente opzionale; `"ideogram-4.5"` è il modello precedente (predefinito: `"ideogram-4.6"`). | DYNAMIC_COMBO | Sì | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `prompt` | Prompt testuale, oppure una didascalia JSON strutturata di Ideogram come un `final_prompt` precedente (predefinito: stringa vuota). | STRING | Sì | 1 a 10000 caratteri |
| `magic_prompt` | Riscrive il prompt in una didascalia strutturata dettagliata prima di generare; `"off"` mantiene la formulazione il più letterale possibile. La didascalia viene restituita come `final_prompt` (predefinito: `"auto"`). Questa è un'impostazione avanzata. | COMBO | Sì | `"auto"`<br>`"on"`<br>`"off"` |
| `seed` | Seed per la generazione. La generazione da testo a immagine non è riproducibile dal solo seed perché il prompt viene riscritto a ogni esecuzione; per riprodurre un'immagine, riutilizza il suo `final_prompt` con `magic_prompt` impostato su `"off"` e lo stesso seed (predefinito: 42). | INT | Sì | 0 a 2147483647 |

### Input di Ideogram 4.6

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size` | Dimensione output. `"auto"` lascia che il modello scelga una tela adatta al prompt. Un preset fissa sia la dimensione in pixel sia le proporzioni; i livelli `(1K)`, `(2K)` e `(4K)` descrivono il budget di pixel anziché un lato lungo fisso. Seleziona `"custom"` per usare la larghezza e l'altezza seguenti (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(4K) 4096x4096 (1:1)"`<br>`"(4K) 2880x5760 (1:2)"`<br>`"(4K) 5760x2880 (2:1)"`<br>`"(4K) 3328x4992 (2:3)"`<br>`"(4K) 4992x3328 (3:2)"`<br>`"(4K) 3584x4480 (4:5)"`<br>`"(4K) 4480x3584 (5:4)"`<br>`"(4K) 2880x5120 (9:16)"`<br>`"(4K) 5120x2880 (16:9)"`<br>`"(4K) 3200x5120 (5:8)"`<br>`"(4K) 5120x3200 (8:5)"`<br>`"(4K) 3456x4608 (3:4)"`<br>`"(4K) 4608x3456 (4:3)"`<br>`"(4K) 2304x5888 (9:23)"`<br>`"(4K) 5888x2304 (23:9)"`<br>`"(4K) 2496x6656 (3:8)"`<br>`"(4K) 6656x2496 (8:3)"`<br>`"(4K) 2560x6144 (5:12)"`<br>`"(4K) 6144x2560 (12:5)"`<br>`"(4K) 2048x6144 (1:3)"`<br>`"(4K) 6144x2048 (3:1)"`<br>`"custom"` |
| `width` | Larghezza output personalizzata in pixel, usata solo quando `size` è `"custom"` (predefinito: 2048). | INT | Sì | 256 a 8192 (passo 32) |
| `height` | Altezza output personalizzata in pixel, usata solo quando `size` è `"custom"` (predefinito: 2048). | INT | Sì | 256 a 8192 (passo 32) |
| `quality` | Livello di qualità. I livelli più alti costano di più e richiedono più tempo (predefinito: `"medium"`). | COMBO | Sì | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `background` | `"transparent"` restituisce l'immagine con un canale alpha, `"opaque"` forza uno sfondo solido, `"auto"` segue il prompt (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"opaque"`<br>`"transparent"` |

### Input di Ideogram 4.5

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size` | Dimensione output. `"auto"` lascia che il modello scelga una tela adatta al prompt; un preset fissa sia la dimensione in pixel sia le proporzioni (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1296x3168 (9:22)"`<br>`"(2K) 3168x1296 (22:9)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(1K) 720x1280 (9:16)"`<br>`"(1K) 1280x720 (16:9)"`<br>`"(1K) 720x1440 (1:2)"`<br>`"(1K) 1440x720 (2:1)"` |
| `quality` | Livello di qualità. I livelli più alti costano di più e richiedono più tempo (predefinito: `"medium"`). | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"` |

### Vincoli dei parametri

- **Prompt:** almeno un carattere diverso da uno spazio e al massimo 10000 caratteri. Imposta `magic_prompt` su `"off"` quando fornisci una tua didascalia JSON.
- **Dimensione personalizzata (4.6):** larghezza per altezza non deve superare 16,7 MP (4096x4096); ciascun lato deve essere compreso tra 256 e 8192 e arrotondato a un multiplo di 32; il lato più lungo non deve superare 6 volte il lato più corto.
- **Qualità `very_low` (4.6):** limitata a 4 MP (2048x2048); dimensioni maggiori generano un errore.
- **Riproducibilità:** con `magic_prompt` impostato su `"auto"` o `"on"`, il prompt viene riscritto a ogni esecuzione, quindi lo stesso seed può produrre un'immagine diversa.
- **Sicurezza dei contenuti:** se il filtro di sicurezza dei contenuti di Ideogram blocca la generazione, il nodo genera un errore anziché restituire un'immagine.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine generata come batch. | IMAGE |
| `final_prompt` | La didascalia strutturata da cui è stata generata l'immagine. Reintroducila con `magic_prompt` impostato su `"off"` e lo stesso seed per riprodurre l'immagine. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramTextToImageApi/it.md)

---
**Source fingerprint (SHA-256):** `a21f1faed9ca7a7bc63dae74003cc7599f11013075f718af9e5860d2cd666828`
