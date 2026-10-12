# Converti spazio colore dell'immagine

Il nodo ImageColorSpace converte le immagini tra gli spazi colore sRGB (Rec.709), Rec.709 lineare, HDR (Rec.2020 HLG), HDR PQ (Rec.2020 PQ), HDR LogC3 e HDR ACEScct. LogC3 utilizza la curva EI 800 con primari Rec.709 e codici limitati a [0, 1]; ACEScct utilizza primari AP1 e bianco D60, con adattamento Bradford a D65. Quando converte verso l'output SDR, o da HDR PQ a HDR, applica il tone mapping alla luminanza in eccesso sull'intero batch e comprime i colori fuori gamut; gli output lineari e ACEScct, e le conversioni da lineare a HDR, preservano i valori estesi. Gli output HLG e PQ applicano il clipping ai canali negativi. Le conversioni sono calcolate in float32 e qualsiasi canale alfa viene passato invariato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da convertire. | IMAGE | Sì | Qualsiasi immagine valida. |
| `source` | Spazio colore dei pixel di input. Predefinito: "sRGB". | COMBO | Sì | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"`<br>`"HDR LogC3"`<br>`"HDR ACEScct"` |
| `destination` | Spazio colore dei pixel di output. Imposta il nodo di salvataggio su questo stesso spazio colore. Converti LogC3 o ACEScct in lineare prima di salvare in EXR, oppure in sRGB/HDR/HDR PQ prima di salvare video. Predefinito: "sRGB". | COMBO | Sì | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"`<br>`"HDR LogC3"`<br>`"HDR ACEScct"` |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine convertita nello spazio colore di destinazione specificato. | IMAGE |

## Note

- Il valore lineare 1.0 utilizza lo stesso bianco di riferimento da 203 nit di sRGB; HLG utilizza un display di riferimento da 1000 nit.
- Gli output lineari e ACEScct preservano i valori estesi; le conversioni da lineare a HDR preservano le alte luci senza tone mapping.
- L'output SDR e la conversione da PQ a HLG applicano il tone mapping alla luminanza in eccesso sull'intero batch (condividendo un unico punto di bianco, così l'esposizione non cambia da un fotogramma all'altro) e comprimono i colori fuori gamut. Gli output HLG e PQ applicano il clipping ai canali negativi.
- Le conversioni sono calcolate in float32 e vengono restituite sul dispositivo e con il dtype intermedi.
- LogC3 e ACEScct sono codifiche log della camera: convertili in lineare per il salvataggio in EXR, oppure in sRGB/HDR/HDR PQ prima di salvare video.
- L'alpha straight non subisce trasformazioni colore; vengono convertiti solo i canali RGB.
- Se `source` e `destination` sono uguali, non viene applicata alcuna trasformazione colore — l'immagine viene solo spostata sul dispositivo e sul dtype intermedi.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/it.md)

---
**Source fingerprint (SHA-256):** `fdf8b4f16a1e0c7ff9a86b8cc40f6f796175205e4b1f491b595a74a8456b9b94`
