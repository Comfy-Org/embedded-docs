# TextEncodeQwenImageEditPlus

Voici la traduction en français de la documentation du nœud ComfyUI `TextEncodeQwenImageEditPlus` :

Le nœud TextEncodeQwenImageEditPlus traite des instructions textuelles et des images optionnelles pour générer des données de conditionnement destinées à des tâches de génération ou d'édition d'images. Il utilise un modèle spécialisé pour analyser les images d'entrée et comprendre comment les instructions textuelles doivent les modifier, puis encode ces informations pour les utiliser dans les étapes de génération ultérieures. Le nœud peut gérer jusqu'à trois images d'entrée et, éventuellement, générer des latents de référence lorsqu'un VAE est fourni.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour la tokenisation et l'encodage | CLIP | Oui | - |
| `invite` | Instruction textuelle décrivant la modification d'image souhaitée (prend en charge les entrées multilignes et les instructions dynamiques) | STRING | Oui | - |
| `vae` | Modèle VAE optionnel pour générer des latents de référence à partir des images d'entrée | VAE | Non | - |
| `image1` | Première image d'entrée optionnelle pour l'analyse et la modification | IMAGE | Non | - |
| `image2` | Deuxième image d'entrée optionnelle pour l'analyse et la modification | IMAGE | Non | - |
| `image3` | Troisième image d'entrée optionnelle pour l'analyse et la modification | IMAGE | Non | - |

**Remarque :** Lorsqu'un VAE est fourni, le nœud génère des latents de référence à partir de toutes les images d'entrée. Le nœud peut traiter jusqu'à trois images simultanément. Les images sont automatiquement redimensionnées à 384x384 pixels pour le traitement vision-langage, et à des dimensions divisibles par 8 (avec une zone cible de 1024x1024 pixels) pour l'encodage VAE.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Données de conditionnement encodées contenant les tokens textuels et les latents de référence optionnels pour la génération d'images | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/fr.md)

---
**Source fingerprint (SHA-256):** `54889d9a3b70e41d623020f3fd5e3c798c72799492c67a9efd99f543c88bb968`
