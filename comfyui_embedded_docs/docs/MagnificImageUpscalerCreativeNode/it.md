# MagnificImageUpscalerCreativeNode

Questo nodo utilizza il servizio Magnific AI per eseguire l'upscale e migliorare in modo creativo un'immagine. Consente di guidare il miglioramento con un prompt testuale, scegliere uno stile specifico su cui ottimizzare e controllare vari aspetti del processo creativo, come dettaglio, somiglianza con l'originale e forza di stilizzazione. Il nodo restituisce in output un'immagine upscalata con il fattore scelto (2x, 4x, 8x o 16x), con una dimensione massima di output di 25,3 megapixel.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da upscalare e migliorare. | IMAGE | Sì | - |
| `prompt` | Una descrizione testuale per guidare il miglioramento creativo dell'immagine. Il valore predefinito è una stringa vuota (in tal caso non viene inviato alcun prompt). | STRING | Sì | - |
| `scale_factor` | Il fattore di ingrandimento delle dimensioni dell'immagine. | COMBO | Sì | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `optimized_for` | Lo stile o il tipo di contenuto per cui ottimizzare il processo di miglioramento. | COMBO | Sì | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `creativity` | Controlla il livello di interpretazione creativa applicata all'immagine (predefinito: 0). | INT | Sì | -10 a 10 |
| `hdr` | Il livello di definizione e dettaglio (predefinito: 0). | INT | Sì | -10 a 10 |
| `resemblance` | Il livello di somiglianza con l'immagine originale (predefinito: 0). | INT | Sì | -10 a 10 |
| `fractality` | La forza del prompt e la complessità per pixel quadrato (predefinito: 0). | INT | Sì | -10 a 10 |
| `engine` | Il motore AI specifico da usare per l'elaborazione. Questo è un parametro avanzato. | COMBO | Sì | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `auto_downscale` | Ridimensiona automaticamente l'immagine di input verso il basso se l'output supererebbe il limite massimo di pixel (predefinito: False). Questo è un parametro avanzato. | BOOLEAN | Sì | - |

**Vincoli:**

* L'input `image` deve essere esattamente un'immagine.
* L'immagine di input deve avere altezza e larghezza minime di 160 pixel.
* Il rapporto d'aspetto dell'immagine di input deve essere compreso tra 1:3 e 3:1.
* La dimensione finale dell'output (dimensioni di input moltiplicate per `scale_factor`) non può superare 25.300.000 pixel. Se questo limite verrebbe superato:
  - Quando `auto_downscale` è abilitato, il nodo riduce automaticamente la dimensione dell'immagine di input (l'ulteriore ridimensionamento viene mantenuto a un massimo di 2x) oppure usa uno `scale_factor` inferiore, in modo che l'output rimanga entro il limite.
  - Quando `auto_downscale` è disabilitato, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine di output migliorata creativamente e upscalata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/it.md)

---
**Source fingerprint (SHA-256):** `36c38e87f9f1e568c78cf794aeb0a268c6d25d639006eb2cf18ee040d3071ad4`
