# BriaExpandImage

Bria Expand Image étend une image au-delà de ses bordures d'origine en générant un nouveau contenu avec Bria. Il permet de choisir un ratio d'aspect cible, un ratio personnalisé, ou de définir un canevas avec un placement manuel de l'image d'origine. L'expansion peut être guidée par un prompt texte, et Bria en génère un automatiquement si le prompt est laissé vide.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à étendre. | IMAGE | Oui | — |
| `expand_mode` | Forme cible de l'image étendue : un ratio d'aspect prédéfini, un ratio personnalisé, ou un placement manuel de l'image d'origine sur un canevas. Le mode manuel est le seul à pouvoir atteindre un canevas plus haut que 1:2. La sélection de `custom_ratio` révèle `ratio_width` et `ratio_height`. La sélection de `manual` révèle les paramètres de canevas et de placement de l'image. | DYNAMIC_COMBO | Oui | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"custom_ratio"`<br>`"manual"` |
| `ratio_width` | Côté largeur du ratio cible : 21 et 9 donnent 21:9. Valeur par défaut : 21. | INT | Conditionnel | 1–100 |
| `ratio_height` | Côté hauteur du ratio cible : 21 et 9 donnent 21:9. Bria n'accepte que les ratios largeur/hauteur entre 0,5 et 3,0, donc tout ce qui est plus haut que 1:2 nécessite le mode manuel. Valeur par défaut : 9. | INT | Conditionnel | 1–100 |
| `canvas_width` | Largeur du canevas de sortie en pixels. Valeur par défaut : 1000. | INT | Conditionnel | 64–5000 |
| `canvas_height` | Hauteur du canevas de sortie en pixels. Valeur par défaut : 1000. | INT | Conditionnel | 64–5000 |
| `image_width` | Largeur de l'image d'origine dans le canevas. Valeur par défaut : 500. | INT | Conditionnel | 1–5000 |
| `image_height` | Hauteur de l'image d'origine dans le canevas. Valeur par défaut : 500. | INT | Conditionnel | 1–5000 |
| `image_x` | Position X du coin supérieur gauche de l'image dans le canevas ; peut se situer en dehors du canevas, ce qui recadre l'image. Valeur par défaut : 250. | INT | Conditionnel | -5000–5000 |
| `image_y` | Position Y du coin supérieur gauche de l'image dans le canevas ; peut se situer en dehors du canevas, ce qui recadre l'image. Valeur par défaut : 250. | INT | Conditionnel | -5000–5000 |
| `prompt` | Description facultative de la scène étendue ; si elle est vide, Bria en génère une à partir de l'image. Valeur par défaut : chaîne vide. | STRING | Non | Toute chaîne |
| `negative_prompt` | Un prompt négatif facultatif pour l'expansion. Valeur par défaut : chaîne vide. | STRING | Non | Toute chaîne |
| `seed` | Graine pour le processus de génération aléatoire. Valeur par défaut : 42. | INT | Non | 1–2147483647 |
| `moderation` | Paramètres de modération. Lorsqu'elle est définie sur `true`, des options de modération supplémentaires sont affichées. | DYNAMIC_COMBO | Non | `"false"`<br>`"true"` |
| `prompt_content_moderation` | Si activé, modère le contenu du prompt. Valeur par défaut : false. Disponible uniquement lorsque `moderation` est `true`. | BOOLEAN | Conditionnel | true/false |
| `visual_input_moderation` | Si activé, modère l'entrée visuelle. Valeur par défaut : false. Disponible uniquement lorsque `moderation` est `true`. | BOOLEAN | Conditionnel | true/false |
| `visual_output_moderation` | Si activé, modère la sortie visuelle. Valeur par défaut : false. Disponible uniquement lorsque `moderation` est `true`. | BOOLEAN | Conditionnel | true/false |

Lorsque `expand_mode` est `custom_ratio`, `ratio_width` et `ratio_height` définissent un ratio d'aspect cible. Bria n'accepte que les ratios largeur/hauteur entre 0,5 et 3,0. Si le ratio est en dehors de cette plage, une erreur est levée et le mode `manual` doit être utilisé à la place.

Lorsque `expand_mode` est `manual`, l'image d'origine est placée sur un canevas à la taille et à la position spécifiées. L'image peut s'étendre en dehors du canevas, auquel cas la partie extérieure est recadrée.

Lorsque `moderation` est `true`, les trois booléens de modération sont envoyés à Bria. Lorsque `moderation` est `false`, ils sont ignorés.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image étendue générée par Bria. | IMAGE |
| `prompt` | Le prompt utilisé pour l'expansion ; auto-généré par Bria lorsque le prompt d'entrée est vide. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaExpandImage/fr.md)

---
**Source fingerprint (SHA-256):** `d2c9431837f200ccbcb39037f7b26013494c4dea3d40d899db4e717ddbbea71c`
