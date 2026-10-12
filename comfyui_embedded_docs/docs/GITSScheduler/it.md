# GITSScheduler

Il nodo GITSScheduler genera i sigma della pianificazione del rumore per il metodo di campionamento GITS (Generative Iterative Time Steps). Calcola i valori sigma in base a un parametro coefficiente e al numero di passaggi, con un fattore di denoising che può ridurre il numero totale di passaggi utilizzati. Il nodo utilizza livelli di rumore predefiniti e interpolazione per creare la pianificazione sigma finale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `coeff` | Parametro avanzato. Il valore del coefficiente che controlla la curva della pianificazione del rumore (predefinito: 1.20). Il valore viene arrotondato a due decimali e seleziona quale tabella di livelli di rumore predefinita viene utilizzata. | FLOAT | Sì | 0.80 - 1.50 (passo 0.05) |
| `steps` | Il numero totale di passaggi di campionamento per cui generare i sigma (predefinito: 10). | INT | Sì | 2 - 1000 |
| `denoise` | Fattore di denoising che riduce il numero di passaggi utilizzati (predefinito: 1.0). | FLOAT | Sì | 0.0 - 1.0 (passo 0.01) |

**Nota:** Quando `denoise` è 0.0 o inferiore, il nodo restituisce un tensore vuoto. Quando `denoise` è inferiore a 1.0, il numero effettivo di passaggi utilizzati viene calcolato come `round(steps * denoise)` e viene mantenuta solo l'ultima parte corrispondente della pianificazione. Per passaggi compresi tra 2 e 20, il nodo seleziona una pianificazione del rumore predefinita corrispondente. Per passaggi maggiori di 20, il nodo utilizza l'interpolazione log-lineare per estendere i livelli di rumore predefiniti al numero di passaggi desiderato.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `sigmas` | I valori sigma generati per la pianificazione del rumore. Per N passaggi di campionamento, vengono restituiti N+1 valori sigma e l'ultimo sigma è impostato a 0. | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/it.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
