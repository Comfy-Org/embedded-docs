# OpenAI GPT Image 2.6

## Aperçu

OpenAI GPT Image 2.6 génère des images à partir d'un prompt et les modifie lorsque vous connectez des images de référence, en utilisant les modèles GPT Image d'OpenAI. Le nœud propose quatre modèles : `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare` et `gpt-image-2.5-sunburst`. Dessinez des annotations sur la première image de référence et connectez-les sous forme de paire de balisage pour indiquer au modèle exactement où effectuer les modifications.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle GPT Image à utiliser. La sélection d'un modèle révèle les paramètres de ce modèle. | DYNAMIC_COMBO | Oui | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"`<br>`"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"` |

### Entrées gpt-image-2.6-flare et gpt-image-2.6-sunburst

Ces entrées apparaissent lorsque `model` est défini sur `gpt-image-2.6-flare` ou `gpt-image-2.6-sunburst`. Les deux modèles partagent les mêmes paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.prompt` | Ce qu'il faut générer, ou la modification à apporter. (par défaut : `""`) | STRING | Oui | N/A |
| `model.size` | Taille de l'image. Sélectionnez "Custom" pour utiliser la largeur et la hauteur personnalisées. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Utilisé uniquement lorsque `model.size` est "Custom". Doit être un multiple de 16. (par défaut : `1024`) | INT | Non | 480 à 3840 (pas : 16) |
| `model.custom_height` | Utilisé uniquement lorsque `model.size` est "Custom". Doit être un multiple de 16. (par défaut : `1024`) | INT | Non | 480 à 3840 (pas : 16) |
| `model.background` | Renvoyer l'image avec ou sans arrière-plan. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualité de l'image. Les niveaux plus élevés coûtent plus cher et prennent plus de temps. (par défaut : `"low"`) | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Dans quelle mesure le modèle planifie l'image avant le rendu. (par défaut : `"high"`) | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Images de référence facultatives pour l'édition. Jusqu'à 16. | AUTOGROW | Non | 0 à 16 |
| `model.markup` | Annotations dessinées sur la première image de référence, indiquant où effectuer les modifications. Doit correspondre à la taille de cette image et doit être connecté avec `model.markup_alpha`. | IMAGE | Non | N/A |
| `model.markup_alpha` | Le blanc marque les annotations dans `model.markup`. La sortie MASK du nœud Painter convient directement ; un masque Load Image nécessite d'abord Invert Mask. | MASK | Non | N/A |
| `model.seed` | Contrôle si le nœud se réexécute ; les résultats sont non déterministes quel que soit la graine. (par défaut : `42`) | INT | Oui | 0 à 2147483647 |

### Entrées gpt-image-2.5-flare et gpt-image-2.5-sunburst

Ces entrées apparaissent lorsque `model` est défini sur `gpt-image-2.5-flare` ou `gpt-image-2.5-sunburst`. Ils correspondent aux modèles 2.6, sauf que `model.complexity` n'est pas proposé.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.prompt` | Ce qu'il faut générer, ou la modification à apporter. (par défaut : `""`) | STRING | Oui | N/A |
| `model.size` | Taille de l'image. Sélectionnez "Custom" pour utiliser la largeur et la hauteur personnalisées. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Utilisé uniquement lorsque `model.size` est "Custom". Doit être un multiple de 16. (par défaut : `1024`) | INT | Non | 480 à 3840 (pas : 16) |
| `model.custom_height` | Utilisé uniquement lorsque `model.size` est "Custom". Doit être un multiple de 16. (par défaut : `1024`) | INT | Non | 480 à 3840 (pas : 16) |
| `model.background` | Renvoyer l'image avec ou sans arrière-plan. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualité de l'image. Les niveaux plus élevés coûtent plus cher et prennent plus de temps. (par défaut : `"low"`) | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Images de référence facultatives pour l'édition. Jusqu'à 16. | AUTOGROW | Non | 0 à 16 |
| `model.markup` | Annotations dessinées sur la première image de référence, indiquant où effectuer les modifications. Doit correspondre à la taille de cette image et doit être connecté avec `model.markup_alpha`. | IMAGE | Non | N/A |
| `model.markup_alpha` | Le blanc marque les annotations dans `model.markup`. La sortie MASK du nœud Painter convient directement ; un masque Load Image nécessite d'abord Invert Mask. | MASK | Non | N/A |
| `model.seed` | Contrôle si le nœud se réexécute ; les résultats sont non déterministes quel que soit la graine. (par défaut : `42`) | INT | Oui | 0 à 2147483647 |

**Contraintes et limitations des paramètres :**

- Lorsque `model.size` est défini sur "Custom", `model.custom_width` et `model.custom_height` doivent tous deux être des multiples de 16, le bord le plus long ne doit pas dépasser 3840, le rapport d'aspect ne doit pas dépasser 3:1 et le nombre total de pixels doit être compris entre 655,360 et 8,294,400.
- `model.markup` et `model.markup_alpha` doivent être connectés ensemble. Le balisage nécessite au moins une image de référence, et sa largeur et sa hauteur doivent correspondre à la première image de référence.
- Sans `model.images`, le nœud génère des images à partir du seul prompt ; avec des images de référence, il les modifie et les combine.
- Les images de référence sont réduites avant d'être envoyées à l'API.
- `model.complexity` existe uniquement sur `gpt-image-2.6-flare` et `gpt-image-2.6-sunburst` ; les modèles 2.5 utilisent une profondeur de planification fixe.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image ou les images générées. Toutes les images renvoyées sont empilées dans un seul lot ; si leurs dimensions diffèrent, elles sont redimensionnées pour correspondre à la première image. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV3/fr.md)

---
**Source fingerprint (SHA-256):** `33f5d91af56c215cc7f7c704f9b123fe1c35bf287012072b818b76b551c04667`
