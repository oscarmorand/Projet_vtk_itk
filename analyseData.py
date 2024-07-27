import numpy as np
import skimage.measure
import json

def compute_tumor_volume_evolution(regions1, regions2):
    areas1 = np.array([region.area for region in regions1])
    areas2 = np.array([region.area for region in regions2])

    area1 = areas1.sum()
    area2 = areas2.sum()

    return ((area2 - area1) / area1), area1, area2

def compute_centroids_evolution(regions1, regions2):
    centroids1 = np.array([region.centroid for region in regions1])
    centroids2 = np.array([region.centroid for region in regions2])

    if len(centroids1) > len(centroids2):
        print("Warning: a tumor has disappeared")
    elif len(centroids1) < len(centroids2):
        print("Warning: a tumor has appeared")
    else:
        print("No evolution in the number of tumors")
        min_dist = []
        for centroid1 in centroids1:
            distances = [((centroid1[0] - centroid2[0])**2 + (centroid1[1] - centroid2[1])**2)**0.5 for centroid2 in centroids2]
            min_dist.append(distances.index(min(distances)))
        return min_dist
    return None

def compute_tumors_evolution(mask1, mask2):
    regions1 = skimage.measure.regionprops(mask1.astype(np.uint8))
    regions2 = skimage.measure.regionprops(mask2.astype(np.uint8))

    tumor_volume_evolution, volume1, volume2 = compute_tumor_volume_evolution(regions1, regions2)
    centroids_evolution = compute_centroids_evolution(regions1, regions2)

    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump({"scan1_tumors_volume": f"{volume1} voxels",
                   "scan2_tumors_volume": f"{volume2} voxels",
                   "tumors_volume_evolution": f"{tumor_volume_evolution * 100:.2f} %",
                   "centroids_evolution": centroids_evolution}, f, ensure_ascii=False, indent=4)

def analyseData(segmentation1, segmentation2):
    compute_tumors_evolution(segmentation1, segmentation2)
