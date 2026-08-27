# Remplacer les images latentes vidéo

ReplaceVideoLatentFrames remplace une plage d'images dans une vidéo latente de destination par des images d'une vidéo latente source, à partir d'un index d'image spécifié. Si aucun latent source n'est fourni, le latent de destination est retourné inchangé. Le nœud prend en charge les index négatifs et journalise un avertissement lorsque les images sources ne tiennent pas dans la destination.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `destination` | Le latent de destination dans lequel les images seront remplacées. | LATENT | Oui | - |
| `source` | Le latent source fournissant les images à insérer dans le latent de destination. S'il n'est pas fourni, le latent de destination est retourné inchangé. | LATENT | Non | - |
| `index` | L'index d'image latent de départ dans le latent de destination où les images du latent source seront placées. Les valeurs négatives comptent à partir de la fin (défaut : 0). | INT | Oui | -MAX_RESOLUTION à MAX_RESOLUTION |

**Contraintes :**

* Un `index` négatif est ajusté en l'ajoutant au nombre d'images de la destination, de sorte qu'il compte en arrière depuis la fin du latent de destination.
* Si `index` pointe au-delà du nombre d'images de la destination, ou si les images sources ne tiennent pas dans la destination à partir de `index`, un avertissement est journalisé et le latent de destination est retourné inchangé.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo latente résultante après l'opération de remplacement d'images. Si le remplacement ne peut pas être effectué, le latent de destination est retourné inchangé. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/fr.md)

---
**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`
