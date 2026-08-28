# Nano Banana Pro (Google Gemini Image)

Le nœud GeminiImage2Node génère ou modifie des images à l'aide du modèle Gemini de Google Vertex AI. Vous fournissez une invite textuelle et éventuellement des images ou fichiers de référence ; le nœud les envoie à l'API et renvoie l'image générée, ainsi qu'une réponse textuelle si demandé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle décrivant l'image à générer ou les modifications à appliquer. Incluez toutes les contraintes, les styles ou les détails que le modèle doit suivre. L'invite doit contenir au moins un caractère après suppression des espaces. | STRING | Oui | N/A |
| `model` | Le modèle Gemini spécifique à utiliser pour la génération. L'option « Nano Banana 2 (Gemini 3.1 Flash Image) » correspond en interne au modèle `gemini-3.1-flash-image`, et « gemini-3-pro-image-preview » correspond à `gemini-3-pro-image`. | COMBO | Oui | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Lorsque la graine est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. La sortie déterministe n'est pas garantie. De plus, modifier le modèle ou les paramètres, comme la température, peut entraîner des variations dans la réponse même avec la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée. Défaut : 42. | INT | Oui | 0 à 18446744073709551615 |
| `aspect_ratio` | Si elle est définie sur « auto », correspond au rapport hauteur/largeur de votre image d'entrée ; si aucune image n'est fournie, un format 16:9 est généralement généré. Défaut : « auto ». | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Résolution de sortie cible. Pour la 2K/4K, l'upscaler natif de Gemini est utilisé. | COMBO | Oui | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Choisissez « IMAGE » pour une sortie image uniquement, ou « IMAGE+TEXT » pour obtenir à la fois l'image générée et une réponse textuelle. | COMBO | Oui | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | Image(s) de référence facultative(s). Pour inclure plusieurs images, utilisez le nœud Batch Images (jusqu'à 14). | IMAGE | Non | N/A |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | Non | N/A |
| `system_prompt` | Instructions fondamentales qui déterminent le comportement d'une IA. Défaut : invite système prédéfinie pour la génération d'images. | STRING | Non | N/A |

**Contraintes :**

* L'entrée `images` prend en charge un maximum de 14 images. Si plus d'images sont fournies, une erreur est déclenchée.
* Lorsque plus de 10 images sont fournies, les 10 premières sont téléchargées comme références URL et les images restantes sont envoyées en ligne dans la requête.
* L'entrée `files` doit être connectée à un nœud qui produit le type de données `GEMINI_INPUT_FILES`.
* Lorsque `response_modalities` est défini sur « IMAGE », seule l'image est renvoyée et la sortie textuelle est vide.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image générée ou modifiée par le modèle Gemini. | IMAGE |
| `string` | La réponse textuelle du modèle. Cette sortie sera vide si `response_modalities` est défini sur « IMAGE ». | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/fr.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
