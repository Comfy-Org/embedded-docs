# Ideogram 4.5 Modifica

Modifica o combina fino a 5 immagini guidate da un prompt testuale con Ideogram 4.6 o 4.5. L'immagine 1 è l'immagine da modificare e le immagini successive sono riferimenti opzionali. L'intera immagine viene renderizzata nuovamente, quindi le dimensioni o le proporzioni del risultato possono cambiare; usa invece Ideogram Precise Edit per mantenere invariati i pixel non toccati, e modifica una regione lì quando un'immagine sorgente di grandi dimensioni deve mantenere la sua esatta risoluzione, perché una modifica dell'intera immagine viene prima ridimensionata.

## Input

La selezione di un `model` determina quali input vengono visualizzati. Ideogram 4.6 aggiunge il parametro `background`, le dimensioni `(4K)` e dimensioni personalizzate fino a 8192 pixel per lato; 4.5 mantiene i preset `(1K)` e `(2K)` con al massimo 4608 pixel per lato. Entrambi i modelli offrono qui i livelli di qualità `very_low`, `low`, `medium` e `high`.

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modello da usare. `"ideogram-4.6"` esegue il rendering fino a 4K con uno sfondo trasparente opzionale; `"ideogram-4.5"` è il modello precedente (predefinito: `"ideogram-4.6"`). | DYNAMIC_COMBO | Sì | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Slot espandibile: l'immagine 1 è l'immagine da modificare e le immagini da 2 a 5 sono riferimenti opzionali (`image_1` ... `image_5`). Fai riferimento a esse nel prompt come @Image1, @Image2, ...; un input in batch conta una volta per immagine. Ogni immagine deve avere un rapporto d'aspetto compreso tra 1:6 e 6:1. | IMAGE | Sì | 1 a 5 immagini |
| `prompt` | Istruzioni di modifica. Supporta riferimenti in stile @Image1 alle immagini collegate (predefinito: stringa vuota). | STRING | Sì | 1 a 10000 caratteri |
| `seed` | Seed per la generazione. Le stesse immagini, il prompt, le impostazioni e il seed danno lo stesso risultato o un risultato molto simile (predefinito: 42). | INT | Sì | 0 a 2147483647 |

### Input di Ideogram 4.6

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `size` | Dimensione dell'output. `"auto"` sceglie una tela di circa 2K dalle immagini e dal prompt, `"source"` mantiene la dimensione dell'immagine 1 (le immagini sopra 16,7 MP, o con uno dei due lati sopra 8192 pixel, vengono prima ridimensionate), e un preset con un rapporto d'aspetto diverso ricompone la scena. Seleziona `"custom"` per usare la larghezza e l'altezza sotto (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"source"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(4K) 4096x4096 (1:1)"`<br>`"(4K) 2880x5760 (1:2)"`<br>`"(4K) 5760x2880 (2:1)"`<br>`"(4K) 3328x4992 (2:3)"`<br>`"(4K) 4992x3328 (3:2)"`<br>`"(4K) 3584x4480 (4:5)"`<br>`"(4K) 4480x3584 (5:4)"`<br>`"(4K) 2880x5120 (9:16)"`<br>`"(4K) 5120x2880 (16:9)"`<br>`"(4K) 3200x5120 (5:8)"`<br>`"(4K) 5120x3200 (8:5)"`<br>`"(4K) 3456x4608 (3:4)"`<br>`"(4K) 4608x3456 (4:3)"`<br>`"(4K) 2304x5888 (9:23)"`<br>`"(4K) 5888x2304 (23:9)"`<br>`"(4K) 2496x6656 (3:8)"`<br>`"(4K) 6656x2496 (8:3)"`<br>`"(4K) 2560x6144 (5:12)"`<br>`"(4K) 6144x2560 (12:5)"`<br>`"(4K) 2048x6144 (1:3)"`<br>`"(4K) 6144x2048 (3:1)"`<br>`"custom"` |
| `width` | Larghezza personalizzata dell'output in pixel, usata solo quando `size` è `"custom"` (predefinito: 2048). | INT | Sì | 256 a 8192 (passo 32) |
| `height` | Altezza personalizzata dell'output in pixel, usata solo quando `size` è `"custom"` (predefinito: 2048). | INT | Sì | 256 a 8192 (passo 32) |
| `quality` | Livello di qualità. I livelli più alti costano di più e richiedono più tempo (predefinito: `"medium"`). | COMBO | Sì | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `background` | `"transparent"` restituisce l'immagine con un canale alfa, `"opaque"` forza uno sfondo solido, `"auto"` segue il prompt (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"opaque"`<br>`"transparent"` |

### Input di Ideogram 4.5

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `size` | Dimensione dell'output. `"auto"` sceglie una tela di circa 2K dalle immagini e dal prompt, `"source"` mantiene la dimensione dell'immagine 1 (le immagini sopra circa 4 MP, o con uno dei due lati sopra 4608 pixel, vengono prima ridimensionate), e un preset con un rapporto d'aspetto diverso ricompone la scena. Seleziona `"custom"` per usare la larghezza e l'altezza sotto (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"source"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"custom"` |
| `width` | Larghezza personalizzata dell'output in pixel, usata solo quando `size` è `"custom"` (predefinito: 2048). | INT | Sì | 256 a 4608 (passo 32) |
| `height` | Altezza personalizzata dell'output in pixel, usata solo quando `size` è `"custom"` (predefinito: 2048). | INT | Sì | 256 a 4608 (passo 32) |
| `quality` | Livello di qualità. I livelli più alti costano di più e richiedono più tempo (predefinito: `"medium"`). | COMBO | Sì | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Vincoli dei parametri

- **Numero di immagini:** almeno 1 e al massimo 5 immagini; un input in batch conta una volta per immagine. L'immagine 1 è l'immagine da modificare, le altre sono riferimenti.
- **Rapporto d'aspetto delle immagini:** ogni immagine non deve essere più larga di 6 volte la sua altezza né più alta di 6 volte la sua larghezza (tra 1:6 e 6:1).
- **Tag del prompt:** `@ImageN` viene confrontato senza distinzione tra maiuscole e minuscole e non deve superare il numero di immagini collegate; il prompt non deve essere composto solo da spazi bianchi e deve contenere al massimo 10000 caratteri.
- **Dimensione personalizzata:** la larghezza moltiplicata per l'altezza non deve superare 16,7 MP (4096x4096) su 4.6 e 4194304 pixel (2048x2048) su 4.5, e il lato più lungo non deve superare 6 volte il lato più corto. Larghezza e altezza vengono arrotondate al multiplo di 32 più vicino.
- **Ridimensionamento per il caricamento:** 4.6 invia l'immagine 1 fino a 16,7 MP e 8192 pixel per lato, ricodificandola come JPEG quando ciò la mantiene sotto il limite di caricamento; 4.5 ridimensiona l'immagine 1 sopra circa 4 MP o 4608 pixel per lato.
- **Sicurezza dei contenuti:** se il filtro di sicurezza dei contenuti di Ideogram blocca il risultato, il nodo genera un errore invece di restituire un'immagine.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `IMAGE` | L'immagine modificata o combinata come batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramEditApi/it.md)

---
**Source fingerprint (SHA-256):** `58c189d65502373ff7b56f5f32d9f2e7ee8019fc58f1bbbb80abc859cf978f67`
