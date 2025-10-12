> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/fr.md)

Le nœud WAN Context Windows (Manual) vous permet de configurer manuellement les fenêtres de contexte pour les modèles de type WAN avec un traitement bidimensionnel. Il applique des paramètres personnalisés de fenêtre de contexte pendant l'échantillonnage en spécifiant la longueur de la fenêtre, le chevauchement, la méthode de planification et la technique de fusion. Cela vous donne un contrôle précis sur la façon dont le modèle traite l'information à travers différentes régions de contexte.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel appliquer les fenêtres de contexte pendant l'échantillonnage. |
| `context_length` | INT | Oui | 1 à 1048576 | La longueur de la fenêtre de contexte (par défaut : 81). |
| `context_overlap` | INT | Oui | 0 à 1048576 | Le chevauchement de la fenêtre de contexte (par défaut : 30). |
| `context_schedule` | COMBO | Oui | "static_standard"<br>"uniform_standard"<br>"uniform_looped"<br>"batched" | La méthode de planification de la fenêtre de contexte. |
| `context_stride` | INT | Oui | 1 à 1048576 | Le pas de la fenêtre de contexte ; applicable uniquement aux planifications uniformes (par défaut : 1). |
| `closed_loop` | BOOLEAN | Oui | - | Indique s'il faut fermer la boucle de la fenêtre de contexte ; applicable uniquement aux planifications en boucle (par défaut : False). |
| `fuse_method` | COMBO | Oui | "pyramid" | La méthode à utiliser pour fusionner les fenêtres de contexte (par défaut : "pyramid"). |

**Note :** Le paramètre `context_stride` n'affecte que les planifications uniformes, et `closed_loop` ne s'applique qu'aux planifications en boucle. Les valeurs de longueur et de chevauchement de contexte sont automatiquement ajustées pour garantir des valeurs minimales valides pendant le traitement.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle avec la configuration de fenêtre de contexte appliquée. |
