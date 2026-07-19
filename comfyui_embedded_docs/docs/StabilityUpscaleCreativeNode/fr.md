# Stability AI Upscale Creative

Voici la traduction en français de la documentation technique du nœud ComfyUI, en respectant les règles établies :

Ce nœud agrandit l'image avec un minimum de modifications jusqu'à une résolution 4K. Il utilise la technologie de mise à l'échelle créative de Stability AI pour améliorer la résolution de l'image tout en préservant le contenu original et en ajoutant des détails créatifs subtils.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à agrandir | IMAGE | Oui | - |
| `prompt` | Ce que vous souhaitez voir dans l'image de sortie. Un prompt fort et descriptif définissant clairement les éléments, couleurs et sujets donnera de meilleurs résultats. (par défaut : chaîne vide) | STRING | Oui | - |
| `créativité` | Contrôle la probabilité de créer des détails supplémentaires non fortement conditionnés par l'image initiale. (par défaut : 0.3) | FLOAT | Oui | 0.1-0.5 |
| `style_prédéfini` | Style souhaité pour l'image générée (optionnel). (par défaut : "None") | STRING | Oui | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` |
| `graine` | La graine aléatoire utilisée pour créer le bruit. (par défaut : 0) | INT | Oui | 0-4294967294 |
| `prompt_négatif` | Mots-clés de ce que vous ne souhaitez pas voir dans l'image de sortie. Il s'agit d'une fonctionnalité avancée. (par défaut : chaîne vide) | STRING | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image agrandie en résolution 4K | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/fr.md)

---
**Source fingerprint (SHA-256):** `46f7bdd3cb4254b6305407f43e4a9a69a54fd3a0ac285d784c899dbf52edd552`
