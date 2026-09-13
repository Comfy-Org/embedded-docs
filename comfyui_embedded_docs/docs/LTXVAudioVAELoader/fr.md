# Chargeur Audio VAE LTXV

Le nœud LTXV Audio VAE Loader charge un modèle Audio Variational Autoencoder (VAE) pré-entraîné à partir d'un fichier de checkpoint. Il lit le checkpoint spécifié, conserve les poids de l'audio VAE et du vocodeur, puis prépare le modèle pour une utilisation dans les workflows de génération ou de traitement audio au sein de ComfyUI.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `ckpt_name` | Checkpoint Audio VAE à charger. Il s'agit d'une liste déroulante remplie avec tous les fichiers trouvés dans votre répertoire `checkpoints` de ComfyUI. | COMBO | Oui | Tous les fichiers du dossier `checkpoints`. La liste est générée à l'exécution. |

Le fichier sélectionné doit être un checkpoint LTXV audio VAE valide. Le nœud conserve uniquement les poids de l'audio VAE et du vocodeur à partir du fichier, et déclenche une erreur si le modèle chargé n'est pas un VAE valide.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `Audio VAE` | Le modèle Audio Variational Autoencoder chargé, prêt à être connecté à d'autres nœuds de traitement audio. | VAE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/fr.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
