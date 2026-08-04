# MinimaxHailuo03FirstLastFrameNode

Ce nœud génère une vidéo à partir d'une première image et d'une image finale optionnelle en utilisant le modèle MiniMax H3. La vidéo respecte le format d'image des images fournies et, lorsqu'une image finale est fournie, anime la transition de la première image vers l'image finale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser pour la génération de la vidéo. Ce combo inclut le choix du modèle (« MiniMax H3 »), une invite textuelle décrivant la vidéo à générer, la résolution de sortie et la durée de la vidéo. L'invite doit contenir au moins un caractère non blanc. | COMBO | Oui | « MiniMax H3 » |
| `first_frame` | Première image de la vidéo. Le format de la vidéo générée suit cette image. Doit faire au moins 256×256 pixels, avec un rapport largeur/hauteur compris entre 0,4 et 2,5. | IMAGE | Oui | - |
| `last_frame` | Image finale optionnelle pour la vidéo. Lorsqu'elle est fournie, la vidéo commence à la première image et se termine à cette image. Doit respecter les mêmes exigences de taille et de format que `first_frame`. | IMAGE | Non | - |
| `seed` | Graine aléatoire. La même requête avec la même graine donne des résultats similaires, mais pas nécessairement identiques. Inclut une option « contrôle après génération » pour randomiser après chaque génération. Défaut : 42. | INT | Oui | 0 à 4294967295 |
| `watermark` | Indique s'il faut ajouter un filigrane AIGC à la vidéo. Il s'agit d'un paramètre avancé. Défaut : False. | BOOLEAN | Oui | True<br>False |

**Remarque sur les contraintes :**
- L'invite textuelle dans le combo `model` ne peut pas être vide ; les invites composées uniquement d'espaces sont rejetées.
- Toute image fournie (`first_frame` et, si utilisée, `last_frame`) doit faire au moins 256 pixels de large et 256 pixels de haut, avec un rapport largeur/hauteur compris entre 0,4 et 2,5 (approximativement de 2:5 à 5:2).
- `last_frame` est optionnel. Lorsqu'il est omis, la vidéo est générée uniquement à partir de la première image.
- Le format de la vidéo de sortie est déterminé par les images fournies, et non par un paramètre de format séparé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée à partir de la première image et de l'image finale optionnelle en utilisant le modèle MiniMax H3. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `f4cb9217eb346019680c64b30c1beacce16f0050616b7b76265edc5840f6b21e`
