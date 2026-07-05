# SAM3 Suivi Vidéo

Voici la traduction de la documentation du nœud ComfyUI `SAM3_VideoTrack` :

## Aperçu

Suivez des objets à travers les images d'une vidéo à l'aide du tracker basé sur la mémoire de SAM3. Ce nœud traite une séquence d'images vidéo et maintient l'identité des objets d'une image à l'autre, en utilisant soit des masques initiaux, soit des invites textuelles pour définir ce qui doit être suivi.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Images vidéo sous forme d'images par lots | IMAGE | Oui | Images vidéo par lots |
| `modèle` | Le modèle SAM3 à utiliser pour le suivi | MODEL | Oui | Modèle SAM3 |
| `masque_initial` | Masque(s) pour la première image à suivre (un par objet). Requis si `conditionnement` n'est pas fourni. | MASK | Non | Un masque par objet |
| `conditionnement` | Conditionnement textuel pour détecter de nouveaux objets pendant le suivi. Requis si `masque_initial` n'est pas fourni. | CONDITIONING | Non | Conditionnement textuel |
| `seuil_de_détection` | Seuil de score pour la détection par invite textuelle | FLOAT | Non | 0.0 à 1.0 (par défaut : 0.5) |
| `objets_max` | Nombre maximal d'objets suivis. Les masques initiaux comptent dans cette limite. 0 utilise la limite interne de 64. | INT | Non | 0 à 64 (par défaut : 0) |
| `intervalle_de_détection` | Exécute la détection toutes les N images (1 = chaque image). Des valeurs plus élevées économisent des ressources de calcul. | INT | Non | 1 à illimité (par défaut : 1) |

**Remarque :** `initial_mask` ou `conditioning` doit être fourni. Si les deux sont omis, le nœud générera une erreur.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `données_suivi` | Données de suivi contenant les masques d'objets et les métadonnées pour toutes les images vidéo | SAM3TrackData |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/fr.md)

---
**Source fingerprint (SHA-256):** `30768bdf5839c1d7b984675e68a127a27f21b17724a2dc885e27f00c272db3cb`
