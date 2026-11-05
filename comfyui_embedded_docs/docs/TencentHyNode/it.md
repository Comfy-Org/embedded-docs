# Tencent HY

Questo nodo genera risposte testuali con il modello Hy4 di Tencent. Invia un prompt testuale e, facoltativamente, una o più immagini come contesto, quindi restituisce la risposta del modello come testo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello utilizzato per generare la risposta. Selezionandolo vengono mostrati i relativi input di seguito. Predefinito: `"Hy4"`. | DYNAMIC_COMBO | Sì | `"Hy4"` |

### Input di Hy4

Questi input compaiono quando `model` è impostato su `"Hy4"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Il messaggio da inviare al modello. Non deve essere vuoto. Predefinito: "" (stringa vuota). | STRING | Sì | Almeno 1 carattere |
| `images` | Fino a 20 immagini. Ogni immagine in un batch viene conteggiata. Predefinito: nessuna immagine. | AUTOGROW | No | 0 a 20 immagini |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati sono non deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |
| `system_prompt` | Istruzioni fondamentali che determinano il comportamento del modello. Predefinito: "" (stringa vuota). | STRING | No | - |
| `reasoning` | Il modello ragiona prima di rispondere. Le risposte richiedono più tempo e utilizzano più token; le attività molto difficili possono andare in timeout. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `temperature` | Controlla la casualità. I risultati variano comunque a 0. Predefinito: 1.0. | FLOAT | Sì | 0.0 a 1.4 (passo: 0.01) |
| `max_tokens` | Numero massimo di token da generare, inclusi i token di ragionamento quando `reasoning` è attivo. Le risposte molto lunghe possono andare in timeout. Predefinito: 32000. | INT | Sì | 1 a 64000 |

**Vincoli:**

* Vengono accettate al massimo 20 immagini per richiesta, conteggiando ogni immagine di un batch.
* Il filtro dei contenuti di Tencent può bloccare una richiesta, generando un errore.
* Se `max_tokens` si esaurisce prima che la risposta sia completata, il nodo genera un errore: aumentare `max_tokens` o disattivare `reasoning`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `STRING` | La risposta testuale del modello Hy4. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentHyNode/it.md)

---
**Source fingerprint (SHA-256):** `c7c1d2908d2fba8172fa279b7d273f5f3f96cf10b531f81650824fc8e0176f21`
