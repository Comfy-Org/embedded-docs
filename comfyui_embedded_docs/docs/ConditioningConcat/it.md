# Conditioning (Concatena)

Il nodo ConditioningConcat è progettato per concatenare vettori di condizionamento, fondendo nello specifico il vettore 'conditioning_from' nel vettore 'conditioning_to'. Questa operazione è fondamentale negli scenari in cui le informazioni di condizionamento provenienti da due origini devono essere combinate in un'unica rappresentazione unificata.

## Input

| Parametro | Descrizione | Tipo Comfy |
| --- | --- | --- |
| `conditioning_to` | Rappresenta l'insieme primario di vettori di condizionamento a cui verranno concatenati i vettori 'conditioning_from'. Funge da base per il processo di concatenazione. | `CONDITIONING` |
| `conditioning_from` | È costituito dai vettori di condizionamento che devono essere concatenati ai vettori 'conditioning_to'. Questo parametro consente di integrare ulteriori informazioni di condizionamento nell'insieme esistente. | `CONDITIONING` |

## Output

| Parametro | Descrizione | Tipo Comfy |
| --- | --- | --- |
| `conditioning` | L'output è un insieme unificato di vettori di condizionamento, risultante dalla concatenazione dei vettori 'conditioning_from' nei vettori 'conditioning_to'. | `CONDITIONING` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/it.md)
