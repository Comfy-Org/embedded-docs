# HappyHorse Image vers Vidéo

Ce nœud génère une courte vidéo à partir d’une image de départ unique en utilisant le modèle HappyHorse. Vous fournissez une image initiale et un prompt textuel décrivant le mouvement et la scène souhaités, puis le nœud crée une vidéo qui se poursuit à partir de cette image.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle HappyHorse à utiliser pour la génération vidéo. | DYNAMIC_COMBO | Oui | `"happyhorse-1.1-i2v"`<br>`"happyhorse-1.0-i2v"` |
| `first_frame` | Image du premier frame. Le rapport hauteur/largeur de la sortie est dérivé de cette image. | IMAGE | Oui | 300×300 px min ; 1:2.5 à 2.5:1 |
| `seed` | Graine à utiliser pour la génération. (défaut : 0) | INT | Oui | 0 à 2147483647 |
| `watermark` | Indique s’il faut ajouter un filigrane généré par IA au résultat. (option avancée ; défaut : False) | BOOLEAN | Oui | True / False |

### happyhorse-1.1-i2v and happyhorse-1.0-i2v Entrées

Les deux versions du modèle partagent le même ensemble de paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt décrivant les éléments et les caractéristiques visuelles. Prend en charge l’anglais et le chinois. (défaut : "") | STRING | Non | N/A |
| `resolution` | La résolution de la vidéo de sortie. (défaut : `"720P"`) | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `duration` | La durée de la vidéo générée en secondes. (défaut : 5) | INT | Oui | 3 à 15 |

Remarque : l’image `first_frame` doit faire au moins 300 × 300 pixels, et son rapport hauteur/largeur doit être compris entre 1:2.5 et 2.5:1.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `4bf6eece0d1b4104ce2d84e29b2c918a0a6ba782da1dd801b66cbfa1666d150b`
