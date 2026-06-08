Voici la traduction en français de la documentation du nœud ReplaceVideoLatentFrames :

Le nœud ReplaceVideoLatentFrames insère des images d'un latent vidéo source dans un latent vidéo de destination, à partir d'un index d'image spécifié. Si le latent source n'est pas fourni, le latent de destination est retourné inchangé. Le nœud gère l'indexation négative et émet un avertissement si les images sources ne tiennent pas dans la destination.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `destination` | Le latent de destination dans lequel les images seront remplacées. | LATENT | Oui | - |
| `source` | Le latent source fournissant les images à insérer dans le latent de destination. S'il n'est pas fourni, le latent de destination est retourné inchangé. | LATENT | Non | - |
| `index` | L'index de l'image latente de départ dans le latent de destination où les images du latent source seront placées. Les valeurs négatives comptent à partir de la fin (par défaut : 0). | INT | Oui | -MAX_RESOLUTION à MAX_RESOLUTION |

**Contraintes :**

* L'`index` doit se situer dans les limites du nombre d'images du latent de destination. Si ce n'est pas le cas, un avertissement est enregistré et la destination est retournée inchangée.
* Les images du latent source doivent tenir dans les images du latent de destination à partir de l'`index` spécifié. Si ce n'est pas le cas, un avertissement est enregistré et la destination est retournée inchangée.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le latent vidéo résultant après l'opération de remplacement d'images. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/fr.md)

---
**Source fingerprint (SHA-256):** `b4e2b3dcdaa5c400fefc30262ae05cd1849896e6cb6bbb3a1bd6ce4d31583e23`
