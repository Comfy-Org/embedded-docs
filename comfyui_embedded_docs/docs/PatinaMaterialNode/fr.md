# Patina Material

Génère un matériau PBR complet et carrelable sans raccord à partir d'une description textuelle : une texture de base plus jusqu'à cinq cartes de matériau, avec mise à l'échelle SeedVR optionnelle des cartes. Une image d'entrée peut piloter le résultat comme passe image-to-image, et une image d'entrée avec un masque transforme le traitement en passe d'inpainting. Utilisez-le pour produire des surfaces prêtes pour le jeu ou la 3D sans scanner un matériau réel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description du matériau ou de la texture à générer. | STRING | Oui | Texte multiligne |
| `image_size` | Taille de la texture de sortie. `"custom"` affiche les entrées `width` et `height`. Par défaut : `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Oui | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Génère la carte basecolor (albédo). Par défaut : True. | BOOLEAN | Oui | true<br>false |
| `normal` | Génère la carte de normales. Par défaut : True. | BOOLEAN | Oui | true<br>false |
| `roughness` | Génère la carte de rugosité. Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `metalness` | Génère la carte de métallicité. Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `height` | Génère la carte de hauteur (déplacement). Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `upscale_factor` | Mise à l'échelle SeedVR sans raccord des cartes PBR. La texture de base n'est pas mise à l'échelle, et un facteur 4x transforme une carte de 2048 pixels en une carte 8K. Par défaut : 0 (désactivé). | INT | Oui | 0 à 4 (pas 2) |
| `seed` | Graine pour une génération reproductible. Par défaut : 42. | INT | Oui | 0 à 2147483646 |
| `tiling_mode` | Direction de carrelage : omnidirectionnelle, horizontale ou verticale. Réglage avancé. Par défaut : `"both"`. | COMBO | Oui | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Étapes de débruitage pour la génération de texture. Réglage avancé. Par défaut : 8. | INT | Oui | 1 à 8 |
| `tile_size` | Taille de tuile dans l'espace latent, où 64 signifie 512 pixels et 128 signifie 1024 pixels. Réglage avancé. Par défaut : 128. | INT | Oui | 32 à 256 (pas 2) |
| `tile_stride` | Pas de tuile dans l'espace latent. Réglage avancé. Par défaut : 64. | INT | Oui | 16 à 128 (pas 2) |
| `image` | Image source optionnelle. Seule, elle exécute une passe image-to-image ; avec un masque, elle exécute une passe d'inpainting. | IMAGE | Non | - |
| `mask` | Masque d'inpainting optionnel, nécessite une image d'entrée. Les zones blanches sont régénérées et les zones noires sont conservées. | MASK | Non | - |
| `strength` | Amplitude de transformation de l'image d'entrée. Utilisé uniquement lorsqu'une image est connectée. Réglage avancé. Par défaut : 0.6. | FLOAT | Oui | 0.01 à 1.0 (pas 0.01) |
| `prompt_expansion` | Développe le prompt avec un modèle de langage pour obtenir des détails de texture plus riches. Désactivé par défaut, car l'expansion reformule le prompt comme une photographie et tend à délaver la carte de métallicité. Réglage avancé. | BOOLEAN | Oui | true<br>false |
| `safety_checker` | Exécute la vérification de sécurité du contenu du fournisseur sur la requête. Réglage avancé. Par défaut : False. | BOOLEAN | Oui | true<br>false |

### Entrées de taille d'image personnalisée

Ces entrées apparaissent lorsque `image_size` est défini sur `"custom"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image_size.width` | Largeur de la texture en pixels. Par défaut : 1024. | INT | Oui | 512 à 2048 (pas 16) |
| `image_size.height` | Hauteur de la texture en pixels. Par défaut : 1024. | INT | Oui | 512 à 2048 (pas 16) |

**Contraintes et comportement :**

* Il est permis de n'activer aucune carte de matériau : le nœud ne renvoie alors que la texture de base, et chaque sortie de carte reste un espace réservé de 1x1.
* Un masque nécessite une image d'entrée ; un masque seul déclenche une erreur.
* Un résultat 8K provient d'une mise à l'échelle 4x des cartes d'un rendu de 2048 pixels, et non d'une génération 8K unique.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `texture` | La texture de base du matériau, sans aucune carte appliquée. | IMAGE |
| `basecolor` | La carte basecolor (albédo), ou un espace réservé de 1x1 lorsque cette carte est désactivée. | IMAGE |
| `normal` | La carte de normales, ou un espace réservé de 1x1 lorsque cette carte est désactivée. | IMAGE |
| `roughness` | La carte de rugosité, ou un espace réservé de 1x1 lorsque cette carte est désactivée. | IMAGE |
| `metalness` | La carte de métallicité, ou un espace réservé de 1x1 lorsque cette carte est désactivée. | IMAGE |
| `height` | La carte de hauteur (déplacement), ou un espace réservé de 1x1 lorsque cette carte est désactivée. | IMAGE |
| `expanded_prompt` | Le prompt réellement utilisé par le fournisseur, qui ne diffère de l'entrée que lorsque `prompt_expansion` est activé. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialNode/fr.md)

---
**Source fingerprint (SHA-256):** `4e8305fa56a29dce72c54de12ae05207e8de39a1fea1f4753906c26e8af60383`
