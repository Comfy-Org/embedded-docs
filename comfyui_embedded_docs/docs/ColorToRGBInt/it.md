# ColorToRGBInt

Il nodo **ColorToRGBInt** converte un colore fornito in formato esadecimale (come `#FF5733`) in un singolo valore intero RGB. Estrae le componenti rossa, verde e blu dalla stringa del colore, le combina in un unico intero e restituisce anche la rappresentazione esadecimale originale e il valore alfa (opacità).

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `color` | Un valore di colore nel formato esadecimale `#RRGGBB` o `#RRGGBBAA`. Deve essere lungo 7 o 9 caratteri e iniziare con `#`. | COLOR | Sì | `#RRGGBB`<br>`#RRGGBBAA` |

**Nota:** La stringa di input `color` deve seguire il formato `#RRGGBB` o `#RRGGBBAA`. Se non è lunga 7 o 9 caratteri, non inizia con `#` o contiene caratteri esadecimali non validi, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `rgb_int` | Il valore intero RGB calcolato, derivato dalla formula: `(Red * 65536) + (Green * 256) + Blue`. | INT |
| `hex` | La stringa di colore esadecimale nel formato `#RRGGBB`. Se l'input includeva un canale alfa, questo viene rimosso da questo output. | COLOR |
| `alpha` | Il valore alfa (opacità) compreso tra 0.0 e 1.0. È uguale a 1.0 quando l'input è `#RRGGBB`, oppure al valore del canale alfa diviso per 255 quando l'input è `#RRGGBBAA`. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/it.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`
