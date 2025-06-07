
Le nœud LatentAdd est conçu pour l'addition de deux représentations latentes. Il facilite la combinaison des caractéristiques ou des traits encodés dans ces représentations en effectuant une addition élément par élément.

## Entrées

| Paramètre    | Data Type | Description |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | Le premier ensemble d'échantillons latents à ajouter. Il représente l'une des entrées dont les caractéristiques doivent être combinées avec un autre ensemble d'échantillons latents. |
| `samples2`   | `LATENT`    | Le second ensemble d'échantillons latents à ajouter. Il sert d'autre entrée dont les caractéristiques sont combinées avec le premier ensemble d'échantillons latents par addition élément par élément. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Le résultat de l'addition élément par élément de deux échantillons latents, représentant un nouvel ensemble d'échantillons latents qui combine les caractéristiques des deux entrées. |
