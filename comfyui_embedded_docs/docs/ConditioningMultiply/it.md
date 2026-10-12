# ConditioningMultiply

Questo nodo moltiplica i valori di condizionamento per un fattore specificato, consentendo di scalare l'influenza del condizionamento sul processo di generazione. Funziona applicando il moltiplicatore sia al tensore di condizionamento principale che ai valori di output aggregati.

## Input

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `conditioning` | I dati di condizionamento da scalare | CONDITIONING | Sì | - |
| `multiplier` | Il fattore per cui moltiplicare i valori di condizionamento (predefinito: 1.0) | FLOAT | Sì | -100.0 a 100.0 (passo: 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `CONDITIONING` | I dati di condizionamento scalati con valori moltiplicati | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/it.md)

---
**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`
