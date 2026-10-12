# Dual CFG Guider

Il nodo Dual CFG Guider crea un sistema di guida per il campionamento che utilizza due input di condizionamento insieme a un input di condizionamento negativo. Applica due scale di guida separate per controllare quanto fortemente ciascun condizionamento influenza il risultato generato e supporta due modi di combinare tali scale: "regular" e "nested".

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello da usare per la guida | MODEL | Sì | - |
| `cond1` | Il primo input di condizionamento positivo | CONDITIONING | Sì | - |
| `cond2` | Il secondo input di condizionamento, usato come riferimento tra il primo condizionamento positivo e il condizionamento negativo | CONDITIONING | Sì | - |
| `negative` | L'input di condizionamento negativo | CONDITIONING | Sì | - |
| `cfg_conds` | Scala di guida applicata al primo condizionamento positivo (predefinito: 8.0) | FLOAT | Sì | 0.0 - 100.0 |
| `cfg_cond2_negative` | Scala di guida applicata tra il secondo condizionamento e il condizionamento negativo (predefinito: 8.0) | FLOAT | Sì | 0.0 - 100.0 |
| `style` | Lo stile di guida da applicare (predefinito: "regular"). Quando è impostato su "nested", la guida viene applicata in modo annidato | COMBO | Sì | "regular"<br>"nested" |

Nota: Nello stile `regular`, `cfg_cond2_negative` viene applicato tra `cond2` e `negative`, mentre `cfg_conds` viene applicato tra `cond1` e `cond2`. Nello stile `nested`, `cfg_conds` viene applicato prima tra `cond1` e `cond2`, quindi la previsione risultante viene guidata lontano da `negative` usando `cfg_cond2_negative`.

Nota: Nello stile `regular`, quando `cfg_cond2_negative` è uguale a 1.0, il condizionamento negativo viene saltato, e quando anche `cfg_conds` è uguale a 1.0, viene saltato anche il secondo condizionamento. Questo riduce il numero di valutazioni del modello eseguite.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `GUIDER` | Un sistema di guida configurato, pronto per l'uso con il campionamento | GUIDER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/it.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
