# TextEncodeQwenImageEditPlus

Le nœud TextEncodeQwenImageEditPlus traite une invite textuelle et jusqu’à trois images facultatives pour produire des données de conditionnement destinées à des tâches de génération ou d’édition d’images. Il utilise un gabarit spécialisé qui demande d’abord au modèle de décrire les caractéristiques principales des images d’entrée, puis d’expliquer comment l’instruction textuelle de l’utilisateur doit les modifier, afin que le résultat encodé comprenne à la fois les images et la modification demandée. Lorsqu’un VAE est fourni, le nœud crée également des latents de référence à partir des images d’entrée.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `clip` | Le modèle CLIP utilisé pour la tokenisation et l’encodage | CLIP | Oui | - |
| `invite` | Instruction textuelle décrivant la modification d’image souhaitée (prend en charge les entrées multilignes et les prompts dynamiques) | STRING | Oui | - |
| `vae` | Modèle VAE facultatif pour générer des latents de référence à partir des images d’entrée | VAE | Non | - |
| `image1` | Première image d’entrée facultative pour l’analyse et la modification | IMAGE | Non | - |
| `image2` | Deuxième image d’entrée facultative pour l’analyse et la modification | IMAGE | Non | - |
| `image3` | Troisième image d’entrée facultative pour l’analyse et la modification | IMAGE | Non | - |

**Remarque :** Lorsqu’un VAE est fourni, le nœud génère des latents de référence à partir de toutes les images d’entrée fournies. Jusqu’à trois images peuvent être traitées simultanément. Les images sont redimensionnées à une zone cible de 384x384 pixels (proportions conservées) pour le traitement vision-langage, et à des dimensions divisibles par 8 (avec une zone cible de 1024x1024 pixels) pour l’encodage VAE.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Données de conditionnement encodées contenant les tokens de texte et, éventuellement, des latents de référence pour la génération d’images | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/fr.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
