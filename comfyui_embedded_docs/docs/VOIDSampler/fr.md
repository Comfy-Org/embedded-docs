> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/fr.md)

Voici la traduction en français de la documentation du nœud VOIDSampler :

## Aperçu

Le nœud VOIDSampler fournit une méthode d'échantillonnage DDIM spécialisée, conçue spécifiquement pour les modèles d'inpainting VOID. Il implémente le même processus de débruitage que celui utilisé lors de l'entraînement des modèles VOID, sans la mise à l'échelle du bruit appliquée par les KSamplers standard. Ce nœud est destiné à être utilisé avec les nœuds SamplerCustom ou SamplerCustomAdvanced, et doit être associé à RandomNoise ou VOIDWarpedNoiseSource.

## Entrées

Ce nœud ne possède aucun paramètre d'entrée configurable. Il s'agit d'un échantillonneur autonome qui applique un algorithme d'échantillonnage DDIM fixe.

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| *Aucune entrée* | - | - | - | Ce nœud n'accepte aucun paramètre d'entrée. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `SAMPLER` | SAMPLER | Un objet échantillonneur implémentant l'algorithme DDIM VOID, prêt à être connecté aux nœuds SamplerCustom ou SamplerCustomAdvanced. |