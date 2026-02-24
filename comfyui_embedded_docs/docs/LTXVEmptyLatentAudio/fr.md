> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/fr.md)

## Vue d'ensemble

Le nœud LTXV Empty Latent Audio crée un lot de tenseurs latents audio vides (remplis de zéros). Il utilise la configuration d'un modèle VAE Audio fourni pour déterminer les dimensions correctes de l'espace latent, telles que le nombre de canaux et de bandes de fréquence. Ce latent vide sert de point de départ pour les flux de travail de génération ou de manipulation audio dans ComfyUI.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `frames_number` | INT | Oui | 1 à 1000 | Nombre de trames. La valeur par défaut est 97. |
| `frame_rate` | INT | Oui | 1 à 1000 | Nombre de trames par seconde. La valeur par défaut est 25. |
| `batch_size` | INT | Oui | 1 à 4096 | Le nombre d'échantillons audio latents dans le lot. La valeur par défaut est 1. |
| `audio_vae` | VAE | Oui | N/A | Le modèle VAE Audio à partir duquel obtenir la configuration. Ce paramètre est requis. |

**Note :** L'entrée `audio_vae` est obligatoire. Le nœud générera une erreur si elle n'est pas fournie.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `Latent` | LATENT | Un tenseur latent audio vide avec la structure (échantillons, fréquence d'échantillonnage, type) configurée pour correspondre au VAE Audio d'entrée. |
