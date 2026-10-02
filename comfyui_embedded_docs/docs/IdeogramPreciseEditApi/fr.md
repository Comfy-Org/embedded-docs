# Ideogram 4.5 Precise Edit

Modifiez une image guidée par un prompt textuel grâce à l'édition précise d'Ideogram 4.5 : seuls les changements demandés par le prompt sont appliqués, les pixels non modifiés restent identiques et la sortie conserve la taille de l'image 1. L'image 1 est l'image à modifier et jusqu'à 4 images supplémentaires peuvent être connectées comme références.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser. (par défaut : `"ideogram-4.5"`) | DYNAMIC_COMBO | Oui | `"ideogram-4.5"` |
| `images` | Emplacement extensible : l'image 1 est l'image à modifier et les images 2 à 5 sont des références facultatives (`image_1` ... `image_5`). Référencez-les dans le prompt sous la forme @Image1, @Image2, ... ; une entrée groupée compte une fois par image. Chaque image doit avoir un rapport d'aspect compris entre 1:6 et 6:1. | IMAGE | Oui | 1 à 5 images |
| `prompt` | Instructions de modification. Prend en charge les références de style @Image1 vers les images connectées. (par défaut : chaîne vide) | STRING | Oui | 1 à 10000 caractères |
| `quality` | Niveau de qualité. Les niveaux plus élevés coûtent plus cher et prennent plus de temps. (par défaut : `"medium"`) | COMBO | Oui | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Graine pour la génération. Les mêmes images, le même prompt, les mêmes réglages et la même graine donnent le même résultat. (par défaut : 42) | INT | Oui | 0 à 2147483647 |

### Contraintes des paramètres

- **Nombre d'images :** au moins 1 et au plus 5 images ; une entrée groupée compte une fois par image. L'image 1 est l'image à modifier et les images 2 à 5 sont des références.
- **Taille de sortie :** le résultat conserve la taille de l'image 1, ce nœud n'a donc aucune entrée de taille, largeur ou hauteur.
- **Rapport d'aspect des images :** chaque image ne doit pas être plus large que 6 fois sa hauteur ni plus haute que 6 fois sa largeur (entre 1:6 et 6:1).
- **Balises de prompt :** `@ImageN` est mis en correspondance sans distinction de casse et ne doit pas dépasser le nombre d'images connectées ; le prompt ne doit pas être composé uniquement d'espaces et contenir au plus 10000 caractères.
- **Mise à l'échelle à l'envoi :** les images dépassant environ 4 MP, ou 4608 px sur le côté le plus long, sont réduites avant d'être envoyées.
- **Sécurité du contenu :** si le filtre de sécurité du contenu d'Ideogram bloque le résultat, le nœud renvoie une erreur au lieu de retourner une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image modifiée sous forme de lot, à la taille de l'image 1. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `74ba429ac93e4528e44c864ccfd3928f6c42108cfcc83577c8963a099a66f527`
