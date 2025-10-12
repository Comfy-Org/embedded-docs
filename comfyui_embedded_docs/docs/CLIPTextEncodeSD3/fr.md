> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/fr.md)

Le nœud CLIPTextEncodeSD3 traite les entrées textuelles pour les modèles Stable Diffusion 3 en encodant plusieurs invites textuelles à l'aide de différents modèles CLIP. Il gère trois entrées textuelles distinctes (clip_g, clip_l et t5xxl) et propose des options pour gérer le remplissage des textes vides. Le nœud assure un alignement correct des tokens entre les différentes entrées textuelles et retourne des données de conditionnement adaptées aux pipelines de génération SD3.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Requis | - | - | Le modèle CLIP utilisé pour l'encodage du texte |
| `clip_l` | STRING | Multiligne, Invites dynamiques | - | - | Entrée texte pour le modèle CLIP local |
| `clip_g` | STRING | Multiligne, Invites dynamiques | - | - | Entrée texte pour le modèle CLIP global |
| `t5xxl` | STRING | Multiligne, Invites dynamiques | - | - | Entrée texte pour le modèle T5-XXL |
| `remplissage_vide` | COMBO | Sélection | - | ["none", "empty_prompt"] | Contrôle la gestion des entrées textuelles vides |

**Contraintes des paramètres :**
- Lorsque `empty_padding` est défini sur "none", les entrées textuelles vides pour `clip_g`, `clip_l` ou `t5xxl` entraîneront des listes de tokens vides au lieu d'un remplissage
- Le nœud équilibre automatiquement les longueurs de tokens entre les entrées `clip_l` et `clip_g` en complétant la plus courte avec des tokens vides lorsque les longueurs diffèrent
- Toutes les entrées textuelles prennent en charge les invites dynamiques et la saisie de texte multiligne

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement textuel encodées, prêtes à être utilisées dans les pipelines de génération SD3 |