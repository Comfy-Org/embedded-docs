# VAE Decode (Tiled)

Le nœud VAEDecodeTiled décode des représentations latentes en images en utilisant une approche par tuiles pour gérer efficacement les grandes images. Il traite l’entrée en tuiles plus petites afin de gérer l’utilisation de la mémoire tout en préservant la qualité de l’image. Le nœud prend également en charge les VAE vidéo en traitant les trames temporelles par blocs avec chevauchement pour des transitions fluides.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `samples` | La représentation latente à décoder en images | LATENT | Oui | - |
| `vae` | Le modèle VAE utilisé pour décoder les échantillons latents | VAE | Oui | - |
| `tile_size` | La taille de chaque tuile pour le traitement (défaut : 512) | INT | Oui | 64-4096 (pas : 32) |
| `overlap` | La quantité de chevauchement entre les tuiles adjacentes (défaut : 64) | INT | Oui | 0-4096 (pas : 32) |
| `temporal_size` | Utilisé uniquement pour les VAE vidéo : nombre de trames à décoder à la fois (défaut : 64) | INT | Oui | 8-4096 (pas : 4) |
| `temporal_overlap` | Utilisé uniquement pour les VAE vidéo : nombre de trames à chevaucher (défaut : 8) | INT | Oui | 4-4096 (pas : 4) |

**Remarque :** Le nœud ajuste automatiquement les valeurs de chevauchement si elles dépassent les limites pratiques. Si `tile_size` est inférieur à 4 fois `overlap`, le chevauchement est réduit à un quart de la taille de la tuile. De même, si `temporal_size` est inférieur à deux fois `temporal_overlap`, le chevauchement temporel est divisé par deux. Le nœud prend également en compte les taux de compression internes du VAE lors du calcul des tailles de tuiles et de chevauchement pour les dimensions spatiales et temporelles. Pour les VAE sans compression temporelle (VAE non vidéo), les paramètres `temporal_size` et `temporal_overlap` sont ignorés.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | L’image ou les images décodées générées à partir de la représentation latente. Lors du décodage de latents vidéo, toutes les images décodées sont combinées en une seule liste d’images. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/fr.md)

---
**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`
