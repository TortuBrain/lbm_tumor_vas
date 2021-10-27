from dipy.io.stateful_tractogram import StatefulTractogram
from dipy.io.streamline import load_tractogram
import taubrain as tb
tracto = load_tractogram("data/data.trk", "same", bbox_valid_check=False)
streamlines = tracto.streamlines
print(tb.tortuosity.tortuosity_geometric_track(streamlines[0:300]))
