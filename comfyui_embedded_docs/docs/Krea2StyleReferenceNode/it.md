# Krea2StyleReferenceNode

Il nodo Krea 2 Style Reference consente di aggiungere un'immagine di riferimento per influenzare lo stile di una generazione di immagini Krea 2. È possibile concatenare più riferimenti di stile insieme (fino a 10 in totale) e collegare il risultato combinato a un nodo Krea 2 Image. Ogni immagine fornita viene caricata nello storage ComfyAPI e passata come URL.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | Immagine di riferimento il cui stile influenza la generazione. | IMAGE | Sì | - |
| `strength` | Forza del riferimento; i valori negativi invertono l'influenza dello stile (predefinito: 1.0). | FLOAT | Sì | da -2.0 a 2.0 (passo: 0.05) |
| `style_reference` | Catena di riferimenti di stile in ingresso opzionale; questo nodo ne aggiunge uno ulteriore. | STYLE_REF | No | - |

**Nota sui vincoli:** È possibile concatenare un massimo di 10 riferimenti di stile in totale. Se si tenta di aggiungere un undicesimo riferimento, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `style_reference` | Un elenco di voci di riferimento di stile, ognuna contenente un URL e un valore di forza. Collega questo output a un nodo Krea 2 Image. | STYLE_REF |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2StyleReferenceNode/it.md)

---
**Source fingerprint (SHA-256):** `a7e52408245b6a3caaca558c8d4d07d090686f32f5d5c7df77ab07311c9c1c6e`
