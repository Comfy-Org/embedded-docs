> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/fr.md)

Voici la traduction de la documentation technique du nœud ComfyUI :

## Aperçu

Modifie une image existante en fonction d'une invite textuelle. Ce nœud envoie vos images et une description textuelle à l'API Grok, qui modifie les images selon vos instructions et renvoie le résultat.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/A | L'invite textuelle utilisée pour générer l'image. Doit contenir au moins 1 caractère après suppression des espaces. |
| `model` | MODEL | Oui | Voir Description | Le modèle d'image Grok à utiliser. Ce paramètre comporte plusieurs sous-options qui apparaissent après la sélection d'un modèle. Modèles disponibles : `grok-imagine-image-quality`, `grok-imagine-image-pro`, `grok-imagine-image`. Chaque modèle a des capacités différentes (voir note ci-dessous). |
| `seed` | INT | Oui | 0 à 2147483647 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine. (valeur par défaut : 0) |

**Note sur les contraintes du paramètre `model` :**
- Le paramètre `model` est une liste déroulante dynamique qui inclut des sous-options pour `resolution`, `number_of_images`, `images` et `aspect_ratio`.
- **`grok-imagine-image-quality`** : Prend en charge jusqu'à 3 images d'entrée et permet un rapport hauteur/largeur personnalisé.
- **`grok-imagine-image-pro`** : Prend en charge seulement 1 image d'entrée et ne permet pas de rapport hauteur/largeur personnalisé.
- **`grok-imagine-image`** : Prend en charge jusqu'à 3 images d'entrée et permet un rapport hauteur/largeur personnalisé.
- **Au moins une image d'entrée est requise** pour la modification. Le nœud générera une erreur si aucune image n'est fournie.
- **Le rapport hauteur/largeur personnalisé** (sous-option `aspect_ratio`) n'est autorisé que lorsque plusieurs images sont connectées à l'entrée d'image. Si une seule image est fournie, le rapport hauteur/largeur doit être défini sur "auto".

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `IMAGE` | IMAGE | La ou les images modifiées renvoyées par l'API Grok. Si une seule image est générée, elle est renvoyée directement. Si plusieurs images sont générées, elles sont concaténées en un seul tenseur par lots. |