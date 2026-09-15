# LTXV Ajouter des images clés générées

Le nœud LTXV Add Generated Keyframes ajoute des keyframes de détail à un latent vidéo. Chaque keyframe est une trame latente de tokens positionnée sur une seule trame pixel ; elle est débruitée avec la vidéo et ne fait pas partie de la sortie décodée. Le placement se fait un emplacement tous les `interval_frames` pixels, en ignorant les trames I2V, les guides existants et les keyframes générées déjà présentes sur le conditionnement ; récupérez-les avec LTXV Separate Generated Keyframes. Un checkpoint entraîné pour les keyframes générées (contenant `keyframes_abs_pos_embedding`) est requis.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `positive` | Conditionnement positif auquel les keyframes sont attachées. | CONDITIONING | Oui | N/A |
| `negative` | Conditionnement négatif auquel les keyframes sont attachées. | CONDITIONING | Oui | N/A |
| `vae` | Utilisé uniquement pour lire les facteurs d'échelle du latent. | VAE | Oui | N/A |
| `latent` | Latent vidéo 5D simple sur lequel générer des keyframes en parallèle. Ajoutez-les avant Concat AV Latent. | LATENT | Oui | N/A |
| `interval_frames` | Pas de trames pixel pour le placement automatique. La valeur par défaut de 24 correspond à environ une keyframe par seconde à 24 fps. Les pixels occupés sont ignorés. Ignoré lorsque `frame_indices` est défini. (par défaut : 24) | INT | Non | 1-1024 |
| `keyframes` | Contenu facultatif pour initialiser les nouvelles keyframes. Connectez des keyframes issues d'un Separate antérieur (même taille spatiale), ou un latent vidéo simple pour copier la trame la plus proche à chaque nouvel emplacement (par ex. après un agrandissement temporel). Celles-ci sont toujours débruitées, et non épinglées comme guides. Les indices enregistrés sur un latent de keyframes sont ignorés, sauf si `frame_indices` est défini. N'a d'effet que lorsque l'échantillonnage commence en dessous de sigma 1. | LATENT | Non | N/A |
| `frame_indices` | Indices de trames pixel facultatifs. Laissez vide pour placer à partir de `interval_frames` sur le canevas actuel. Lorsqu'il est défini, cette liste constitue le placement (les keyframes connectées sont associées dans l'ordre). La dernière trame est autorisée ; la trame 0 ne l'est pas (elle est déjà un token autonome). (par défaut : chaîne vide) | STRING | Non | Entiers séparés par des virgules ; de 1 à la dernière trame pixel (trame 0 exclue) |

**Note :** Le `latent` doit être un latent vidéo 5D simple avec des keyframes générées ajoutées avant Concat AV Latent. Lorsque `frame_indices` est défini, chaque trame pixel listée doit être unique et ne peut pas déjà contenir une keyframe d'image, un guide ou une keyframe générée. Si `frame_indices` est vide, les pixels occupés sont ignorés automatiquement ; si aucun emplacement de détail libre n'existe, le nœud déclenche une erreur. Lors d'un ajout à des keyframes générées existantes, le latent doit toujours avoir le même nombre de tokens par trame et le bloc existant doit se terminer à la dernière trame latente.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positive` | Conditionnement positif avec l'attention des keyframes générées attachée. | CONDITIONING |
| `negative` | Conditionnement négatif avec l'attention des keyframes générées attachée. | CONDITIONING |
| `latent` | Latent vidéo avec les keyframes générées ajoutées sur T. | LATENT |

## Remarques

- Le paramètre `interval_frames` définit l'espacement des keyframes placées automatiquement. Une valeur plus élevée donne moins de keyframes et un espacement plus large ; une valeur plus faible produit plus de keyframes.
- L'entrée `keyframes` vous permet d'initialiser les nouvelles keyframes avec des keyframes existantes ou un latent vidéo. Si un latent vidéo simple plus long est fourni, la trame vidéo la plus proche est copiée à chaque nouvel emplacement. Ces keyframes sont toujours débruitées et ne sont pas épinglées comme guides.
- Le paramètre `frame_indices` vous permet de spécifier les indices exacts de trames pixel où les keyframes doivent être placées. Lorsqu'il est fourni, `interval_frames` est ignoré. La liste doit contenir des entiers uniques dans la plage de pixels valide, et la trame 0 n'est pas autorisée.
- Les sorties `positive` et `negative` contiennent le conditionnement avec l'attention des keyframes générées attachée.
- La sortie `latent` contient le latent vidéo avec les keyframes générées ajoutées sur T.
- Un checkpoint entraîné pour les keyframes générées (contenant `keyframes_abs_pos_embedding`) est requis.
- Récupérez les keyframes générées avec LTXV Separate Generated Keyframes.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/fr.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`
