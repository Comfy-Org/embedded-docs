# Mélange Latent

Le nœud LatentBlend combine deux échantillons latents en les fusionnant à l'aide d'un facteur de mélange spécifié. Il prend deux entrées latentes et crée une nouvelle sortie où le premier échantillon est pondéré par le facteur de mélange et le second par son inverse. Si les échantillons d'entrée ont des formes différentes, le second échantillon est automatiquement redimensionné pour correspondre aux dimensions du premier.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `échantillons1` | Premier échantillon latent à fusionner | LATENT | Oui | - |
| `échantillons2` | Second échantillon latent à fusionner | LATENT | Oui | - |
| `facteur_de_mélange` | Contrôle le ratio de mélange entre les deux échantillons (par défaut : 0,5) | FLOAT | Oui | 0 à 1 |

**Remarque :** Si `samples1` et `samples2` ont des formes différentes, `samples2` sera automatiquement redimensionné pour correspondre aux dimensions de `samples1` en utilisant une interpolation bicubique avec recadrage centré.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latent` | L'échantillon latent fusionné combinant les deux échantillons d'entrée | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/fr.md)

---
**Source fingerprint (SHA-256):** `a19808c5b606a8c05f2685fcd78d9f08c1ba51613a4029b36cf0ce5305618c2f`
