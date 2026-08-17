# Nano Banana 2

Ce nœud génère ou modifie des images de manière synchrone à l'aide du modèle Gemini de Google Vertex AI (Nano Banana 2 / Gemini 3.1 Flash Image). Il envoie une invite de texte, ainsi que des images ou fichiers de référence facultatifs, à l'API et renvoie l'image générée, tout texte d'accompagnement et éventuellement une image issue du processus de réflexion du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite de texte décrivant l'image à générer ou les modifications à appliquer. Incluez toutes les contraintes, styles ou détails que le modèle doit suivre. Doit contenir au moins un caractère non blanc. | STRING | Oui | N/A |
| `model` | Le modèle Gemini spécifique à utiliser pour la génération d'images. La seule option disponible correspond au modèle `gemini-3.1-flash-image-preview`. | COMBO | Oui | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Lorsque la graine est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des demandes répétées. La sortie déterministe n'est pas garantie. De plus, changer le modèle ou les paramètres, comme la température, peut entraîner des variations dans la réponse même si vous utilisez la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée. (par défaut : 42) | INT | Oui | 0 à 18446744073709551615 |
| `aspect_ratio` | Si défini sur « auto », correspond au rapport hauteur/largeur de votre image d'entrée ; si aucune image n'est fournie, un carré 16:9 est généralement généré. (par défaut : « auto ») | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Résolution de sortie cible. Pour la 2K/4K, l'upscaler natif Gemini est utilisé. | COMBO | Oui | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Détermine le type de contenu renvoyé par le modèle : `IMAGE` renvoie uniquement l'image, `IMAGE+TEXT` renvoie également le texte de raisonnement du modèle. (avancé) | COMBO | Oui | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `thinking_level` | Contrôle la profondeur du processus de raisonnement du modèle. | COMBO | Oui | `"MINIMAL"`<br>`"HIGH"` |
| `images` | Image(s) de référence facultative(s). Pour inclure plusieurs images, utilisez le nœud Batch Images (jusqu'à 14). | IMAGE | Non | Jusqu'à 14 images |
| `files` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | Non | N/A |
| `system_prompt` | Instructions fondamentales qui régissent le comportement d'une IA. (par défaut : instructions intégrées qui exigent que le modèle produise toujours une image) (avancé) | STRING | Non | N/A |

**Remarque :** L'entrée `images` accepte un maximum de 14 images ; en fournir plus provoque une erreur. Lorsque plus de 10 images de référence sont fournies, les 10 premières sont envoyées sous forme d'URL de fichiers et les images restantes sont envoyées sous forme de données intégrées. Le `prompt` ne doit pas être vide après suppression des espaces. Ce nœud est marqué comme obsolète.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image principale générée ou modifiée par le modèle. | IMAGE |
| `string` | Tout contenu textuel renvoyé par le modèle. | STRING |
| `thought_image` | Première image du processus de réflexion du modèle. Disponible uniquement avec thinking_level HIGH et la modalité IMAGE+TEXT. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/fr.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
