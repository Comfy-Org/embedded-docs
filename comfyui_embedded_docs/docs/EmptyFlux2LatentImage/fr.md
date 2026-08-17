# Flux vide vers latent

Le nœud EmptyFlux2LatentImage crée une représentation latente vide et vierge. Il génère un tenseur rempli de zéros, qui sert de point de départ au processus de débruitage du modèle Flux. Les dimensions du latent sont déterminées par la largeur et la hauteur d'entrée, réduites d'un facteur 16.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `width` | La largeur de l'image finale à générer. La largeur du latent sera cette valeur divisée par 16. La valeur par défaut est 1024. | INT | Oui | 16 à 16384 |
| `height` | La hauteur de l'image finale à générer. La hauteur du latent sera cette valeur divisée par 16. La valeur par défaut est 1024. | INT | Oui | 16 à 16384 |
| `batch_size` | Le nombre d'échantillons latents à générer dans un seul lot. La valeur par défaut est 1. | INT | Non | 1 à 4096 |

**Remarque :** Les entrées `width` et `height` doivent être divisibles par 16, car le nœud les divise en interne par ce facteur pour créer les dimensions du latent.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Un tenseur latent rempli de zéros. La forme est `[batch_size, 128, height // 16, width // 16]`. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/fr.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`
