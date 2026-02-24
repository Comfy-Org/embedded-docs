> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/fr.md)

## Entrées

| Paramètre | Type de données | Obligatoire | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | STRING | Oui | Tous les fichiers du dossier `checkpoints`.<br>*Exemple : `"audio_vae.safetensors"`* | Point de contrôle de l'autoencodeur variationnel audio à charger. Il s'agit d'une liste déroulante contenant tous les fichiers présents dans votre répertoire `checkpoints` de ComfyUI. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `Audio VAE` | VAE | Le modèle d'autoencodeur variationnel audio chargé, prêt à être connecté à d'autres nœuds de traitement audio. |
