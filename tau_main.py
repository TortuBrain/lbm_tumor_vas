from dipy.io.streamline import load_tractogram
import taubrain as tb
tracto = load_tractogram("data/tractogram_probabilistic_thresh_all.trk", "same", bbox_valid_check=False)
streamlines = tracto.streamlines
print(tb.tortuosity.stram_tortuosity(streamlines))










