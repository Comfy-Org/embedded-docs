# CLIPMergeSimple

`CLIPMergeSimple` fusionne deux modèles d'encodeur de texte CLIP en un seul. Il clone le premier modèle CLIP comme modèle de base et applique des correctifs de paramètres pondérés provenant du second modèle CLIP, de sorte que le résultat combine les caractéristiques des deux. Le paramètre `ratio` contrôle la force de contribution de chaque modèle ; par défaut, à 1.0, le premier modèle est utilisé tel quel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip1` | Le premier modèle CLIP. Il est cloné et utilisé comme modèle de base pour la fusion. | CLIP | Oui | — |
| `clip2` | Le second modèle CLIP. Ses patchs de paramètres sont appliqués au modèle de base, à l'exception des patchs dont les clés se terminent par `.position_ids` ou `.logit_scale`. | CLIP | Oui | — |
| `ratio` | Contrôle la force relative des deux modèles. Le modèle de base (`clip1`) conserve une force égale à `ratio`, et les patchs de `clip2` sont appliqués avec une force de `1.0 - ratio`. Par défaut, à 1.0, la sortie est identique à `clip1` ; des valeurs plus faibles intègrent davantage `clip2` ; à 0.0, les patchs de `clip2` sont appliqués à pleine puissance. | FLOAT | Oui | 0.0 à 1.0 (défaut : 1.0, pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `clip` | Le modèle CLIP fusionné : un clone de `clip1` avec les patchs de `clip2` appliqués selon `ratio`. | CLIP |

## Mécanisme de fusion expliqué

### Algorithme de fusion

Le nœud utilise une application pondérée des patchs pour combiner les deux modèles :

1. **Cloner le modèle de base** : Clone `clip1` pour servir de modèle de base.
2. **Obtenir les patchs** : Collecte tous les patchs de paramètres (valeurs de paramètres) de `clip2`.
3. **Filtrer les clés spéciales** : Ignore les clés se terminant par `.position_ids` et `.logit_scale`, afin que ces paramètres restent inchangés.
4. **Appliquer la fusion pondérée** : Applique les patchs de `clip2` au modèle de base cloné avec une force de patch de `1.0 - ratio`, tandis que le modèle de base conserve une force de `ratio`.

### Explication du paramètre ratio

- **ratio = 1.0** : La force de base est de 1.0 et la force des patchs est de 0.0, donc la sortie est identique à `clip1` (défaut).
- **ratio = 0.5** : La force de base et la force des patchs sont toutes deux de 0.5, donc les deux modèles contribuent avec une force égale.
- **ratio = 0.0** : La force de base est de 0.0 et la force des patchs est de 1.0, donc les patchs de `clip2` sont appliqués à pleine puissance.

## Cas d'utilisation

1. **Fusion de styles de modèles** : Combiner les caractéristiques de modèles CLIP entraînés sur des données différentes.
2. **Optimisation des performances** : Équilibrer les forces et les faiblesses de différents modèles.
3. **Recherche expérimentale** : Explorer des combinaisons de différents encodeurs CLIP.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSimple/fr.md)

---
**Source fingerprint (SHA-256):** `42c4b2042c56c3f21a9416aa577e2d41fef1dcc749c4e5c7953851110a4fb6bc`
