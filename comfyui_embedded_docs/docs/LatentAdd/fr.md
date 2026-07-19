# LatentAdd

Le nœud LatentAdd est conçu pour l'addition de deux représentations latentes. Il facilite la combinaison des caractéristiques ou propriétés encodées dans ces représentations en effectuant une addition élément par élément.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `samples1` | Le premier ensemble d'échantillons latents à additionner. Il représente l'une des entrées dont les caractéristiques doivent être combinées avec un autre ensemble d'échantillons latents. | `LATENT` |
| `samples2` | Le second ensemble d'échantillons latents à additionner. Il sert d'autre entrée dont les caractéristiques sont combinées avec le premier ensemble d'échantillons latents par addition élément par élément. | `LATENT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | Le résultat de l'addition élément par élément de deux échantillons latents, représentant un nouvel ensemble d'échantillons latents qui combine les caractéristiques des deux entrées. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentAdd/fr.md)
