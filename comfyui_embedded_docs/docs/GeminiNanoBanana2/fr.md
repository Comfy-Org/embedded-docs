# Nano Banana 2

Le nœud GeminiNanoBanana2 génère ou modifie des images à l’aide du modèle Gemini de Google Vertex AI. Il envoie une invite textuelle, accompagnée d’images ou de fichiers de référence facultatifs, à l’API, puis renvoie l’image générée ainsi que tout texte associé. Ce nœud est marqué comme obsolète.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle décrivant l’image à générer ou les modifications à appliquer. Incluez toutes les contraintes, styles ou détails que le modèle doit suivre. Ne peut pas être vide. (par défaut : vide) | STRING | Oui | N/A |
| `modèle` | Le modèle Gemini spécifique à utiliser pour la génération d’images. | COMBO | Oui | "Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `graine` | Lorsque la graine est fixée à une valeur spécifique, le modèle s’efforce de fournir la même réponse pour des requêtes répétées. La sortie déterministe n’est pas garantie. De plus, modifier le modèle ou les réglages des paramètres, comme la température, peut entraîner des variations dans la réponse même si vous utilisez la même valeur de graine. Par défaut, une valeur de graine aléatoire est utilisée. (par défaut : 42) | INT | Oui | 0 à 18446744073709551615 |
| `rapport d’aspect` | Si réglé sur « auto », correspond au rapport hauteur/largeur de votre image d’entrée ; si aucune image n’est fournie, une image au format 16:9 est généralement générée. (par défaut : « auto ») | COMBO | Oui | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `résolution` | Résolution de sortie cible. Pour 2K/4K, l’upscaler natif de Gemini est utilisé. | COMBO | Oui | "1K"<br>"2K"<br>"4K" |
| `modalités de réponse` | Détermine le type de contenu renvoyé par le modèle : « IMAGE » renvoie uniquement une image, « IMAGE+TEXT » renvoie également du texte. (avancé) | COMBO | Oui | "IMAGE"<br>"IMAGE+TEXT" |
| `niveau de réflexion` | Contrôle la profondeur du processus de raisonnement du modèle. | COMBO | Oui | "MINIMAL"<br>"HIGH" |
| `images` | Image(s) de référence facultative(s). Pour inclure plusieurs images, utilisez le nœud Batch Images (jusqu’à 14). | IMAGE | Non | 1 à 14 images |
| `fichiers` | Fichier(s) facultatif(s) à utiliser comme contexte pour le modèle. Accepte les entrées du nœud Gemini Generate Content Input Files. | CUSTOM | Non | N/A |
| `invite système` | Instructions fondamentales qui dictent le comportement d’une IA. (par défaut : une invite prédéfinie qui demande au modèle de toujours produire une image) (avancé) | STRING | Non | N/A |

**Remarque :** L’entrée `images` prend en charge un maximum de 14 images. Si davantage sont fournies, le nœud générera une erreur. L’entrée `prompt` ne doit pas être vide ou composée uniquement d’espaces.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image principale générée ou modifiée par le modèle. | IMAGE |
| `string` | Tout contenu textuel renvoyé par le modèle. | STRING |
| `thought_image` | Première image du processus de réflexion du modèle. Disponible uniquement avec thinking_level HIGH et la modalité IMAGE+TEXT. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/fr.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
