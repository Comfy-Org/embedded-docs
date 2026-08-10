# Qwen Image Layered latent vide

Le nœud Empty Qwen Image Layered Latent prépare la toile vierge sur laquelle le modèle Qwen-Image-Layered peint. Imaginez une pile de feuilles de papier calque propres, maintenues dans l'ordre : le modèle remplit la première feuille avec l'image complète, et chaque feuille suivante avec une partie de cette image. Ce nœud décide de la taille et du nombre des feuilles. Il ne dessine rien lui-même.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `largeur` | La largeur de l'image latente à créer. La valeur doit être divisible par 16. (par défaut : 640) | INT | Oui | 16 à MAX_RESOLUTION |
| `hauteur` | La hauteur de l'image latente à créer. La valeur doit être divisible par 16. (par défaut : 640) | INT | Oui | 16 à MAX_RESOLUTION |
| `couches` | En combien de couches diviser l'image. Une feuille supplémentaire est toujours réservée à l'image complète, vous obtenez donc `layers + 1` images, et non `layers`. Réglez-le sur 2 et vous obtenez l'image complète plus 2 couches. Réglez-le sur 0 et vous obtenez uniquement l'image complète. (par défaut : 3) | INT | Oui | 0 à MAX_RESOLUTION |
| `taille_lot` | Le nombre d'échantillons latents à générer dans un lot. (par défaut : 1) | INT | Non | 1 à 4096 |

**Remarque :** Les paramètres `width` et `height` sont divisés en interne par 8 pour déterminer les dimensions spatiales du tenseur latent de sortie.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Un tenseur latent rempli de zéros. Sa forme est `[batch_size, 16, layers + 1, height // 8, width // 8]`. | LATENT |

## Pourquoi vous obtenez une image de plus que demandé

Qwen-Image-Layered ne se contente pas de décomposer une image. Il repeint également l'image complète, sur sa propre feuille, en plus des couches. C'est pourquoi la pile est toujours d'une feuille plus haute que le nombre de couches demandé.

- **La première image est l'image complète, pas une couche.** C'est la même image que vous avez déjà, jetez-la donc lorsque vous ne voulez que les couches.
- **Si vous superposez toutes les couches, vous obtenez à nouveau l'image complète.** Si elles ne correspondent pas à cette première image, la séparation n'a pas fonctionné comme vous le vouliez, c'est donc un moyen rapide de vérifier le résultat.
- **Gardez les feuilles dans l'ordre.** La pile est le seul moyen de savoir quelle couche se trouve au-dessus de laquelle. Rien n'est écrit sur les feuilles pour indiquer où elles vont, donc réorganiser ou supprimer des images signifie réorganiser ou perdre des couches.
- **Les couches sortent avec de la transparence**, elles peuvent donc être empilées sans que les couches inférieures soient masquées par un fond opaque.

## Suggestions d'utilisation

Envoyez la sortie à l'échantillonneur comme vous le feriez avec un latent vide normal, puis placez LatentCutToBatch avec `dim` défini sur `t` avant le décodage VAE. C'est l'étape qui sépare la pile en images individuelles, dans l'ordre, en commençant par l'image complète.

Commencez avec la valeur par défaut de 3 couches. En demander plus signifie une génération plus longue et une séparation plus fine, et cela ne vaut pas la peine d'augmenter tant que vous n'avez pas vu ce que le modèle fait avec un petit nombre.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/fr.md)

---
**Source fingerprint (SHA-256):** `fe97966663c534dd347aa49a908a8026f2c34716631f1d17be97d74eacc3574e`
