# Ideogram 4.5 Modifica

Modifica o combina fino a 5 immagini guidate da un prompt testuale con Ideogram 4.5. L'immagine 1 è l'immagine da modificare e le immagini successive sono riferimenti opzionali. L'intera immagine viene renderizzata di nuovo, quindi le dimensioni o il rapporto d'aspetto del risultato possono cambiare; usa Ideogram 4.5 Precise Edit per mantenere invariati i pixel non toccati.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare. (predefinito: `"ideogram-4.5"`) | DYNAMIC_COMBO | Sì | `"ideogram-4.5"` |
| `images` | Slot espandibile: l'immagine 1 è l'immagine da modificare e le immagini da 2 a 5 sono riferimenti opzionali (`image_1` ... `image_5`). Fai riferimento a esse nel prompt come @Image1, @Image2, ...; un input in batch conta una volta per immagine. Ogni immagine deve avere un rapporto d'aspetto compreso tra 1:6 e 6:1. | IMAGE | Sì | 1 to 5 images |
| `prompt` | Istruzioni di modifica. Supporta riferimenti in stile @Image1 alle immagini collegate. (predefinito: stringa vuota) | STRING | Sì | 1 to 10000 characters |
| `size` | Dimensione dell'output. `"auto"` sceglie una tela di circa 2K dalle immagini e dal prompt, `"source"` mantiene la dimensione dell'immagine 1 (le immagini sopra circa 4 MP vengono prima ridimensionate), e un preset con un rapporto d'aspetto diverso ricompone la scena. Seleziona `"custom"` per usare la larghezza e l'altezza riportate di seguito. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>`"source"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"custom"` |
| `width` | Larghezza personalizzata dell'output in pixel. Usata solo quando `size` è `"custom"`. (predefinito: 2048) | INT | Sì | 256 to 4608 (step 32) |
| `height` | Altezza personalizzata dell'output in pixel. Usata solo quando `size` è `"custom"`. (predefinito: 2048) | INT | Sì | 256 to 4608 (step 32) |
| `quality` | Livello di qualità. I livelli più alti costano di più e richiedono più tempo. (predefinito: `"medium"`) | COMBO | Sì | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Seme per la generazione. Le stesse immagini, prompt, impostazioni e seed danno lo stesso risultato. (predefinito: 42) | INT | Sì | 0 to 2147483647 |

### Vincoli dei parametri

- **Numero di immagini:** almeno 1 e al massimo 5 immagini; un input in batch conta una volta per immagine. L'immagine 1 è l'immagine da modificare, le altre sono riferimenti.
- **Rapporto d'aspetto delle immagini:** ogni immagine non deve essere più larga di 6 volte la sua altezza né più alta di 6 volte la sua larghezza (tra 1:6 e 6:1).
- **Tag del prompt:** `@ImageN` viene confrontato senza distinzione tra maiuscole e minuscole e non deve superare il numero di immagini collegate; il prompt non deve essere composto solo da spazi bianchi e deve contenere al massimo 10000 caratteri.
- **Dimensione personalizzata:** usata solo quando `size` è `"custom"`. Il prodotto tra larghezza e altezza non deve superare 4194304 pixel (2048x2048), e il lato più lungo non deve superare 6 volte il lato più corto. Larghezza e altezza devono essere comprese tra 256 e 4608 e vengono arrotondate a multipli di 32.
- **Ridimensionamento al caricamento:** le immagini più grandi di circa 4 MP, o più grandi di 4608 px sul lato lungo, vengono ridimensionate prima di essere inviate.
- **Sicurezza dei contenuti:** se il filtro di sicurezza dei contenuti di Ideogram blocca il risultato, il nodo genera un errore invece di restituire un'immagine.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine o le immagini modificate o combinate come batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramEditApi/it.md)

---
**Source fingerprint (SHA-256):** `58c189d65502373ff7b56f5f32d9f2e7ee8019fc58f1bbbb80abc859cf978f67`
