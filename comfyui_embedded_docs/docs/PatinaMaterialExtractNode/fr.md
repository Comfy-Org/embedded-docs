# Patina Material Extract

Extrait un matériau PBR à raccord sans couture depuis une région d’une image d’entrée, guidé par un prompt qui nomme ce qu’il faut prélever : un mur, un sol, un tissu. Il renvoie la texture de base extraite ainsi que jusqu’à cinq cartes de matériau, avec un agrandissement SeedVR facultatif des cartes. Utilisez-le pour transformer la photo d’une surface réelle en un matériau réutilisable et raccordable.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image à partir de laquelle extraire une texture. | IMAGE | Oui | - |
| `prompt` | Description de la texture à extraire de l’image, par exemple `"the wall"`. | STRING | Oui | Texte multiligne |
| `image_size` | Taille de la texture de sortie. `"custom"` révèle les entrées `width` et `height`. Par défaut : `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Oui | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Générer la carte basecolor (albédo). Par défaut : True. | BOOLEAN | Oui | true<br>false |
| `normal` | Générer la carte de normales. Par défaut : True. | BOOLEAN | Oui | true<br>false |
| `roughness` | Générer la carte de rugosité. Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `metalness` | Générer la carte de métallicité. Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `height` | Générer la carte de hauteur (déplacement). Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `upscale_factor` | Agrandissement SeedVR sans couture des cartes PBR. La texture de base n’est pas agrandie, et un facteur 4x transforme une carte de 2048 pixels en une carte 8K. Par défaut : 0 (désactivé). | INT | Oui | 0 à 4 (pas de 2) |
| `seed` | Graine pour une génération reproductible. Par défaut : 42. | INT | Oui | 0 à 2147483646 |
| `strength` | Niveau de transformation de l’image d’entrée. Paramètre avancé. Par défaut : 0.6. | FLOAT | Oui | 0.01 à 1.0 (pas de 0.01) |
| `tiling_mode` | Direction de répétition : omnidirectionnelle, horizontale ou verticale. Paramètre avancé. Par défaut : `"both"`. | COMBO | Oui | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Étapes de débruitage pour la génération de texture. Paramètre avancé. Par défaut : 8. | INT | Oui | 1 à 8 |
| `tile_size` | Taille des tuiles dans l’espace latent, où 64 correspond à 512 pixels et 128 à 1024 pixels. Paramètre avancé. Par défaut : 128. | INT | Oui | 32 à 256 (pas de 2) |
| `tile_stride` | Pas de progression des tuiles dans l’espace latent. Paramètre avancé. Par défaut : 64. | INT | Oui | 16 à 128 (pas de 2) |
| `prompt_expansion` | Développer le prompt avec un modèle de langage pour obtenir des détails de texture plus riches. Désactivé par défaut, car l’expansion reformule le prompt comme une photographie et tend à écraser la carte de métallicité. Paramètre avancé. | BOOLEAN | Oui | true<br>false |
| `safety_checker` | Exécuter le contrôle de sécurité du contenu du fournisseur sur la requête. Paramètre avancé. Par défaut : False. | BOOLEAN | Oui | true<br>false |

### Entrées de taille d’image personnalisée

Ces entrées apparaissent lorsque `image_size` est défini sur `"custom"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image_size.width` | Largeur de la texture en pixels. Par défaut : 1024. | INT | Oui | 512 à 2048 (pas de 16) |
| `image_size.height` | Hauteur de la texture en pixels. Par défaut : 1024. | INT | Oui | 512 à 2048 (pas de 16) |

**Contraintes et comportement :**

* Au moins une carte de matériau doit être activée, sinon l’exécution échoue.
* Le prompt est obligatoire et ne doit pas être vide ; nommez la région à extraire aussi précisément que possible.
* Un résultat 8K provient d’un agrandissement 4x des cartes d’un rendu de 2048 pixels, et non d’une génération 8K unique.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `texture` | La texture de base extraite, sans aucune carte appliquée. | IMAGE |
| `basecolor` | La carte basecolor (albédo), ou un espace réservé 1x1 lorsque cette carte est désactivée. | IMAGE |
| `normal` | La carte de normales, ou un espace réservé 1x1 lorsque cette carte est désactivée. | IMAGE |
| `roughness` | La carte de rugosité, ou un espace réservé 1x1 lorsque cette carte est désactivée. | IMAGE |
| `metalness` | La carte de métallicité, ou un espace réservé 1x1 lorsque cette carte est désactivée. | IMAGE |
| `height` | La carte de hauteur (déplacement), ou un espace réservé 1x1 lorsque cette carte est désactivée. | IMAGE |
| `expanded_prompt` | Le prompt que le fournisseur a réellement utilisé, qui diffère de l’entrée uniquement lorsque `prompt_expansion` est activé. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialExtractNode/fr.md)

---
**Source fingerprint (SHA-256):** `484b8eaa57388541e352cd88c8998c63aa0b2a99d98cd8e602252625064f16ba`
