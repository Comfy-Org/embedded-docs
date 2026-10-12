# Luma Ray 3.2 Estendi Video

Luma Ray 3.2 Extend Video continua una precedente generazione video Luma Ray 3.2 creando un nuovo segmento di 5 secondi o dopo il clip originale (forward) o prima di esso (backward). Collega l'output `generation_id` da un nodo Luma Ray 3.2 precedente per usare quel clip come fotogramma iniziale (forward) o fotogramma finale (backward) dell'estensione. Le estensioni sono sempre lunghe 5 secondi.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `source_generation_id` | ID di generazione del video Ray 3.2 precedente da estendere. Collega l'output `generation_id` di un altro nodo Luma Ray 3.2. Predefinito: "" (vuoto). Questo valore è obbligatorio e non deve essere vuoto. | STRING | Sì | – |
| `direction` | Forward continua dopo il clip precedente; backward viene anteposto prima di esso. Forward usa il clip di origine come fotogramma iniziale; backward lo usa come fotogramma finale. Selezionando "Forward (continue after)" si aggiunge l'opzione `loop`. | DYNAMIC_COMBO | Sì | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `prompt` | Prompt testuale per il nuovo contenuto. Predefinito: "" (vuoto). Deve essere compreso tra 1 e 6000 caratteri. | STRING | Sì | da 1 a 6000 caratteri |
| `resolution` | Risoluzione di output per il segmento video esteso. Predefinito: "720p". | COMBO | Sì | "540p"<br>"720p"<br>"1080p" |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati sono non deterministici indipendentemente dal seed. Predefinito: 0. | INT | Sì | da 0 a 0xFFFFFFFFFFFFFFFF (18446744073709551615) |

### Input di Forward (continue after)

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `loop` | Esegue il loop del video esteso senza interruzioni (solo estensione forward). Predefinito: False. | BOOLEAN | No | True<br>False |

### Input di Backward (lead-in before)

Questa direzione non aggiunge parametri aggiuntivi.

**Nota:** Le estensioni durano sempre 5 secondi. Il parametro `loop` è disponibile solo quando `direction` è "Forward (continue after)"; quando si usa "Backward (lead-in before)", l'opzione `loop` non è disponibile. Il `prompt` deve essere compreso tra 1 e 6000 caratteri. Il `source_generation_id` è obbligatorio e deve essere collegato dall'output `generation_id` di un nodo Luma Ray 3.2 precedente.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `VIDEO` | Il segmento video esteso generato, della durata di 5 secondi. | VIDEO |
| `generation_id` | Identificatore univoco per questa generazione, che può essere collegato a un altro nodo Luma Ray 3.2 Extend Video per ulteriori estensioni. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
