# Créer un modèle de crochet comme LoRA

Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLora/en.md)

Ce nœud crée un modèle de hook en tant que LoRA (Adaptation de Bas Rang) en chargeant les poids d'un point de contrôle et en appliquant des ajustements de force à la fois au modèle et aux composants CLIP. Il permet d'appliquer des modifications de type LoRA à des modèles existants via une approche basée sur les hooks, permettant un réglage fin et une adaptation sans modifications permanentes du modèle. Le nœud peut se combiner avec des hooks précédents et met en cache les poids chargés pour plus d'efficacité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nom_ckpt` | Le fichier de point de contrôle à partir duquel charger les poids (sélectionner parmi les points de contrôle disponibles) | STRING | Oui | Plusieurs options disponibles |
| `force_modele` | Le multiplicateur de force appliqué aux poids du modèle (par défaut : 1.0) | FLOAT | Oui | -20.0 à 20.0 |
| `force_clip` | Le multiplicateur de force appliqué aux poids CLIP (par défaut : 1.0) | FLOAT | Oui | -20.0 à 20.0 |
| `crochets_precedents` | Hooks précédents facultatifs à combiner avec les nouveaux hooks LoRA créés | HOOKS | Non | - |

**Contraintes des paramètres :**

- Le paramètre `ckpt_name` charge les points de contrôle depuis le dossier des points de contrôle disponibles
- Les deux paramètres de force acceptent des valeurs de -20.0 à 20.0 avec des incréments de 0.01
- Lorsque `prev_hooks` n'est pas fourni, le nœud crée un nouveau groupe de hooks
- Le nœud met en cache les poids chargés pour éviter de recharger le même point de contrôle plusieurs fois

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `HOOKS` | Les hooks LoRA créés, combinés avec les hooks précédents le cas échéant | HOOKS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLora/fr.md)

---
**Source fingerprint (SHA-256):** `8c0dd6b2e8e99e1d7dbc864aa802c0713842fb0d4ee018ea5cbedfb7896a770d`
