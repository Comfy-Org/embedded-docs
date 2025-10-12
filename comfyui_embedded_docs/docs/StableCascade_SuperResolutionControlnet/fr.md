> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/fr.md)

Le nœud StableCascade_SuperResolutionControlnet prépare les entrées pour le traitement de super-résolution Stable Cascade. Il prend une image d'entrée et l'encode à l'aide d'un VAE pour créer une entrée controlnet, tout en générant des représentations latentes de substitution pour les étapes C et B du pipeline Stable Cascade.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à traiter pour la super-résolution |
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder l'image d'entrée |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `controlnet_input` | IMAGE | La représentation encodée de l'image adaptée pour l'entrée controlnet |
| `stage_c` | LATENT | Représentation latente de substitution pour l'étape C du traitement Stable Cascade |
| `stage_b` | LATENT | Représentation latente de substitution pour l'étape B du traitement Stable Cascade |