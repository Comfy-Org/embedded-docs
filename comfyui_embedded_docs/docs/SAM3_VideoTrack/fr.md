# SAM3 Suivi Vidéo

Suivre des objets à travers les images vidéo à l’aide du tracker à mémoire de SAM3. Le nœud traite une séquence d’images vidéo et maintient les identités des objets entre les images, en utilisant soit des masques initiaux, soit des prompts textuels pour définir ce qu’il faut suivre, et peut détecter de nouveaux objets en cours de route à l’aide d’un conditionnement textuel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Images de trames vidéo sous forme de lots d’images | IMAGE | Oui | Trames vidéo en lots |
| `model` | Le modèle SAM3 à utiliser pour le suivi | MODEL | Oui | Modèle SAM3 |
| `initial_mask` | Masque(s) pour la première image à suivre (un par objet) | MASK | Non | Un masque par objet |
| `conditioning` | Conditionnement textuel pour détecter de nouveaux objets pendant le suivi | CONDITIONING | Non | Conditionnement textuel |
| `detection_threshold` | Seuil de score pour la détection déclenchée par prompt textuel (par défaut : 0,5) | FLOAT | Non | 0,0 à 1,0 (pas de 0,01) |
| `max_objects` | Nombre maximal d’objets suivis. Les masques initiaux comptent dans cette limite. 0 utilise la limite interne de 64. (par défaut : 4) | INT | Non | 0 à 64 |
| `detect_interval` | Exécuter la détection toutes les N images (1 = chaque image). Des valeurs plus élevées réduisent le coût de calcul. (par défaut : 1) | INT | Non | 1 ou plus |

**Remarque :** L’un de `initial_mask` ou `conditioning` doit être fourni. Si les deux sont omis, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `track_data` | Données de suivi contenant les masques d’objets et les métadonnées pour toutes les images vidéo | SAM3_TRACK_DATA |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/fr.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
