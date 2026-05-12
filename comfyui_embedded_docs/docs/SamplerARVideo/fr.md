> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/fr.md)

# Sampler AR Video

Le nœud Sampler AR Video fournit une méthode d'échantillonnage spécialisée pour les modèles vidéo autorégressifs, tels que ceux utilisant les techniques de Forçage Causal ou d'Auto-Forçage. Il gère tous les paramètres liés à la boucle autorégressive (AR) directement dans le workflow, facilitant la configuration de la façon dont le modèle génère les images vidéo une par une.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `num_frame_per_block` | INT | Oui | 1 à 64 | Images par bloc autorégressif. Une valeur de 1 signifie que le modèle génère une image à la fois (image par image), tandis qu'une valeur de 3 signifie qu'il génère trois images ensemble (par blocs). Ce paramètre doit correspondre au mode d'entraînement du checkpoint. Valeur par défaut : 1. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `SAMPLER` | SAMPLER | Un objet échantillonneur configuré qui utilise la fonction d'échantillonnage "ar_video" avec les paramètres autorégressifs spécifiés. |