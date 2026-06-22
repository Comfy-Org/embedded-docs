# CLIPMergeSimple

Voici la traduction en français de la documentation du nœud `CLIPMergeSimple` :

`CLIPMergeSimple` est un nœud avancé de fusion de modèles utilisé pour combiner deux encodeurs de texte CLIP selon un ratio spécifié.

Ce nœud est spécialisé dans la fusion de deux modèles CLIP selon un ratio spécifié, en mélangeant efficacement leurs caractéristiques. Il applique sélectivement des correctifs d'un modèle à l'autre, en excluant des composants spécifiques comme les identifiants de position et l'échelle logit, pour créer un modèle hybride combinant les caractéristiques des deux modèles sources.

## Entrées

| Paramètre | Description | Type de données | Type d'entrée | Défaut | Plage |
| --- | --- | --- | --- | --- | --- |
| `clip1` | Le premier modèle CLIP à fusionner. Il sert de modèle de base pour le processus de fusion. | CLIP | REQUIS | - | - |
| `clip2` | Le second modèle CLIP à fusionner. Ses correctifs clés, à l'exception des identifiants de position et de l'échelle logit, sont appliqués au premier modèle en fonction du ratio spécifié. | CLIP | REQUIS | - | - |
| `ratio` | Détermine la proportion des caractéristiques du second modèle à intégrer dans le premier modèle. Un ratio de 1.0 signifie une adoption complète des caractéristiques du second modèle, tandis que 0.0 conserve uniquement les caractéristiques du premier modèle. | FLOAT | REQUIS | 1.0 | 0.0 - 1.0 (pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `clip` | Le modèle CLIP fusionné résultant, intégrant les caractéristiques des deux modèles d'entrée selon le ratio spécifié. | CLIP |

## Explication du Mécanisme de Fusion

### Algorithme de Fusion

Le nœud utilise une moyenne pondérée pour fusionner les deux modèles :

1. **Cloner le modèle de base** : Clone d'abord `clip1` comme modèle de base
2. **Obtenir les correctifs** : Récupère tous les correctifs clés de `clip2`
3. **Filtrer les clés spéciales** : Ignore les clés se terminant par `.position_ids` et `.logit_scale`
4. **Appliquer la fusion pondérée** : Utilise la formule `(1.0 - ratio) * clip1 + ratio * clip2`

### Explication du Paramètre Ratio

- **ratio = 0.0** : Utilise entièrement clip1, ignore clip2
- **ratio = 0.5** : Contribution de 50 % de chaque modèle
- **ratio = 1.0** : Utilise entièrement clip2, ignore clip1

## Cas d'Utilisation

1. **Fusion de styles de modèles** : Combiner les caractéristiques de modèles CLIP entraînés sur différentes données
2. **Optimisation des performances** : Équilibrer les forces et les faiblesses de différents modèles
3. **Recherche expérimentale** : Explorer les combinaisons de différents encodeurs CLIP

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSimple/fr.md)

---
**Source fingerprint (SHA-256):** `0d3c8388dbe88675ea7fb51161ab41ce898bcf63983b3d2817b16ec5bfa613e5`
