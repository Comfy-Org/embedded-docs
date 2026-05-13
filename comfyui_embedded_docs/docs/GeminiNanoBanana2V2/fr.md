> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI :

## Aperçu

Ce nœud génère ou modifie des images en envoyant une invite textuelle à l'API Vertex AI de Google. Il utilise un modèle Gemini spécifique pour créer de nouvelles images ou modifier des images existantes en fonction de vos instructions.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/D | Invite textuelle décrivant l'image à générer ou les modifications à appliquer. Incluez toutes les contraintes, styles ou détails que le modèle doit suivre. |
| `modèle` | COMBO | Oui | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` | Sélectionne le modèle Gemini à utiliser pour la génération d'images. Une seule option est actuellement disponible. |
| `graine` | INT | Oui | 0 à 18446744073709551615 | Lorsque la graine est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. Une sortie déterministe n'est pas garantie. De plus, la modification du modèle ou des paramètres, comme la température, peut entraîner des variations dans la réponse, même avec la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée. (valeur par défaut : 42) |
| `modalités de réponse` | COMBO | Oui | `"IMAGE"`<br>`"IMAGE+TEXT"` | Détermine le format de la réponse. Choisissez "IMAGE" pour recevoir uniquement une image, ou "IMAGE+TEXT" pour recevoir à la fois une image et une description textuelle. (valeur par défaut : "IMAGE") |
| `invite système` | STRING | Non | N/D | Instructions fondamentales qui dictent le comportement d'une IA. Il s'agit d'un paramètre avancé. |

**Remarque sur le paramètre `model` :** Le paramètre `model` est une liste déroulante dynamique qui inclut des sous-paramètres supplémentaires pour la résolution, le rapport hauteur/largeur et le niveau de réflexion. Ces sous-paramètres sont définis dans la sélection du modèle et ne sont pas répertoriés comme des entrées distinctes dans ce tableau.

**Remarque sur l'entrée d'image :** Vous pouvez fournir jusqu'à 14 images en entrée au modèle. Ces images sont transmises via le sous-champ image du paramètre `model` et sont utilisées pour l'édition ou comme contexte visuel pour la génération.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `IMAGE` | IMAGE | L'image générée ou modifiée. |
| `image de réflexion` | STRING | Une description textuelle ou une légende générée par le modèle. |
| `thought_image` | IMAGE | Première image du processus de réflexion du modèle. Disponible uniquement avec le niveau de réflexion HIGH et la modalité IMAGE+TEXT. |

---
**Source fingerprint (SHA-256):** `6b91afcdd12e08ff0e3afdbb5596bfd63463cda4d2b031019dedf03bd122fa87`
