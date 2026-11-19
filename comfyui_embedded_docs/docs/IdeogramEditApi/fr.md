# Ideogram 4.5 Modifier

Éditez ou combinez jusqu'à 5 images guidées par un prompt texte avec Ideogram 4.6 ou 4.5. L'image 1 est l'image à éditer et les images suivantes sont des références facultatives. L'image entière est rendue à nouveau, de sorte que la taille ou le rapport d'aspect du résultat peut changer ; utilisez Ideogram Precise Edit pour conserver les pixels non modifiés intacts.

## Entrées

Le choix d'un `model` détermine les entrées qui apparaissent. Ideogram 4.6 ajoute `background`, les tailles `(4K)` et des tailles personnalisées jusqu'à 8192 pixels par côté ; 4.5 conserve les préréglages `(1K)` et `(2K)` avec au plus 4608 pixels par côté.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. `"ideogram-4.6"` effectue le rendu jusqu'à 4K avec un arrière-plan transparent facultatif ; `"ideogram-4.5"` est le modèle antérieur (par défaut : `"ideogram-4.6"`). | DYNAMIC_COMBO | Oui | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Emplacement extensible : l'image 1 est l'image à éditer et les images 2 à 5 sont des références facultatives (`image_1` ... `image_5`). Faites-y référence dans le prompt sous la forme @Image1, @Image2, ... ; une entrée par lot compte une fois par image. Chaque image doit avoir un rapport d'aspect compris entre 1:6 et 6:1. | IMAGE | Oui | 1 à 5 images |
| `prompt` | Instructions d'édition. Prend en charge les références de style @Image1 vers les images connectées (par défaut : chaîne vide). | STRING | Oui | 1 à 10000 caractères |
| `seed` | Graine pour la génération. Les mêmes images, prompt, paramètres et graine donnent un résultat identique ou très similaire (par défaut : 42). | INT | Oui | 0 à 2147483647 |

### Entrées Ideogram 4.6

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | Taille de sortie. `"auto"` choisit un canevas d'environ 2K à partir des images et du prompt, `"source"` conserve la taille de l'image 1 (les images dépassant 16,7 MP ou 8192 pixels par côté sont d'abord réduites), et un préréglage avec un rapport d'aspect différent recompose la scène. Sélectionnez `"custom"` pour utiliser la largeur et la hauteur ci-dessous (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"source"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(4K) 4096x4096 (1:1)"`<br>`"(4K) 2880x5760 (1:2)"`<br>`"(4K) 5760x2880 (2:1)"`<br>`"(4K) 3328x4992 (2:3)"`<br>`"(4K) 4992x3328 (3:2)"`<br>`"(4K) 3584x4480 (4:5)"`<br>`"(4K) 4480x3584 (5:4)"`<br>`"(4K) 2880x5120 (9:16)"`<br>`"(4K) 5120x2880 (16:9)"`<br>`"(4K) 3200x5120 (5:8)"`<br>`"(4K) 5120x3200 (8:5)"`<br>`"(4K) 3456x4608 (3:4)"`<br>`"(4K) 4608x3456 (4:3)"`<br>`"(4K) 2304x5888 (9:23)"`<br>`"(4K) 5888x2304 (23:9)"`<br>`"(4K) 2496x6656 (3:8)"`<br>`"(4K) 6656x2496 (8:3)"`<br>`"(4K) 2560x6144 (5:12)"`<br>`"(4K) 6144x2560 (12:5)"`<br>`"(4K) 2048x6144 (1:3)"`<br>`"(4K) 6144x2048 (3:1)"`<br>`"custom"` |
| `width` | Largeur de sortie personnalisée en pixels, utilisée uniquement lorsque `size` vaut `"custom"` (par défaut : 2048). | INT | Oui | 256 à 8192 (pas : 32) |
| `height` | Hauteur de sortie personnalisée en pixels, utilisée uniquement lorsque `size` vaut `"custom"` (par défaut : 2048). | INT | Oui | 256 à 8192 (pas : 32) |
| `quality` | Niveau de qualité. Les niveaux plus élevés coûtent plus cher et prennent plus de temps (par défaut : `"medium"`). | COMBO | Oui | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `background` | `"transparent"` renvoie l'image avec un canal alpha, `"opaque"` force un arrière-plan uni, `"auto"` suit le prompt (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"opaque"`<br>`"transparent"` |

### Entrées Ideogram 4.5

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | Taille de sortie. `"auto"` choisit un canevas d'environ 2K à partir des images et du prompt, `"source"` conserve la taille de l'image 1 (les images dépassant environ 4 MP sont d'abord réduites), et un préréglage avec un rapport d'aspect différent recompose la scène. Sélectionnez `"custom"` pour utiliser la largeur et la hauteur ci-dessous (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"source"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"custom"` |
| `width` | Largeur de sortie personnalisée en pixels, utilisée uniquement lorsque `size` vaut `"custom"` (par défaut : 2048). | INT | Oui | 256 à 4608 (pas : 32) |
| `height` | Hauteur de sortie personnalisée en pixels, utilisée uniquement lorsque `size` vaut `"custom"` (par défaut : 2048). | INT | Oui | 256 à 4608 (pas : 32) |
| `quality` | Niveau de qualité. Les niveaux plus élevés coûtent plus cher et prennent plus de temps (par défaut : `"medium"`). | COMBO | Oui | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Contraintes des paramètres

- **Nombre d'images :** au moins 1 et au plus 5 images ; une entrée par lot compte une fois par image. L'image 1 est l'image à éditer, les autres sont des références.
- **Rapport d'aspect des images :** chaque image ne doit pas être plus large que 6 fois sa hauteur ni plus haute que 6 fois sa largeur (entre 1:6 et 6:1).
- **Balises du prompt :** `@ImageN` est mis en correspondance sans tenir compte de la casse et ne doit pas dépasser le nombre d'images connectées ; le prompt ne doit pas être composé uniquement d'espaces et doit comporter au maximum 10000 caractères.
- **Taille personnalisée :** la largeur multipliée par la hauteur ne doit pas dépasser 16,7 MP (4096x4096) sur 4.6 et 4194304 pixels (2048x2048) sur 4.5, et le côté le plus long ne doit pas dépasser 6 fois le côté le plus court. La largeur et la hauteur sont alignées sur des multiples de 32.
- **Mise à l'échelle à l'envoi :** 4.6 envoie l'image 1 jusqu'à 16,7 MP et 8192 pixels par côté, en la réencodant en JPEG lorsque cela permet de la maintenir sous la limite d'envoi ; 4.5 réduit l'image 1 au-delà d'environ 4 MP ou 4608 pixels par côté.
- **Sécurité du contenu :** si le filtre de sécurité du contenu d'Ideogram bloque le résultat, le nœud lève une erreur au lieu de renvoyer une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image éditée ou combinée, sous forme de lot. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `58c189d65502373ff7b56f5f32d9f2e7ee8019fc58f1bbbb80abc859cf978f67`
