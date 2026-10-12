# LoadLoraTextEncoder

Applica una serie di LoRA a un codificatore di testo CLIP in un singolo nodo. Ogni riga di `loras` contiene un file LoRA, la sua forza e un interruttore on/off; le righe vengono applicate dall'alto verso il basso, quindi ogni riga applica una patch al risultato della riga precedente. I file LoRA che modificano il codificatore di testo vengono solitamente applicati anche al modello, quindi questo nodo viene normalmente abbinato a Load LoRA (Model) usando le stesse righe.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il codificatore di testo CLIP a cui verranno applicati i LoRA. | CLIP | Sì | - |
| `loras` | Gruppo espandibile di LoRA, applicati al codificatore di testo nell'ordine delle righe (`loras.0`, `loras.1` e così via). Aggiungi una riga per ogni LoRA; ogni riga contiene un file, una forza e un interruttore on/off. | DYNAMIC_GROUP | Sì | da 1 a 20 righe |

### Campi della riga `loras`

Ogni riga ripete i seguenti campi e ciascun campo è obbligatorio all'interno di una riga inviata.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `lora_name` | Il nome del file LoRA da applicare. | COMBO | Sì | Più opzioni disponibili |
| `strength` | Con quale intensità applicare questo LoRA al codificatore di testo. `0` lo disattiva e un valore negativo inverte l'effetto. (predefinito: 1.0) | FLOAT | Sì | da -100 a 100 (passo 0.01) |
| `enabled` | Disattiva per saltare questo LoRA senza modificarne il file o la forza. (predefinito: true) | BOOLEAN | Sì | false / true |

### Vincoli dei parametri

- **Numero di righe:** è necessario inviare almeno una riga e sono accettate al massimo 20 righe, quindi l'indice di riga più alto è 19.
- **Righe saltate:** una riga viene saltata quando il suo file è vuoto, quando `enabled` è disattivato o quando `strength` è `0`. Una forza negativa viene passata anziché saltata.
- **Ordine delle righe:** le righe vengono applicate nell'ordine in cui compaiono e ogni riga parte dal codificatore di testo restituito dalla riga precedente.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CLIP` | Il codificatore di testo CLIP dopo che sono state applicate le righe LoRA non saltate. | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraTextEncoder/it.md)

---
**Source fingerprint (SHA-256):** `0b290d2caddc3937e962e65c70a5c99cbd4cdb40ab6f86bba8f0c270e5cebf00`
