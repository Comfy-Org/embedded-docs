> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI :

## Aperçu

Générer des réponses textuelles à partir d'un modèle Anthropic Claude. Ce nœud envoie une invite textuelle et des images optionnelles à un modèle Claude et renvoie la réponse textuelle générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `invite` | STRING | Oui | N/A | Saisie textuelle pour le modèle. (par défaut : chaîne vide) |
| `modèle` | COMBO | Oui | `"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` | Le modèle Claude utilisé pour générer la réponse. |
| `graine` | INT | Oui | 0 à 2147483647 | La graine contrôle si le nœud doit se réexécuter ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) |
| `images` | IMAGE | Non | 0 à 20 images | Image(s) optionnelle(s) à utiliser comme contexte pour le modèle. Jusqu'à 20 images. |
| `invite système` | STRING | Non | N/A | Instructions fondamentales qui dictent le comportement du modèle. (par défaut : chaîne vide) |

### Contraintes des paramètres

- **Limite d'images** : Un maximum de 20 images peut être fourni par requête.
- **Gestion de la température** : Lorsque la réflexion est activée ou lors de l'utilisation du modèle "Opus 4.7", le paramètre de température est automatiquement désactivé (par défaut à 1.0) comme requis par l'API Anthropic. Pour les autres modèles, la température peut être définie via la configuration du modèle.
- **Réflexion/Raisonnement** : La configuration du modèle inclut un paramètre `reasoning_effort` qui contrôle si la réflexion est activée. Lorsqu'elle est activée, le nœud configure automatiquement le mode de réflexion approprié (adaptatif ou basé sur un budget) en fonction du modèle sélectionné.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | STRING | La réponse textuelle générée par le modèle Claude. Renvoie "Réponse vide du modèle Claude." si aucun texte n'est généré. |

---
**Source fingerprint (SHA-256):** `e3bab004535d4d406582aa42f28bb64a2988f8331788d51ec1fa4e943d8d4382`
