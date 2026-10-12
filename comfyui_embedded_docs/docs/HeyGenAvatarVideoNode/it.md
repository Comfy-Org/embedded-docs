# HeyGenAvatarVideoNode

Genera un video con presentatore parlante da un avatar HeyGen. Questo nodo crea un video di un avatar AI che parla del testo fornito o esegue il lip-sync sul tuo audio, utilizzando i motori di rendering di HeyGen.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `engine` | Motore di rendering; ogni scelta elenca solo gli avatar che lo supportano. "auto" offre ogni avatar e sceglie il suo motore migliore (Avatar IV preferito). Avatar V è il più fedele, Avatar III è il più economico. | DYNAMIC_COMBO | Sì | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `custom_avatar_id` | ID opzionale dell'aspetto avatar di HeyGen. Se impostato, sovrascrive l'avatar selezionato sopra. Può essere utilizzato qualsiasi aspetto pubblico di HeyGen (oltre 3000) (o i tuoi avatar privati). Predefinito: `""`. | STRING | No |  |
| `speech` | Guida l'avatar con un copione testuale (sintesi vocale di HeyGen) o il tuo audio. Nome visualizzato: "sorgente vocale". | DYNAMIC_COMBO | Sì | `"script"`<br>`"audio"` |
| `resolution` | Risoluzione del video in uscita. Predefinito: `"1080p"`. | COMBO | No | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Proporzioni del video in uscita. "auto" segue il filmato di origine dell'avatar. Predefinito: `"auto"`. | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `background_color` | Colore di sfondo solido opzionale come codice esadecimale (es. `"#00ff00"`). Lasciare vuoto per utilizzare lo sfondo dell'avatar. Se fornito, il valore deve iniziare con `#`. Predefinito: `""`. | STRING | No |  |
| `seed` | Non inviato a HeyGen; modificalo per forzare una nuova esecuzione. Predefinito: `42`. | INT | No | Minimo: 0<br>Massimo: 2147483647 |

### Input di `auto`

Quando `engine` è `"auto"`, il seguente sotto-parametro è disponibile:

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `avatar` | Aspetto avatar per presentare il video (curato dalla libreria pubblica di HeyGen). Il miglior motore supportato dall'aspetto viene scelto automaticamente. | COMBO | Sì | Più opzioni disponibili |

### Input di `avatar_iv`

Quando `engine` è `"avatar_iv"`, il seguente sotto-parametro è disponibile:

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `avatar` | Aspetti avatar che supportano il motore Avatar IV. | COMBO | Sì | Più opzioni disponibili |

### Input di `avatar_iii`

Quando `engine` è `"avatar_iii"`, il seguente sotto-parametro è disponibile:

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `avatar` | Aspetti avatar che supportano il motore Avatar III. | COMBO | Sì | Più opzioni disponibili |

### Input di `avatar_v`

Quando `engine` è `"avatar_v"`, il seguente sotto-parametro è disponibile:

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `avatar` | Aspetti avatar che supportano il motore Avatar V. | COMBO | Sì | Più opzioni disponibili |

### Input di `script`

Quando `speech` è `"script"`, i seguenti sotto-parametri sono disponibili:

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `text` | Testo che l'avatar deve pronunciare (fino a 5000 caratteri). Il parlato generato deve durare almeno 1 secondo. Predefinito: `""`. | STRING | Sì | Minimo: 1 carattere<br>Massimo: 5000 caratteri |
| `voice` | Voce per il copione. L'opzione predefinita utilizza la voce che HeyGen ha assegnato all'avatar. Ignorata se `custom_voice_id` è impostato. | COMBO | Sì | `"(avatar's default voice)"`<br>Più opzioni vocali generali disponibili |
| `custom_voice_id` | ID voce HeyGen opzionale. Se impostato, sovrascrive la voce selezionata sopra. Può essere utilizzata qualsiasi voce dalla libreria di HeyGen (oltre 2000). Predefinito: `""`. | STRING | No |  |
| `voice_speed` | Moltiplicatore della velocità del parlato. Predefinito: `1.0`. | FLOAT | No | Minimo: 0.5<br>Massimo: 1.5<br>Passo: 0.05 |

### Input di `audio`

Quando `speech` è `"audio"`, il seguente sotto-parametro è disponibile:

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `audio` | Audio per il lip-sync dell'avatar, fino a 10 minuti. | AUDIO | Sì |  |

Nota: `engine` e `speech` sono selettori che rivelano sotto-parametri diversi a seconda del valore scelto. Il selettore `speech` ha due modalità mutuamente esclusive: nella modalità `"script"`, `text` è obbligatorio; se viene fornito `custom_voice_id`, questo sovrascrive `voice`. Nella modalità `"audio"`, l'avatar esegue il lip-sync sul clip audio fornito. `background_color` deve essere un codice colore esadecimale che inizia con `#` quando fornito. Quando `custom_avatar_id` è impostato, sovrascrive la selezione di `avatar`, e il `engine` selezionato deve essere supportato da quell'aspetto avatar; altrimenti viene generato un errore a meno che `engine` non sia `"auto"`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `VIDEO` | Il video del presentatore avatar generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `86dc799d3a8cf2666449b0d422853b12feffb81ce002f84594f9b925d58b522a`
