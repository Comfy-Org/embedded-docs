# Immagine Flux 3

Flux 3 Image genera un'immagine con FLUX 3 a partire da un prompt, oppure modifica e combina immagini di riferimento. Scrivi ciò che desideri come istruzione, poi collega fino a 10 immagini di riferimento e fai riferimento a esse nel prompt come image 1, image 2 e così via. Il prompt viene interpretato ed espanso prima della generazione, e il risultato viene renderizzato con le proporzioni e la risoluzione scelte.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Cosa generare o la modifica da apportare. Il prompt viene interpretato ed espanso prima della generazione. Fai riferimento alle immagini di riferimento collegate come image 1, image 2 e così via. (predefinito: "") | STRING | Sì | da 1 a 15000 caratteri |
| `images` | Slot espandibile per immagini di riferimento; collegane fino a 10 in totale. Ogni immagine deve essere di almeno 256x256 pixel e le sue proporzioni non possono essere più estreme di 64:1. | IMAGE | No | da 0 a 10 immagini |
| `bounding_boxes` | Riquadri opzionali dal nodo Create Bounding Boxes che posizionano oggetti o testo nell'output. Le posizioni sono relative alla tela, quindi fornisci al nodo le proporzioni dell'output. | ARRAY | No | - |
| `aspect_ratio` | Proporzioni dell'immagine generata. "auto" segue la prima immagine di riferimento oppure sceglie un rapporto dal prompt. (predefinito: "auto") | COMBO | Sì | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"7:5"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"5:7"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"9:21"` |
| `resolution` | Dimensione dell'output con le proporzioni scelte: 0.75K è circa 0,6 megapixel, 1K 1 MP, 1.5K 2,4 MP, 2K 4,2 MP, 4K 16,8 MP. (predefinito: "2K") | COMBO | Sì | `"0.75K"`<br>`"1K"`<br>`"1.5K"`<br>`"2K"`<br>`"4K"` |
| `grounding` | Consente al modello di fare ricerche sul prompt con la ricerca web e immagini prima della generazione. (predefinito: True) | BOOLEAN | Sì | True<br>False |
| `safety_tolerance` | Tolleranza della moderazione; 0 è il valore più restrittivo. (predefinito: 4) | INT | Sì | da 0 a 4 |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; FLUX 3 sceglie il proprio seed, quindi i risultati effettivi sono non deterministici indipendentemente da questo valore. (predefinito: 42) | INT | Sì | da 0 a 4294967295 |

`safety_tolerance` è un input avanzato, e `seed` include i controlli Control After Generate nell'interfaccia utente.

Le immagini di riferimento vengono caricate prima dell'invio della richiesta. Un singolo slot può contenere un batch e ogni frame di ogni batch conta ai fini del limite di 10 immagini.

Le righe di `bounding_boxes` vengono aggiunte al prompt, quindi il prompt e le descrizioni dei riquadri insieme non devono superare i 15000 caratteri.

Il prezzo visualizzato dipende da `resolution`: $0.05863 a 0.75K, $0.06864 a 1K, $0.1001 a 1.5K, $0.143 a 2K e $0.86801 a 4K.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine generata, scaricata dal risultato di FLUX 3. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageNode/it.md)

---
**Source fingerprint (SHA-256):** `f32a90887227f9ce9e6ed04a76cde452a70f36fb97d8c36d7c55140855c1f593`
