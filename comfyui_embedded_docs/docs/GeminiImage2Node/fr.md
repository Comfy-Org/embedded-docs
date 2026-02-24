> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/fr.md)

Le nœud GeminiImage2Node génère ou modifie des images en utilisant le modèle Gemini de Google Vertex AI. Il envoie une instruction textuelle et des images ou fichiers de référence optionnels à l'API et renvoie l'image générée et/ou une description textuelle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Instruction textuelle décrivant l'image à générer ou les modifications à appliquer. Incluez toutes les contraintes, styles ou détails que le modèle doit suivre. |
| `model` | COMBO | Oui | `"gemini-3-pro-image-preview"` | Le modèle Gemini spécifique à utiliser pour la génération. |
| `seed` | INT | Oui | 0 à 18446744073709551615 | Lorsqu'il est fixé à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse à des requêtes répétées. Une sortie déterministe n'est pas garantie. Changer le modèle ou d'autres paramètres peut entraîner des variations même avec la même graine. Par défaut : 42. |
| `aspect_ratio` | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` | Le rapport d'aspect souhaité pour l'image de sortie. Si défini sur 'auto', il correspond au rapport d'aspect de votre image d'entrée ; si aucune image n'est fournie, un carré 16:9 est généralement généré. Par défaut : "auto". |
| `resolution` | COMBO | Oui | `"1K"`<br>`"2K"`<br>`"4K"` | Résolution cible de sortie. Pour 2K/4K, l'upscaleur natif de Gemini est utilisé. |
| `response_modalities` | COMBO | Oui | `"IMAGE+TEXT"`<br>`"IMAGE"` | Choisissez 'IMAGE' pour une sortie image uniquement, ou 'IMAGE+TEXT' pour renvoyer à la fois l'image générée et une réponse textuelle. |
| `images` | IMAGE | Non | N/A | Image(s) de référence optionnelle(s). Pour inclure plusieurs images, utilisez le nœud Batch Images (jusqu'à 14). |
| `files` | CUSTOM | Non | N/A | Fichier(s) optionnel(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. |
| `system_prompt` | STRING | Non | N/A | Instructions fondamentales qui dictent le comportement de l'IA. Par défaut : Une instruction système prédéfinie pour la génération d'images. |

**Contraintes :**

* L'entrée `images` supporte un maximum de 14 images. Si plus sont fournies, une erreur sera levée.
* L'entrée `files` doit être connectée à un nœud qui produit le type de données `GEMINI_INPUT_FILES`.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image générée ou modifiée par le modèle Gemini. |
| `string` | STRING | La réponse textuelle du modèle. Cette sortie sera vide si `response_modalities` est défini sur "IMAGE". |
