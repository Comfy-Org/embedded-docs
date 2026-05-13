> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentAdd/fr.md)

Le nœud LatentAdd est conçu pour l'addition de deux représentations latentes. Il facilite la combinaison des caractéristiques ou propriétés encodées dans ces représentations en effectuant une addition élément par élément.

## Entrées

| Paramètre   | Type de données | Description |
|-------------|-----------------|-------------|
| `samples1`  | `LATENT`        | Le premier ensemble d'échantillons latents à additionner. Il représente l'une des entrées dont les caractéristiques doivent être combinées avec un autre ensemble d'échantillons latents. |
| `samples2`  | `LATENT`        | Le second ensemble d'échantillons latents à additionner. Il sert d'autre entrée dont les caractéristiques sont combinées avec le premier ensemble d'échantillons latents par addition élément par élément. |

## Sorties

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `latent`  | `LATENT`        | Le résultat de l'addition élément par élément de deux échantillons latents, représentant un nouvel ensemble d'échantillons latents qui combine les caractéristiques des deux entrées. |