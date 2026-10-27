"""
This is where the Django app plugs into the model Person 1 trains and
pushes to Hugging Face (see ml_predictor/train/train_model.py and
push_to_hf.py).

How it works:
1. Person 1 trains a model and runs push_to_hf.py, which uploads a single
   file — model.joblib — to a Hugging Face Hub *model* repo, e.g.
   "yourusername/realestate-price-predictor".
2. That repo ID goes into .env as HF_MODEL_REPO_ID (see .env.example).
3. The first time a prediction is requested, load_model() below downloads
   model.joblib via huggingface_hub, caches it on disk (huggingface_hub's
   own cache — usually ~/.cache/huggingface), and keeps the deserialized
   object in memory (via lru_cache) for the lifetime of the process.
   Every prediction after that is a local, no-network call.
4. If the repo is private, set HF_TOKEN in .env too.

Nothing else in the codebase needs to change when Person 1 pushes an
improved model — just re-run push_to_hf.py and restart the server (or
call load_model.cache_clear() to pick up the new version without a
restart).
"""
from functools import lru_cache

import joblib
from django.conf import settings
from huggingface_hub import hf_hub_download


@lru_cache(maxsize=1)
def load_model():
    """
    Downloads (once) and returns the trained model bundle:
        {"model": <sklearn LinearRegression>, "encoders": {...}, "feature_order": [...]}
    """
    repo_id = settings.HF_MODEL_REPO_ID
    filename = settings.HF_MODEL_FILENAME
    token = settings.HF_TOKEN or None

    if not repo_id:
        raise RuntimeError(
            "HF_MODEL_REPO_ID is not set. Once Person 1 has trained a model "
            "and pushed it with ml_predictor/train/push_to_hf.py, add the "
            "repo id (e.g. 'yourusername/realestate-price-predictor') to .env."
        )

    local_path = hf_hub_download(repo_id=repo_id, filename=filename, token=token)
    return joblib.load(local_path)


def reload_model():
    """Call this after pushing an updated model to pick it up without restarting."""
    load_model.cache_clear()
    return load_model()
