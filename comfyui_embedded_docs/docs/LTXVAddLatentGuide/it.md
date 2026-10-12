# LTXV Aggiungi guida latent

Il nodo LTXV Add Latent Guide fissa un latente già codificato come guida, per quando la guida proviene da uno stadio precedente anziché da un'immagine. Ha lo stesso effetto di LTXV Add Guide senza il ciclo di decodifica/codifica VAE. Una guida spazialmente più piccola del target (un riferimento IC-LoRA o di dettaglio) viene dilatata su una griglia sparsa, e le sue posizioni finali RoPE vengono espanse dello stesso rapporto, in modo che copra il canvas di destinazione invece di indirizzare solo l'angolo in alto a sinistra.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `positive` | Input di condizionamento positivo. | CONDITIONING | Sì | N/A |
| `negative` | Input di condizionamento negativo. | CONDITIONING | Sì | N/A |
| `vae` | Il modello VAE usato per leggere la formula dell'indice di downscale per il posizionamento dei frame. | VAE | Sì | N/A |
| `latent` | Video latente di destinazione su cui viene fissata la guida. | LATENT | Sì | N/A |
| `guiding_latent` | Latente della guida. La sua dimensione spaziale deve dividere quella del target per lo stesso numero intero su entrambi gli assi; una dimensione uguale la fissa così com'è, una dimensione dimezzata viene trattata come riferimento IC-LoRA x2. | LATENT | Sì | N/A |
| `latent_idx` | Indice del frame latente da cui iniziare la guida, contato in frame latenti anziché in frame pixel. I valori negativi posizionano la guida su frame precedenti all'inizio del latente, non contati a ritroso dalla sua fine. Predefinito: 0. | INT | Sì | -9999 to 9999 |
| `strength` | Limitato a 1.0. Una guida dilatata contrassegna le sue posizioni di padding con una maschera denoise negativa, così il modello le scarta; sopra 1.0 anche le posizioni mantenute diventerebbero negative e l'intera guida verrebbe scartata. Per amplificare oltre 1.0, usa invece `attention_mask`. Predefinito: 1.0. | FLOAT | Sì | 0.0 to 1.0, step 0.01 |
| `attention_mask` | Maschera spaziale opzionale nello spazio pixel. Controlla l'influenza del condizionamento per regione tramite self-attention, moltiplicata per `strength`. | MASK | No | N/A |

### Note

- Sia `latent` che `guiding_latent` devono essere latenti video 5D con forma (batch, canali, frame, altezza, larghezza).
- La guida deve rientrare nel latente di destinazione: il conteggio dei frame della guida aggiunto a `latent_idx` non deve superare la fine del latente di destinazione. I valori negativi di `latent_idx` sono consentiti e posizionano la guida prima dell'inizio del latente.
- La dimensione spaziale della guida deve dividere quella del target per un numero intero sia sull'asse dell'altezza sia su quello della larghezza.
- Il rapporto dell'altezza e il rapporto della larghezza devono avere lo stesso valore (un rapporto quadrato). Un rapporto non quadrato genera un errore, perché la dilatazione e il posizionamento RoPE usano un singolo fattore di downscale per entrambi gli assi.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `positive` | Condizionamento positivo con la guida associata. | CONDITIONING |
| `negative` | Condizionamento negativo con la guida associata. | CONDITIONING |
| `latent` | Output latente con la guida applicata, inclusa la `noise_mask` aggiornata. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/it.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
