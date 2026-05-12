> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI :

## Aperçu

Ce nœud génère ou modifie des images en envoyant une invite textuelle à l'API Vertex AI de Google. Il utilise un modèle Gemini spécifique pour créer de nouvelles images ou modifier des images existantes selon vos instructions.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/D | Invite textuelle décrivant l'image à générer ou les modifications à appliquer. Incluez toutes les contraintes, styles ou détails que le modèle doit suivre. |
| `model` | COMBO | Oui | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` | Sélectionne le modèle Gemini à utiliser pour la génération d'images. Actuellement, une seule option est disponible. |
| `seed` | INT | Oui | 0 à 18446744073709551615 | Lorsque la graine est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. Une sortie déterministe n'est pas garantie. De plus, la modification du modèle ou des paramètres, comme la température, peut entraîner des variations dans la réponse, même avec la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée. (valeur par défaut : 42) |
| `response_modalities` | COMBO | Oui | `"IMAGE"`<br>`"IMAGE+TEXT"` | Détermine le format de la réponse. Choisissez "IMAGE" pour recevoir uniquement une image, ou "IMAGE+TEXT" pour recevoir à la fois une image et une description textuelle. (valeur par défaut : "IMAGE") |
| `system_prompt` | STRING | Non | N/D | Instructions fondamentales qui dictent le comportement d'une IA. Il s'agit d'un paramètre avancé. |

**Remarque sur le paramètre `model` :** Le paramètre `model` est une liste déroulante dynamique qui inclut des sous-paramètres supplémentaires pour la résolution, le rapport hauteur/largeur et le niveau de réflexion. Ces sous-paramètres sont définis dans la sélection du modèle et ne sont pas répertoriés comme des entrées distinctes dans ce tableau.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `IMAGE` | IMAGE | L'image générée ou modifiée. |
| `STRING` | STRING | Une description textuelle ou une légende générée par le modèle. |
| `thought_image` | IMAGE | Première image issue du processus de réflexion du modèle. Disponible uniquement avec le niveau de réflexion ÉLEVÉ et la modalité IMAGE+TEXT. |