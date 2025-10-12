> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/fr.md)

Le nœud Context Windows (Manual) permet de configurer manuellement les fenêtres de contexte pour les modèles lors de l'échantillonnage. Il crée des segments de contexte qui se chevauchent avec une longueur, un chevauchement et des motifs de planification spécifiés pour traiter les données par blocs gérables tout en maintenant la continuité entre les segments.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle auquel appliquer les fenêtres de contexte pendant l'échantillonnage. |
| `context_length` | INT | Non | 1+ | La longueur de la fenêtre de contexte (par défaut : 16). |
| `context_overlap` | INT | Non | 0+ | Le chevauchement de la fenêtre de contexte (par défaut : 4). |
| `context_schedule` | COMBO | Non | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` | Le pas de la fenêtre de contexte. |
| `context_stride` | INT | Non | 1+ | Le pas de la fenêtre de contexte ; applicable uniquement aux planifications uniformes (par défaut : 1). |
| `closed_loop` | BOOLEAN | Non | - | Indique s'il faut fermer la boucle de la fenêtre de contexte ; applicable uniquement aux planifications en boucle (par défaut : False). |
| `fuse_method` | COMBO | Non | `PYRAMID`<br>`LIST_STATIC` | La méthode à utiliser pour fusionner les fenêtres de contexte (par défaut : PYRAMID). |
| `dim` | INT | Non | 0-5 | La dimension à laquelle appliquer les fenêtres de contexte (par défaut : 0). |

**Contraintes des paramètres :**

- `context_stride` n'est utilisé que lorsque les planifications uniformes sont sélectionnées
- `closed_loop` n'est applicable qu'aux planifications en boucle
- `dim` doit être compris entre 0 et 5 inclus

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle avec les fenêtres de contexte appliquées pendant l'échantillonnage. |
