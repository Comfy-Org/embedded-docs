> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/fr.md)

Le nœud TextEncodeQwenImageEditPlus traite des invites textuelles et des images optionnelles pour générer des données de conditionnement destinées à des tâches de génération ou de modification d'image. Il utilise un modèle spécialisé pour analyser les images d'entrée et comprendre comment les instructions textuelles doivent les modifier, puis encode ces informations pour une utilisation dans les étapes de génération ultérieures. Le nœud peut gérer jusqu'à trois images d'entrée et générer optionnellement des latents de référence lorsqu'un VAE est fourni.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Oui | - | Le modèle CLIP utilisé pour la tokenisation et l'encodage |
| `prompt` | STRING | Oui | - | Instruction textuelle décrivant la modification d'image souhaitée (prend en charge la saisie multiligne et les invites dynamiques) |
| `vae` | VAE | Non | - | Modèle VAE optionnel pour générer des latents de référence à partir des images d'entrée |
| `image1` | IMAGE | Non | - | Première image d'entrée optionnelle pour l'analyse et la modification |
| `image2` | IMAGE | Non | - | Deuxième image d'entrée optionnelle pour l'analyse et la modification |
| `image3` | IMAGE | Non | - | Troisième image d'entrée optionnelle pour l'analyse et la modification |

**Note :** Lorsqu'un VAE est fourni, le nœud génère des latents de référence à partir de toutes les images d'entrée. Le nœud peut traiter jusqu'à trois images simultanément, et les images sont automatiquement redimensionnées aux dimensions appropriées pour le traitement.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Données de conditionnement encodées contenant les tokens textuels et les latents de référence optionnels pour la génération d'image |
