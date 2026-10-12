# LoopProgress

LoopProgress è un nodo ausiliario solo per lo sviluppo che segnala l'avanzamento di un ciclo all'interfaccia server di ComfyUI. A ogni esecuzione invia il testo "Iteration X / Y" al client e restituisce la posizione dell'iterazione corrente invariata, il che gli consente di essere inserito inline all'interno di un ciclo senza alterare il flusso dati.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `start_id` | Identificatore dell'istanza di prompt/ciclo a cui appartiene il messaggio di avanzamento. Il primo elemento della lista fornita viene utilizzato per instradare il testo di avanzamento all'esecuzione in corso corretta. | STRING | Sì | - |
| `position` | La posizione (indice) dell'iterazione corrente. Il primo elemento della lista fornita viene utilizzato nel messaggio di avanzamento ed è anche restituito come output. | INT | Sì | - |
| `total` | Il numero totale di iterazioni. Usato insieme a `position` per costruire il messaggio di avanzamento "Iteration X / Y". | INT | Sì | - |

Nota: questo nodo è dichiarato con input di tipo lista (`is_input_list=True`) e accetta tutti gli input, quindi ogni valore connesso viene trattato come una lista e viene letto solo il suo primo elemento. Il nodo viene sempre eseguito (la sua impronta degli input è fissa), quindi viene rieseguito a ogni passaggio del ciclo.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `position` | La posizione dell'iterazione corrente, passata invariata dall'input `position`. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopProgress/it.md)

---
**Source fingerprint (SHA-256):** `505ba814b93533679516b4f4239f5eee0dbac125d7ea16746c6cdbb7a68f803d`
