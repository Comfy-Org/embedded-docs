# Ideogram 4.5 Edit

Modifiez ou combinez jusqu'à 5 images guidées par une invite textuelle avec Ideogram 4.5. L'image 1 est l'image à modifier et les images suivantes sont des références facultatives. L'image entière est rendue à nouveau, donc la taille ou le rapport d'aspect du résultat peut changer ; utilisez plutôt Ideogram 4.5 Precise Edit pour conserver les pixels non modifiés tels quels.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Modèle à utiliser. (valeur par défaut : `"ideogram-4.5"`) | DYNAMIC_COMBO | Oui | `"ideogram-4.5"` |
| `images` | Emplacement extensible : l'image 1 est l'image à modifier et les images 2 à 5 sont des références facultatives (`image_1` ... `image_5`). Faites-y référence dans l'invite sous la forme @Image1, @Image2, ... ; une entrée par lot compte une fois par image. Chaque image doit avoir un rapport d'aspect compris entre 1:6 et 6:1. | IMAGE | Oui | 1 à 5 images |
| `prompt` | Instructions de modification. Prend en charge les références de style @Image1 vers les images connectées. (valeur par défaut : chaîne vide) | STRING | Oui | 1 à 10000 caractères |
| `size` | Taille de sortie. `"auto"` choisit un canevas d'environ 2K à partir des images et de l'invite, `"source"` conserve la taille de l'image 1 (les images dépassant environ 4 MP sont d'abord réduites), et un préréglage avec un rapport d'aspect différent recompose la scène. Sélectionnez `"custom"` pour utiliser la largeur et la hauteur ci-dessous. (valeur par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"source"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"custom"` |
| `width` | Largeur de sortie personnalisée en pixels. Utilisée uniquement lorsque `size` vaut `"custom"`. (valeur par défaut : 2048) | INT | Oui | 256 à 4608 (pas de 32) |
| `height` | Hauteur de sortie personnalisée en pixels. Utilisée uniquement lorsque `size` vaut `"custom"`. (valeur par défaut : 2048) | INT | Oui | 256 à 4608 (pas de 32) |
| `quality` | Niveau de qualité. Les niveaux plus élevés coûtent plus cher et prennent plus de temps. (valeur par défaut : `"medium"`) | COMBO | Oui | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Graine pour la génération. Les mêmes images, invite, réglages et graine donnent le même résultat. (valeur par défaut : 42) | INT | Oui | 0 à 2147483647 |

### Contraintes des paramètres

- **Nombre d'images :** au moins 1 et au plus 5 images ; une entrée par lot compte une fois par image. L'image 1 est l'image à modifier, les autres sont des références.
- **Rapport d'aspect des images :** chaque image ne doit pas être plus large que 6 fois sa hauteur ni plus haute que 6 fois sa largeur (entre 1:6 et 6:1).
- **Balises d'invite :** `@ImageN` est mis en correspondance sans tenir compte de la casse et ne doit pas dépasser le nombre d'images connectées ; l'invite ne doit pas être constituée uniquement d'espaces et ne doit pas dépasser 10000 caractères.
- **Taille personnalisée :** utilisée uniquement lorsque `size` vaut `"custom"`. Le produit de la largeur par la hauteur ne doit pas dépasser 4194304 pixels (2048x2048), et le côté le plus long ne doit pas dépasser 6 fois le côté le plus court. La largeur et la hauteur doivent être comprises entre 256 et 4608 et sont alignées sur des multiples de 32.
- **Mise à l'échelle au téléversement :** les images dépassant environ 4 MP, ou 4608 px sur le côté long, sont réduites avant d'être envoyées.
- **Sécurité du contenu :** si le filtre de sécurité du contenu d'Ideogram bloque le résultat, le nœud lève une erreur au lieu de renvoyer une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | La ou les images modifiées ou combinées sous forme de lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `58c189d65502373ff7b56f5f32d9f2e7ee8019fc58f1bbbb80abc859cf978f67`
