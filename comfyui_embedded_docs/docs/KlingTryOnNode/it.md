# KlingTryOnNode

Vesti una persona con un capo di abbigliamento tramite il virtual try-on di Kling. Collega una foto di una persona e una foto del capo, e il nodo restituisce una nuova immagine di quella persona che indossa l'indumento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `person_image` | Foto di una persona, idealmente frontale o di tre quarti. Deve essere almeno 300x300 pixel; le immagini con un lato superiore a 2048 pixel vengono prima ridimensionate. | IMAGE | Sì | N/A |
| `garment_image` | Il capo da indossare: foto di prodotto, flat lay, manichino o foto indossata da un modello. Una foto indossata da un modello può riportare anche il resto di quel completo. Deve essere almeno 300x300 pixel. Solo abbigliamento; scarpe, borse e accessori non sono supportati. | IMAGE | Sì | N/A |
| `keep_pose` | Disattiva per consentire alla posa di cambiare per una migliore presentazione del completo. Parametro avanzato (predefinito: True). | BOOLEAN | Sì | `True`<br>`False` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Questo parametro ha la funzionalità "control after generate" (predefinito: 42). | INT | Sì | 0 a 2147483647 |

**Nota:** Il risultato ha le stesse dimensioni di `person_image`, con un limite di 2048 pixel sul lato più lungo. Entrambi gli input vengono caricati sull'API di Kling, il che può richiedere un momento.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | La persona che indossa il capo di abbigliamento. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTryOnNode/it.md)

---
**Source fingerprint (SHA-256):** `03c2f9f1169ec2de3dd58162f9a7718a9c1f9af584aa63f280a0c4feefb70478`
