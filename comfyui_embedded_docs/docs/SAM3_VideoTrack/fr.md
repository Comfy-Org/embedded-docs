> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI **SAM3_VideoTrack** :

## Aperçu

Suivez des objets à travers les images d’une vidéo à l’aide du tracker basé sur la mémoire de SAM3. Ce nœud traite une séquence d’images vidéo et maintient l’identité des objets d’une image à l’autre, en utilisant soit des masques initiaux, soit des invites textuelles pour définir ce qui doit être suivi.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `images` | IMAGE | Oui | Images vidéo par lots | Images vidéo sous forme d’images regroupées en lots |
| `model` | MODEL | Oui | Modèle SAM3 | Le modèle SAM3 à utiliser pour le suivi |
| `initial_mask` | MASK | Non | Un masque par objet | Masque(s) pour la première image à suivre (un par objet). Requis si `conditioning` n’est pas fourni. |
| `conditioning` | CONDITIONING | Non | Conditionnement textuel | Conditionnement textuel pour détecter de nouveaux objets pendant le suivi. Requis si `initial_mask` n’est pas fourni. |
| `detection_threshold` | FLOAT | Non | 0,0 à 1,0 (par défaut : 0,5) | Seuil de score pour la détection par invite textuelle |
| `max_objects` | INT | Non | 0 à illimité (par défaut : 0) | Nombre maximal d’objets suivis (0 = illimité). Les masques initiaux comptent dans cette limite. |
| `detect_interval` | INT | Non | 1 à illimité (par défaut : 1) | Exécuter la détection toutes les N images (1 = chaque image). Des valeurs plus élevées économisent des ressources de calcul. |

**Remarque :** `initial_mask` ou `conditioning` doit être fourni. Si les deux sont omis, le nœud générera une erreur.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `track_data` | SAM3TrackData | Données de suivi contenant les masques d’objets et les métadonnées sur toutes les images vidéo |