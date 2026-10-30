# Ideogram 4.5 Modification précise

Modifiez une image guidée par un prompt textuel grâce à l’édition précise d’Ideogram 4.5 : seul ce que le prompt demande est modifié, les pixels non touchés restent identiques et la sortie conserve la taille de l’image 1. L’image 1 est l’image à modifier et jusqu’à 4 images supplémentaires peuvent être connectées comme références. Une seule région de l’image 1 peut également être modifiée isolément, sélectionnée par un masque ou par des boîtes englobantes, ce qui renvoie l’image en taille réelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser. (par défaut : `"ideogram-4.5"`) | DYNAMIC_COMBO | Oui | `"ideogram-4.5"` |
| `images` | Emplacement extensible : l’image 1 est l’image à modifier et les images 2 à 5 sont des références facultatives (`image_1` ... `image_5`). Faites-y référence dans le prompt sous la forme @Image1, @Image2, ... ; une entrée par lot compte une fois par image. Chaque image doit avoir un rapport d’aspect compris entre 1:6 et 6:1, sauf que l’image 1 n’est pas vérifiée quant au rapport d’aspect lorsqu’une fenêtre de contexte est utilisée. | IMAGE | Oui | 1 à 5 images |
| `prompt` | Instructions de modification. Prend en charge les références de style @Image1 vers les images connectées. (par défaut : chaîne vide) | STRING | Oui | 1 à 10000 caractères |
| `quality` | Niveau de qualité. Les niveaux supérieurs coûtent plus cher et prennent plus de temps. (par défaut : `"medium"`) | COMBO | Oui | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Graine pour la génération. Les mêmes images, le même prompt, les mêmes réglages et la même graine donnent le même résultat. (par défaut : 42) | INT | Oui | 0 à 2147483647 |
| `context_window` | Région de l’image 1 à modifier. `"none"` modifie l’image entière. `"auto"` modifie une région autour de `context_window_mask` et `"custom"` la région issue de `context_window_bboxes` ; les deux conservent l’image 1 en taille réelle et laissent le reste de l’image inchangé. (par défaut : `"none"`) | COMBO | Non | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Région de l’image 1 à modifier, par exemple la sortie de Create Bounding Boxes. Requis lorsque `context_window` vaut `"custom"` ; non utilisé sinon. Plusieurs boîtes sont fusionnées en une seule région, qui est agrandie à au moins 256 pixels par côté et à un rapport d’aspect de 6:1. La région peut atteindre 4608 pixels par côté et environ 4 MP (par ex. 2048x2048). | BOUNDING_BOX | Non | - |
| `context_window_mask` | Le blanc indique ce qu’il faut modifier ; la région de modification est placée autour. Requis lorsque `context_window` vaut `"auto"` ; non utilisé sinon. Le masque doit contenir à la fois des zones blanches (modifier) et noires (conserver). | MASK | Non | - |

### Contraintes des paramètres

- **Nombre d’images :** au moins 1 et au plus 5 images ; une entrée par lot compte une fois par image. L’image 1 est l’image à modifier et les images 2 à 5 sont des références. Avec `context_window_mask`, au plus 4 images sont acceptées, soit l’image 1 et 3 références.
- **Taille de sortie :** le résultat conserve la taille de l’image 1 ; ce nœud n’a donc aucune entrée de taille, de largeur ou de hauteur. Cela vaut également lorsqu’une région est modifiée : l’image complète est renvoyée avec uniquement la région modifiée.
- **Rapport d’aspect des images :** chaque image ne doit pas être plus large que 6 fois sa hauteur ni plus haute que 6 fois sa largeur (entre 1:6 et 6:1). L’image 1 en est exemptée tant que `context_window` vaut `"auto"` ou `"custom"`, car seule sa région sélectionnée est envoyée.
- **Taille de la source de la région :** lorsqu’une fenêtre de contexte est utilisée, l’image 1 peut atteindre 8192x8192 pixels (environ 67 MP) ; les sources plus grandes déclenchent une erreur. Sans fenêtre de contexte, les images plus grandes qu’environ 4 MP ou 4608 px sur le côté le plus long sont réduites avant d’être envoyées.
- **Limites de région :** une région issue de `context_window_bboxes` peut atteindre 4608 pixels par côté et environ 4 MP ; les boîtes situées entièrement en dehors de l’image 1 déclenchent une erreur.
- **Balises de prompt :** `@ImageN` est mis en correspondance sans tenir compte de la casse et ne doit pas dépasser le nombre d’images connectées ; le prompt ne doit pas être vide (hors espaces) et doit comporter au plus 10000 caractères.
- **Limite de téléversement :** l’image 1, le masque et les références ensemble doivent tenir dans la limite de téléversement de 50 Mo d’Ideogram ; l’image 1 est réencodée en JPEG si nécessaire et le nœud déclenche une erreur si l’ensemble ne tient toujours pas.
- **Sécurité du contenu :** si le filtre de sécurité du contenu d’Ideogram bloque le résultat, le nœud déclenche une erreur au lieu de renvoyer une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L’image modifiée sous forme de lot, à la taille de l’image 1. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
