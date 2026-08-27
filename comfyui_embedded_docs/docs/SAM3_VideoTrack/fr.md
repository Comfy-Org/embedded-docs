# SAM3 Suivi Vidéo

Suivez des objets à travers les images d'une vidéo à l'aide du tracker basé sur la mémoire de SAM3. Ce nœud traite une séquence d'images vidéo et maintient les identités des objets à travers les images, en utilisant soit des masques initiaux, soit des invites textuelles pour définir ce qui doit être suivi.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Images vidéo sous forme d'images par lots | IMAGE | Oui | Images vidéo par lots |
| `modèle` | Le modèle SAM3 à utiliser pour le suivi | MODEL | Oui | Modèle SAM3 |
| `masque_initial` | Masque(s) pour la première image à suivre (un par objet) | MASK | Non | Un masque par objet |
| `conditionnement` | Conditionnement textuel pour détecter de nouveaux objets pendant le suivi | CONDITIONING | Non | Conditionnement textuel |
| `seuil_de_détection` | Seuil de score pour la détection par invite textuelle (défaut : 0.5) | FLOAT | Non | 0.0 à 1.0 |
| `objets_max` | Nombre maximal d'objets suivis. Les masques initiaux comptent dans cette limite. 0 utilise la limite interne de 64. (défaut : 4) | INT | Non | 0 à 64 |
| `intervalle_de_détection` | Exécuter la détection toutes les N images (1 = chaque image). Des valeurs plus élevées économisent du calcul. (défaut : 1) | INT | Non | 1 ou plus |

**Remarque :** `initial_mask` ou `conditioning` doit être fourni. Si les deux sont omis, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `données_suivi` | Données de suivi contenant les masques d'objets et les métadonnées sur toutes les images vidéo | SAM3TrackData |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/fr.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
