# Ideogram 4.5 Modification précise

Modifiez une image guidée par un prompt texte avec l'édition précise d'Ideogram 4.6 ou 4.5 : seul ce que le prompt demande est modifié, les pixels non touchés restent identiques et la sortie conserve la taille de l'image 1. Une modification de l'image entière sur 4.6 renvoie une image plus petite lorsque la source dépasse 16.7 MP ou 8192 pixels par côté, car elle est réduite avant l'envoi. L'image 1 est l'image à modifier et jusqu'à 4 images supplémentaires peuvent être connectées comme références. Une seule région de l'image 1 peut également être modifiée isolément, sélectionnée par un masque ou par des boîtes englobantes, ce qui renvoie l'image en taille réelle.

## Entrées

La sélection d'un `model` détermine les entrées qui apparaissent. Les deux modèles modifient une région via `context_window`, mais 4.6 prend son masque sur `mask` tandis que 4.5 le prend sur `context_window_mask`, et 4.6 utilise `"auto"` par défaut au lieu de `"none"`.

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser. `"ideogram-4.6"` gère des sources plus grandes et des régions plus larges ; `"ideogram-4.5"` est le modèle antérieur (par défaut : `"ideogram-4.6"`). | DYNAMIC_COMBO | Oui | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Emplacement extensible : l'image 1 est l'image à modifier et les images 2 à 5 sont des références facultatives (`image_1` ... `image_5`). Référez-vous à elles dans le prompt sous la forme @Image1, @Image2, ... ; une entrée par lot compte une fois par image. Chaque image doit avoir un rapport d'aspect compris entre 1:6 et 6:1, sauf que le rapport d'aspect de l'image 1 n'est pas vérifié lorsqu'une fenêtre de contexte est utilisée. | IMAGE | Oui | 1 à 5 images |
| `prompt` | Instructions de modification. Prend en charge les références de style @Image1 vers les images connectées (par défaut : chaîne vide). | STRING | Oui | 1 à 10000 caractères |
| `quality` | Niveau de qualité. Les niveaux plus élevés coûtent plus cher et prennent plus de temps (par défaut : `"medium"`). | COMBO | Oui | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Graine pour la génération. Les mêmes images, le même prompt, les mêmes réglages et la même graine donnent un résultat identique ou très similaire (par défaut : 42). | INT | Oui | 0 à 2147483647 |

### Entrées Ideogram 4.6

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `context_window` | Région de l'image 1 à modifier. `"auto"` modifie la région autour du masque et conserve l'image 1 en taille réelle, ou l'image entière lorsqu'aucun masque n'est connecté ; `"none"` modifie l'image entière ; `"custom"` modifie la région issue de `context_window_bboxes` et conserve l'image 1 en taille réelle (par défaut : `"auto"`). | COMBO | Non | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Région de l'image 1 à modifier, par exemple la sortie de Create Bounding Boxes. Requis lorsque `context_window` vaut `"custom"` ; non utilisé sinon. Plusieurs boîtes sont fusionnées en une seule région, qui est agrandie pour faire au moins 256 pixels par côté et présenter un rapport d'aspect de 6:1. La région peut atteindre 8192 pixels par côté et environ 16.7 MP (p. ex. 4096x4096). | BOUNDING_BOX | Non | - |
| `mask` | Le blanc indique la zone à modifier ; la région à modifier est placée autour. Le masque doit contenir à la fois des zones blanches (à modifier) et noires (à conserver). Il est envoyé dès qu'il est connecté, dans tous les modes `context_window`, et il fait passer la limite d'images à 4 (voir les contraintes ci-dessous). | MASK | Non | - |

### Entrées Ideogram 4.5

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `context_window` | Région de l'image 1 à modifier. `"none"` modifie l'image entière. `"auto"` modifie une région autour de `context_window_mask` et `"custom"` la région issue de `context_window_bboxes` ; les deux conservent l'image 1 en taille réelle et laissent le reste de l'image inchangé (par défaut : `"none"`). | COMBO | Non | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Région de l'image 1 à modifier, par exemple la sortie de Create Bounding Boxes. Requis lorsque `context_window` vaut `"custom"` ; non utilisé sinon. La région peut atteindre 4608 pixels par côté et environ 4 MP (p. ex. 2048x2048). | BOUNDING_BOX | Non | - |
| `context_window_mask` | Le blanc indique la zone à modifier ; la région à modifier est placée autour. Requis lorsque `context_window` vaut `"auto"` ; non utilisé sinon. Le masque doit contenir à la fois des zones blanches (à modifier) et noires (à conserver). | MASK | Non | - |

### Contraintes des paramètres

- **Nombre d'images :** au moins 1 et au plus 5 images ; une entrée par lot compte une fois par image. Dès qu'un masque est connecté, au plus 4 images sont acceptées, soit l'image 1 et 3 références.
- **Taille de sortie :** le nœud n'a pas d'entrées de taille, de largeur ou de hauteur. Une modification de région renvoie l'image complète à la taille de l'image 1. Une modification de l'image entière renvoie la taille de l'image 1 telle qu'envoyée : sur 4.6, une image dépassant 16.7 MP ou 8192 pixels par côté est d'abord réduite, et sur 4.5, la même chose se produit au-delà d'environ 4 MP ou 4608 pixels par côté.
- **Taille de la source de la région :** lorsqu'une fenêtre de contexte est utilisée, l'image 1 peut atteindre 8192x8192 pixels (environ 67 MP) ; les sources plus grandes déclenchent une erreur.
- **Limites de région :** une région issue de `context_window_bboxes` peut atteindre 8192 pixels par côté et environ 16.7 MP sur 4.6, et jusqu'à 4608 pixels par côté et environ 4 MP sur 4.5. Les boîtes entièrement situées hors de l'image 1 déclenchent une erreur.
- **Balises de prompt :** `@ImageN` est comparé sans tenir compte de la casse et ne doit pas dépasser le nombre d'images connectées ; le prompt doit contenir au moins un caractère autre qu'un espace et au plus 10000 caractères.
- **Limite d'envoi :** l'image 1, le masque et les références doivent ensemble respecter la limite d'envoi de 50 MB d'Ideogram ; l'image 1 est réencodée en JPEG si nécessaire et le nœud déclenche une erreur si elle ne passe toujours pas dans la limite.
- **Sécurité du contenu :** si le filtre de sécurité du contenu d'Ideogram bloque le résultat, le nœud déclenche une erreur au lieu de renvoyer une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image modifiée sous forme de lot, à la taille de l'image 1. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
