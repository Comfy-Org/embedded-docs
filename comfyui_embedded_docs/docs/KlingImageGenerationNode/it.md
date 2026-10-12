# KlingImageGenerationNode

Il nodo Kling Image Generation genera immagini da prompt testuali con l'opzione di usare un'immagine di riferimento come guida. Crea una o più immagini in base alla descrizione testuale e alle impostazioni di riferimento, quindi restituisce le immagini generate come output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale positivo. Obbligatorio, deve essere compreso tra 1 e 500 caratteri. | STRING | Sì | Massimo 500 caratteri |
| `negative_prompt` | Prompt testuale negativo. | STRING | Sì | Massimo 500 caratteri |
| `image_type` | Selezione del tipo di riferimento immagine (avanzato). Obbligatorio quando viene fornita un'immagine di riferimento. | COMBO | Sì | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | Intensità del riferimento per le immagini caricate dall'utente (predefinito: 0.5, avanzato) | FLOAT | Sì | 0.0 - 1.0 |
| `human_fidelity` | Somiglianza del riferimento del soggetto (predefinito: 0.45, avanzato) | FLOAT | Sì | 0.0 - 1.0 |
| `model_name` | Selezione del modello per la generazione di immagini (predefinito: "kling-v3") | COMBO | Sì | `"kling-v3"` |
| `aspect_ratio` | Rapporto d'aspetto per le immagini generate (predefinito: "16:9") | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | Numero di immagini generate (predefinito: 1) | INT | Sì | 1 - 9 |
| `image` | Immagine di riferimento opzionale | IMAGE | No | - |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati sono non deterministici indipendentemente dal seed (predefinito: 0) | INT | No | 0 - 2147483647 |

**Vincoli dei parametri:**

- Il parametro `image` è opzionale. Quando viene fornita un'immagine di riferimento, il parametro `image_type` determina se il riferimento viene usato come riferimento del soggetto o come riferimento di stile.
- Quando non viene fornita alcuna immagine di riferimento, le impostazioni relative al riferimento (`image_type`, `image_fidelity`, `human_fidelity`) non hanno alcun effetto sul risultato.
- `prompt` e `negative_prompt` hanno una lunghezza massima di 500 caratteri.
- Il parametro `seed` è opzionale e non garantisce risultati deterministici.
- Il parametro `n` controlla quante immagini vengono prodotte e determina anche il prezzo della richiesta.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Immagine/i generate in base ai parametri di input. Quando `n` è maggiore di 1, vengono restituite più immagini come batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/it.md)

---
**Source fingerprint (SHA-256):** `fd344519346f63ac03975b93f03725749ed9697245d6dfa2378884c59a5325cd`
