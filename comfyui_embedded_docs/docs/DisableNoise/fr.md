> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/fr.md)

Le nœud DisableNoise fournit une configuration de bruit vide qui peut être utilisée pour désactiver la génération de bruit dans les processus d'échantillonnage. Il retourne un objet de bruit spécial qui ne contient aucune donnée de bruit, permettant à d'autres nœuds de sauter les opérations liées au bruit lorsqu'ils sont connectés à cette sortie.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| *Aucun paramètre d'entrée* | - | - | - | Ce nœud ne nécessite aucun paramètre d'entrée. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `NOISE` | NOISE | Retourne une configuration de bruit vide qui peut être utilisée pour désactiver la génération de bruit dans les processus d'échantillonnage. |