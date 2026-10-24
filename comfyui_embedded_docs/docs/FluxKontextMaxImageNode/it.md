# Flux.1 Kontext [max] Immagine

Genera o modifica un'immagine con Flux.1 Kontext [max] tramite l'API BFL, in base a un prompt e a un rapporto d'aspetto. Con `input_image` collegato, il prompt descrive la modifica; senza, il nodo genera una nuova immagine basandosi solo sul prompt. Espone gli stessi input di Flux.1 Kontext [pro] Image.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt per la generazione dell'immagine. Con un'immagine di input, specifica cosa e come modificare. | STRING | Sì | - |
| `aspect_ratio` | Rapporto d'aspetto dell'immagine; deve essere compreso tra 1:4 e 4:1 (predefinito: `"16:9"`). | STRING | Sì | - |
| `guidance` | Forza di guidance per il processo di generazione dell'immagine (predefinito: 3.0). | FLOAT | Sì | da 0.1 a 99.0 (passo 0.1) |
| `steps` | Numero di passaggi per il processo di generazione dell'immagine (predefinito: 50). | INT | Sì | da 1 a 150 |
| `seed` | Il seed casuale utilizzato per creare il rumore (predefinito: 1234). | INT | Sì | da 0 a 18446744073709551615 |
| `prompt_upsampling` | Indica se eseguire l'upsampling sul prompt. Se attivo, il prompt viene modificato automaticamente per una generazione più creativa, ma i risultati sono non deterministici, quindi lo stesso seed non produrrà esattamente lo stesso risultato (predefinito: `False`). Questa è un'impostazione avanzata. | BOOLEAN | Sì | True / False |
| `input_image` | Immagine opzionale da modificare. Se omessa, il prompt viene convalidato per assicurarsi che non sia vuoto. | IMAGE | No | - |

**Nota:** Il nodo invia la richiesta a BFL ed esegue polling finché l'immagine non è pronta. Le richieste rifiutate dalla moderazione dei contenuti di BFL falliscono invece di restituire un'immagine.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `IMAGE` | L'immagine generata o modificata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMaxImageNode/it.md)

---
**Source fingerprint (SHA-256):** `557f9e69de37ee89e161dffdaef7458ed026b884298594f2046454b6b8d3c415`
