# Sonilo Music 1.5

Il nodo Sonilo Music 1.5 genera una canzone completa con voce cantata a partire da un prompt testuale. Descrivi genere, atmosfera, strumenti e voce e, facoltativamente, fornisci il tuo testo; il nodo invia la richiesta al servizio Sonilo e restituisce il brano finito come audio. Usalo quando ti serve una canzone completa anziché un estratto strumentale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt` | Descrizione della canzone: genere, atmosfera, strumenti e voce. Per impostare personalmente il testo, aggiungi un blocco `Lyrics:` con i tag `[Verse]` e `[Chorus]`; senza di esso il modello scrive il proprio testo. Deve contenere da 1 a 2000 caratteri dopo la rimozione degli spazi bianchi iniziali e finali. | STRING | Sì | Da 1 a 2000 caratteri |
| `duration` | `auto` adatta la durata della canzone al testo. `custom` usa il valore `seconds`, tagliando il testo che non rientra e ripetendo quelli brevi. | DYNAMIC_COMBO | Sì | `"auto"`<br>`"custom"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 42). | INT | Sì | Da 0 a 18446744073709551615 |

### Parametri di durata personalizzata (quando `duration` è `"custom"`)

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `seconds` | Durata della canzone generata in secondi (predefinito: 60). | INT | Sì | Da 10 a 360 |

**Nota:** l'input `prompt` è obbligatorio e non deve essere vuoto. Il nodo verifica che contenga almeno 1 carattere dopo la rimozione degli spazi bianchi iniziali e finali e non più di 2000.

**Nota:** l'utilizzo viene addebitato a $0.0032175 per secondo della durata richiesta e l'indicatore del prezzo segue `duration.seconds` quando è selezionato `custom`.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `audio` | La canzone generata, incluse le voci, come file audio. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloMusic15/it.md)

---
**Source fingerprint (SHA-256):** `65ccf74ccdfa7a710d8c7bd9871e666d79ceadc7304644fe0101956832ca6024`
