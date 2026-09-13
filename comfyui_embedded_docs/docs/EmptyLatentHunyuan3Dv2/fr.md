# EmptyLatentHunyuan3Dv2

Ce nœud crée un lot d’échantillons latents vides (tous à zéro) formatés pour les modèles de génération 3D Hunyuan3Dv2. Il produit le tenseur latent de forme correcte qui sert de point de départ aux workflows de génération 3D, le latent étant étiqueté avec le type « hunyuan3dv2 ».

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `resolution` | La dimension de résolution de l’espace latent à créer (par défaut : 3072) | INT | Oui | 1 - 8192 |
| `batch_size` | Le nombre d’images latentes dans le lot (par défaut : 1) | INT | Oui | 1 - 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Un tenseur latent vide de forme [batch_size, 64, resolution] contenant des échantillons remplis de zéros, étiqueté avec le type « hunyuan3dv2 » | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/fr.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`
