# Remplacer les images latentes vidéo

Le nœud ReplaceVideoLatentFrames insère les images d'une vidéo latente source dans une vidéo latente de destination, à partir d'un index d'image spécifié. Si le latent source n'est pas fourni, le latent de destination est renvoyé inchangé. Le nœud gère l'indexation négative et émet un avertissement si les images source ne tiennent pas dans la destination.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `destination` | Le latent de destination dans lequel les images seront remplacées. | LATENT | Oui | - |
| `source` | Le latent source fournissant les images à insérer dans le latent de destination. S'il n'est pas fourni, le latent de destination est renvoyé inchangé. | LATENT | Non | - |
| `index` | L'index de l'image latente de départ dans le latent de destination où les images du latent source seront placées. Les valeurs négatives comptent à partir de la fin (par défaut : 0). | INT | Oui | -MAX_RESOLUTION to MAX_RESOLUTION (step: 1) |

**Contraintes :**

* L'`index` doit être compris dans les limites du nombre d'images du latent de destination. Sinon, un avertissement est consigné et le latent de destination est renvoyé inchangé.
* Les images du latent source doivent tenir dans les images du latent de destination à partir de l'`index` spécifié. Si ce n'est pas le cas, un avertissement est consigné et le latent de destination est renvoyé inchangé.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo latente résultante après l'opération de remplacement d'images. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/fr.md)

---
**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`
