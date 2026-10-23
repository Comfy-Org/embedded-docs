# ClipLoader

Il nodo CLIPLoader carica un modello di codifica testuale (CLIP, T5 o simile) da un file, rendendolo disponibile per l'uso in altri nodi che necessitano di convertire prompt testuali in rappresentazioni numeriche. Supporta una vasta gamma di architetture di modelli, ognuna delle quali richiede un tipo specifico di encoder.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip_name` | Il nome del file del modello di codifica testuale da caricare. Deve essere un file situato nella directory `ComfyUI/models/text_encoders/`. | STRING | Sì | Elenco dei file trovati nella cartella `text_encoders` |
| `type` | Il tipo di architettura del modello da caricare. Determina quale variante specifica di encoder utilizzare (predefinito: `"stable_diffusion"`). | COMBO | Sì | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"`<br>`"yue2"`<br>`"flux3"`<br>`"moss_image"`<br>`"fibo2"` |
| `device` | Il dispositivo su cui caricare il modello. `"default"` utilizza la GPU se disponibile, mentre `"cpu"` forza il caricamento sulla CPU. Questa è un'opzione avanzata (predefinito: `"default"`). | COMBO | No | `"default"`<br>`"cpu"` |

### Mappature supportate tra Tipo ed Encoder

Il parametro `type` seleziona l'encoder corretto per una data architettura di modello. Di seguito sono riportate le mappature comuni:

| Tipo | Encoder |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (226-token padding) |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (recommended) or t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL or Music3 Qwen/RVQ |
| flux3 | qwen3-vl 4B |
| fibo2 | qwen3-vl 4B |

## Output

| Nome dell'output | Descrizione | Tipo di dati |
|------------------|-------------|--------------|
| `CLIP` | Il modello di codifica testuale caricato, pronto per essere collegato ad altri nodi per la codifica del testo e il condizionamento. | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/it.md)

---
**Source fingerprint (SHA-256):** `75cf64ce955946681dee79035fc91b54be0a99e3fc22b8c4737929ce0bdff13e`
