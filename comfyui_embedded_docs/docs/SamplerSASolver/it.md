# SamplerSASolver

Il nodo SamplerSASolver crea e configura un sampler personalizzato per i modelli di diffusione. Utilizza l'algoritmo di campionamento "sa_solver" con uno schema predittore-correttore configurabile e impostazioni di equazioni differenziali stocastiche (SDE), restituendo un oggetto sampler che può essere collegato a un nodo di campionamento. I valori `sde_start_percent` e `sde_end_percent` vengono convertiti in valori sigma usando la schedulazione di campionamento del modello collegato per definire l'intervallo in cui viene applicata la componente stocastica.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione la cui schedulazione di campionamento viene utilizzata per costruire il sampler | MODEL | Sì | - |
| `eta` | Controlla il fattore di scala della dimensione del passo del solver SDE (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `sde_start_percent` | Percentuale iniziale del processo di campionamento in cui inizia la componente stocastica (SDE); convertita in un valore sigma usando la schedulazione del modello (predefinito: 0.2) | FLOAT | No | 0.0 - 1.0 |
| `sde_end_percent` | Percentuale finale del processo di campionamento in cui termina la componente stocastica (SDE); convertita in un valore sigma usando la schedulazione del modello (predefinito: 0.8) | FLOAT | No | 0.0 - 1.0 |
| `s_noise` | Controlla la quantità di rumore aggiunto durante il campionamento (predefinito: 1.0) | FLOAT | No | 0.0 - 100.0 |
| `predictor_order` | L'ordine della componente predittore nel solver (predefinito: 3) | INT | No | 1 - 6 |
| `corrector_order` | L'ordine della componente correttore nel solver (predefinito: 4) | INT | No | 0 - 6 |
| `use_pece` | Abilita il metodo PECE (Predict-Evaluate-Correct-Evaluate) (predefinito: disabilitato) | BOOLEAN | No | - |
| `simple_order_2` | Abilita calcoli semplificati del secondo ordine (predefinito: disabilitato) | BOOLEAN | No | - |

Tutti gli input opzionali sono contrassegnati come avanzati nell'interfaccia.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `sampler` | Un oggetto sampler configurato (che utilizza l'algoritmo `sa_solver`) che può essere usato dai nodi di campionamento | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/it.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
