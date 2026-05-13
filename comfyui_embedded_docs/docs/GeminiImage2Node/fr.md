> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/fr.md)

Le nœud GeminiImage2Node génère ou modifie des images à l'aide du modèle Gemini Vertex AI de Google. Il envoie une invite textuelle et des images ou fichiers de référence facultatifs à l'API, puis retourne l'image générée et/ou une description textuelle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Invite textuelle décrivant l'image à générer ou les modifications à appliquer. Incluez toutes les contraintes, styles ou détails que le modèle doit suivre. |
| `model` | COMBO | Oui | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` | Le modèle Gemini spécifique à utiliser pour la génération. L'option "Nano Banana 2" correspond en interne au modèle `gemini-3.1-flash-image-preview`. |
| `seed` | INT | Oui | 0 à 18446744073709551615 | Lorsqu'il est fixé à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. Une sortie déterministe n'est pas garantie. Changer le modèle ou d'autres paramètres peut entraîner des variations même avec la même graine. Par défaut : 42. |
| `aspect_ratio` | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` | Le rapport hauteur/largeur souhaité pour l'image de sortie. Si réglé sur 'auto', il correspond au rapport hauteur/largeur de votre image d'entrée ; si aucune image n'est fournie, un carré 16:9 est généralement généré. Par défaut : "auto". |
| `resolution` | COMBO | Oui | `"1K"`<br>`"2K"`<br>`"4K"` | Résolution de sortie cible. Pour 2K/4K, le suréchantillonneur natif Gemini est utilisé. |
| `response_modalities` | COMBO | Oui | `"IMAGE+TEXT"`<br>`"IMAGE"` | Choisissez 'IMAGE' pour une sortie uniquement image, ou 'IMAGE+TEXT' pour retourner à la fois l'image générée et une réponse textuelle. |
| `images` | IMAGE | Non | N/A | Image(s) de référence facultative(s). Pour inclure plusieurs images, utilisez le nœud Batch Images (jusqu'à 14). |
| `files` | CUSTOM | Non | N/A | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. |
| `system_prompt` | STRING | Non | N/A | Instructions fondamentales qui dictent le comportement d'une IA. Par défaut : une invite système prédéfinie pour la génération d'images. |

**Contraintes :**

* L'entrée `images` prend en charge un maximum de 14 images. Si davantage sont fournies, une erreur sera générée.
* L'entrée `files` doit être connectée à un nœud qui produit le type de données `GEMINI_INPUT_FILES`.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | L'image générée ou modifiée par le modèle Gemini. |
| `string` | STRING | La réponse textuelle du modèle. Cette sortie sera vide si `response_modalities` est réglé sur "IMAGE". |

---
**Source fingerprint (SHA-256):** `20a937a635f883a42e22582ae415f6d2a9a6ecc50f147c9090431877e5461144`
