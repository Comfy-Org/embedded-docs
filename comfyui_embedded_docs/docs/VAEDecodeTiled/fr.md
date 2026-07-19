# VAE Decode (Tiled)

Le nœud VAEDecodeTiled décode les représentations latentes en images à l'aide d'une approche par tuiles pour traiter efficacement les grandes images. Il traite l'entrée en tuiles plus petites afin de gérer l'utilisation de la mémoire tout en préservant la qualité de l'image. Le nœud prend également en charge les VAE vidéo en traitant les trames temporelles par lots avec chevauchement pour des transitions fluides.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `échantillons` | La représentation latente à décoder en images | LATENT | Oui | - |
| `vae` | Le modèle VAE utilisé pour décoder les échantillons latents | VAE | Oui | - |
| `taille_de_tuile` | La taille de chaque tuile pour le traitement (par défaut : 512) | INT | Oui | 64-4096 (pas : 32) |
| `chevauchement` | Le chevauchement entre les tuiles adjacentes (par défaut : 64) | INT | Oui | 0-4096 (pas : 32) |
| `taille_temporelle` | Utilisé uniquement pour les VAE vidéo : nombre de trames à décoder à la fois (par défaut : 64) | INT | Oui | 8-4096 (pas : 4) |
| `chevauchement_temporel` | Utilisé uniquement pour les VAE vidéo : nombre de trames à chevaucher (par défaut : 8) | INT | Oui | 4-4096 (pas : 4) |

**Remarque :** Le nœud ajuste automatiquement les valeurs de chevauchement si elles dépassent les limites pratiques. Si `tile_size` est inférieur à 4 fois `overlap`, le chevauchement est réduit à un quart de la taille de la tuile. De même, si `temporal_size` est inférieur à deux fois `temporal_overlap`, le chevauchement temporel est réduit de moitié. Le nœud prend également en compte les taux de compression internes du VAE lors du calcul des tailles de tuiles et de chevauchement pour les dimensions spatiales et temporelles.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | L'image ou les images décodées générées à partir de la représentation latente | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/fr.md)

---
**Source fingerprint (SHA-256):** `193d5cb219d66855ae581d3e4488b7b6ae3a45b735fb0f9f784fea1f5d466e46`
