# Convert SDR to HDR

Il nodo **Convert SDR to HDR** espande le immagini sRGB a gamma dinamica standard in HDR HLG Rec.2020. Mantiene l'aspetto esistente dell'immagine e mappa la sua luminosità in un intervallo più ampio, quindi il risultato deve essere salvato con uno spazio colore HDR selezionato. L'alpha viene preservato invariato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine (o le immagini) SDR in sRGB da espandere in HDR. | IMAGE | Sì | - |
| `algorithm` | Algoritmo di espansione HDR. Selezionando un algoritmo vengono rivelati i suoi parametri (`target_luminance`). | DYNAMIC_COMBO | Sì | `"lottes"` |

### Input di lottes

Questi parametri appaiono quando `algorithm` è impostato su `"lottes"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `target_luminance` | Target di picco del bianco in nit. 0 mantiene il rendering calibrato. Le immagini scure non vengono normalizzate a questo picco. (predefinito: 650.0) | FLOAT | Sì | 0.0 a 10000.0 (passo 1.0) |

Ogni immagine del batch viene convertita separatamente: la codifica sRGB viene invertita in luce lineare, la luminosità viene espansa con una curva razionale in stile Lottes combinata con una curva calibrata di guadagno logaritmico monotono, e il risultato viene ricodificato come Rec.2020 HLG. Poiché l'output è HDR, il nodo di salvataggio deve utilizzare lo spazio colore `HDR`; salvarlo come sRGB renderizza la luminosità in modo errato.

HLG presuppone un display di riferimento da 1000 nit, quindi i valori di `target_luminance` inferiori a 1000 mantengono quel riferimento e un valore di `0` lascia il rendering calibrato invariato. Le immagini a canale singolo vengono espanse a tre canali prima della conversione, e il canale alpha viene copiato invariato.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine (o le immagini) HDR HLG Rec.2020. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSDRToHDR/it.md)

---
**Source fingerprint (SHA-256):** `51eb0beac3d48345a30ba66d80d95873384cf5155fc06c33353b6d1dc029658a`
