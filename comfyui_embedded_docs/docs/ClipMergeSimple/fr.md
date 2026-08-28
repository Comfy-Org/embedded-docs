# ClipMergeSimple

`CLIPMergeSimple` est un nœud de fusion de modèles qui combine deux modèles d’encodeur de texte CLIP selon un ratio spécifié. Il clone le premier modèle CLIP et applique des patches pondérés du second modèle CLIP, en ignorant les composants position_ids et logit_scale, pour produire un modèle hybride qui mélange les caractéristiques des deux sources.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip1` | Le premier modèle CLIP à fusionner. Il sert de modèle de base pour le processus de fusion. | CLIP | Oui | - |
| `clip2` | Le second modèle CLIP à fusionner. Ses patches de clés, à l’exception de position_ids et logit_scale, sont appliqués au premier modèle selon le ratio spécifié. | CLIP | Oui | - |
| `ratio` | Détermine la proportion de caractéristiques du second modèle à mélanger dans le premier modèle. Un ratio de 1.0 signifie l’adoption complète des caractéristiques du second modèle, tandis que 0.0 ne conserve que les caractéristiques du premier modèle. Défaut : 1.0. | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `clip` | Le modèle CLIP fusionné résultant, intégrant les caractéristiques des deux modèles d’entrée selon le ratio spécifié. | CLIP |

## Explication du mécanisme de fusion

### Algorithme de fusion

Le nœud utilise une moyenne pondérée pour fusionner les deux modèles :

1. **Cloner le modèle de base** : Clone d’abord `clip1` comme modèle de base.
2. **Obtenir les patches** : Récupère tous les patches de clés de `clip2`.
3. **Filtrer les clés spéciales** : Ignore les clés se terminant par `.position_ids` et `.logit_scale`.
4. **Appliquer la fusion pondérée** : Utilise la formule `(1.0 - ratio) * clip1 + ratio * clip2`.

### Explication du paramètre ratio

- **ratio = 0.0** : Utilise entièrement clip1, ignore clip2.
- **ratio = 0.5** : Contribution de 50 % de chaque modèle.
- **ratio = 1.0** : Utilise entièrement clip2, ignore clip1.

## Cas d’utilisation

1. **Fusion de styles de modèles** : Combiner les caractéristiques de modèles CLIP entraînés sur différentes données.
2. **Optimisation des performances** : Équilibrer les forces et les faiblesses de différents modèles.
3. **Recherche expérimentale** : Explorer des combinaisons de différents encodeurs CLIP.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipMergeSimple/fr.md)

---
**Source fingerprint (SHA-256):** `42c4b2042c56c3f21a9416aa577e2d41fef1dcc749c4e5c7953851110a4fb6bc`
