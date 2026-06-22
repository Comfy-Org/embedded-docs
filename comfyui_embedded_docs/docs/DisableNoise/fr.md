# DésactiverBruit

Le nœud DisableNoise fournit une configuration de bruit vide qui peut être utilisée pour désactiver la génération de bruit dans les processus d'échantillonnage. Il renvoie un objet de bruit spécial ne contenant aucune donnée de bruit, permettant aux autres nœuds d'ignorer les opérations liées au bruit lorsqu'ils sont connectés à cette sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| *Aucun paramètre d'entrée* | Ce nœud ne nécessite aucun paramètre d'entrée. | - | - | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `NOISE` | Renvoie une configuration de bruit vide qui peut être utilisée pour désactiver la génération de bruit dans les processus d'échantillonnage. | NOISE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/fr.md)

---
**Source fingerprint (SHA-256):** `527152dff69bd5c55c622c634b87e625eb16708f8595fa02d69cf38f1125c5eb`
