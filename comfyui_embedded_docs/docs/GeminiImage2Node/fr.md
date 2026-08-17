# Nano Banana Pro (Google Gemini Image)

Nano Banana Pro (Google Gemini Image) génère ou édite des images à l'aide des modèles d'image Gemini de Google Vertex AI. Il envoie une invite textuelle accompagnée d'images ou de fichiers de référence optionnels à l'API Gemini, puis retourne l'image générée ainsi qu'une réponse textuelle facultative.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle décrivant l'image à générer ou les modifications à appliquer. Incluez toutes les contraintes, styles ou détails que le modèle doit suivre. Par défaut : chaîne vide. | STRING | Oui | N/A |
| `model` | Le modèle d'image Gemini à utiliser. L'option « Nano Banana 2 (Gemini 3.1 Flash Image) » est envoyée à l'API sous la forme `gemini-3.1-flash-image` ; « gemini-3-pro-image-preview » est envoyée sous la forme `gemini-3-pro-image`. | COMBO | Oui | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Lorsque la graine est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. La sortie déterministe n'est pas garantie. Changer le modèle ou d'autres paramètres peut entraîner des variations dans la réponse, même avec la même valeur de graine. Par défaut : 42. | INT | Oui | 0 à 18446744073709551615 |
| `aspect_ratio` | Le rapport hauteur/largeur souhaité de l'image de sortie. Si la valeur est « auto », il correspond au rapport hauteur/largeur de votre image d'entrée ; si aucune image n'est fournie, une image 16:9 est généralement générée. Par défaut : « auto ». | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Résolution de sortie cible. Pour les résolutions 2K/4K, l'upscaler natif de Gemini est utilisé. | COMBO | Oui | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Choisissez « IMAGE » pour une sortie image uniquement, ou « IMAGE+TEXT » pour obtenir à la fois l'image générée et une réponse textuelle. | COMBO | Oui | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | Image(s) de référence optionnelle(s) utilisée(s) comme contexte visuel. Pour inclure plusieurs images, utilisez le nœud Batch Images (jusqu'à 14). | IMAGE | Non | N/A |
| `files` | Fichier(s) optionnel(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | Non | N/A |
| `system_prompt` | Instructions fondamentales qui dictent le comportement du modèle. Par défaut : une invite système prédéfinie qui demande au modèle de toujours générer une image. | STRING | Non | N/A |

**Contraintes :**

* L'`prompt` ne doit pas être vide après suppression des espaces de début et de fin ; sinon, une erreur est levée.
* L'entrée `images` accepte un maximum de 14 images. Si plus de 14 sont fournies, une erreur est levée.
* L'entrée `files` doit être connectée à un nœud qui produit le type de données `GEMINI_INPUT_FILES`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image générée ou éditée par le modèle Gemini. | IMAGE |
| `string` | La réponse textuelle du modèle. Cette sortie est vide lorsque `response_modalities` est défini sur « IMAGE ». | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/fr.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
