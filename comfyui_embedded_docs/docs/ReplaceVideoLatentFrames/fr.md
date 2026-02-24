> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/fr.md)

## Vue d'ensemble

Le nœud ReplaceVideoLatentFrames insère des trames d'une vidéo latente source dans une vidéo latente de destination, à partir d'un index de trame spécifié. Si la source latente n'est pas fournie, la destination latente est renvoyée inchangée. Le nœud gère l'indexation négative et émettra un avertissement si les trames source ne rentrent pas dans la destination.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `destination` | LATENT | Oui | - | La destination latente dans laquelle les trames seront remplacées. |
| `source` | LATENT | Non | - | La source latente fournissant les trames à insérer dans la destination latente. Si non fournie, la destination latente est renvoyée inchangée. |
| `index` | INT | Non | -MAX_RESOLUTION à MAX_RESOLUTION | L'index de la trame latente de départ dans la destination latente où les trames de la source latente seront placées. Les valeurs négatives comptent à partir de la fin (par défaut : 0). |

**Contraintes :**

* L'`index` doit être dans les limites du nombre de trames de la destination latente. Si ce n'est pas le cas, un avertissement est enregistré et la destination est renvoyée inchangée.
* Les trames de la source latente doivent pouvoir tenir dans les trames de la destination latente à partir de l'`index` spécifié. Si ce n'est pas le cas, un avertissement est enregistré et la destination est renvoyée inchangée.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | LATENT | La vidéo latente résultante après l'opération de remplacement de trames. |
