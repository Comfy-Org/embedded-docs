# ByteDanceSeedreamNode

Il nodo ByteDance Seedream 4.5 & 5.0 offre capacità unificate di generazione da testo a immagine e di modifica precisa tramite una singola frase, fino a una risoluzione di 4K. Può creare nuove immagini da prompt testuali o modificare immagini esistenti usando istruzioni testuali. Il nodo supporta sia la generazione di una singola immagine sia la generazione sequenziale di più immagini correlate.

**Nota:** questo nodo è contrassegnato come deprecato nel codice sorgente.

## Input

| Parametro | Descrizione | Tipo di dati | Richiesto | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello Seedream da usare per la generazione. | STRING | Sì | "seedream 5.0 pro"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |
| `prompt` | Prompt testuale per creare o modificare un'immagine. Deve contenere almeno 1 carattere. | STRING | Sì | - |
| `image` | Immagine/i di input per la generazione da immagine a immagine. Immagine/i di riferimento per la generazione con riferimento singolo o multiplo. Massimo 14 immagini di riferimento per seedream-5-0-260128, oppure 10 per gli altri modelli. | IMAGE | No | - |
| `size_preset` | Scegli una dimensione consigliata. Seleziona Custom per usare la larghezza e l'altezza indicate di seguito. | STRING | No | Sono disponibili più opzioni |
| `width` | Larghezza personalizzata per l'immagine. Il valore viene usato solo se `size_preset` è impostato su `Custom`. Predefinito: 2048. | INT | No | 1024 a 6240 (passo 2) |
| `height` | Altezza personalizzata per l'immagine. Il valore viene usato solo se `size_preset` è impostato su `Custom`. Predefinito: 2048. | INT | No | 1024 a 4992 (passo 2) |
| `sequential_image_generation` | Modalità di generazione di immagini in gruppo. "disabled" genera una singola immagine. "auto" lascia che il modello decida se generare più immagini correlate (ad es. scene di una storia, varianti di personaggi). Predefinito: "disabled". | STRING | No | "disabled"<br>"auto" |
| `max_images` | Numero massimo di immagini da generare quando `sequential_image_generation='auto'`. Il numero totale di immagini (input + generate) non può superare 15. Predefinito: 1. | INT | No | 1 a 15 (passo 1) |
| `seed` | Seme da usare per la generazione. Predefinito: 0. | INT | No | 0 a 2147483647 (passo 1) |
| `watermark` | Indica se aggiungere un watermark "AI generated" all'immagine. Predefinito: False. | BOOLEAN | No | - |
| `fail_on_partial` | Se abilitato, interrompe l'esecuzione se una qualsiasi delle immagini richieste è mancante o restituisce un errore. Predefinito: True. | BOOLEAN | No | - |

**Note sui vincoli dei parametri:**
- La risoluzione minima dell'immagine dipende dal modello selezionato: 3,68 MP per i modelli seedream-4-5 e seedream-5-0, 0,92 MP per i modelli seedream-4-0.
- La risoluzione massima dell'immagine è 10,4 MP per i modelli seedream-5-0 e 16,78 MP per gli altri modelli.
- Le immagini di riferimento devono avere un rapporto d'aspetto compreso tra 1:3 e 3:1.
- Quando `sequential_image_generation` è impostato su "auto", il numero totale di immagini di input più `max_images` non può superare 15.
- I parametri `width` e `height` vengono usati solo quando `size_preset` è impostato su "Custom".

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `IMAGE` | Immagine/i generata/e in base ai parametri di input e al prompt. Restituisce un singolo tensore immagine o un batch di tensori immagine se vengono generate più immagini. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/it.md)

---
**Source fingerprint (SHA-256):** `78086df431c887c241796ddb5db1ebbfe5b57faab0839da842be81480f1e113b`
