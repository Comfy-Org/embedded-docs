# Pika Music

Questo nodo genera musica a partire da una descrizione testuale e da testi opzionali, oppure esegue una cover di un brano fornito, con Pika. Scegli `"text to music"` per scrivere un nuovo brano della durata che imposti, oppure `"cover"` per registrare di nuovo un brano mantenendone la durata.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mode` | Cosa fa il nodo: `"text to music"` scrive un nuovo brano, `"cover"` registra di nuovo un brano fornito. Ogni modalità mostra i propri input di seguito. Predefinito: `"text to music"`. | DYNAMIC_COMBO | Sì | `"text to music"`<br>`"cover"` |

### Input di Text to Music

Questi input compaiono quando `mode` è impostato su `"text to music"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Come deve suonare la musica. Non può essere vuoto. Predefinito: "" (stringa vuota). | STRING | Sì | 1 a 4000 caratteri |
| `lyrics` | Testi opzionali. Sono consentiti tag di sezione come `[Verse]` e `[Chorus]`. Predefinito: "" (stringa vuota). | STRING | Sì | 0 a 8000 caratteri |
| `duration` | Durata del brano in secondi. Predefinito: 30.0. | FLOAT | Sì | 10.0 a 360.0 (passo: 0.1) |
| `rewrite_prompt` | Espande un prompt breve o vago con un modello prima della generazione. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `seed` | Seme per il campionamento. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

### Input di Cover

Questi input compaiono quando `mode` è impostato su `"cover"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `source_audio` | Il brano di cui eseguire la cover. Il risultato ha la stessa durata, limitata a un intervallo da 5 a 360 secondi. | AUDIO | Sì | - |
| `prompt` | Come deve suonare la cover. Non può essere vuoto. Predefinito: "" (stringa vuota). | STRING | Sì | 1 a 4000 caratteri |
| `lyrics` | Testi opzionali. Sono consentiti tag di sezione come `[Verse]` e `[Chorus]`. Predefinito: "" (stringa vuota). | STRING | Sì | 0 a 8000 caratteri |
| `rewrite_prompt` | Espande un prompt breve o vago con un modello prima della generazione. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `seed` | Seme per il campionamento. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

**Vincoli:**

* Il prompt deve essere compreso tra 1 e 4000 caratteri, mentre i testi non devono superare gli 8000 caratteri.
* La modalità cover ignora `duration`: l'output corrisponde alla durata di `source_audio`, limitata a un intervallo da 5 a 360 secondi.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `AUDIO` | Il brano generato, oppure la cover del brano fornito. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaMusicNode/it.md)

---
**Source fingerprint (SHA-256):** `e3051b2d0cfff72cf7e359d7383f4e0d133df0338ff42a00f0649387f504ec28`
