Voici la traduction en français de la documentation du nœud LatentSubtract :

Le nœud LatentSubtract est conçu pour soustraire une représentation latente d'une autre. Cette opération peut être utilisée pour manipuler ou modifier les caractéristiques des sorties des modèles génératifs en supprimant efficacement les caractéristiques ou attributs représentés dans un espace latent d'un autre.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `samples1` | Le premier ensemble d'échantillons latents à partir duquel la soustraction est effectuée. Il sert de base à l'opération de soustraction. | `LATENT` |
| `samples2` | Le second ensemble d'échantillons latents qui sera soustrait du premier ensemble. Cette opération peut modifier la sortie du modèle génératif résultant en supprimant des attributs ou des caractéristiques. | `LATENT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | Le résultat de la soustraction du second ensemble d'échantillons latents du premier. Cette représentation latente modifiée peut être utilisée pour d'autres tâches génératives. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentSubtract/fr.md)
