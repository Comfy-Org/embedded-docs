# Qwen Image Layered latent vide

Empty Qwen Image Layered Latent prépare la toile vierge sur laquelle le modèle Qwen-Image-Layered va peindre. Considérez-le comme une pile de feuilles de calque propres, maintenues ensemble dans l’ordre : le modèle remplit la première feuille avec l’image complète, puis chaque feuille suivante avec une partie de cette image. Ce nœud détermine la taille des feuilles et leur nombre. Il ne dessine rien lui-même.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de l’image latente à créer. La valeur doit être divisible par 16. (défaut : 640) | INT | Oui | 16 to MAX_RESOLUTION (step 16) |
| `hauteur` | La hauteur de l’image latente à créer. La valeur doit être divisible par 16. (défaut : 640) | INT | Oui | 16 to MAX_RESOLUTION (step 16) |
| `couches` | Combien de couches pour séparer l’image. Une feuille supplémentaire est toujours réservée à l’image complète, vous obtenez donc `layers + 1` images, et non `layers`. Réglez-le sur 2 et vous obtenez l’image complète plus 2 couches. Réglez-le sur 0 et vous obtenez uniquement l’image complète. (défaut : 3) | INT | Oui | 0 to MAX_RESOLUTION (step 1) |
| `taille_lot` | Le nombre d’échantillons latents à générer dans un lot. (défaut : 1) | INT | Oui | 1 à 4096 |

**Remarque :** Les paramètres `width` et `height` sont divisés en interne par 8 pour déterminer les dimensions spatiales du tenseur latent de sortie.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Un tenseur latent rempli de zéros. Sa forme est `[batch_size, 16, layers + 1, height // 8, width // 8]`. | LATENT |

## Pourquoi vous obtenez une image de plus que demandé

Qwen-Image-Layered ne se contente pas de décomposer une image. Il repeint également l’image complète sur sa propre feuille, en plus des couches. C’est pourquoi la pile contient toujours une feuille de plus que le nombre de couches demandé.

- **La première image est l’image complète, et non une couche.** C’est la même image que vous avez déjà, alors jetez-la si vous ne voulez que les couches.
- **Superposez toutes les couches les unes sur les autres et vous retrouvez l’image complète.** Si leur somme ne redonne pas cette première image, la séparation n’a pas fonctionné comme vous le souhaitiez ; c’est donc un moyen rapide de vérifier le résultat.
- **Conservez l’ordre des feuilles.** La pile est la seule trace de l’ordre des couches. Rien n’est inscrit sur les feuilles pour indiquer leur position ; réorganiser ou supprimer des images revient donc à réorganiser ou perdre des couches.
- **Les couches sont produites avec de la transparence**, ce qui permet de les empiler sans que les couches inférieures soient masquées par un arrière-plan opaque.

## Suggestions d’utilisation

Envoyez la sortie à l’échantillonneur comme vous le feriez avec un latent vide normal, puis placez LatentCutToBatch avec `dim` défini sur `t` avant VAE Decode. C’est cette étape qui sépare la pile en images distinctes, dans l’ordre, en commençant par l’image complète.

Commencez avec la valeur par défaut de 3 couches. En demander plus signifie une génération plus longue et une séparation plus fine ; cela ne vaut pas la peine d’augmenter ce nombre avant d’avoir vu ce que le modèle fait avec un petit nombre de couches.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/fr.md)

---
**Source fingerprint (SHA-256):** `5ccac979fcbcefb65f28867a89401c095cb330e09c13270008c32feeeafb1287`
