# SamplerDPMAdaptative

Il nodo SamplerDPMAdaptative implementa un campionatore DPM adattivo (modello probabilistico di diffusione) che regola automaticamente le dimensioni dei passi durante il processo di campionamento. Utilizza un controllo dell'errore basato sulla tolleranza per determinare le dimensioni ottimali dei passi, bilanciando l'efficienza computazionale con l'accuratezza del campionamento. Questo approccio adattivo aiuta a mantenere la qualità riducendo potenzialmente il numero di passi necessari.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `order` | L'ordine del metodo di campionamento (predefinito: 3) | INT | Sì | 2-3 |
| `rtol` | Tolleranza relativa per il controllo dell'errore (predefinito: 0.05) | FLOAT | Sì | 0.0-100.0 |
| `atol` | Tolleranza assoluta per il controllo dell'errore (predefinito: 0.0078) | FLOAT | Sì | 0.0-100.0 |
| `h_init` | Dimensione iniziale del passo (predefinito: 0.05) | FLOAT | Sì | 0.0-100.0 |
| `pcoeff` | Coefficiente proporzionale per il controllo della dimensione del passo (predefinito: 0.0) | FLOAT | Sì | 0.0-100.0 |
| `icoeff` | Coefficiente integrale per il controllo della dimensione del passo (predefinito: 1.0) | FLOAT | Sì | 0.0-100.0 |
| `dcoeff` | Coefficiente derivativo per il controllo della dimensione del passo (predefinito: 0.0) | FLOAT | Sì | 0.0-100.0 |
| `accept_safety` | Fattore di sicurezza per l'accettazione del passo (predefinito: 0.81) | FLOAT | Sì | 0.0-100.0 |
| `eta` | Parametro di stocasticità (predefinito: 0.0) | FLOAT | Sì | 0.0-100.0 |
| `s_noise` | Fattore di scala del rumore (predefinito: 1.0) | FLOAT | Sì | 0.0-100.0 |

Tutti gli input sono parametri avanzati usati per mettere a punto il comportamento di campionamento adattivo. Tutti gli input numerici consentono valori decimali e accettano un minimo di 0.0 e un massimo di 100.0, fatta eccezione per `order`, che è limitato ai valori interi 2 o 3.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sampler` | Restituisce un'istanza configurata di campionatore DPM adattivo | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/it.md)

---
**Source fingerprint (SHA-256):** `07b2e5b9f21ec101eabccc6be245d043e64a996a14db10434b03eaae0a91b1d8`
