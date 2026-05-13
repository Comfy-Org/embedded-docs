> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/fr.md)

Génère des images de manière synchrone en fonction du prompt et de la résolution. Ce nœud crée des images à l'aide du modèle Stable Image Ultra de Stability AI, en traitant votre prompt textuel et en générant une image correspondante avec le rapport hauteur/largeur et le style spécifiés.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Ce que vous souhaitez voir dans l'image de sortie. Un prompt fort et descriptif qui définit clairement les éléments, les couleurs et les sujets donnera de meilleurs résultats. Pour contrôler le poids d'un mot donné, utilisez le format `(mot:poids)`, où `mot` est le mot dont vous souhaitez contrôler le poids et `poids` est une valeur comprise entre 0 et 1. Par exemple : `The sky was a crisp (blue:0.3) and (green:0.8)` indiquerait un ciel bleu et vert, mais plus vert que bleu. |
| `aspect_ratio` | COMBO | Oui | `"1:1"`<br>`"16:9"`<br>`"21:9"`<br>`"2:3"`<br>`"3:2"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"9:21"` | Rapport hauteur/largeur de l'image générée (par défaut : "1:1"). |
| `style_preset` | COMBO | Non | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` | Style souhaité (optionnel) de l'image générée. Sélectionnez "None" pour n'appliquer aucun style prédéfini. |
| `seed` | INT | Oui | 0 - 4294967294 | La graine aléatoire utilisée pour créer le bruit. |
| `image` | IMAGE | Non | - | Image d'entrée optionnelle pour la génération image-à-image. |
| `negative_prompt` | STRING | Non | - | Un court texte décrivant ce que vous ne souhaitez pas voir dans l'image de sortie. Il s'agit d'une fonctionnalité avancée. |
| `image_denoise` | FLOAT | Non | 0.0 - 1.0 | Dénoyaute de l'image d'entrée ; 0.0 produit une image identique à l'entrée, 1.0 équivaut à l'absence d'image fournie (par défaut : 0.5). |

**Remarque :** Lorsqu'aucune image d'entrée n'est fournie, le paramètre `image_denoise` est automatiquement désactivé et ignoré.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | IMAGE | L'image générée en fonction des paramètres d'entrée. |

---
**Source fingerprint (SHA-256):** `2fd9e106a3460a39c33ecc9a15ab6414dab1914fdc43e4f546827e02c889cf62`
