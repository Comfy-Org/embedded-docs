> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/fr.md)

Le nœud EmptyLatentHunyuan3Dv2 crée des tenseurs latents vides spécifiquement formatés pour les modèles de génération 3D Hunyuan3Dv2. Il génère des espaces latents vides avec les dimensions et la structure correctes requises par l'architecture Hunyuan3Dv2, vous permettant de démarrer des flux de travail de génération 3D à partir de zéro. Le nœud produit des tenseurs latents remplis de zéros qui servent de fondation pour les processus de génération 3D ultérieurs.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `resolution` | INT | Oui | 1 - 8192 | La dimension de résolution pour l'espace latent (par défaut : 3072) |
| `batch_size` | INT | Oui | 1 - 4096 | Le nombre d'images latentes dans le lot (par défaut : 1) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Retourne un tenseur latent contenant des échantillons vides formatés pour la génération 3D Hunyuan3Dv2 |