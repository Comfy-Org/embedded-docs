# Ideogram & Pruna P-Image

Ideogram & Pruna P-Image genera immagini da un prompt testuale utilizzando il modello text-to-image veloce di Ideogram, noto per la tipografia forte e il fotorealismo. Supporta inoltre le didascalie JSON strutturate di Ideogram 4.0 per un controllo preciso su stringhe di testo, colori e layout. Il nodo restituisce le immagini generate insieme al prompt finale con cui l'immagine è stata effettivamente generata.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `prompt` | Prompt testuale. Accetta anche una didascalia JSON strutturata di Ideogram 4.0 (colori esatti come esadecimali #RRGGBB, stringhe di testo esatte, layout con bounding-box) — impostare prompt_upsampling su OFF per usarla così com'è. Non deve essere vuoto. (predefinito: "") | STRING | Sì | Qualsiasi testo non vuoto |
| `quality` | Livello di velocità/prezzo/qualità. MEDIUM è il valore predefinito per l'uso quotidiano; HIGH per prompt complessi, dettagli fini e testo difficile; VERY_LOW/LOW per bozze su larga scala. Il testo difficile viene reso male sotto MEDIUM. (predefinito: "MEDIUM") | COMBO | Sì | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | Classe di dimensione dell'output (i pixel esatti seguono le proporzioni, ad es. 16:9 dà 1280x720 a 1K e 2560x1440 a 2K). Preferire HIGH + 2K per una tipografia nitida. (predefinito: "1K") | COMBO | Sì | "1K"<br>"2K" |
| `aspect_ratio` | Le proporzioni per la generazione dell'immagine. (predefinito: "1:1") | COMBO | Sì | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | Espande i prompt brevi in una didascalia strutturata dettagliata prima della generazione (il prompt riscritto viene restituito come final_prompt). Impostare su OFF quando si fornisce una propria didascalia JSON o una formulazione esatta. (predefinito: "AUTO") | COMBO | Sì | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Seme per una generazione riproducibile. Con prompt_upsampling OFF, lo stesso seme e le stesse impostazioni restituiscono la stessa immagine; con ON/AUTO la riscrittura del prompt varia a ogni esecuzione — per riprodurre un risultato, riutilizzare il suo output final_prompt con prompt_upsampling OFF e lo stesso seme. (predefinito: 42) | INT | No | da 0 a 2147483647 |

**Nota sui vincoli:** Il prompt deve contenere almeno un carattere non di spaziatura, altrimenti il nodo fallisce. Impostare `prompt_upsampling` su OFF quando si fornisce una propria didascalia JSON strutturata o una formulazione esatta. Quando `prompt_upsampling` è ON o AUTO, il prompt viene riscritto prima della generazione, quindi lo stesso seme potrebbe non riprodurre la stessa immagine; per riprodurre un'immagine, riutilizzare il suo output `final_prompt` con `prompt_upsampling` OFF e lo stesso seme.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine o le immagini generate, restituite come batch di immagini. Se il filtro di sicurezza dei contenuti di Ideogram blocca la generazione, viene invece sollevato un errore. | IMAGE |
| `final_prompt` | Il prompt con cui l'immagine è stata effettivamente generata (la didascalia strutturata riscritta quando prompt_upsampling è stato eseguito, altrimenti il tuo prompt). Reimmettilo con prompt_upsampling OFF e lo stesso seme per riprodurre questa immagine. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/it.md)

---
**Source fingerprint (SHA-256):** `6b014c2f097c49b5930f38869a4e2da0ebb19863763ae5817d6e566a36d2b8e8`
