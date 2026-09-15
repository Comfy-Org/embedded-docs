# DésactiverBruit

Ce nœud fournit une configuration de bruit vide qui désactive la génération de bruit pendant l'échantillonnage. Il produit un objet de bruit spécial ne contenant aucune donnée de bruit, de sorte que tout nœud qui y est connecté ignore les opérations liées au bruit. Il peut également être recherché sous l'alias « zero noise ».

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| *Aucun paramètre d'entrée* | Ce nœud ne nécessite aucun paramètre d'entrée. | - | - | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `NOISE` | Renvoie une configuration de bruit vide pouvant être utilisée pour désactiver la génération de bruit dans les processus d'échantillonnage. | NOISE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/fr.md)

---
**Source fingerprint (SHA-256):** `b9edcda655dab3196233b6c66fdb41eb0585b153616b793016d532992b922934`
