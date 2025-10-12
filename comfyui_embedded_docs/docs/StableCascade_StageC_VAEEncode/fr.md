> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/fr.md)

Le nœud StableCascade_StageC_VAEEncode traite les images via un encodeur VAE pour générer des représentations latentes destinées aux modèles Stable Cascade. Il prend une image en entrée et la compresse en utilisant le modèle VAE spécifié, puis produit deux représentations latentes : une pour l'étape C et un espace réservé pour l'étape B. Le paramètre de compression contrôle le niveau de réduction d'échelle appliqué à l'image avant l'encodage.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à encoder dans l'espace latent |
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder l'image |
| `compression` | INT | Non | 4-128 | Le facteur de compression appliqué à l'image avant l'encodage (par défaut : 42) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `stage_b` | LATENT | La représentation latente encodée pour l'étape C du modèle Stable Cascade |
| `stage_b` | LATENT | Une représentation latente réservée pour l'étape B (retourne actuellement des zéros) |
