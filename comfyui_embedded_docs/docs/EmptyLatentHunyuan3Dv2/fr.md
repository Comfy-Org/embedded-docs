# EmptyLatentHunyuan3Dv2

Le nœud EmptyLatentHunyuan3Dv2 crée des tenseurs latents vierges spécialement formatés pour les modèles de génération 3D Hunyuan3Dv2. Il génère des espaces latents vides avec les dimensions et la structure correctes requises par l'architecture Hunyuan3Dv2, vous permettant de démarrer des flux de travail de génération 3D à partir de zéro. Le nœud produit des tenseurs latents remplis de zéros qui servent de base aux processus ultérieurs de génération 3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `resolution` | La dimension de résolution de l'espace latent (par défaut : 3072) | INT | Oui | 1 - 8192 |
| `batch_size` | Le nombre d'images latentes dans le lot (par défaut : 1) | INT | Oui | 1 - 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Renvoie un tenseur latent contenant des échantillons vides formatés pour la génération 3D Hunyuan3Dv2 | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/fr.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`
