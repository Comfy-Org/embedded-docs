Le nœud GeminiNanoBanana2 génère ou modifie des images à l'aide du modèle Gemini de Google Vertex AI. Il fonctionne en envoyant une invite textuelle, accompagnée d'images ou de fichiers de référence facultatifs, à l'API, puis retourne l'image générée et tout texte d'accompagnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Invite textuelle décrivant l'image à générer ou les modifications à appliquer. Incluez toutes les contraintes, styles ou détails que le modèle doit suivre. | STRING | Oui | N/A |
| `modèle` | Le modèle Gemini spécifique à utiliser pour la génération d'images. | COMBO | Oui | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `graine` | Lorsque la graine est fixée à une valeur spécifique, le modèle fait de son mieux pour fournir la même réponse pour des requêtes répétées. Une sortie déterministe n'est pas garantie. De plus, la modification du modèle ou des paramètres, comme la température, peut entraîner des variations dans la réponse, même en utilisant la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée. (par défaut : 42) | INT | Oui | 0 à 18446744073709551615 |
| `rapport d’aspect` | Si réglé sur 'auto', correspond au rapport hauteur/largeur de votre image d'entrée ; si aucune image n'est fournie, un carré 16:9 est généralement généré. (par défaut : "auto") | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `résolution` | Résolution de sortie cible. Pour 2K/4K, le suréchantillonneur natif Gemini est utilisé. | COMBO | Oui | `"1K"`<br>`"2K"`<br>`"4K"` |
| `modalités de réponse` | Détermine le type de contenu que le modèle retournera. (avancé) | COMBO | Oui | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `niveau de réflexion` | Contrôle la profondeur du processus de raisonnement du modèle. | COMBO | Oui | `"MINIMAL"`<br>`"HIGH"` |
| `images` | Image(s) de référence facultative(s). Pour inclure plusieurs images, utilisez le nœud Batch Images (jusqu'à 14). | IMAGE | Non | N/A |
| `fichiers` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. | CUSTOM | Non | N/A |
| `invite système` | Instructions fondamentales qui dictent le comportement d'une IA. (avancé) | STRING | Non | N/A |

**Remarque :** L'entrée `images` prend en charge un maximum de 14 images. Si plus d'images sont fournies, le nœud générera une erreur.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image principale générée ou modifiée par le modèle. | IMAGE |
| `thought_image` | Tout contenu textuel retourné par le modèle. | STRING |
| `thought_image` | Première image issue du processus de réflexion du modèle. Disponible uniquement avec le niveau de réflexion HIGH et la modalité IMAGE+TEXT. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/fr.md)

---
**Source fingerprint (SHA-256):** `bd53363da73ff0db66a872fc04f1af8ce4dfee1191ca01bd813701b5ad5e4f17`
