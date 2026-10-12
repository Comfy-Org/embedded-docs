# FreeU_V2

FreeU_V2 migliora la qualità della generazione di immagini applicando modifiche basate sulla frequenza all'architettura U-Net di un modello di diffusione. Utilizza fattori di scala configurabili per regolare i canali delle feature in blocchi diversi, migliorando l'output senza richiedere addestramento aggiuntivo. Il nodo funziona applicando patch ai blocchi di output del modello e filtrando le componenti ad alta frequenza degli stati nascosti.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione a cui applicare il miglioramento FreeU | MODEL | Sì | - |
| `b1` | Fattore di scala delle feature del backbone per il primo blocco (predefinito: 1.3) | FLOAT | Sì | 0.0 - 10.0 |
| `b2` | Fattore di scala delle feature del backbone per il secondo blocco (predefinito: 1.4) | FLOAT | Sì | 0.0 - 10.0 |
| `s1` | Fattore di scala delle feature di skip per il primo blocco (predefinito: 0.9) | FLOAT | Sì | 0.0 - 10.0 |
| `s2` | Fattore di scala delle feature di skip per il secondo blocco (predefinito: 0.2) | FLOAT | Sì | 0.0 - 10.0 |

Nota: `b1`, `b2`, `s1` e `s2` sono parametri avanzati nascosti per impostazione predefinita nell'interfaccia utente del nodo. Possono essere impostati con incrementi di 0,01 all'interno dell'intervallo 0.0 - 10.0. `b1` e `s1` controllano il blocco U-Net con il maggior numero di canali (quattro volte il numero di canali di base del modello), mentre `b2` e `s2` controllano il blocco con la metà dei canali (due volte il numero di canali di base).

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello di diffusione migliorato con le modifiche FreeU applicate | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/it.md)

---
**Source fingerprint (SHA-256):** `4cef2af9b04164a8ead25bea9c9bb3311be9224f2539a5cc6edbe97ad8465d65`
