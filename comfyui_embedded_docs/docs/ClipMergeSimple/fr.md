`CLIPMergeSimple` est un nœud avancé de fusion de modèles utilisé pour combiner deux modèles d'encodeur de texte CLIP selon un ratio spécifié.

Ce nœud se spécialise dans la fusion de deux modèles CLIP selon un ratio spécifié, mélangeant efficacement leurs caractéristiques. Il applique sélectivement des patches d'un modèle à un autre, en excluant des composants spécifiques comme les IDs de position et l'échelle des logits, pour créer un modèle hybride qui combine les caractéristiques des deux modèles sources.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| clip1     | CLIP      | Le premier modèle CLIP à fusionner. Il sert de modèle de base pour le processus de fusion. |
| clip2     | CLIP      | Le second modèle CLIP à fusionner. Ses patches clés, à l'exception des IDs de position et de l'échelle des logits, sont appliqués au premier modèle selon le ratio spécifié. |
| ratio     | FLOAT     | Plage `0.0 - 1.0`, détermine la proportion de caractéristiques du second modèle à intégrer dans le premier modèle. Un ratio de 1.0 signifie adopter entièrement les caractéristiques du second modèle, tandis que 0.0 conserve uniquement les caractéristiques du premier modèle. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|-------------|-------------|
| clip      | CLIP      | Le modèle CLIP fusionné résultant, incorporant des caractéristiques des deux modèles d'entrée selon le ratio spécifié. |

## Explication du Mécanisme de Fusion

### Algorithme de Fusion

Le nœud utilise une moyenne pondérée pour fusionner les deux modèles :

1. **Clonage du Modèle de Base** : Clone d'abord clip1 comme modèle de base
2. **Obtention des Patches** : Obtient tous les patches clés de clip2
3. **Filtrage des Clés Spéciales** : Ignore les clés se terminant par `.position_ids` et `.logit_scale`
4. **Application de la Fusion Pondérée** : Utilise la formule `(1.0 - ratio) * clip1 + ratio * clip2`

### Explication du Paramètre Ratio

- **ratio = 0.0** : Utilise entièrement clip1, ignore clip2
- **ratio = 0.5** : Contribution de 50% de chaque modèle
- **ratio = 1.0** : Utilise entièrement clip2, ignore clip1

## Cas d'Utilisation

1. **Fusion de Styles de Modèles** : Combiner les caractéristiques des modèles CLIP entraînés sur différentes données
2. **Optimisation des Performances** : Équilibrer les forces et les faiblesses de différents modèles
3. **Recherche Expérimentale** : Explorer les combinaisons de différents encodeurs CLIP
