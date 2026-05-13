> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSetLastLayer/fr.md)

Voici la traduction en français de la documentation du nœud `CLIP Set Last Layer` :

`CLIP Set Last Layer` est un nœud central de ComfyUI permettant de contrôler la profondeur de traitement des modèles CLIP. Il offre un contrôle précis sur l'étape à laquelle l'encodeur de texte CLIP cesse son traitement, influençant à la fois la profondeur de la compréhension textuelle et le style des images générées.

Imaginez le modèle CLIP comme un cerveau intelligent composé de 24 couches :

- Couches superficielles (1 à 8) : Reconnaissance des lettres et mots de base
- Couches intermédiaires (9 à 16) : Compréhension de la grammaire et de la structure des phrases
- Couches profondes (17 à 24) : Saisie des concepts abstraits et de la sémantique complexe

`CLIP Set Last Layer` fonctionne comme un **« contrôleur de profondeur de réflexion »** :

- -1 : Utilise les 24 couches (compréhension complète)
- -2 : S'arrête à la couche 23 (légèrement simplifié)
- -12 : S'arrête à la couche 13 (compréhension moyenne)
- -24 : Utilise uniquement la couche 1 (compréhension basique)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `clip` | CLIP | Oui | - | Le modèle CLIP à modifier |
| `stop_at_clip_layer` | INT | Oui | -24 à -1 | Spécifie la couche à laquelle s'arrêter. Une valeur de -1 utilise toutes les couches, tandis que -24 utilise uniquement la première couche (valeur par défaut : -1) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `clip` | CLIP | Le modèle CLIP modifié avec la couche spécifiée définie comme dernière couche |

## Pourquoi définir la dernière couche

- **Optimisation des performances** : Comme il n'est pas nécessaire d'avoir un doctorat pour comprendre des phrases simples, une compréhension superficielle est parfois suffisante et plus rapide
- **Contrôle du style** : Différents niveaux de compréhension produisent différents styles artistiques
- **Compatibilité** : Certains modèles peuvent offrir de meilleures performances à des couches spécifiques

---
**Source fingerprint (SHA-256):** `82f3e7fb1d4c0bdd2b242a449085a5497ba8af8616d1800c5c0ee7a85ab42c15`
