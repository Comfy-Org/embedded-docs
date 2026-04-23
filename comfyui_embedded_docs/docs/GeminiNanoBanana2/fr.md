> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/fr.md)

Le nœud GeminiNanoBanana2 génère ou modifie des images en utilisant le modèle Gemini de Vertex AI de Google. Il fonctionne en envoyant une invite textuelle, ainsi que des images ou fichiers de référence optionnels, à l'API et renvoie l'image générée ainsi que tout texte d'accompagnement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | N/A | L'invite textuelle décrivant l'image à générer ou les modifications à appliquer. Incluez toutes les contraintes, styles ou détails que le modèle doit suivre. |
| `model` | COMBO | Oui | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` | Le modèle Gemini spécifique à utiliser pour la génération d'image. |
| `seed` | INT | Oui | 0 à 18446744073709551615 | Lorsque la graine est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. Une sortie déterministe n'est pas garantie. De plus, changer le modèle ou les paramètres, comme la température, peut entraîner des variations dans la réponse même en utilisant la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée. (par défaut : 42) |
| `aspect_ratio` | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` | Si défini sur 'auto', correspond au ratio d'aspect de votre image d'entrée ; si aucune image n'est fournie, un carré 16:9 est généralement généré. (par défaut : "auto") |
| `resolution` | COMBO | Oui | `"1K"`<br>`"2K"`<br>`"4K"` | Résolution de sortie cible. Pour 2K/4K, l'upscaleur natif de Gemini est utilisé. |
| `response_modalities` | COMBO | Oui | `"IMAGE"`<br>`"IMAGE+TEXT"` | Détermine le type de contenu que le modèle renverra. (avancé) |
| `thinking_level` | COMBO | Oui | `"MINIMAL"`<br>`"HIGH"` | Contrôle la profondeur du processus de raisonnement du modèle. |
| `images` | IMAGE | Non | N/A | Image(s) de référence optionnelle(s). Pour inclure plusieurs images, utilisez le nœud Batch Images (jusqu'à 14). |
| `files` | CUSTOM | Non | N/A | Fichier(s) optionnel(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. |
| `system_prompt` | STRING | Non | N/A | Instructions fondamentales qui dictent le comportement de l'IA. (avancé) |

**Note :** L'entrée `images` supporte un maximum de 14 images. Si plus sont fournies, le nœud générera une erreur.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image principale générée ou modifiée par le modèle. |
| `string` | STRING | Tout contenu textuel renvoyé par le modèle. |
| `thought_image` | IMAGE | Première image issue du processus de réflexion du modèle. Disponible uniquement avec le niveau de réflexion HIGH et la modalité IMAGE+TEXT. |