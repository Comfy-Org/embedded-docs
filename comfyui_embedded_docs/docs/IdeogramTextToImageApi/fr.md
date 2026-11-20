# Ideogram 4.5 Texte vers image

Générez des images à partir d’une invite textuelle avec Ideogram 4.6 ou 4.5. L’invite accepte également une légende JSON structurée Ideogram, par exemple le `final_prompt` renvoyé par une exécution précédente, ce qui permet un contrôle exact des chaînes de texte, des couleurs et de la mise en page. Le nœud renvoie l’image ainsi que la légende à partir de laquelle l’image a réellement été générée.

## Entrées

La sélection d’un `model` détermine les entrées affichées. Ideogram 4.6 ajoute `background`, le niveau de qualité `very_low`, les tailles `(4K)` ainsi qu’une largeur et une hauteur personnalisées ; 4.5 conserve les préréglages `(1K)` et `(2K)`.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. `"ideogram-4.6"` génère jusqu’à 4K avec un arrière-plan transparent facultatif ; `"ideogram-4.5"` est le modèle précédent (par défaut : `"ideogram-4.6"`). | DYNAMIC_COMBO | Oui | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `prompt` | Invite textuelle, ou une légende JSON structurée Ideogram telle qu’un `final_prompt` précédent (par défaut : chaîne vide). | STRING | Oui | 1 à 10000 caractères |
| `magic_prompt` | Réécrit l’invite en une légende structurée détaillée avant la génération ; `"off"` conserve votre formulation aussi littéralement que possible. La légende est renvoyée sous le nom `final_prompt` (par défaut : `"auto"`). Il s’agit d’un réglage avancé. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `seed` | Graine pour la génération. La génération texte-image n’est pas reproductible à partir de la graine seule, car l’invite est réécrite à chaque exécution ; pour reproduire une image, réutilisez son `final_prompt` avec `magic_prompt` défini sur `"off"`, la même graine et les mêmes réglages de modèle, taille, qualité et arrière-plan (par défaut : 42). | INT | Oui | 0 à 2147483647 |

### Entrées Ideogram 4.6

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | Taille de sortie. `"auto"` laisse le modèle choisir un canevas adapté à l’invite. Un préréglage fixe à la fois la taille en pixels et le rapport d’aspect ; les niveaux `(1K)`, `(2K)` et `(4K)` décrivent le budget en pixels plutôt qu’un grand côté fixe. Sélectionnez `"custom"` pour utiliser la largeur et la hauteur ci-dessous (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(4K) 4096x4096 (1:1)"`<br>`"(4K) 2880x5760 (1:2)"`<br>`"(4K) 5760x2880 (2:1)"`<br>`"(4K) 3328x4992 (2:3)"`<br>`"(4K) 4992x3328 (3:2)"`<br>`"(4K) 3584x4480 (4:5)"`<br>`"(4K) 4480x3584 (5:4)"`<br>`"(4K) 2880x5120 (9:16)"`<br>`"(4K) 5120x2880 (16:9)"`<br>`"(4K) 3200x5120 (5:8)"`<br>`"(4K) 5120x3200 (8:5)"`<br>`"(4K) 3456x4608 (3:4)"`<br>`"(4K) 4608x3456 (4:3)"`<br>`"(4K) 2304x5888 (9:23)"`<br>`"(4K) 5888x2304 (23:9)"`<br>`"(4K) 2496x6656 (3:8)"`<br>`"(4K) 6656x2496 (8:3)"`<br>`"(4K) 2560x6144 (5:12)"`<br>`"(4K) 6144x2560 (12:5)"`<br>`"(4K) 2048x6144 (1:3)"`<br>`"(4K) 6144x2048 (3:1)"`<br>`"custom"` |
| `width` | Largeur de sortie personnalisée en pixels, utilisée uniquement lorsque `size` vaut `"custom"` (par défaut : 2048). | INT | Oui | 256 à 8192 (pas 32) |
| `height` | Hauteur de sortie personnalisée en pixels, utilisée uniquement lorsque `size` vaut `"custom"` (par défaut : 2048). | INT | Oui | 256 à 8192 (pas 32) |
| `quality` | Niveau de qualité. Les niveaux plus élevés coûtent plus cher et prennent plus de temps (par défaut : `"medium"`). | COMBO | Oui | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `background` | `"transparent"` renvoie l’image avec un canal alpha, `"opaque"` force un arrière-plan uni, `"auto"` suit l’invite (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"opaque"`<br>`"transparent"` |

### Entrées Ideogram 4.5

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `size` | Taille de sortie. `"auto"` laisse le modèle choisir un canevas adapté à l’invite ; un préréglage fixe à la fois la taille en pixels et le rapport d’aspect (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1296x3168 (9:22)"`<br>`"(2K) 3168x1296 (22:9)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(1K) 720x1280 (9:16)"`<br>`"(1K) 1280x720 (16:9)"`<br>`"(1K) 720x1440 (1:2)"`<br>`"(1K) 1440x720 (2:1)"` |
| `quality` | Niveau de qualité. Les niveaux plus élevés coûtent plus cher et prennent plus de temps (par défaut : `"medium"`). | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |

### Contraintes des paramètres

- **Invite :** au moins un caractère non blanc et au maximum 10000 caractères. Définissez `magic_prompt` sur `"off"` lorsque vous fournissez votre propre légende JSON.
- **Taille personnalisée (4.6) :** la largeur multipliée par la hauteur ne doit pas dépasser 16,7 MP (4096x4096), chaque côté doit être compris entre 256 et 8192 et aligné sur un multiple de 32, et le côté le plus long ne doit pas dépasser 6 fois le côté le plus court.
- **Qualité `very_low` (4.6) :** limitée à 4 MP (2048x2048) ; les tailles plus grandes déclenchent une erreur.
- **Reproductibilité :** avec `magic_prompt` défini sur `"auto"` ou `"on"`, l’invite est réécrite à chaque exécution, de sorte que la même graine peut produire une image différente.
- **Sécurité du contenu :** si le filtre de sécurité du contenu d’Ideogram bloque la génération, le nœud déclenche une erreur au lieu de renvoyer une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L’image générée sous forme de lot. | IMAGE |
| `final_prompt` | La légende structurée à partir de laquelle l’image a été générée. Renvoyez-la avec `magic_prompt` défini sur `"off"` et les mêmes graine, modèle, taille, qualité et arrière-plan pour reproduire l’image. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramTextToImageApi/fr.md)

---
**Source fingerprint (SHA-256):** `a21f1faed9ca7a7bc63dae74003cc7599f11013075f718af9e5860d2cd666828`
