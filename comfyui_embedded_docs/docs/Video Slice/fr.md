> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/fr.md)

Le nœud Video Slice permet d'extraire un segment spécifique d'une vidéo. Vous pouvez définir un temps de début et une durée pour rogner la vidéo, ou simplement ignorer les images du début. Si la durée demandée est plus longue que le reste de la vidéo, le nœud peut soit renvoyer ce qui est disponible, soit générer une erreur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Oui | - | La vidéo d'entrée à découper. |
| `start_time` | FLOAT | Non | -1e5 à 1e5 | Le temps de début en secondes à partir duquel commencer la découpe. Une valeur négative ignorera des images depuis le début de la vidéo. (par défaut : 0.0) |
| `duration` | FLOAT | Non | 0.0 et plus | La longueur de la découpe en secondes. Une valeur de 0.0 signifie que le nœud renverra toute la vidéo du temps de début jusqu'à la fin. (par défaut : 0.0) |
| `strict_duration` | BOOLEAN | Non | - | Si défini sur True, le nœud générera une erreur si la durée demandée ne peut pas être respectée (par exemple, si la découpe dépasse la fin de la vidéo). Si False, il renverra la vidéo disponible jusqu'à la fin. (par défaut : False) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | Le segment vidéo rogné. |