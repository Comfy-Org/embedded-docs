Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

## Aperçu

Modifier une image existante en fonction d'une instruction textuelle. Ce nœud envoie vos images et une description textuelle à l'API Grok, qui modifie les images selon vos instructions et renvoie le résultat.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | L'instruction textuelle utilisée pour générer l'image. Doit comporter au moins 1 caractère après suppression des espaces blancs. | STRING | Oui | N/A |
| `modèle` | Le modèle d'image Grok à utiliser. Ce paramètre possède plusieurs sous-options qui apparaissent après la sélection d'un modèle. Modèles disponibles : `grok-imagine-image-quality`, `grok-imagine-image-pro`, `grok-imagine-image`. Chaque modèle a des capacités différentes (voir note ci-dessous). | MODEL | Oui | Voir Description |
| `graine` | Graine pour déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine. (par défaut : 0) | INT | Oui | 0 à 2147483647 |

**Note sur les contraintes du paramètre `model` :**
- Le paramètre `model` est une liste déroulante dynamique qui inclut des sous-options pour `resolution`, `number_of_images`, `images` et `aspect_ratio`.
- **`grok-imagine-image-quality`** : Prend en charge jusqu'à 3 images en entrée et permet un rapport hauteur/largeur personnalisé.
- **`grok-imagine-image-pro`** : Prend en charge seulement 1 image en entrée et ne permet pas de rapport hauteur/largeur personnalisé.
- **`grok-imagine-image`** : Prend en charge jusqu'à 3 images en entrée et permet un rapport hauteur/largeur personnalisé.
- **Au moins une image en entrée est requise** pour la modification. Le nœud générera une erreur si aucune image n'est fournie.
- **Le rapport hauteur/largeur personnalisé** (sous-option `aspect_ratio`) n'est autorisé que lorsque plusieurs images sont connectées à l'entrée image. Si une seule image est fournie, le rapport hauteur/largeur doit être défini sur "auto".

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | La ou les images modifiées renvoyées par l'API Grok. Si une seule image est générée, elle est renvoyée directement. Si plusieurs images sont générées, elles sont concaténées en un seul tenseur de lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `b041b40bb5712a67b09dcb0c841f00cbdd9ef77b9e4f3fdc6b2c4038be447ba5`
