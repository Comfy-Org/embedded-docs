# Ideogram 4.5 Modification précise

Permet de modifier une image guidée par un prompt textuel avec l’édition précise d’Ideogram 4.6 ou 4.5 : seul ce que demande le prompt est modifié. Une édition de région conserve l’image 1 à sa taille et à sa résolution exactes. Une édition de l’image entière redimensionne l’image 1 à la baisse avant le téléversement lorsqu’elle dépasse la limite du modèle, de sorte que le résultat peut être plus petit que l’entrée : 16,7 MP ou 8192 pixels par côté sur 4.6, environ 4 MP ou 4608 pixels par côté sur 4.5. L’image 1 est l’image à modifier et jusqu’à 4 images supplémentaires peuvent être connectées comme références. Une seule région de l’image 1 peut également être modifiée isolément, sélectionnée par un masque ou par des boîtes englobantes, ce qui renvoie l’image à sa taille complète.

## Entrées

La sélection d’un `model` détermine les entrées qui apparaissent. Les deux modèles modifient une région via `context_window`, mais 4.6 prend son masque sur `mask` tandis que 4.5 le prend sur `context_window_mask`, et 4.6 utilise `"auto"` par défaut au lieu de `"none"`.

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Modèle à utiliser. `"ideogram-4.6"` gère des sources plus grandes et des régions plus larges ; `"ideogram-4.5"` est le modèle antérieur (par défaut : `"ideogram-4.6"`). | DYNAMIC_COMBO | Oui | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Emplacement extensible : l’image 1 est l’image à modifier et les images 2 à 5 sont des références facultatives (`image_1` ... `image_5`). Faites-y référence dans le prompt sous la forme @Image1, @Image2, ... ; une entrée par lots compte une fois par image. Chaque image doit avoir un rapport d’aspect compris entre 1:6 et 6:1, sauf que l’image 1 n’est pas soumise au contrôle du rapport d’aspect lorsqu’une fenêtre de contexte est utilisée. | IMAGE | Oui | 1 à 5 images |
| `prompt` | Instructions de modification. Prend en charge les références de style @Image1 aux images connectées (par défaut : chaîne vide). | STRING | Oui | 1 à 10000 caractères |
| `quality` | Niveau de qualité. Les niveaux plus élevés coûtent plus cher et prennent plus de temps (par défaut : `"medium"`). | COMBO | Oui | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Graine de génération. Sur 4.6, les mêmes images, prompt, réglages et graine donnent le même résultat ou un résultat très similaire ; sur 4.5, ils donnent le même résultat (par défaut : 42). | INT | Oui | 0 à 2147483647 |

### Entrées Ideogram 4.6

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `context_window` | Région de l’image 1 à modifier. `"auto"` modifie la région autour du masque et conserve l’image 1 à sa taille complète, ou l’image entière lorsqu’aucun masque n’est connecté ; `"none"` modifie l’image entière ; `"custom"` modifie la région à partir de `context_window_bboxes` et conserve l’image 1 à sa taille complète (par défaut : `"auto"`). Un `mask` connecté est envoyé dans les trois modes, y compris `"none"`. | COMBO | Non | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Région de l’image 1 à modifier, par exemple la sortie de Create Bounding Boxes. Obligatoire lorsque `context_window` vaut `"custom"` ; non utilisé sinon. Plusieurs boîtes sont fusionnées en une seule région, qui est agrandie jusqu’à au moins 256 pixels par côté et étendue davantage uniquement si nécessaire pour rester dans le rapport d’aspect maximal de 6:1. La région peut atteindre 8192 pixels par côté et environ 16,7 MP (par ex. 4096x4096) ; l’aire est vérifiée après l’arrondi supérieur de chaque côté à un multiple de 32, de sorte qu’une région de 4097x4095 est rejetée même si son aire brute est inférieure à 16,7 MP. | BOUNDING_BOX | Non | - |
| `mask` | Le blanc indique ce qu’il faut modifier ; la région d’édition est placée autour. Le masque doit contenir à la fois des zones blanches (modifier) et noires (conserver). Il est envoyé dès qu’il est connecté, dans chaque mode `context_window`, et il abaisse la limite d’images à 4 (voir les contraintes ci-dessous). | MASK | Non | - |

