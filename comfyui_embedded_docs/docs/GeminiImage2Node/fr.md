Le nœud GeminiImage2Node génère ou modifie des images à l'aide du modèle Gemini Vertex AI de Google. Il envoie une invite textuelle et des images ou fichiers de référence facultatifs à l'API, puis retourne l'image générée et/ou une description textuelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Invite textuelle décrivant l'image à générer ou les modifications à appliquer. Incluez toutes les contraintes, styles ou détails que le modèle doit suivre. | STRING | Oui | N/A |
| `model` | Le modèle Gemini spécifique à utiliser pour la génération. L'option "Nano Banana 2" correspond en interne au modèle `gemini-3.1-flash-image-preview`. | COMBO | Oui | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Lorsqu'il est fixé à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. Une sortie déterministe n'est pas garantie. Changer le modèle ou d'autres paramètres peut entraîner des variations même avec la même graine. Par défaut : 42. | INT | Oui | 0 à 18446744073709551615 |
| `aspect_ratio` | Le rapport hauteur/largeur souhaité pour l'image de sortie. Si réglé sur 'auto', il correspond au rapport hauteur/largeur de votre image d'entrée ; si aucune image n'est fournie, un carré 16:9 est généralement généré. Par défaut : "auto". | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Résolution de sortie cible. Pour 2K/4K, le suréchantillonneur natif Gemini est utilisé. | COMBO | Oui | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Choisissez 'IMAGE' pour une sortie uniquement image, ou 'IMAGE+TEXT' pour retourner à la fois l'image générée et une réponse textuelle. | COMBO | Oui | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | Image(s) de référence facultative(s). Pour inclure plusieurs images, utilisez le nœud Batch Images (jusqu'à 14). | IMAGE | Non | N/A |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. | CUSTOM | Non | N/A |
| `system_prompt` | Instructions fondamentales qui dictent le comportement d'une IA. Par défaut : une invite système prédéfinie pour la génération d'images. | STRING | Non | N/A |

**Contraintes :**

* L'entrée `images` prend en charge un maximum de 14 images. Si davantage sont fournies, une erreur sera générée.
* L'entrée `files` doit être connectée à un nœud qui produit le type de données `GEMINI_INPUT_FILES`.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image générée ou modifiée par le modèle Gemini. | IMAGE |
| `string` | La réponse textuelle du modèle. Cette sortie sera vide si `response_modalities` est réglé sur "IMAGE". | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/fr.md)

---
**Source fingerprint (SHA-256):** `20a937a635f883a42e22582ae415f6d2a9a6ecc50f147c9090431877e5461144`
