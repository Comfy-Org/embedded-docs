# LoadLoraModel

Applica una pila di LoRA a un modello di diffusione in un unico nodo. Ogni riga di `loras` contiene un file LoRA, la sua forza e un interruttore on/off, e le righe vengono applicate dall'alto verso il basso, così ogni riga applica una patch al risultato della riga precedente. Usa questo nodo invece di concatenare diversi caricatori LoRA singoli quando un flusso di lavoro applica un lungo elenco di LoRA allo stesso modello.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione a cui verranno applicati i LoRA. | MODEL | Sì | - |
| `loras` | Gruppo espandibile di LoRA, applicati al modello nell'ordine delle righe (`loras.0`, `loras.1` e così via). Aggiungi una riga per ogni LoRA; ogni riga contiene un file, una forza e un interruttore on/off. | DYNAMIC_GROUP | Sì | da 1 a 20 righe |

### Campi della riga `loras`

Ogni riga ripete i seguenti campi e ciascun campo è obbligatorio all'interno di una riga inviata.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `lora_name` | Il nome del file LoRA da applicare. | COMBO | Sì | Più opzioni disponibili |
| `strength` | Quanto fortemente applicare questo LoRA. `0` lo disattiva, e un valore negativo ne inverte l'effetto. (predefinito: 1.0) | FLOAT | Sì | da -100 a 100 (passo 0.01) |
| `enabled` | Disattiva per saltare questo LoRA senza modificarne il file o la forza. (predefinito: true) | BOOLEAN | Sì | false / true |

### Vincoli sui parametri

- **Numero di righe:** è necessario inviare almeno una riga e sono accettate al massimo 20 righe, quindi l'indice di riga più alto è 19.
- **Righe saltate:** una riga viene saltata quando il suo file è vuoto, quando `enabled` è disattivato o quando `strength` è `0`. Una forza negativa viene passata invece di essere saltata.
- **Ordine delle righe:** le righe vengono applicate nell'ordine in cui compaiono e ogni riga parte dal modello restituito dalla riga precedente.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `MODEL` | Il modello di diffusione dopo che sono state applicate le righe LoRA non saltate. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraModel/it.md)

---
**Source fingerprint (SHA-256):** `a656bba0248d2f6d4eb65e15e3a19f2e76edecd4b34710921a02f3ba5c598e1d`
