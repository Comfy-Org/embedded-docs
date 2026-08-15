# MiniMax H3 Première-Dernière-Image vers Vidéo

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser pour la génération de vidéo. La sélection d'un modèle révèle ses paramètres spécifiques (prompt, résolution, durée). | DYNAMIC_COMBO | Oui | "MiniMax H3" |
| `first_frame` | Image initiale pour la vidéo. Le rapport hauteur/largeur de la vidéo générée suit cette image. Doit être d'au moins 256x256 pixels avec un rapport largeur/hauteur compris entre 0,4 et 2,5. | IMAGE | Oui | - |
| `last_frame` | Image finale facultative pour la vidéo. Lorsqu'elle est fournie, la vidéo démarre à partir de l'image initiale et se termine à cette image. Doit respecter les mêmes exigences de taille et de rapport hauteur/largeur que `first_frame`. | IMAGE | Non | - |
| `seed` | Graine aléatoire. La même requête avec la même graine donne des résultats similaires, mais pas garantis identiques. Comprend une option « contrôle après génération » pour randomiser après chaque génération. Par défaut : 42. | INT | Oui | 0 à 4294967295 |
| `watermark` | Indique s'il faut ajouter un filigrane AIGC à la vidéo. Il s'agit d'un paramètre avancé. Par défaut : False. | BOOLEAN | Oui | True<br>False |

### Entrées MiniMax H3

Ces entrées apparaissent lorsque « MiniMax H3 » est sélectionné dans le sélecteur `model`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération de vidéo. Doit contenir au moins un caractère non blanc. | STRING | Oui | - |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | "768P"<br>"2K" |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). Par défaut : 5. | INT | Oui | 4 à 15 |

**Remarque sur les contraintes :**

- Le prompt texte dans la combinaison `model` ne peut pas être vide ; les prompts composés uniquement d'espaces sont rejetés.
- Toute image fournie (`first_frame` et, si utilisée, `last_frame`) doit mesurer au moins 256 pixels de large et 256 pixels de haut, avec un rapport largeur/hauteur compris entre 0,4 et 2,5 (environ 2:5 à 5:2).
- `last_frame` est facultatif. Lorsqu'elle est omise, la vidéo est générée à partir de l'image initiale uniquement.
- Le rapport hauteur/largeur de la vidéo de sortie est déterminé par les images fournies, et non par un paramètre de rapport séparé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée à partir de l'image initiale et de l'image finale facultative à l'aide du modèle MiniMax H3. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `5c9fadf20f994950df9f1b0630fdce1416fe4459ad23bcd20dfa6f22adbe4598`
