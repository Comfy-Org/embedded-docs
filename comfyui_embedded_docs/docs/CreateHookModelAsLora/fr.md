> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLora/fr.md)

Ce nœud crée un modèle hook sous forme de LoRA (Adaptation Bas-Rang) en chargeant les poids d'un point de contrôle et en appliquant des ajustements de force aux composants du modèle et de CLIP. Il vous permet d'appliquer des modifications de style LoRA aux modèles existants via une approche basée sur les hooks, permettant un réglage fin et une adaptation sans modifications permanentes du modèle. Le nœud peut se combiner avec des hooks précédents et met en cache les poids chargés pour plus d'efficacité.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `nom_ckpt` | COMBO | Oui | Plusieurs options disponibles | Le fichier de point de contrôle à partir duquel charger les poids (sélectionnez parmi les points de contrôle disponibles) |
| `force_modele` | FLOAT | Oui | -20.0 à 20.0 | Le multiplicateur de force appliqué aux poids du modèle (par défaut : 1.0) |
| `force_clip` | FLOAT | Oui | -20.0 à 20.0 | Le multiplicateur de force appliqué aux poids de CLIP (par défaut : 1.0) |
| `crochets_precedents` | HOOKS | Non | - | Hooks précédents optionnels à combiner avec les nouveaux hooks LoRA créés |

**Contraintes des paramètres :**
- Le paramètre `ckpt_name` charge les points de contrôle à partir du dossier des points de contrôle disponibles
- Les deux paramètres de force acceptent des valeurs de -20.0 à 20.0 avec des incréments de 0.01
- Lorsque `prev_hooks` n'est pas fourni, le nœud crée un nouveau groupe de hooks
- Le nœud met en cache les poids chargés pour éviter de recharger plusieurs fois le même point de contrôle

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Les hooks LoRA créés, combinés avec tous les hooks précédents si fournis |