> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode/fr.md)

Génère des images de manière synchrone en fonction de l'invite et du rapport d'aspect. Ce nœud crée des images à l'aide de descriptions textuelles et vous permet de contrôler les dimensions et le style de l'image grâce à diverses entrées de référence.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite pour la génération d'image (par défaut : chaîne vide) |
| `model` | COMBO | Oui | Plusieurs options disponibles | Sélection du modèle pour la génération d'image |
| `aspect_ratio` | COMBO | Oui | Plusieurs options disponibles | Rapport d'aspect pour l'image générée (par défaut : ratio 16:9) |
| `seed` | INT | Oui | 0 à 18446744073709551615 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) |
| `style_image_weight` | FLOAT | Non | 0.0 à 1.0 | Poids de l'image de style. Ignoré si aucune `style_image` n'est fournie (par défaut : 1.0) |
| `image_luma_ref` | LUMA_REF | Non | - | Connexion au nœud de référence Luma pour influencer la génération avec des images d'entrée ; jusqu'à 4 images peuvent être prises en compte |
| `style_image` | IMAGE | Non | - | Image de référence de style ; seule 1 image sera utilisée |
| `character_image` | IMAGE | Non | - | Images de référence de personnage ; peut être un lot de plusieurs images, jusqu'à 4 images peuvent être prises en compte |

**Contraintes des paramètres :**
- Le paramètre `image_luma_ref` peut accepter jusqu'à 4 images de référence
- Le paramètre `character_image` peut accepter jusqu'à 4 images de référence de personnage
- Le paramètre `style_image` n'accepte qu'une seule image de référence de style
- Le paramètre `style_image_weight` n'est utilisé que lorsque `style_image` est fournie

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | IMAGE | L'image générée basée sur les paramètres d'entrée |