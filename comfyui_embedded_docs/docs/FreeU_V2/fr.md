> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/fr.md)

Le nœud FreeU_V2 applique une amélioration basée sur les fréquences aux modèles de diffusion en modifiant l'architecture U-Net. Il met à l'échelle différents canaux de caractéristiques en utilisant des paramètres configurables pour améliorer la qualité de génération d'images sans nécessiter d'entraînement supplémentaire. Le nœud fonctionne en modifiant les blocs de sortie du modèle pour appliquer des facteurs d'échelle à des dimensions de canaux spécifiques.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle de diffusion auquel appliquer l'amélioration FreeU |
| `b1` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle des caractéristiques de base pour le premier bloc (par défaut : 1.3) |
| `b2` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle des caractéristiques de base pour le deuxième bloc (par défaut : 1.4) |
| `s1` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle des caractéristiques de saut pour le premier bloc (par défaut : 0.9) |
| `s2` | FLOAT | Oui | 0.0 - 10.0 | Facteur d'échelle des caractéristiques de saut pour le deuxième bloc (par défaut : 0.2) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `modèle` | MODEL | Le modèle de diffusion amélioré avec les modifications FreeU appliquées |
