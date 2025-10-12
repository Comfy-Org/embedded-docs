> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/fr.md)

Le nœud LatentBlend combine deux échantillons latents en les fusionnant à l'aide d'un facteur de mélange spécifié. Il prend deux entrées latentes et crée une nouvelle sortie où le premier échantillon est pondéré par le facteur de mélange et le second échantillon est pondéré par l'inverse. Si les échantillons d'entrée ont des formes différentes, le deuxième échantillon est automatiquement redimensionné pour correspondre aux dimensions du premier échantillon.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `échantillons1` | LATENT | Oui | - | Le premier échantillon latent à mélanger |
| `échantillons2` | LATENT | Oui | - | Le deuxième échantillon latent à mélanger |
| `facteur_de_mélange` | FLOAT | Oui | 0 à 1 | Contrôle le ratio de mélange entre les deux échantillons (par défaut : 0.5) |

**Note :** Si `samples1` et `samples2` ont des formes différentes, `samples2` sera automatiquement redimensionné pour correspondre aux dimensions de `samples1` en utilisant une interpolation bicubique avec rognage central.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `latent` | LATENT | L'échantillon latent mélangé combinant les deux échantillons d'entrée |
