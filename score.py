import os
from sugar3.activity.activity import get_activity_root


_SCORE_PATH = None

def get_score_path():
    global _SCORE_PATH

    if _SCORE_PATH:
        return _SCORE_PATH

    _SCORE_PATH = os.path.join(get_activity_root(), 'data', 'score.pkl')
    return _SCORE_PATH
