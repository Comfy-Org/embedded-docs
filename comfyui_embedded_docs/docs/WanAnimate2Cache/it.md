# WanAnimate2Cache

Memorizza nella cache le attivazioni per blocco del video di posa una sola volta, così non devono essere ricalcolate a ogni passo di campionamento, riducendo all'incirca della metà il tempo di generazione. Il compromesso è un maggiore utilizzo di memoria: circa 12,5 GB di RAM di sistema a risoluzione 480x832 con 81 frame in bf16, con aumento proporzionale alla risoluzione e alla durata del video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello Wan Animate2 a cui collegare la cache. | MODEL | Sì | |
| `device` | Dove conservare la cache. cpu (RAM) è la scelta sicura, la cache non entrerà nella VRAM insieme al modello alle dimensioni tipiche. gpu (VRAM) può essere più veloce se c'è spazio. (predefinito: "cpu") | STRING | Sì | "cpu"<br>"gpu" |
| `dtype` | Precisione di archiviazione. default memorizza le attivazioni nel dtype di calcolo del modello. int8 dimezza la cache, int4 la riduce a un quarto, convrot viene usato per mantenere l'accuratezza. (predefinito: "default") | STRING | Sì | "default"<br>"int8"<br>"int4" |

Nota: quando vengono utilizzate le finestre di contesto, ogni finestra viene memorizzata separatamente nella cache, quindi l'utilizzo di memoria aumenta con il numero di finestre. Dovrebbe essere utilizzata la pianificazione static_standard, perché le pianificazioni uniformi spostano le finestre a ogni passo e la cache non viene mai riutilizzata.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model` | Il modello clonato con la cache delle attivazioni del video di posa collegata. La cache viene liberata automaticamente al termine della generazione. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2Cache/it.md)

---
**Source fingerprint (SHA-256):** `06305432601afd7c797ef29ef4be3f2bb1aa660e05edde270499e94ccdd54f84`