### Entrées Ideogram 4.5

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `context_window` | Région de l’image 1 à modifier. `"none"` modifie l’image entière. `"auto"` modifie une région autour de `context_window_mask` et `"custom"` la région issue de `context_window_bboxes` ; les deux conservent l’image 1 à sa taille complète et laissent le reste de l’image inchangé (par défaut : `"none"`). | COMBO | Non | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Région de l’image 1 à modifier, par exemple la sortie de Create Bounding Boxes. Obligatoire lorsque `context_window` vaut `"custom"` ; non utilisé sinon. Plusieurs boîtes sont fusionnées en une seule région, qui est agrandie jusqu’à au moins 256 pixels par côté et étendue davantage uniquement si nécessaire pour rester dans le rapport d’aspect maximal de 6:1, de sorte qu’une petite boîte comme 32x32 modifie aussi les pixels qui l’entourent. La région peut atteindre 4608 pixels par côté et environ 4 MP (par ex. 2048x2048), vérifiée après l’arrondi supérieur de chaque côté à un multiple de 32. | BOUNDING_BOX | Non | - |
| `context_window_mask` | Le blanc indique ce qu’il faut modifier ; la région d’édition est placée autour. Obligatoire lorsque `context_window` vaut `"auto"` ; non utilisé sinon. Le masque doit contenir à la fois des zones blanches (modifier) et noires (conserver). | MASK | Non | - |

### Contraintes des paramètres

- **Nombre d’images :** au moins 1 et au plus 5 images ; une entrée par lots compte une fois par image. Lorsque le nœud utilise un masque, au plus 4 images sont acceptées, soit l’image 1 et 3 références. Sur 4.6, un `mask` connecté est utilisé dans chaque mode ; sur 4.5, le masque est `context_window_mask` et n’est utilisé que dans `"auto"`, donc `"none"` et `"custom"` acceptent encore 5 images avec un masque connecté.
- **Taille de sortie :** le nœud ne comporte pas d’entrées de taille, de largeur ou de hauteur. Une édition de région renvoie l’image complète à la taille de l’image 1. Une édition de l’image entière renvoie la taille de l’image 1 telle que téléversée : sur 4.6, une image dépassant 16,7 MP ou 8192 pixels par côté est d’abord réduite, et sur 4.5, la même chose se produit au-delà d’environ 4 MP ou 4608 pixels par côté.
- **Taille de la source de la région :** lorsqu’une fenêtre de contexte est utilisée, l’image 1 peut atteindre 67 108 864 pixels au total (environ 67 MP), par exemple 8192x8192 ou 10000x5000 ; la limite porte sur l’aire, pas sur un côté.
- **Limites de région :** une région issue de `context_window_bboxes` peut atteindre 8192 pixels par côté et environ 16,7 MP sur 4.6, et jusqu’à 4608 pixels par côté et environ 4 MP sur 4.5. Les boîtes ne lèvent une erreur que lorsque leur région fusionnée sort de l’image 1, donc une boîte à gauche de l’image et une autre à droite fusionnent en une région qui couvre l’image.
- **Balises de prompt :** `@ImageN` est mis en correspondance sans tenir compte de la casse et ne doit pas dépasser le nombre d’images connectées ; le prompt ne doit pas être composé uniquement d’espaces et doit comporter au maximum 10000 caractères.
- **Limite de téléversement :** l’image 1, le masque et les références réunis doivent tenir dans la limite de téléversement de 50 Mo d’Ideogram. Une édition 4.6 et une édition de région 4.5 réencodent l’image 1 en JPEG lorsque les fichiers ne tiennent pas et lèvent une erreur si cela ne tient toujours pas ; une édition de l’image entière 4.5 envoie toujours du PNG et ne dispose pas de cette solution de repli.
- **Sécurité du contenu :** si le filtre de sécurité du contenu d’Ideogram bloque le résultat, le nœud lève une erreur au lieu de renvoyer une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L’image modifiée sous forme de lot, à la taille de l’image 1. Une édition de l’image entière revient plus petite lorsque la source dépasse le budget de téléversement : 16,7 MP ou 8192 pixels par côté sur 4.6, environ 4 MP ou 4608 pixels par côté sur 4.5. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
