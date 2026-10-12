# Kling 3.0 Omni Immagine

Il nodo Kling Omni Image (Pro) crea o modifica immagini usando il più recente modello Kling AI. Genera immagini basandosi su una descrizione testuale e può facoltativamente utilizzare immagini di riferimento per guidare lo stile o il contenuto. Il nodo invia una richiesta a un'API esterna, che elabora l'attività e restituisce l'immagine o le immagini finali.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_name` | Il modello Kling AI specifico da usare per la generazione delle immagini. | COMBO | Sì | `"kling-v3-omni"`<br>`"kling-image-o1"` |
| `prompt` | Un prompt testuale che descrive il contenuto dell'immagine. Può includere sia descrizioni positive sia negative. Il testo deve essere lungo da 1 a 2500 caratteri. Puoi usare `@image`, `@image1`, `@image2`, ecc. o `@video`, `@video1`, `@video2`, ecc. per fare riferimento a immagini o video caricati nel prompt. | STRING | Sì | - |
| `resolution` | La risoluzione target per l'immagine generata. Nota: la risoluzione 4K non è supportata per il modello `kling-image-o1`. | COMBO | Sì | `"1K"`<br>`"2K"`<br>`"4K"` |
| `aspect_ratio` | Il rapporto d'aspetto desiderato (larghezza rispetto all'altezza) per l'immagine generata. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"21:9"` |
| `series_amount` | Genera una serie di immagini. Questa funzione non è supportata per il modello `kling-image-o1`. (predefinito: "disabled") | COMBO | Sì | `"disabled"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` |
| `reference_images` | Fino a 10 immagini di riferimento aggiuntive. Ogni immagine deve avere almeno 300 pixel sia in larghezza sia in altezza, e il suo rapporto d'aspetto deve essere compreso tra 1:2.5 e 2.5:1. | IMAGE | No | - |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati sono non deterministici indipendentemente dal seed. (predefinito: 0) | INT | No | 0 a 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine (o le immagini) finale generate o modificate dal modello Kling AI. Se è stata richiesta una serie, vengono restituite più immagini come batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/it.md)

---
**Source fingerprint (SHA-256):** `923db96e956e0f11c9290478ceb105304893f28d35af9f0e13077ca0f88dff79`
