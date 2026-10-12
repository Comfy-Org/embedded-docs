# Flux Video Edit

Modifica una clip video esistente a partire da un'istruzione scritta. Puoi rimuovere, aggiungere o sostituire oggetti, cambiare l'ambientazione, rielaborare lo stile del filmato, modificare il testo a schermo o sostituire il dialogo parlato. La durata, l'inquadratura, il movimento della telecamera e l'audio provengono dalla clip di origine, quindi tutto ciò che non menzioni nel prompt rimarrà com'era.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Clip di origine da 0.7 a 15 secondi, almeno 160x160 pixel. L'output viene renderizzato a 24 fps e limitato a circa 0.9 megapixel per frame, quindi un'origine più grande viene restituita più piccola. | VIDEO | Sì | 0.7–15 secondi; minimo 160x160 pixel |
| `prompt` | Cosa modificare, in linguaggio semplice, fino a 4096 caratteri. Tutto ciò che non menzioni è destinato a rimanere com'era. Il dialogo sostitutivo deve adattarsi al tempo occupato dal parlato originale, e una clip silenziosa rimane silenziosa. Predefinito: stringa vuota. | STRING | Sì | 1–4096 caratteri |
| `auto_downscale` | Ridimensiona automaticamente verso il basso le origini più grandi di 1280x704 pixel in area prima del caricamento. Le proporzioni vengono preservate; i video più piccoli restano invariati. Predefinito: true. | BOOLEAN | No | true<br>false |
| `safety_tolerance` | Tolleranza di moderazione, 0 è il valore più severo. Predefinito: 4. | INT | No | 0–4 |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; FLUX sceglie il proprio seed, quindi i risultati effettivi sono non deterministici indipendentemente da questo valore. Predefinito: 42. | INT | No | 0–4294967295 |

**Nota:** Il `prompt` deve contenere almeno 1 carattere e non più di 4096 caratteri. Il `video` di origine deve durare tra 0.7 e 15 secondi e avere almeno 160x160 pixel; i caricamenti che non rispettano questi limiti vengono rifiutati prima dell'invio della richiesta.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | La clip video modificata restituita dal servizio FLUX. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoEditNode/it.md)

---
**Source fingerprint (SHA-256):** `169b14700acfee3f6ccc247f08f3ae8c5f3c4610062a447e8215246460299b6a`
