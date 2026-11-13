# Breeze Voice Design

Crea una nuova voce Breeze da una descrizione scritta. Fornisci una descrizione della voce e una frase che pronunci; la voce viene creata da questa anteprima e salvata nel tuo account.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `description` | Descrizione della voce in 3 a 500 caratteri: età, genere, accento, tono, ritmo. Predefinito: vuoto. | STRING | Sì | 3 a 500 caratteri |
| `preview_text` | La frase che la nuova voce pronuncia nell'anteprima, fino a 500 caratteri. Scrivila nella lingua selezionata, perché la voce viene creata da questa anteprima. Predefinito: vuoto. | STRING | Sì | 1 a 500 caratteri |
| `language` | Lingua del testo di anteprima. Inglese e cinese possono usare entrambi i modelli; le altre lingue usano Breeze TTS 2 Multilingual. | DYNAMIC_COMBO | Sì | Più opzioni disponibili |
| `strength` | Quanto fedelmente la voce segue la descrizione. Predefinito: 4.0. | FLOAT | No | 1.0 a 10.0 (passo: 0.1) |
| `seed` | Controlla se il nodo viene rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | No | 0 a 2147483647 |

### Input per lingua "English" e "Chinese"

Questi campi compaiono solo quando `language` è English o Chinese.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` o `Breeze TTS 2 Multilingual`. Predefinito: `"Breeze TTS 2"`. | COMBO | Sì | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `voice` | La nuova voce Breeze, denominata in base alla descrizione. | BREEZE_VOICE |
| `preview` | Anteprima audio della voce progettata. | AUDIO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceDesign/it.md)

---
**Source fingerprint (SHA-256):** `5b0ea4ccd03e442972a71ec839be7b755f569686400e472967a09a956de0982f`
